#!/usr/bin/env python3
"""Validate schema-v3 learning content under content/<area>/<group>/<topic>/.

    python3 tools/validate_v3.py                          # every topic
    python3 tools/validate_v3.py system-design             # one area
    python3 tools/validate_v3.py system-design/caching     # one group
    python3 tools/validate_v3.py system-design/caching/cache-invalidation
    python3 tools/validate_v3.py --strict                  # warnings become errors
    python3 tools/validate_v3.py --quiet                   # only the summary

ERRORS are contract breaks — the app or the regen step would misbehave. WARNINGS are
quality drift (char bands, missing MCQs) worth a human look but not a build break.
PENDING lines are deliberately-deferred work — `<<< Image: prompt >>>` diagram
placeholders awaiting an SVG. They never fail a run, not even under --strict.

Char bands are advisory only — length never fails a run. They're calibrated against the
measured length distribution of the full 1331-topic v3 corpus (2026-08), not the v2 numbers
in AUTHORING.md (which the v3 corpus already exceeds by design) and not the earlier
278-topic calibration (which the wave-2 depth bar made the corpus outgrow — nearly every
topic was tripping a band). Bands now flag roughly the top/bottom decile per category, not
the norm. The interview answerMarkdown band is the one exception: it tracks the explicit
900-1800 char contract in the authoring spec rather than the raw distribution. Use
--strict when you do want length drift to fail.
"""
import collections
import json
import os
import re
import sys
import xml.etree.ElementTree as ET

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT = os.path.join(ROOT, "content")

LEVELS = {"beginner", "intermediate", "advanced", "expert"}
DIFFICULTIES = {"easy", "medium", "hard"}
# No "interview" type: in v3 interview questions live in interview.json, never as slides
# (nothing in the corpus uses it). A slide typed "interview" is an authoring mistake.
SLIDE_TYPES = {"overview", "concept", "compare", "diagram", "code", "pitfall"}

TOPIC_KEYS = ["id", "title", "area", "group", "order", "slug", "summary",
              "level", "slideCount", "estReadMinutes", "slides"]
SLIDE_KEYS = ["id", "order", "sectionTitle", "subTitle", "type", "markdown",
              "assets", "hasCode", "hasTable", "estReadSeconds", "mcqIds"]

# min / target / "very long" — all three are advisory (warnings only). Set from the
# measured corpus distribution (see module docstring): min ~ p10, target ~ p90, very-long
# a bit above p99, so each band flags roughly its top/bottom decile rather than the norm.
BANDS = {"overview": (400, 800,  1050),
         "concept":  (480, 1050, 1400),
         "compare":  (520, 1050, 1400),
         "pitfall":  (520, 1100, 1450),
         "diagram":  (300, 800,  1200),
         "code":     (480, 1050, 1550)}
# interview.json answerMarkdown — deliberately NOT distribution-calibrated like BANDS
# above. The authoring spec (prompts/authoring-agent-v3-area.md) holds every agent to an
# explicit 900-1800 char contract, so the band mirrors that contract directly: min=900 and
# target=1800 are the spec's own bounds (anything past 1800 is "over target" by the spec's
# own rule, not by corpus norms), and 2200 (just above the corpus's measured p99) is the
# hard ceiling for genuinely-too-long outliers.
ANSWER_BAND = (900, 1800, 2200)
SUMMARY_BAND = (110, 210, 300)
SANE_SLIDES = (5, 24)                     # warn outside this

IMG_RE = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")
# Deferred-diagram placeholder, per AUTHORING.md 6. The preview renders it as a dashed
# "Diagram not yet generated" box with the prompt inside (tools/serve_v3.py).
PLACEHOLDER_RE = re.compile(r"<<<\s*Image:\s*(.*?)>>>", re.S)
LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([a-z0-9-]+)\)")
TABLE_ROW = re.compile(r"^\s*\|.*\|\s*$", re.M)
TABLE_SEP = re.compile(r"^\s*\|[-:\s|]+\|\s*$", re.M)
HEADING = re.compile(r"^\s{0,3}#{1,6}\s", re.M)
FENCE_BLOCK = re.compile(r"```.*?(?:```|\Z)", re.S)


def outside_fences(md):
    """Drop fenced code blocks so a shell/YAML/Python `# comment` never reads as a heading."""
    return FENCE_BLOCK.sub("", md or "")
# The app prepends its own header — models.dart toBlockMarkdown() returns
#   "<star>**Q: <question>**\n\n<answerMarkdown>"
# so an answer that opens with its own Q header renders the question twice.
ANSWER_Q_HDR = re.compile(r"^\s*(⭐\s*)?\*\*Q:")


class Report:
    def __init__(self):
        self.errors, self.warnings, self.pendings = [], [], []
        # correctIndex tallies per "area/group" — answer-position skew only means
        # something across a whole bank, so it's judged after the walk, in main().
        self.answer_pos = collections.defaultdict(collections.Counter)

    def err(self, where, msg):
        self.errors.append(f"{where}: {msg}")

    def warn(self, where, msg):
        self.warnings.append(f"{where}: {msg}")

    def pending(self, where, msg):
        """Deliberately-deferred work (e.g. an SVG we haven't spent tokens on yet).
        Never fails a run, not even under --strict — it's a to-do, not a defect."""
        self.pendings.append(f"{where}: {msg}")

    def check_svg(self, where, label, path):
        """A malformed SVG passes every content check but silently fails to render
        in the app — most often a bare '&' that should be '&amp;'. We parse with the
        stdlib (this repo is dependency-free), so first reject any DTD: external
        entities and entity-expansion bombs both need one, and no diagram we author
        has any reason to declare one."""
        try:
            with open(path, "rb") as fh:
                head = fh.read(4096)
            if b"<!DOCTYPE" in head or b"<!ENTITY" in head:
                self.err(where, f"image '{label}' declares a DTD/entity — "
                                "not allowed in authored SVGs")
                return
            ET.parse(path)
        except ET.ParseError as exc:
            self.err(where, f"image '{label}' is not well-formed XML — {exc}")
        except OSError as exc:
            self.err(where, f"image '{label}' could not be read — {exc}")


def load(path, rep, where):
    if not os.path.exists(path):
        return None
    try:
        with open(path, encoding="utf-8") as fh:
            return json.load(fh)
    except json.JSONDecodeError as exc:
        rep.err(where, f"unparseable JSON — {exc}")
        return None


def has_table(md):
    return bool(TABLE_SEP.search(md) and TABLE_ROW.search(md))


def check_band(rep, where, label, text, band):
    """Length is a style signal, never a build break — always a warning.

    Length alone can't tell filler from a legitimately dense slide, so this never
    errors. Use --strict when you want length drift to fail a run.
    """
    lo, target, hard = band
    n = len(text)
    if n < lo:
        rep.warn(where, f"{label} short ({n} chars, guide min {lo}) — check it isn't filler")
    elif n > hard:
        rep.warn(where, f"{label} very long ({n} chars, guide {target}) — consider splitting")
    elif n > target:
        rep.warn(where, f"{label} over target ({n} chars, target {target})")


def validate_topic(tdir, all_slugs, rep):
    rel = os.path.relpath(tdir, CONTENT)
    parts = rel.split(os.sep)
    if len(parts) != 3:
        rep.err(rel, "topic must sit at content/<area>/<group>/<topic>/")
        return 0, 0, 0
    area, group, folder = parts

    t = load(os.path.join(tdir, "topic.json"), rep, rel)
    if t is None:
        rep.err(rel, "topic.json missing or unreadable")
        return 0, 0, 0

    for k in TOPIC_KEYS:
        if k not in t:
            rep.err(rel, f"topic.json missing required key '{k}'")
    if any(k not in t for k in ("slug", "slides")):
        return 0, 0, 0

    slug = t["slug"]
    for key, want, label in (("slug", folder, "slug"), ("id", folder, "id"),
                             ("area", area, "area"), ("group", group, "group")):
        if t.get(key) != want:
            rep.err(rel, f"{label} '{t.get(key)}' must equal folder '{want}'")
    if t.get("level") not in LEVELS:
        rep.err(rel, f"level '{t.get('level')}' not in {sorted(LEVELS)}")
    if not isinstance(t.get("order"), int) or t["order"] < 1:
        rep.err(rel, f"order must be a positive int, got {t.get('order')!r}")
    if isinstance(t.get("summary"), str):
        check_band(rep, rel, "summary", t["summary"], SUMMARY_BAND)
    else:
        rep.err(rel, "summary must be a string")

    slides = t["slides"]
    if not isinstance(slides, list) or not slides:
        rep.err(rel, "slides[] is empty")
        return 0, 0, 0
    if not SANE_SLIDES[0] <= len(slides) <= SANE_SLIDES[1]:
        rep.warn(rel, f"{len(slides)} slides — outside the usual {SANE_SLIDES[0]}-{SANE_SLIDES[1]}")
    if t.get("slideCount") != len(slides):
        rep.err(rel, f"slideCount {t.get('slideCount')} != {len(slides)} actual slides")

    secs = 0
    seen_ids, mcq_backrefs = set(), {}
    for i, s in enumerate(slides, 1):
        sid = s.get("id", f"<slide #{i}>")
        w = f"{rel} [{sid}]"
        for k in SLIDE_KEYS:
            if k not in s:
                rep.err(w, f"slide missing required key '{k}'")
        if s.get("order") != i:
            rep.err(w, f"order {s.get('order')} != position {i} (must be contiguous 1..n)")
        want_id = f"{slug}-s{i:02d}"
        if s.get("id") != want_id:
            rep.err(w, f"id must be '{want_id}'")
        if s.get("id") in seen_ids:
            rep.err(w, "duplicate slide id")
        seen_ids.add(s.get("id"))

        stype = s.get("type")
        if stype not in SLIDE_TYPES:
            rep.err(w, f"type '{stype}' not in {sorted(SLIDE_TYPES)}")
        if not s.get("sectionTitle"):
            rep.err(w, "sectionTitle is empty")

        md = s.get("markdown") or ""
        if not md.strip():
            rep.err(w, "markdown is empty")
        else:
            if stype in BANDS:
                check_band(rep, w, f"{stype} markdown", md, BANDS[stype])
            if HEADING.search(outside_fences(md)):
                rep.err(w, "markdown contains a '#' heading — use sectionTitle/subTitle")

        want_code = "```" in md
        if bool(s.get("hasCode")) != want_code:
            rep.err(w, f"hasCode={s.get('hasCode')} but markdown "
                       f"{'has' if want_code else 'has no'} fenced code")
        want_table = has_table(md)
        if bool(s.get("hasTable")) != want_table:
            rep.err(w, f"hasTable={s.get('hasTable')} but markdown "
                       f"{'has' if want_table else 'has no'} table")
        if stype == "code" and not want_code:
            rep.warn(w, "type 'code' but no fenced code block")
        for prompt in PLACEHOLDER_RE.findall(md):
            prompt = " ".join(prompt.split())
            if not prompt:
                rep.err(w, "'<<< Image: ... >>>' placeholder has an empty prompt — "
                           "it must describe the diagram to generate")
            else:
                rep.pending(w, f"SVG to generate — {prompt}")
        if stype == "diagram" and not IMG_RE.search(md) and not PLACEHOLDER_RE.search(md):
            rep.warn(w, "diagram slide has neither an image nor a "
                        "'<<< Image: prompt >>>' placeholder — nothing marks it as pending")
        if not isinstance(s.get("estReadSeconds"), int) or s.get("estReadSeconds", 0) <= 0:
            rep.err(w, "estReadSeconds must be a positive int")
        secs += s.get("estReadSeconds") or 0

        # images: markdown embeds and assets[] must agree, flat paths, files present
        embedded = set(IMG_RE.findall(md))
        listed = {a.get("path") for a in (s.get("assets") or []) if isinstance(a, dict)}
        for a in (s.get("assets") or []):
            if not isinstance(a, dict) or "path" not in a or "alt" not in a:
                rep.err(w, f"assets entry must be {{alt, path}}, got {a!r}")
        for p in embedded | listed:
            if not p:
                continue
            if not p.startswith("assets/") or p.count("/") != 1:
                rep.err(w, f"image path '{p}' must be flat 'assets/<file>'")
            elif not os.path.exists(os.path.join(tdir, p)):
                rep.err(w, f"image '{p}' referenced but file is missing")
            elif p.endswith(".svg"):
                rep.check_svg(w, p, os.path.join(tdir, p))
        for p in embedded - listed:
            rep.err(w, f"image '{p}' embedded in markdown but not listed in assets[]")
        for p in listed - embedded:
            rep.err(w, f"asset '{p}' listed but not embedded in markdown")

        # cross-links must resolve to a real topic slug
        for target in LINK_RE.findall(md):
            if target not in all_slugs:
                rep.err(w, f"cross-link '[...]({target})' points at no existing topic")

        for mid in (s.get("mcqIds") or []):
            mcq_backrefs.setdefault(mid, s.get("id"))

    # estReadMinutes is authored, not generated (regen_v3.py copies it through), and the
    # existing corpus follows no single formula — so only flag values that are wildly off.
    want_min = max(1, round(secs / 60))
    got_min = t.get("estReadMinutes")
    if not isinstance(got_min, int) or got_min < 1:
        rep.err(rel, f"estReadMinutes must be a positive int, got {got_min!r}")
    elif not 0.5 * want_min <= got_min <= 2.5 * want_min:
        rep.warn(rel, f"estReadMinutes {got_min} implausible for {secs}s of slides (~{want_min})")

    # ---- mcq.json
    n_mcq = 0
    mp = os.path.join(tdir, "mcq.json")
    if os.path.exists(mp):
        m = load(mp, rep, f"{rel}/mcq.json")
        if m is not None:
            if m.get("topicId") != slug:
                rep.err(f"{rel}/mcq.json", f"topicId '{m.get('topicId')}' != '{slug}'")
            mcqs = m.get("mcqs")
            if not isinstance(mcqs, list):
                rep.err(f"{rel}/mcq.json", "mcqs[] missing or not a list")
                mcqs = []
            n_mcq = len(mcqs)
            seen_q, per_slide = set(), {}
            for q in mcqs:
                qid = q.get("id", "<no id>")
                w = f"{rel}/mcq.json [{qid}]"
                if qid in seen_q:
                    rep.err(w, "duplicate mcq id")
                seen_q.add(qid)
                sidref = q.get("slideId")
                if sidref not in seen_ids:
                    rep.err(w, f"slideId '{sidref}' is not a slide in this topic")
                elif not re.fullmatch(re.escape(sidref) + r"-q\d+", qid or ""):
                    rep.err(w, f"id must be '<slideId>-q<N>' (slideId '{sidref}')")
                per_slide.setdefault(sidref, []).append(qid)
                opts = q.get("options")
                if not isinstance(opts, list) or len(opts) != 4:
                    rep.err(w, f"needs exactly 4 options, got "
                               f"{len(opts) if isinstance(opts, list) else opts!r}")
                else:
                    if any(not isinstance(o, str) or not o.strip() for o in opts):
                        rep.err(w, "an option is empty")
                    if len({o.strip().lower() for o in opts if isinstance(o, str)}) != 4:
                        rep.err(w, "options are not all distinct")
                ci = q.get("correctIndex")
                if not isinstance(ci, int) or not 0 <= ci <= 3:
                    rep.err(w, f"correctIndex must be 0-3, got {ci!r}")
                else:
                    rep.answer_pos[f"{area}/{group}"][ci] += 1
                if not (q.get("explanation") or "").strip():
                    rep.err(w, "explanation is empty — it must teach")
                elif len(q["explanation"]) < 60:
                    rep.warn(w, f"explanation is thin ({len(q['explanation'])} chars)")
                if q.get("difficulty") not in DIFFICULTIES:
                    rep.err(w, f"difficulty '{q.get('difficulty')}' not in {sorted(DIFFICULTIES)}")
                if q.get("level") not in LEVELS:
                    rep.err(w, f"level '{q.get('level')}' not in {sorted(LEVELS)}")
                if not (q.get("question") or "").strip():
                    rep.err(w, "question is empty")
            # two-way consistency with slide.mcqIds
            for s in slides:
                declared = set(s.get("mcqIds") or [])
                actual = set(per_slide.get(s.get("id"), []))
                if declared != actual:
                    rep.err(f"{rel} [{s.get('id')}]",
                            f"mcqIds {sorted(declared)} != mcqs pointing here {sorted(actual)}")
            for mid, sid in mcq_backrefs.items():
                if mid not in seen_q:
                    rep.err(f"{rel} [{sid}]", f"mcqIds references '{mid}' which does not exist")
    elif mcq_backrefs:
        rep.err(rel, "slides declare mcqIds but mcq.json is missing")
    else:
        rep.warn(rel, "no mcq.json — no comprehension check for this topic")

    # ---- interview.json
    n_iq = 0
    ip = os.path.join(tdir, "interview.json")
    if os.path.exists(ip):
        d = load(ip, rep, f"{rel}/interview.json")
        if d is not None:
            if d.get("topicId") != slug:
                rep.err(f"{rel}/interview.json", f"topicId '{d.get('topicId')}' != '{slug}'")
            qs = d.get("interviewQuestions")
            if not isinstance(qs, list):
                rep.err(f"{rel}/interview.json", "interviewQuestions[] missing or not a list")
                qs = []
            n_iq = len(qs)
            seen = set()
            for n, q in enumerate(qs, 1):
                qid = q.get("id", "<no id>")
                w = f"{rel}/interview.json [{qid}]"
                if qid in seen:
                    rep.err(w, "duplicate interview question id")
                seen.add(qid)
                if not re.fullmatch(re.escape(slug) + r"-iq\d+", qid or ""):
                    rep.err(w, f"id must be '{slug}-iq<N>'")
                question = (q.get("question") or "").strip()
                if not question:
                    rep.err(w, "question is empty")
                elif question[-1] not in "?.":
                    # Imperative prompts ("Walk me through…", "Design a…") are real interview
                    # questions and legitimately end in '.', so only flag missing punctuation.
                    rep.warn(w, "question has no terminal punctuation ('?' or '.')")
                ans = q.get("answerMarkdown") or ""
                if not ans.strip():
                    rep.err(w, "answerMarkdown is empty")
                else:
                    check_band(rep, w, "answerMarkdown", ans, ANSWER_BAND)
                    if HEADING.search(outside_fences(ans)):
                        rep.err(w, "answerMarkdown contains a '#' heading")
                    if ANSWER_Q_HDR.match(ans):
                        rep.err(w, "answerMarkdown starts with its own '**Q:' header — the app "
                                   "already renders '<star>**Q: <question>**' above it "
                                   "(models.dart toBlockMarkdown), so the question would appear "
                                   "twice. Start with the answer itself.")
                if not isinstance(q.get("mostAsked"), bool):
                    rep.err(w, f"mostAsked must be a bool, got {q.get('mostAsked')!r}")
                if q.get("level") not in LEVELS:
                    rep.err(w, f"level '{q.get('level')}' not in {sorted(LEVELS)}")
            if qs and not any(q.get("mostAsked") for q in qs):
                rep.warn(f"{rel}/interview.json",
                         "no question flagged mostAsked — the app badges/sorts on it")
            if len(qs) > 1 and all(q.get("mostAsked") for q in qs):
                rep.warn(f"{rel}/interview.json",
                         f"all {len(qs)} questions are mostAsked — the badge sorts nothing; "
                         "reserve it for genuinely high-frequency questions")
    else:
        # Every v3 topic ships interview questions. A warning let a half-written topic
        # (killed mid-authoring, topic.json + mcq.json on disk) pass silently.
        rep.err(rel, "no interview.json — every topic must ship interview questions")

    # stray files
    for name in os.listdir(tdir):
        if name in ("topic.json", "mcq.json", "interview.json", "assets") \
                or name.startswith("."):
            continue
        rep.warn(rel, f"unexpected file/dir '{name}'")

    return len(slides), n_mcq, n_iq


def topic_dirs(target):
    if not os.path.isdir(CONTENT):
        sys.exit(f"no content/ directory at {CONTENT}")
    out = []
    for area in sorted(os.listdir(CONTENT)):
        adir = os.path.join(CONTENT, area)
        if not os.path.isdir(adir):
            continue
        for grp in sorted(os.listdir(adir)):
            gdir = os.path.join(adir, grp)
            if not os.path.isdir(gdir):
                continue
            for top in sorted(os.listdir(gdir)):
                tdir = os.path.join(gdir, top)
                if os.path.isdir(tdir) and os.path.exists(os.path.join(tdir, "topic.json")):
                    out.append(tdir)
    if target:
        want = target.strip("/").split("/")
        out = [d for d in out
               if os.path.relpath(d, CONTENT).split(os.sep)[:len(want)] == want]
        if not out:
            sys.exit(f"no topics matched '{target}'")
    return out


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    flags = {a for a in sys.argv[1:] if a.startswith("--")}
    strict, quiet = "--strict" in flags, "--quiet" in flags

    every = topic_dirs(None)
    all_slugs = {os.path.basename(d) for d in every}
    targets = topic_dirs(args[0]) if args else every

    # Topic slugs double as topic ids and as cross-link targets, so a slug used by two
    # topics makes every '[...](slug)' link to it ambiguous — it silently resolves to
    # whichever the reader isn't on. Always computed over the whole corpus, never just
    # the requested scope, since collisions are cross-area by nature.
    by_slug = collections.defaultdict(list)
    for d in every:
        by_slug[os.path.basename(d)].append(os.path.relpath(d, CONTENT))

    rep = Report()
    for slug, where in sorted(by_slug.items()):
        if len(where) > 1:
            rep.warn("content", f"slug '{slug}' is used by {len(where)} topics "
                                f"({', '.join(where)}) — cross-links to it are "
                                "ambiguous and the ids collide")

    slides = mcqs = iqs = 0
    for tdir in targets:
        s, m, i = validate_topic(tdir, all_slugs, rep)
        slides += s
        mcqs += m
        iqs += i

    # Answer-position skew: a learner who always picks the same letter should not win.
    for bank, tally in sorted(rep.answer_pos.items()):
        total = sum(tally.values())
        if total < 4:
            continue
        idx, hits = tally.most_common(1)[0]
        # Small banks can't be judged statistically, but an all-one-answer bank is
        # always wrong — so tighten the threshold instead of skipping them.
        limit = 0.45 if total >= 8 else 0.75
        if hits / total > limit:
            rep.warn(bank, f"MCQ answer-position skew — index {idx} is correct in "
                           f"{hits}/{total} ({hits / total:.0%}) of this group's MCQs; "
                           f"spread of {dict(sorted(tally.items()))} "
                           "(always-pick-one-letter should not beat guessing)")

    if not quiet:
        for line in rep.errors:
            print(f"ERROR   {line}")
        for line in rep.warnings:
            print(f"WARN    {line}")
        for line in rep.pendings:
            print(f"PENDING {line}")
        if rep.errors or rep.warnings or rep.pendings:
            print()
    print(f"{len(targets)} topics | {slides} slides | {mcqs} mcqs | {iqs} interview questions")
    if rep.pendings:
        print(f"{len(rep.pendings)} deferred SVGs — find them with: "
              "grep -rn '<<< Image:' content/")
    print(f"{len(rep.errors)} errors | {len(rep.warnings)} warnings"
          + ("  (--strict: warnings count as errors)" if strict else ""))
    return 1 if (rep.errors or (strict and rep.warnings)) else 0


if __name__ == "__main__":
    sys.exit(main())
