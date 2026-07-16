# AUTHORING — building one Study Area's content

The **builder** spec. Given a **Study Area Brief** (produced by [CURRICULUM.md](CURRICULUM.md)), this tells an agent how to generate that Study Area's entire content to the CrackLoop quality bar. [CONSUMING.md](CONSUMING.md) is the read-side contract; this is the write-side.

Reference implementation: **[intro-to-dbms](data/content/databases/intro-to-dbms/topic.json)**. When unsure, open it and match it.

> **Product note.** The **app (Play Store) is the product**; the local preview server (`tools/serve.py`) is a dev tool. JSON field names below are unchanged for app compatibility — the new vocabulary is our shared *language*, not a schema change.

---

## 0. Vocabulary (use these words exactly)

| Level | Term | JSON key | Example |
|---|---|---|---|
| 1 | **Study Area** | `group` | Databases |
| 2 | **Topic** | `topic` (its own file) | Introduction to DBMS |
| 3 | **Subtopic** | `sectionTitle` | "Why databases exist" |
| 4 | **Card** | `block` | one one-screen unit |
| — | **MCQ** | `blockMcqs[]` | a multiple-choice question on a Card |
| — | **Interview Question** | Card of `type:"interview"` | a real, asked question + model answer |

Hierarchy: **Study Area → Topic → Subtopic → Card**, with MCQs and Interview Questions as content on Cards. (Coding practice is a separate track: **Coding Topic → Coding Question**.)

---

## 1. The four rules that override everything

1. **Value filter (top rule).** Nothing exists unless the learner gains **real, non-obvious understanding** from it. If a Card, MCQ, Interview Question, or whole Topic is filler, obvious, boring, or padding — **it does not ship.** Never add something to hit a number.
2. **Counts are topic-driven, never hardcoded.** As many Cards / MCQs / Interview Questions / Topics as the material genuinely needs — no quotas, no caps. A thin topic might be 8 Cards; a rich one 40.
3. **Each Card is concise — one mobile screen.** Depth comes from **more Cards, not longer Cards.** Char bands (below) are enforced.
4. **Interview-forward.** This is an interview-prep product. Interview Questions must be **real and commonly-asked**, not invented trivia. Frame everything toward "will this help me in the room?"

---

## 2. Card length — the char bands (concise, one screen)

Measured on the `markdown` field. Code fences and tables don't count toward the cap, but the whole Card must still fit one mobile screen.

| Card `type` | Min | Max | Target |
|---|---|---|---|
| overview / concept / compare / pitfall | 120 | **600** | 250–450 |
| interview | 150 | **700** | 350–550 |
| code / diagram (surrounding prose) | 80 | **450** | 150–350 |

*[tunable — thresholds live in `tools/validate_content.py`]*

- **Too long → split into multiple Cards**, don't cram. A worked example becomes 2–3 small Cards (setup → the problem → the fix).
- **Too short → it's probably filler** — either enrich it with a why/example, or cut it.
- Under the cap, still write tight: **claim → why → one concrete example → takeaway.** No fluff, no "as we saw above", no restating the title.

---

## 3. Card types & how to write each

| type | When | Must contain |
|---|---|---|
| `overview` | Snapshot at the top of a Topic | The mental model in ≤3 sentences + an analogy or a short disambiguation |
| `concept` | Standard teaching (the workhorse) | claim → why → concrete example → takeaway |
| `compare` | Trade-offs / X vs Y / when-not-to | a real table **plus** one line of *how to decide* |
| `diagram` | A structure/flow clearer shown | an adaptive SVG (§6) + a short prose explanation |
| `code` | Code-relevant topics | a correct, runnable-looking fenced block + expected output |
| `pitfall` | Misconceptions & traps | the wrong belief → why it's wrong → the correct model |
| `interview` | Interview prep (§5) | a real question + model answer (strict format) |

Write in **GitHub-flavored markdown**. Never put `#`/`##` headings in `markdown` — the Subtopic (`sectionTitle`) and Card sub-heading (`subTitle`) are separate fields. Bold key terms on first use; `` `code` `` for identifiers; tables for comparisons.

**Voice:** concrete over abstract (numbers, named tools, tiny scenarios). Active, second person. Analogy for the hook, then precision. Explain jargon the first time. No emoji except the `⭐` interview marker.

---

## 4. MCQs — options are real content

- **Coverage is value-driven**, not per-Card. Add an MCQ only where checking understanding genuinely helps. Skip pure recall.
- **Exactly 4 options.** Vary the correct position across the bank (don't default to B).
- **Every option is substantive** — a real concept or a genuine misconception a half-learner would actually pick. **No throwaway/joke options** (banned: "a spreadsheet application").
- **`explanation` teaches** — why the right answer is right *and* why the most tempting wrong one is wrong. It's shown after answering.
- **`difficulty`** ∈ `easy|medium|hard`, spread. **`level`** mirrors the Card's level.
- Interviewer's-eye: prefer questions probing a real misconception or trade-off over textbook definitions.
- IDs: `<topic-slug>-b<NN>-q<M>`; `blockId` is a real Card; the Card's `mcqIds` lists back every MCQ (two-way).

---

## 5. Interview Questions — real & popular only

The headline feature. Each `interview` Card:

```
⭐ **Q: <the real question, as asked>?**

<model answer — structured, shows HOW to answer, with a concrete example>

**Testing:** <one line — what the interviewer is really probing>
```

- **Only questions actually asked** for this topic. If you can't imagine it in a real interview, cut it.
- **`⭐` marks most-asked** — use it only for genuinely high-frequency questions (the app badges/sorts these first). Order Cards so the most-asked come first.
- The answer **demonstrates how to answer**: a structure ("I'd start from…"), a concrete example, a crisp close — not a wall of facts.
- The `**Testing:**` line names the underlying skill (e.g. "whether you understand isolation vs consistency"). This is what makes it interview-prep, not a quiz.
- `subTitle` = a short label for the question.

---

## 6. Diagrams — one adaptive SVG, theme-follows-the-page

Diagrams are optimized for the **preview website** (the app is separate). One SVG that adapts to light/dark via CSS variables — no two-file, no white-plate.

**Standard:** every fill/stroke uses a `--dg-*` variable with a **light-value fallback**:

```
--dg-ink       text            (light #202124 / dark #E6EDEC)
--dg-muted     secondary text  (#5F6368 / #9AA0A6)
--dg-line      arrows/neutral  (#5F6368 / #8FA09E)
--dg-fill      neutral box     (#F1F3F4 / #1C2827)
--dg-stroke    neutral border  (#9AA0A6 / #3A4A47)
--dg-accent    primary stroke  (#0C8F88 / #2FD6CC)
--dg-accent-bg primary fill    (#E3F3F1 / #123330)
```

Usage: `fill="var(--dg-fill, #F1F3F4)"`, `stroke="var(--dg-accent, #0C8F88)"`, marker paths `fill="var(--dg-line, #5F6368)"`. The preview **inlines** the SVG so it inherits the page's `--dg-*` and follows the toggle; opened standalone it falls back to the light values. See [dbms-architecture.svg](data/content/databases/intro-to-dbms/assets/dbms-architecture.svg).

Rules: `viewBox` + `font-family="-apple-system, …"`; arrow markers in `<defs>`; 2–3-word labels; escape `>`/`&` in text (`-&gt;`, `&#183;`). Reference **flat**: `![alt](assets/name.svg)` (never `assets/<slug>/name.svg`) and list it in the Card's `assets[]` with the byte-identical path. Add a diagram only when it *materially* helps (value filter). If none exists yet, use a placeholder token `<<< Image: prompt >>>` — never raw-shown.

**Cross-links:** `[target-title](target-slug)` — bare Topic slug only, and only to slugs that exist.

---

## 7. Two-phase generation (mandatory)

**Phase 1 — Outline.** Emit only the *plan*, no bodies:
- the Topic list for the Study Area (from the Brief), and for each Topic:
  - its Subtopics (section titles),
  - each Card's heading + type + level (one line each),
  - each MCQ's question stem,
  - each Interview Question stem (⭐ if most-asked).

**→ Approval gate.** A human reviews and trims. Nothing below is written until the outline is approved.

**Phase 2 — Write.** Flesh out only the approved items into full `topic.json` + `mcq.json`, obeying §§1–6.

---

## 8. Correctness — how we guarantee it

Four layers; a Topic isn't done until all pass.

1. **Self-applied acceptance criteria** (the generator checks its own output):
   - Every stated fact is well-established and accurate.
   - Every MCQ `correctIndex` is verifiably correct; all 4 options are plausible.
   - Every Interview answer is accurate and actually answers the question.
   - Every item passes the **value filter** (§1.1).
   - Every Card is within its char band; no `#` headings; links/images resolve.
2. **Verification pass — a separate reviewer agent** re-checks the above independently (writer agent → reviewer agent per Topic) and cuts anything filler or wrong. Findings that survive are kept.
3. **The Phase-1 outline gate** catches weak/duplicate/boring items before any writing.
4. **`tools/validate_content.py`** enforces structural correctness (4 options, refs resolve, char bands, honest `hasCode`/`hasTable`, interview format, flat image paths).

---

## 9. The schema you author

You write `topic.json` + `mcq.json` (+ any `assets/*.svg`). Fields marked ⚙ are recomputed by `tools/regen_index_bundle.py` — approximate or omit them.

```jsonc
// topic.json
{
  "id": "<slug>", "title": "…", "group": "<study-area-slug>",
  "order": 1, "slug": "<slug>",
  "summary": "1–2 sentence hook — what the learner walks away able to do.",
  "contentType": "learningTopic", "level": "beginner",   // or omit
  "blockCount": 0,        // ⚙
  "estReadMinutes": 0,    // ⚙
  "blocks": [ {
    "id": "<slug>-b03", "topicId": "<slug>", "order": 3,   // contiguous 1..n
    "sectionNumber": 1, "sectionTitle": "<Subtopic>", "subTitle": "…|null",
    "type": "concept",                                     // §3 types
    "level": "beginner",                                   // beginner|intermediate|advanced|expert, or omit
    "markdown": "…within the char band…",
    "assets": [],           // {alt,path} only if the markdown embeds an image
    "hasCode": false,       // ⚙   = ("```" in markdown)
    "hasTable": false,      // ⚙   = markdown has a table
    "estReadSeconds": 0,    // ⚙
    "mcqIds": []            // MCQs targeting this Card
  } ]
}
```
```jsonc
// mcq.json
{ "topicId": "<slug>", "blockMcqs": [ {
    "id": "<slug>-b03-q1", "blockId": "<slug>-b03",
    "question": "…", "options": ["…","…","…","…"], "correctIndex": 2,
    "explanation": "why right + why the tempting wrong one is wrong",
    "difficulty": "medium", "level": "beginner" } ] }
```

Levels: layer with `level` so a returning learner can go deeper and a beginner isn't drowned — but let the material decide the mix; don't force a ratio. IDs are load-bearing: Card `= <slug>-b<NN>`, MCQ `= <blockId>-q<M>`.

---

## 10. Remediating existing Topics (fixing the old content)

The old corpus is flashcard-shallow, unlayered, and has broken image paths. Same rules apply — this is a rewrite, not a patch.

Per Topic:
1. Read the current `topic.json` + `mcq.json`; keep any genuinely good bones.
2. **Re-cut to the char bands:** split over-long Cards into several one-screen Cards; enrich or delete thin ones (value filter).
3. **Add what's missing** *only if it adds value:* level layering, real+popular Interview Questions with `**Testing:**` lines, MCQs with substantive options, a diagram where it helps.
4. **Fix images:** flat `assets/x.svg` path + convert the SVG to the adaptive `--dg-*` standard (§6).
5. **Cut** anything filler/boring/duplicated.
6. Run the pipeline (§11). Same two-phase + verification gates as new content.

---

## 11. Pipeline

```bash
# Phase 1: emit the outline → get human approval (§7)
# Phase 2: write data/content/<study-area>/<topic-slug>/{topic.json,mcq.json} (+ assets/*.svg)

python3 tools/validate_content.py <study-area>/<topic-slug>   # 0 errors (hard gate)
python3 tools/serve.py                                        # read it, judge depth
python3 tools/regen_index_bundle.py                           # rebuild index + bundle
python3 tools/regen_index_bundle.py --check                   # confirm no drift
```

One agent owns a Topic (parallelize across Topics/agents); regenerate the index/bundle **once** at the end to avoid collisions. See [tools/README.md](tools/README.md).

---

## 12. Acceptance checklist ("done" = all yes)
- [ ] Every item passes the value filter — nothing filler/obvious/boring.
- [ ] Every Card within its char band; concise; one screen; no `#` headings.
- [ ] Counts driven by the material, not a quota.
- [ ] MCQs: 4 substantive options, correct answer verified, teaching explanation.
- [ ] Interview Questions: real + popular, ⭐ on most-asked, `**Testing:**` line, model answer shows *how*.
- [ ] Diagrams: adaptive `--dg-*` SVG, flat path, added only where they help.
- [ ] Cross-links resolve; images resolve; layered by level where the material warrants.
- [ ] `validate_content.py` = 0 errors; reviewer-agent verification pass done; index/bundle regenerated.
