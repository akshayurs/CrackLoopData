# Authoring agent — schema-v3 content, area-agnostic (wave 2+)

Shared spec for every authoring fan-out after `system-design`. An orchestrator hands each agent
an **area slug** plus one or more **group slugs** with the line range of each group's outline in
that area's brief. Everything else is here.

Derived from the `system-design` wave (473 topics, 0 validator errors) plus the depth upgrade
requested for wave 2: **this content has to carry a candidate from fresher to staff engineer.**

## Your job

Author every topic in your assigned groups as real content files under
`content/<area>/<group>/<topic-slug>/`.

## 0. The depth mandate (this is what changed from wave 1)

Someone who studies your groups end-to-end should be able to hold their own in a real interview
loop — junior screen through staff-level deep dive. That means:

- **More slides per topic than the brief's bullet count.** The brief's outline is a *floor*, not a
  cap. Target **9–16 slides** per topic (validator warns outside 5–24). Where the brief lists 7
  bullets and the material genuinely has more to teach — a mechanism the bullets skip, a real
  failure mode, a numbers/back-of-envelope slide, a "how this shows up in production" slide — add
  the slide. Never pad: every added slide must survive the value filter in §3.
- **Depth ladder inside each topic.** Open at fresher level, close above it. A well-built topic
  reads: snapshot → mechanism → concrete example → comparison/trade-off → real numbers →
  failure modes/pitfalls → the senior-level nuance (what a staff engineer knows that a junior
  doesn't). Mark the deep slides with `level`-appropriate MCQs rather than dumbing them down.
- **More interview questions, and real answers.** **3–5 per topic** (was 2–3), and they must
  span seniority: at least one a fresher would get, at least one a senior/staff candidate would
  get (design trade-off, "how would you debug this in prod", "why is it built this way").
  Answers are **900–1800 chars** — the validator's band is (200, 1200, 2200), so aim near the
  upper-middle. A one-paragraph answer is a wave-1 answer; we want the answer a candidate could
  actually say out loud for 2 minutes and sound senior.
- **More MCQs: 4–6 per topic**, spread across easy/medium/hard, with at least one that tests
  applied judgement rather than recall.
- **You may add topics.** If your group's outline has a genuine interview-relevant gap — a topic
  interviewers ask about that the brief simply missed — author it, appended after the brief's
  topics with the next `order`. Cap this at **2 extra topics per group**, use a clean kebab-case
  slug that collides with nothing in `briefs/parts/_existing-slugs.txt`, and list every addition
  in your final report with one line of justification. Do not add topics that belong to another
  group or another area.

Scale, not bloat: each *slide* stays one mobile screen (§3). Depth comes from more slides and
sharper interview answers, never from longer slides.

## 1. Read your spec (narrow reads only — never read a whole file)

- `briefs/expanded/<area>.md` at the offset/limit you were given. That's your group's full
  outline: each topic's title, slug, level, scope line, and slide-by-slide plan. **Author every
  topic and every bullet listed**, then extend per §0. Merge or drop a bullet only if it is
  genuinely redundant, and say so in your report.
  **One exception — `(interview)` bullets.** A bullet marked `(interview)` is not a slide; it is a
  *seed* interview question for `interview.json`. Keep the seed (usually as the `mostAsked: true`
  one) and add the rest yourself to reach 3–5.
  **Never write a slide that restates the seed's scenario** — the seed belongs in `interview.json`
  and nowhere else. (Wave-1 authors repeatedly wrote a closing "worked example" slide that did
  exactly this.)
- **Before you write a topic's `mcq.json`, re-count the brief's bullets against the slides you
  just wrote.** Silently dropping one bullet is the single most common miss.
- `AUTHORING.md` lines 1–140 — **for the voice and value filter only.** It is the v2 doc: its
  char-band table and its `interview` Card type are stale. `tools/validate_v3.py`'s `BANDS` are
  authoritative. Write to the validator, not to `AUTHORING.md`'s numbers.

## 2. The schema (a validator enforces all of this)

Copy the exact shape from this reference topic — read all three of its files:
`content/system-design/sd-fundamentals/scalability-fundamentals/{topic.json,mcq.json,interview.json}`

**topic.json** — keys in this order:
`id, title, area, group, order, slug, summary, level, slideCount, estReadMinutes, slides`

- `id` = `slug` = topic folder name. `area` = your area slug. `group` = your group slug.
- `order` = position within the group, from 1, following the brief's sequence.
- `level` ∈ `beginner|intermediate|advanced|expert` — from the brief.
- `summary` = 1–2 sentence hook, ~100–260 chars.
- `slideCount` = exact slide count. `estReadMinutes` = `round(sum(estReadSeconds)/60)`, min 1.

Each slide — keys in this order:
`id, order, sectionTitle, subTitle, type, markdown, assets, hasCode, hasTable, estReadSeconds, mcqIds`

- `id` = `"<topic-slug>-s01"`, `-s02`, … zero-padded, contiguous from 1, matching `order`.
  **If you are adding slides to an already-authored topic (remediation), APPEND new ids after the
  existing highest number — never renumber existing slides.** `mcq.json` references slides by
  `slideId`; renumbering silently orphans every MCQ that pointed at the old id.
- `sectionTitle` = the Subtopic heading, required. `subTitle` = short label or `null`.
- `type` ∈ `overview|concept|compare|diagram|code|pitfall` — from the brief's `(type)` marker.
  **There is no `interview` slide type** — the validator rejects it.
- `markdown` — GitHub-flavored. **Never a `#` heading** (the title fields cover that).
  Bold key terms on first use, backticks for identifiers, real tables for comparisons.
- `assets` = `[]` unless the markdown embeds an image (see §4 — usually it won't).
- `hasCode` must equal whether the markdown contains a ``` fence.
  `hasTable` must equal whether it contains a markdown table. Both are checked.
  *Gotcha:* table detection looks for a `|…|` row plus a `|---|` separator, so **pipe-style ASCII
  art inside a fence can read as a table**. Sketch diagrams in arrow style
  (`Client -> Service : places order`), not `|`-delimited boxes.
- `estReadSeconds` = positive int, roughly `words / 2.4`.
- *JSON-escaping gotchas that broke wave-2 writes, again this wave:* straight double-quotes used
  for emphasis inside a string (`the "copy" in "copy-on-write"`) must be escaped, a literal newline
  inside a markdown string must be `\n` not an actual line break, and never backslash-escape
  ordinary punctuation (`\,`) inside an already-escaped `\"…\"` span — all three produce
  unparseable JSON that the validator reports as a file-level error. **Verify immediately after
  every single file write**, not just at validation time:
  `python3 -c "import json; json.load(open('content/<area>/<group>/<slug>/topic.json'))"`
  (repeat for `mcq.json`/`interview.json`). Catching this one file at a time is cheap; catching it
  after several more topics means re-diffing to find which write broke.
- `mcqIds` = ids of MCQs targeting this slide. Two-way consistency is enforced.

**Always open each topic with an `overview` slide** (`sectionTitle: "Snapshot"` works well) even
when the brief doesn't list one — every authored topic in this repo does, and the app expects it.

**mcq.json** — `{"topicId": "<slug>", "mcqs": [...]}`, each with
`id, slideId, question, options, correctIndex, explanation, difficulty, level`

- **Budget before you draft.** Tagging `mcqIds` on every concept/diagram/pitfall slide as you
  write them naturally produces 7–9 candidates against a 4–6 band, forcing a trim pass afterward —
  and a late trim risks leaving a slide's `mcqIds` out of sync with `mcq.json`. Instead, once your
  slide list for a topic is set, **decide up front which 4–6 slides earn a check** (the ones where
  a wrong answer reveals a real misunderstanding) and only tag those. If you do end up trimming,
  immediately re-check that every slide's `mcqIds` and every MCQ's `slideId` still agree — see
  below.
- `id` = `"<slideId>-q1"`. `slideId` must be a real slide in this topic.
- **Exactly 4 options**, all substantive and distinct. No throwaway or joke options.
- **Spread `correctIndex` roughly evenly across 0–3 within each group. This recipe is MANDATORY
  per topic, not advisory** — skew to one index is the norm on a first pass, not the exception
  (agents this wave saw 50% on index 1, and 4 of 6 on one index, despite believing they'd varied
  it). Do it mechanically:
  1. Write the four options in whatever order reads best, tagging the true one `[CORRECT]`.
  2. Count that option's position (0-based) and write it into `correctIndex`.
  3. If your running group tally drifts toward one index, **rebalance by physically moving the
     option text** — reorder the four option strings so the correct one lands in a different
     slot — then recount from the moved text and write the new `correctIndex`.

  This prevents two observed failure modes: drifting to ~68% of answers at index 1, and — worse —
  writing `correctIndex` for a *different* option than the one you actually made true (a silently
  wrong answer key). `validate_v3.py` warns above 45% on one index (75% for banks under 8 MCQs).
  **Changing the `correctIndex` integer alone, without moving the option text, is never a valid
  rebalance — it is always a bug.** Two topics this wave shipped exactly that bug undetected until
  after-the-fact review: `data-engineering/data-governance/data-catalogs-metadata` (all 5 MCQs
  landed on `correctIndex: 1`) and `data-quality-fundamentals` in the same group (4 of 5 on
  index 3) — in both cases the integer had been edited but the true answer never moved.
- **Verify the key mechanically after writing, and again after any rebalance.** Once `mcq.json` is
  written, print what the file actually encodes and read that — do not re-read your draft from
  memory:
  ```bash
  python3 -c "
  import json,sys
  d=json.load(open(sys.argv[1]))
  for m in d['mcqs']:
      print(m['id']); print('  Q:',m['question'])
      print('  KEY:',m['options'][m['correctIndex']])
      print('  WHY:',m['explanation'][:200]); print()
  " <path to mcq.json>
  ```
  Confirm the printed `KEY` line is the option the `WHY` line argues for. Rebalancing for skew is
  itself a common way to (re)introduce a wrong key, so re-run this after every rebalance, not just
  once at the end.

  **Reading your own explanations as prose is not sufficient and has already failed.** An agent
  this wave did exactly that and still shipped two wrong keys (in its `tracing-gc-mark-sweep-and-compact`
  and `interpreters-tree-walking-vs-bytecode` topics); printing `options[correctIndex]` is what
  caught them. Re-reading re-derives the answer you *intended*, while the printout forces the
  answer the JSON *encodes* into view — and the gap between those two is precisely this bug. Use
  the prose re-read only as a secondary sense-check on top of the printout.
- `explanation` teaches: why the right answer is right *and* why the most tempting wrong one is
  wrong. 100+ chars. Never reference an option by position ("option B") — positions shuffle.
- `difficulty` ∈ `easy|medium|hard`, spread. `level` ∈ the four levels.
- Every MCQ's `slideId` must appear in that slide's `mcqIds`, and vice versa — exact match.
- **4–6 per topic**, only where a check genuinely helps. Skip pure recall.

**interview.json** — `{"topicId": "<slug>", "interviewQuestions": [...]}`, each with
`id, question, answerMarkdown, mostAsked, level, subTitle`

- `id` = `"<topic-slug>-iq1"`, contiguous from 1.
- **3–5 questions per topic**, spanning seniority (§0). Only genuinely-asked questions; if you
  can't picture an interviewer asking it, cut it.
- `question` ends with `?`.
- `answerMarkdown` **900–1800 chars** showing HOW to answer, not just the facts:
  an opening frame ("I'd start from the failure it prevents…"), the mechanism in 2–4 crisp
  beats, a **concrete example with real numbers or a named technology**, the trade-off or
  when-not-to, then a one-line close. End with a line `**Testing:** <what's really being probed>`.
  No `#` headings. Short bold lead-ins and bullets are fine and read well on mobile.
  **Start with the answer itself — never repeat the question.** Do not open with
  `⭐ **Q: …**`: the app already renders `<star>**Q: <question>**` above your text
  (`models.dart` `toBlockMarkdown()`), so a Q header shows the question twice. The validator
  errors on it. (Older v2 content does this — don't copy that pattern.)
- `level` should track the question's seniority, so the app can filter a fresher's pass from a
  staff candidate's. `subTitle` = a short focus label (e.g. `"Trade-offs"`, `"Debugging"`,
  `"Fundamentals"`).
- `mostAsked` = **a real boolean, never null**, and **`true` for exactly one question per topic**
  (the highest-frequency one). The app badges and sorts on it.

## 3. Quality bar

- **Value filter is the top rule.** Every slide, MCQ and interview question must give real,
  non-obvious understanding. Filler, obvious or boring → cut it. Never pad to hit a number.
- Each slide is ONE mobile screen: claim → why → concrete example → takeaway. Depth comes from
  more slides, not longer slides.
- Concrete over abstract: real numbers, named technologies, tiny scenarios. Active voice, second
  person. Explain jargon on first use. No emoji.
- Where the material has a real command, config, query or code shape, **show it** in a fenced
  block with a language tag — a candidate should recognise the real thing, not a paraphrase.
- Cross-links are bare topic slugs — `[write-ahead log](write-ahead-logging)` — and **only to
  slugs that exist**; a dangling link is a validator error.
  **Author your topics in brief order.** Then a link to an earlier topic in your own group always
  resolves. A link to a *later* topic in your group, or one in another group/area, does not exist
  yet at validate time — this is where the same-wave problem bites, and "default to plain text
  when unsure" is not enough on its own: in a parallel wave, unsure is the normal state, and
  treating it as license to skip the link silently loses real links to sibling topics a concurrent
  agent is writing right now. **Never trust `briefs/parts/_existing-slugs.txt` as proof of
  absence** — it is a wave-start snapshot and goes stale the moment the wave begins. Before
  concluding a target doesn't exist, `ls content/<area>/<group>/<slug>/` (or the sibling
  group/area path) on disk. The working pattern: write the forward reference as plain text now,
  keep a mental (or scratch) note of what it should link to, then **backfill it into a real
  `[text](slug)` link the moment that target topic is written** — by you if it's in your own
  group, or leave it for the orchestrator's link-backfill pass if it's cross-group/area.
- **Watch inline code containing `[...](...)`-shaped text.** The validator's cross-link regex
  matches that shape anywhere in the markdown, including inside a fenced code block or backtick
  span — e.g. a route handler snippet with `` `[...](request)` `` reads as a dangling link to a
  topic called `request`. Reword the snippet (name the parameter, don't use bracket-paren
  adjacency) rather than triggering a false positive.

## 4. Diagrams are DEFERRED — do not author SVGs

For every slide the brief marks `(diagram)`:

- Write the slide's prose so it **stands on its own** without the picture.
- Put a placeholder token where the image goes, describing precisely what to draw:
  ```
  <<< Image: side-by-side comparison of a single large server vs eight small nodes behind a load balancer, labelled with cost and failure blast radius >>>
  ```
- Leave `assets: []`. Do **not** create any `.svg` file, and do **not** write an
  `![...](assets/...)` embed.

The token is stripped by all three consumers (app shows "🖼️ Diagram coming soon", the preview
shows a dashed box with the prompt, the validator reports it as `PENDING`), so it ships safely.
Write the prompt well enough that someone can draw it without re-reading the slide.

Keep the slide `type` as `diagram`. If a slide doesn't genuinely warrant a picture, make it
`concept` with no placeholder instead.

## 5. Validate and fix until clean

```bash
python3 tools/validate_v3.py <area>/<your-group>
```

Iterate to **0 errors** for every group you own. `PENDING` lines are expected (deferred
diagrams). Char-length `WARN`s are advisory — use judgement, don't contort prose to silence them.

**Validate every 2–3 topics, not just at the end.** The `correctIndex` skew check is group-level,
so it only fires once the whole group is written — wave-2 authors hit 50–55% skews after finishing
six topics and had to retroactively reorder nine questions' options. Running the validator
mid-group catches skew (and JSON-escaping breakage) while the fix is still one topic wide.

**Do NOT run `tools/regen_v3.py`** — the orchestrator runs it once after the whole wave.

## 6. Rules of engagement

- Write files **one topic at a time**: `topic.json`, then `mcq.json`, then `interview.json`, then
  move on. Never batch all topics into one giant write — agents in this project have lost work to
  mid-response connection drops, and incremental writes survive that.
- Write **only** under `content/<area>/<your-group>/`. Never touch another group, another area,
  `data/`, the briefs, the index/bundle, or any tool.
- Finish every topic you were assigned. If you are running out of room, say exactly which topics
  are unwritten in your report — never silently truncate.
- **Do not sub-delegate** (spawn your own sub-agents for slides/topics) unless the orchestrator
  explicitly told you to. You own your groups end to end.

## 7. Final report (under 25 lines)

- each topic slug with slide / MCQ / interview-question counts
- each group's `correctIndex` spread across 0–3
- the exact final line of `python3 tools/validate_v3.py <area>/<group>` per group
- how many `<<< Image: … >>>` placeholders you left
- any topics you ADDED beyond the brief, with one line of justification each
- anything you merged, dropped, or think is wrong in the brief
- anything ambiguous in this spec that should be fixed before the next wave
