# Authoring CrackLoop learning content — the quality bar

This is the **write-side contract**. [CONSUMING.md](CONSUMING.md) tells a client how to *read* the data; this tells an author (human or LLM) how to *produce* it so users actually **learn**, not just skim flashcards.

The reference implementation is **[intro-to-dbms](data/content/databases/intro-to-dbms/topic.json)** — the first topic rebuilt to this bar. When in doubt, open it and match it.

> **The problem we're fixing.** The v1 corpus is flashcard-shallow: ~360 characters per block, bullet lists with no worked examples, no "why", no depth for anyone past day one. Users bounce because there's nothing to sink into. Every topic gets rebuilt to the bar below.

---

## 0. TL;DR for a generator

Produce, per topic, **two files** — `topic.json` and `mcq.json` — into `data/content/<group>/<topic-slug>/`. Then a human/script runs `tools/validate_content.py` (hard gate) and `tools/regen_index_bundle.py` (counts, checksums, bundle). You **only** author the two content files + any SVG assets; everything in `index.json` and `bundle.json.gz` is generated.

The bar, in one line: **20–28 blocks, layered beginner→advanced, every claim earns its place with a why + a concrete example, ≥1 worked example, ≥1 comparison table, ≥2 pitfalls, 6–9 interview cards, and ~one MCQ per teaching block.**

---

## 1. What "deep enough" means (the depth bar)

The single biggest change from v1. Each block must **teach**, not just **name**.

| Dimension | v1 (too thin) | The bar |
|---|---|---|
| Chars per block (avg) | ~360 | **600–900** (overview/interview can be shorter; concept/compare longer) |
| Blocks per topic | ~12–17 | **20–28** |
| Structure of a concept block | 3–5 bare bullets | **Claim → why it's true → concrete example/number → takeaway** |
| Worked examples | none | **≥1** block that walks a concrete scenario step by step |
| Reading time | ~6 min | **12–22 min** |
| MCQs | ~8, sparse | **~1 per non-interview teaching block**; 4 sharp options + teaching explanation |

**Every block answers "so what?"** A bullet like "MVCC handles concurrency" is v1. The bar is: *what* MVCC does, *why* it beats locking here, and a one-line example of two transactions not blocking. Prefer concrete nouns and numbers ("a million rows → a handful of page reads") over adjectives ("very fast").

Depth ≠ padding. If a sentence doesn't add a why, an example, or a distinction, cut it. Dense-and-short beats long-and-vague.

---

## 2. Topic anatomy (the section arc)

A topic is an **ordered list of blocks** grouped into sections. Follow this arc — it's the shape of intro-to-dbms and generalizes to every group:

1. **Snapshot** (`sectionNumber: 0`) — 1–2 `overview` blocks: the one-paragraph mental model + a "X vs Y vs Z" disambiguation. Hook with a concrete analogy.
2. **Why it exists / the problem** — 2–3 blocks: the pain this concept solves, a `compare` against the naive alternative, and a **worked example** that makes the pain concrete.
3. **The core mechanics** — 2–4 `concept` blocks: how it actually works. This is where intermediate/advanced depth lives.
4. **Variants / kinds / trade-offs** — `concept` + `compare` blocks with real tables and decision guidance.
5. **A peek inside / architecture** — a `diagram` block (real SVG, see §5) + a walkthrough `concept` block ("the life of a …").
6. **In practice** — real tools/names + a `code` block where the topic is code-relevant.
7. **When NOT to / limits** — a `compare` block; every technology has a wrong use.
8. **Pitfalls** — ≥2 `pitfall` blocks (one beginner-misconception, one subtler intermediate trap).
9. **Interview Q&A** — 6–9 `interview` blocks (see §4).

Not every topic needs all nine, but a topic with no worked example, no pitfalls, or no interview section is **below bar**.

### Block-type mix (target, for a ~24-block topic)
`overview` 2 · `concept` 8–10 · `compare` 2–3 · `diagram` 1 (if it aids) · `code` 0–2 (code topics only) · `pitfall` 2 · `interview` 6–9.

### Level layering (the skip/filter feature)
Layer with the `level` field so a returning user can go deeper and a beginner isn't drowned. Rough split: **~50% beginner, ~35% intermediate, ~15% advanced**. Put the essential mental model at `beginner`; put internals, edge cases, and formal theory at `intermediate`/`advanced`. Gold standard: 13 / 9 / 4.

---

## 3. Block-type playbook

| type | When | Must contain |
|---|---|---|
| `overview` | Snapshot cards | The mental model in ≤4 sentences + an analogy or a disambiguation table |
| `concept` | Standard teaching | Claim → why → concrete example → takeaway. The workhorse. |
| `compare` | Trade-offs, X vs Y, "when not to" | A real markdown table **plus** prose that says *how to decide*, not just the table |
| `diagram` | A structure/flow that's clearer visually | A real SVG (§5) + prose explaining each part; never rely on the image alone |
| `code` | Code-relevant topics | A fenced block that's **correct and runnable-looking**, comments explaining intent, and the expected output |
| `pitfall` | Misconceptions & traps | The wrong belief, *why* it's wrong, and the correct model. Beginner card = misconceptions; intermediate card = subtle traps. |
| `interview` | Q&A prep | See §4 |

### `interview` blocks — the format is strict
Markdown starts with the question line, then the model answer:

```
⭐ **Q: Explain ACID with an example.**

<model answer in plain markdown — 3–6 sentences, structured, shows reasoning>
```

- Lead with `⭐` **only** for genuinely most-asked questions (surfaced/badged by the app). ~half a topic's interview cards.
- The answer must **demonstrate how to answer**, not just state facts: give structure ("I'd start from the data and the guarantees…"), a concrete example, and a crisp close. This is the difference between passing and failing a real interview.
- `subTitle` = a short label for the question (e.g. "Explain ACID").
- Interview cards are **separate** from MCQs — open-ended, no options.

---

## 4. MCQ playbook (`mcq.json`)

- **Coverage:** roughly **one MCQ per non-interview teaching block** (concept/compare/diagram/code). Skip pure overview recaps and interview cards.
- **Exactly 4 options**, `correctIndex` 0–3. Put the answer in a **random-ish position** across the bank — don't always make it B.
- **Distractors must be plausible** — common misconceptions or adjacent-but-wrong ideas, not obvious throwaways ("a spreadsheet application"). A good distractor is something a half-learner would actually pick.
- **`explanation` teaches** — say *why the right answer is right* (and ideally why the tempting wrong one is wrong), in one or two sentences. It's shown after answering; it's a teaching moment.
- **`difficulty`** ∈ `easy | medium | hard`; spread them. **`level`** mirrors the block's level.
- **IDs:** `<topic-slug>-b<NN>-q<M>` (e.g. `intro-to-dbms-b07-q1`). `blockId` must be a real block; the block's `mcqIds` must list back every MCQ that targets it (two-way consistency — the validator enforces it).

---

## 5. Images & diagrams — read this, it's currently the #1 bug

Two mechanisms, nothing else (no `imageUrl` field exists):

### A. Real SVG asset (preferred where a diagram genuinely helps)
1. Author a self-contained SVG into `data/content/<group>/<topic>/assets/<name>.svg`.
2. Reference it in markdown **relative to the topic folder — flat, no topic-slug segment**:
   ```
   ![clear descriptive alt text](assets/<name>.svg)
   ```
   ✅ `assets/dbms-architecture.svg`   ❌ `assets/intro-to-dbms/dbms-architecture.svg`
3. List it in the block's `assets[]`: `[{ "alt": "…", "path": "assets/<name>.svg" }]` — `path` **must byte-match** the markdown src.

> ⚠️ **Known corpus bug (54 topics, 144 refs):** existing markdown uses the nested form `assets/<topic-slug>/x.svg` while the file sits flat at `assets/x.svg`, so every real diagram renders **broken** in-app. New content must use the flat form. The fix for old content is mechanical (strip the `<topic-slug>/` segment).

**SVG house style** (match existing assets): `viewBox`, `font-family="-apple-system, Segoe UI, Roboto, sans-serif"`, arrow markers in `<defs>`, fixed **light-theme Material palette** — text `#202124`, primary `#4285F4` on `#E8F0FE`, neutral `#5F6368`/`#9AA0A6` on `#F1F3F4`. No `currentColor`, no CSS vars: assets render on a light card. 2–3-word labels only. See [dbms-architecture.svg](data/content/databases/intro-to-dbms/assets/dbms-architecture.svg).

### B. Placeholder (when no SVG is generated yet)
A literal token in the markdown — the app renders a "diagram coming soon" slot, never the raw text:
```
<<< Image: a detailed generation prompt describing the diagram >>>
```
The text after `Image:` is an **AI prompt**, not user copy. Use this only when a diagram would help but doesn't exist yet; don't emit placeholders just to hit a diagram count.

**Cross-links** use the bare target slug as href — `[normalization](normalization)` — never a URL, `.md`, or leading slash. Only link to slugs that exist in `index.json`.

---

## 6. Voice & style

- **Concrete over abstract.** Numbers, named tools, tiny scenarios. "≈O(log n), a handful of page reads" beats "efficient".
- **Active, direct, second person.** "You declare a constraint; the engine enforces it."
- **One idea per bullet**, but each bullet is a full thought with a because, not a fragment.
- **Analogies for the hook**, then drop them for precision.
- **No fluff, no meta** ("In this section we will…", "It is important to note"). No emoji except the `⭐` interview marker.
- **GitHub-flavored markdown**: `**bold**` for key terms on first use, `` `code` `` for identifiers/keywords, tables for comparisons, fenced blocks for code. Do **not** put `#` headings inside `markdown` — section/sub headings come from the `sectionTitle`/`subTitle` fields.
- Keep the reading level accessible; explain jargon the first time it appears.

---

## 7. The schema you author (vs what's generated)

**You write** these fields. **Generated** fields (marked ⚙) are recomputed by the tools — you may omit or approximate them; the pipeline overwrites them.

`topic.json`:
```jsonc
{
  "id": "<slug>",            // == folder name == slug
  "title": "Human Title",
  "group": "<group-slug>",
  "order": 1,                 // position within the group
  "slug": "<slug>",
  "summary": "1–2 sentence hook — what the learner walks away able to do.",
  "contentType": "learningTopic",
  "level": "beginner",        // topic's overall tier (or omit)
  "blockCount": 24,           // ⚙ regen fixes
  "estReadMinutes": 20,       // ⚙ regen fixes (sum of block estReadSeconds)
  "blocks": [ /* see below */ ]
}
```

each block:
```jsonc
{
  "id": "<slug>-b03",         // b + zero-padded order
  "topicId": "<slug>",
  "order": 3,                  // contiguous 1..n
  "sectionNumber": 1,          // consecutive blocks with same number/title = one section
  "sectionTitle": "Why it exists",
  "subTitle": "The pain before databases",   // or null
  "type": "concept",           // overview|concept|code|diagram|compare|pitfall|interview
  "level": "beginner",         // beginner|intermediate|advanced|expert, or omit
  "markdown": "…GFM…",
  "assets": [],                // {alt,path} only if markdown embeds an image
  "hasCode": false,            // ⚙ = ("```" in markdown)
  "hasTable": false,           // ⚙ = markdown has a table
  "estReadSeconds": 30,        // ⚙ = ~len/16 (+ code/table bump)
  "mcqIds": ["<slug>-b03-q1"]  // MCQs targeting this block ([] if none)
}
```

`mcq.json`:
```jsonc
{
  "topicId": "<slug>",
  "blockMcqs": [
    { "id": "<slug>-b03-q1", "blockId": "<slug>-b03",
      "question": "…", "options": ["…","…","…","…"], "correctIndex": 2,
      "explanation": "why right (and why the tempting wrong one is wrong)",
      "difficulty": "medium", "level": "beginner" }
  ]
}
```

**ID conventions are load-bearing** — the app and the validator match on them exactly: block `= <slug>-b<NN>`, MCQ `= <blockId>-q<M>`.

---

## 8. The pipeline (author → gate → generate)

```bash
# 1. Author (human or LLM): write topic.json + mcq.json + any assets/*.svg only.

# 2. Hard gate — must be 0 ERRORS before the content is accepted:
python3 tools/validate_content.py <group>/<slug>

# 3. Regenerate index counts/checksums + the bundle from the content files:
python3 tools/regen_index_bundle.py

# 4. Confirm nothing drifted:
python3 tools/regen_index_bundle.py --check     # exits non-zero on drift

# 5. Eyeball it (optional but recommended for the first topics of each group):
#    render topic.json to HTML and screenshot — see scratchpad/preview.py in the
#    session that built intro-to-dbms, or wire a proper renderer.
```

- **`tools/validate_content.py`** — ERRORS = contract violations (bad JSON, wrong counts, broken image path, dangling MCQ ref, non-4-option MCQ, malformed interview card). WARNINGS = quality-bar misses (avg block too thin, <14 blocks, <3 interview cards, low MCQ coverage, no level layering). **Gate generated content on 0 errors; triage warnings.**
- **`tools/regen_index_bundle.py`** — the *only* thing that should touch `index.json` and `bundle.json.gz`. Never hand-edit those. Checksum = `sha256:` of file bytes; bundle = gzip of `{version:1, files:{relpath:text}}` over all of `data/` except the bundle itself.

---

## 9. Acceptance checklist ("perfect" = all yes)

Contract (validator ERRORS = 0):
- [ ] `topic.json` + `mcq.json` valid JSON; `id`==`slug`==folder.
- [ ] Block `order` contiguous 1..n; every block has all required fields; `topicId` matches.
- [ ] `hasCode`/`hasTable` honest; `estReadSeconds` present.
- [ ] Every embedded image is in `assets[]` **and** the file exists at the **flat** `assets/x.svg` path.
- [ ] Cross-links are bare slugs that resolve in `index.json`.
- [ ] Every MCQ: 4 options, valid `correctIndex`, non-empty teaching `explanation`, real `blockId`; block↔MCQ refs consistent both ways.
- [ ] Interview blocks start with `**Q:`.

Quality bar (validator WARNINGS + human review):
- [ ] 20–28 blocks; avg block ≥ ~600 chars; ~12–22 min read.
- [ ] Layered: ~50/35/15 beginner/intermediate/advanced; ≥1 advanced block.
- [ ] ≥1 worked example; ≥1 real comparison table; ≥2 pitfalls; 6–9 interview cards (≥half ⭐).
- [ ] ~1 MCQ per non-interview teaching block; distractors are plausible; difficulty spread.
- [ ] A diagram where it materially helps (real SVG, flat path, house palette).
- [ ] Voice: concrete, active, no fluff, no in-markdown headings.
- [ ] Cross-links to the natural neighbor topics.

---

## 10. LLM prompt template (paste-ready for a low-cost model)

> You are authoring one topic for **CrackLoop**, a mobile interview-prep app. Produce two JSON files, `topic.json` and `mcq.json`, for the topic **"{{TITLE}}"** (slug `{{SLUG}}`, group `{{GROUP}}`).
>
> Study this gold-standard example first and match its depth, structure, and voice exactly: `{{PASTE intro-to-dbms/topic.json + mcq.json}}`.
>
> Requirements (hard):
> - 20–28 ordered blocks grouped into sections following the arc: Snapshot → Why it exists (incl. a worked example) → core mechanics → kinds/trade-offs → a diagram + walkthrough → in practice (code if code-relevant) → when not to → ≥2 pitfalls → 6–9 interview Q&A.
> - Each teaching block: **claim → why → concrete example/number → takeaway**, 600–900 chars. No bare bullet lists. No fluff, no in-markdown `#` headings.
> - Layer with `level`: ~50% beginner, ~35% intermediate, ~15% advanced.
> - Block ids `{{SLUG}}-bNN` (contiguous). Set `sectionNumber`/`sectionTitle`/`subTitle`. Leave `hasCode`/`hasTable`/`estReadSeconds` approximate — they're recomputed.
> - `interview` blocks: markdown begins `⭐ **Q: …?**` (⭐ only for most-asked), then a model answer that shows *how* to answer.
> - Diagrams: only if one genuinely helps. Reference flat as `![alt](assets/name.svg)`, list in `assets[]`, and output the SVG separately (light Material palette). Otherwise use a `<<< Image: prompt >>>` placeholder.
> - Cross-links: `[target-title](target-slug)` bare slug only.
> - `mcq.json`: ~1 MCQ per non-interview block; ids `{{SLUG}}-bNN-qM`, `blockId` set, and mirror them in each block's `mcqIds`. Exactly 4 plausible options; `explanation` teaches why. Vary the correct position and difficulty.
>
> Output valid JSON only. It will be gated by `validate_content.py` — 0 errors required.

After generation: run the §8 pipeline. Reject and regenerate on any validator ERROR; review WARNINGS.

---

## 11. Anti-patterns (auto-reject)

- Bullet-list-only blocks with no explanatory prose ("flashcard mode").
- Padding to hit length — repetition, restating the title, "as we saw above".
- Distractors that are obviously wrong; explanations that just restate the answer.
- `#`/`##` headings inside `markdown` (use `sectionTitle`/`subTitle`).
- Nested image paths `assets/<slug>/x.svg` (the current corpus bug) — always flat.
- Cross-links as URLs, `.md`, or to non-existent slugs.
- Hand-editing `index.json` or `bundle.json.gz` — always regenerate.
- Every topic identical in shape — the arc is a guide; fit it to the material.
