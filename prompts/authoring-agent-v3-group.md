# Authoring agent — one group of schema-v3 content

Shared spec for the `system-design` authoring fan-out. An orchestrator hands each agent one
**group slug** and the **line range** of that group's outline in the brief. Everything else is
here. Derived from a pilot run of `sd-fundamentals` (0 validator errors) plus the four defects
that pilot exposed.

## Your job

Author every topic in your assigned group as real content files under
`content/system-design/<your-group>/<topic-slug>/`.

## 1. Read your spec (narrow reads only — never read a whole file)

- `briefs/expanded/system-design.md` at the offset/limit you were given. That's your group's
  full outline: each topic's title, slug, level, scope line, and slide-by-slide plan. **Author
  exactly the topics and slides listed.** The outline is human-approved. Merge or drop a slide
  only if it is genuinely redundant, and say so in your report.
  **One exception — `(interview)` bullets.** A bullet marked `(interview)` is not a slide; it is a
  *seed* interview question for `interview.json`. It is a floor, not a cap: the brief lists one,
  the spec requires 2-3 per topic, so keep the seed (usually as the `mostAsked: true` one) and add
  the others yourself.

  **Interview-bank groups have no `(interview)` bullets at all** — in `interview-*` groups the
  *topic title itself is the interview question*. Six independent authors each worked this out from
  scratch, so it is written down now: make the topic's own question `iq1` with `mostAsked: true`,
  then promote two of the outline's `Follow-up:` bullets into `iq2`/`iq3`. Write each as a full
  standalone answer — **do not copy prose from the slides**; the slides teach the material, the
  interview answers model how to *say* it out loud under time pressure.
  **Do not also write a slide that restates the seed's scenario.** It reads like a natural closing
  "worked example" slide and several authors have written one by mistake — the seed belongs in
  `interview.json` and nowhere else.
- **Before you write a topic's `mcq.json`, re-count the brief's bullets against the slides you
  just wrote.** Silently dropping one bullet in a 9-slide topic is the single most common miss.
- `AUTHORING.md` lines 1-140 — the quality bar and voice. **Read it for the *voice and value
  filter only*.** It is the v2 doc: its char-band table and its `interview` Card type are stale.
  `tools/validate_v3.py`'s `BANDS` are the authoritative lengths (they are calibrated higher, and
  match the shipped corpus). Write to the validator, not to `AUTHORING.md`'s numbers.

## 2. The schema (a validator enforces all of this)

Copy the exact shape from this reference topic — read all three of its files:
`content/system-design/sd-fundamentals/scalability-fundamentals/{topic.json,mcq.json,interview.json}`

**topic.json** — keys in this order:
`id, title, area, group, order, slug, summary, level, slideCount, estReadMinutes, slides`

- `id` = `slug` = topic folder name. `area` = `"system-design"`. `group` = your group slug.
- `order` = position within the group, from 1, following the brief's sequence.
- `level` ∈ `beginner|intermediate|advanced|expert` — from the brief.
- `summary` = 1-2 sentence hook, ~100-260 chars.
- `slideCount` = exact slide count. `estReadMinutes` = `round(sum(estReadSeconds)/60)`, min 1.

Each slide — keys in this order:
`id, order, sectionTitle, subTitle, type, markdown, assets, hasCode, hasTable, estReadSeconds, mcqIds`

- `id` = `"<topic-slug>-s01"`, `-s02`, … zero-padded, contiguous from 1, matching `order`.
- `sectionTitle` = the Subtopic heading, required. `subTitle` = short label or `null`.
- `type` ∈ `overview|concept|compare|diagram|code|pitfall` — from the brief's `(type)` marker.
  **There is no `interview` slide type.** Where the brief marks a bullet `(interview)`, that is
  an interview *question*, not a slide — author it in `interview.json` and do not emit a slide
  for it. The validator rejects a slide typed `interview`.
- `markdown` — GitHub-flavored. **Never a `#` heading** (the title fields cover that).
  Bold key terms on first use, backticks for identifiers, real tables for comparisons.
- `assets` = `[]` unless the markdown embeds an image (see §4 — usually it won't).
- `hasCode` must equal whether the markdown contains a ``` fence.
  `hasTable` must equal whether it contains a markdown table. Both are checked — get them right.
  *Gotcha:* table detection looks for a `|…|` row plus a `|---|` separator, so **pipe-style ASCII
  art inside a fence can read as a table**. If you sketch a diagram in text, use arrow style
  (`Client -> Service : places order`) rather than `|`-delimited columns and box borders.
- `estReadSeconds` = positive int, roughly `words / 2.4`.
- `mcqIds` = ids of MCQs targeting this slide. Two-way consistency is enforced.

**Always open each topic with an `overview` slide** (`sectionTitle: "Snapshot"` works well) even
when the brief doesn't list one — every authored topic in this repo does, and the app expects it.

**mcq.json** — `{"topicId": "<slug>", "mcqs": [...]}`, each with
`id, slideId, question, options, correctIndex, explanation, difficulty, level`

- `id` = `"<slideId>-q1"`. `slideId` must be a real slide in this topic.
- **Exactly 4 options**, all substantive and distinct. No throwaway or joke options.
- **Spread `correctIndex` roughly evenly across 0-3 within your group.** Do it mechanically —
  every author who tried to hold a target index in their head while drafting prose got it wrong,
  including ones consciously trying to follow this rule. Use this procedure instead:
  1. Write the four options in whatever order reads best, tagging the true one `[CORRECT]`.
  2. Count that option's position (0-based) and write it into `correctIndex`.
  3. If your running group tally is drifting toward one index, **swap two options** and recount.

  Two failure modes this prevents, both observed repeatedly: drifting to ~68% of answers at index
  1, and — worse — writing `correctIndex` for a *different* option than the one you actually made
  true. That second one is a silently wrong answer key, not a cosmetic imbalance. Counting the
  position of a `[CORRECT]` tag catches both. `validate_v3.py` warns above 45% on one index (75%
  for banks under 8 MCQs); check your own tally before you finish either way.
- `explanation` teaches: why the right answer is right *and* why the most tempting wrong one is
  wrong. 100+ chars. Never reference an option by position ("option B") — positions get shuffled.
- `difficulty` ∈ `easy|medium|hard`, spread. `level` ∈ the four levels.
- Every MCQ's `slideId` must appear in that slide's `mcqIds`, and vice versa — exact match.
- Roughly 3-5 per topic, only where a check genuinely helps. Skip pure recall.

**interview.json** — `{"topicId": "<slug>", "interviewQuestions": [...]}`, each with
`id, question, answerMarkdown, mostAsked, level, subTitle`

- `id` = `"<topic-slug>-iq1"`, contiguous from 1.
- **2-3 questions per topic** — this is an interview-prep product and one per topic is too thin.
  Only genuinely-asked questions; if you can't picture an interviewer asking it, cut it.
- `question` ends with `?`.
- `answerMarkdown` ~600-1200 chars showing HOW to answer: a structure ("I'd start from…"), a
  concrete example, a crisp close. End with a line `**Testing:** <what's really being probed>`.
  No `#` headings.
  **Start with the answer itself — never repeat the question.** Do not open with
  `⭐ **Q: …**`: the app already renders `<star>**Q: <question>**` above your text
  (`models.dart` `toBlockMarkdown()`), so a Q header here shows the question twice. The validator
  now errors on it. (Older v2 content does this — don't copy that pattern.)
- `mostAsked` = **a real boolean, never null**, and **`true` for exactly one question per topic**
  (the highest-frequency one). The app badges and sorts on it, so if everything is starred
  nothing is.

## 3. Quality bar

- **Value filter is the top rule.** Every slide, MCQ and interview question must give real,
  non-obvious understanding. Filler, obvious or boring → cut it. Never pad to hit a number.
- Each slide is ONE mobile screen: claim → why → concrete example → takeaway. Depth comes from
  more slides, not longer slides.
- Concrete over abstract: real numbers, named technologies, tiny scenarios. Active voice, second
  person. Explain jargon on first use. No emoji.
- Cross-links are bare topic slugs — `[cache invalidation](cache-invalidation)` — and **only to
  slugs that exist**. If unsure the target is authored yet, write plain text instead; a dangling
  link is a validator error.
  **Author your topics in brief order.** Then a link to an earlier topic in your own group always
  resolves. A link to a *later* topic in your group does not exist yet at validate time — either
  write it as plain text, or add the link once that topic is written. Targets in other groups are
  usually unauthored while you run: default to plain text there. Don't spend effort hunting for
  whether some other group exists yet — the orchestrator does one link-backfill pass at the end.
  **`briefs/parts/_existing-slugs.txt`** lists every topic already authored repo-wide as
  `area/group/topic` — grep it (`grep -w '<slug>' briefs/parts/_existing-slugs.txt`) before writing
  a cross-link to another group. It is a snapshot from wave start, so absence is not proof.
  **The brief sometimes cites `sd-interview-playbook` (Area 17) — that group was RETIRED and merged
  into `sd-playbook`.** Never link it; link `sd-playbook` if it exists, else plain text.

## 4. Diagrams are DEFERRED — do not author SVGs

SVG authoring costs tokens we're saving for prose. For every slide the brief marks `(diagram)`:

- Write the slide's prose so it **stands on its own** without the picture.
- Put a placeholder token where the image goes, describing precisely what to draw:
  ```
  <<< Image: side-by-side comparison of a single large server vs eight small nodes behind a load balancer, labelled with cost and failure blast radius >>>
  ```
- Leave `assets: []`. Do **not** create any `.svg` file, and do **not** write an
  `![...](assets/...)` embed.

The token is stripped by all three consumers (app shows "🖼️ Diagram coming soon", the preview
shows a dashed box with the prompt, the validator reports it as `PENDING`), so this is safe to
ship. A later pass generates the real SVGs from these prompts — write the prompt well enough
that someone can draw it without re-reading the slide.

Keep the slide `type` as `diagram`. If a slide doesn't genuinely warrant a picture, make it
`concept` with no placeholder instead.

## 5. Validate and fix until clean

```bash
python3 tools/validate_v3.py system-design/<your-group>
```

Iterate to **0 errors**. `PENDING` lines are expected (your deferred diagrams). Char-length
`WARN`s are advisory — use judgement, don't contort prose to silence them.

**Do NOT run `tools/regen_v3.py`** — the orchestrator runs it once after the whole wave.

## 6. Rules of engagement

- Write files **one topic at a time**: `topic.json`, then `mcq.json`, then `interview.json`, then
  move on. Never batch all topics into one giant write — agents in this project have lost work to
  mid-response connection drops, and incremental writes survive that.
- Write **only** under `content/system-design/<your-group>/`. Never touch another group, another
  area, `data/`, the briefs, or any tool.
- If a topic in your outline collides with a slug outside your group, keep your slug and flag it.

## 7. Final report (under 25 lines)

- each topic slug with slide / MCQ / interview-question counts
- your group's `correctIndex` spread across 0-3
- the exact final line of `python3 tools/validate_v3.py system-design/<your-group>`
- how many `<<< Image: … >>>` placeholders you left
- anything you merged, dropped, or think is wrong in the brief
- anything ambiguous in this spec that should be fixed before the next wave
