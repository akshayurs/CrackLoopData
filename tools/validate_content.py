#!/usr/bin/env python3
"""Validate learning-content topics against the data contract + quality bar.

  python3 tools/validate_content.py databases/intro-to-dbms   # one topic
  python3 tools/validate_content.py --all                      # every topic

ERRORS (exit 1) break the contract — a client would mis-render or crash.
WARNINGS (exit 0) are quality-bar misses — content is valid but likely too thin.
Use ERRORS as a hard gate for generated content; treat WARNINGS as a review queue.
"""
import json, re, os, sys, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")
CONTENT = os.path.join(DATA, "content")

TYPES = {"overview", "concept", "code", "diagram", "compare", "pitfall", "interview"}
LEVELS = {"beginner", "intermediate", "advanced", "expert"}

# quality-bar thresholds (see AUTHORING.md)
MIN_AVG_BLOCK_CHARS = 550
MIN_BLOCKS = 14
MIN_MCQ_COVERAGE = 0.45      # fraction of non-interview blocks with >=1 MCQ
MIN_INTERVIEW = 3

def known_topic_ids():
    idx = json.load(open(os.path.join(DATA, "index.json")))
    return {t["id"] for g in idx["groups"] for t in g["topics"]}

TABLE_RE = re.compile(r"\n\|.*\|")
IMG_RE = re.compile(r"!\[([^\]]*)\]\((assets/[^)]+)\)")
LINK_RE = re.compile(r"(?<!\!)\[([^\]]+)\]\(([^)]+)\)")

def validate(topic_rel, ids):
    tdir = os.path.join(CONTENT, topic_rel)
    E, W = [], []
    def err(m): E.append(m)
    def warn(m): W.append(m)

    tpath = os.path.join(tdir, "topic.json")
    if not os.path.exists(tpath):
        return [f"{topic_rel}: no topic.json"], []
    try:
        t = json.load(open(tpath))
    except Exception as e:
        return [f"{topic_rel}: topic.json invalid JSON: {e}"], []

    folder = os.path.basename(topic_rel.rstrip("/"))
    for f in ("id", "title", "group", "order", "slug", "summary", "contentType", "blockCount", "blocks"):
        if f not in t: err(f"missing topic field '{f}'")
    if t.get("id") != folder: err(f"id '{t.get('id')}' != folder '{folder}'")
    if t.get("slug") != folder: err(f"slug '{t.get('slug')}' != folder '{folder}'")
    if t.get("level") not in LEVELS and t.get("level") is not None:
        err(f"bad topic level '{t.get('level')}'")

    blocks = t.get("blocks", [])
    if t.get("blockCount") != len(blocks): err(f"blockCount {t.get('blockCount')} != {len(blocks)} blocks")
    if [b.get("order") for b in blocks] != list(range(1, len(blocks) + 1)):
        err("block orders not contiguous 1..n")

    # mcq
    mpath = os.path.join(tdir, "mcq.json")
    mcqs, mcq_ids = [], set()
    if os.path.exists(mpath):
        try:
            mcqs = json.load(open(mpath)).get("blockMcqs", [])
        except Exception as e:
            err(f"mcq.json invalid JSON: {e}")
        mcq_ids = {q.get("id") for q in mcqs}

    block_ids = {b.get("id") for b in blocks}
    referenced = set()
    interview_n = 0
    covered = non_interview = 0
    total_chars = 0

    for b in blocks:
        bid = b.get("id", "?")
        for f in ("id", "topicId", "order", "type", "markdown", "hasCode", "hasTable", "estReadSeconds", "mcqIds"):
            if f not in b: err(f"{bid}: missing block field '{f}'")
        if b.get("topicId") != t.get("id"): err(f"{bid}: topicId mismatch")
        if b.get("type") not in TYPES: err(f"{bid}: bad type '{b.get('type')}'")
        if b.get("level") is not None and b.get("level") not in LEVELS: err(f"{bid}: bad level")
        md = b.get("markdown", "")
        total_chars += len(md)
        if b.get("hasCode") != ("```" in md): err(f"{bid}: hasCode wrong")
        if b.get("hasTable") != bool(TABLE_RE.search(md)): err(f"{bid}: hasTable wrong")
        if b.get("type") == "interview":
            interview_n += 1
            if "**Q:" not in md: err(f"{bid}: interview block has no '**Q:' line")
        else:
            non_interview += 1
            if b.get("mcqIds"): covered += 1
        for alt, p in IMG_RE.findall(md):
            if not any(a.get("path") == p for a in b.get("assets", [])):
                err(f"{bid}: image {p} not in assets[]")
            if not os.path.exists(os.path.join(tdir, p)):
                err(f"{bid}: asset file missing {p}")
        for _txt, href in LINK_RE.findall(md):
            if href.startswith("assets/"):
                continue
            if href.startswith("http") or href.endswith(".md") or href.startswith("/"):
                err(f"{bid}: bad cross-link '{href}' (use bare topic slug)")
            elif href not in ids:
                warn(f"{bid}: cross-link '{href}' resolves to no known topic")
        referenced |= set(b.get("mcqIds", []))

    for q in mcqs:
        qid = q.get("id", "?")
        if q.get("blockId") not in block_ids: err(f"mcq {qid}: blockId not a block")
        if len(q.get("options", [])) != 4: err(f"mcq {qid}: needs exactly 4 options")
        if not (isinstance(q.get("correctIndex"), int) and 0 <= q["correctIndex"] <= 3):
            err(f"mcq {qid}: correctIndex out of range")
        if not q.get("explanation"): err(f"mcq {qid}: empty explanation")
        if q.get("difficulty") not in {"easy", "medium", "hard"}: err(f"mcq {qid}: bad difficulty")
    dupes = [i for i in mcq_ids if sum(1 for q in mcqs if q.get("id") == i) > 1]
    if dupes: err(f"duplicate mcq ids: {dupes}")
    if referenced - mcq_ids: err(f"blocks reference missing mcq ids: {sorted(referenced - mcq_ids)}")
    if mcq_ids - referenced: err(f"orphan mcqs (no block references them): {sorted(mcq_ids - referenced)}")

    # ---- quality bar (warnings) ----
    if blocks:
        avg = total_chars // len(blocks)
        if avg < MIN_AVG_BLOCK_CHARS: warn(f"avg block {avg} chars < {MIN_AVG_BLOCK_CHARS} (too thin)")
    if len(blocks) < MIN_BLOCKS: warn(f"only {len(blocks)} blocks (< {MIN_BLOCKS})")
    if interview_n < MIN_INTERVIEW: warn(f"only {interview_n} interview blocks (< {MIN_INTERVIEW})")
    if non_interview:
        cov = covered / non_interview
        if cov < MIN_MCQ_COVERAGE: warn(f"MCQ coverage {cov:.0%} of concept blocks (< {MIN_MCQ_COVERAGE:.0%})")
    if not any(b.get("level") in ("intermediate", "advanced", "expert") for b in blocks):
        warn("no intermediate+ blocks — not layered by level")
    return [f"{topic_rel}: {m}" for m in E], [f"{topic_rel}: {m}" for m in W]

def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    ids = known_topic_ids()
    if "--all" in sys.argv:
        rels = sorted(os.path.relpath(os.path.dirname(p), CONTENT) for p in glob.glob(f"{CONTENT}/*/*/topic.json"))
    else:
        rels = args
    if not rels:
        print("usage: validate_content.py <group>/<topic> | --all"); sys.exit(2)
    allE, allW = [], []
    for r in rels:
        E, W = validate(r, ids)
        allE += E; allW += W
    for m in allW: print("WARN ", m)
    for m in allE: print("ERROR", m)
    print(f"\n{len(rels)} topic(s): {len(allE)} errors, {len(allW)} warnings")
    sys.exit(1 if allE else 0)

if __name__ == "__main__":
    main()
