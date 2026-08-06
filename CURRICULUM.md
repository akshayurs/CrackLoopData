# CURRICULUM — planning Areas, Groups and Topics (schema v3)

The **map-maker**, one layer above the authoring spec ([prompts/authoring-agent-v3-area.md](prompts/authoring-agent-v3-area.md)); repo overview: [CLAUDE.md](CLAUDE.md), v3 working notes: [.claude/CLAUDE.md](.claude/CLAUDE.md).

This doc decides *what content exists* — which **Areas** ship, which **Groups** each Area contains, and which **Topics** each Group contains — and produces the two handoff artifacts an authoring agent reads. It also carries the **current-state audit** (§7) so anyone can see at a glance what is authored, what is pending, and what is off.

```
area-group-map.md  →  briefs/expanded/<area>.md  →  authoring-agent-v3-area.md  →  content/<area>/<group>/<topic>/
   (areas+groups)        (groups + topics + slide outline)     (how to write)         topic.json / mcq.json / interview.json
                                                                                   ↓
                                                                       validate_v3.py → regen_v3.py
```

---

## 1. Hierarchy and vocabulary (locked, v3)

| Level | Term | JSON / folder | Example |
|---|---|---|---|
| 1 | **Area** (domain) | `content/<area>/`, `area` field, index `areas[]` | Databases |
| 2 | **Group** (subject) | `content/<area>/<group>/`, `group` field | Storage & Indexing |
| 3 | **Topic** (lesson) | `content/<area>/<group>/<topic>/topic.json` | B-Tree Indexes |
| 4 | **Slide** (one screen) | `slides[]` in `topic.json` | one concept / diagram / code / compare / pitfall page |
| — | **MCQ** | `mcqs[]` in `mcq.json` (keyed by `slideId`) | 4-option quiz |
| — | **Interview Question** | `interviewQuestions[]` in `interview.json` | real asked question + model answer |

Renames from v2: `blocks[]` → `slides[]`, `blockMcqs[]` → `mcqs[]` (`blockId` → `slideId`), interview questions pulled **out** of slides into their own file. The app folds each `(area, group)` pair into one nav group with slug `<area>__<group>`; `regen_v3.py` does that.

Separate track, not planned here: the **coding-question catalog** at `content/coding/` (manifest is source of truth, ~80 questions).

---

## 2. Principles

**Choosing an Area**
1. **Interview-relevance is the only filter.** It ships if it shows up in real technical interviews. Everything else is cut.
2. **Tiered, not equal.** 🟢 Core (near-universal) · 🔵 Rec (commonly asked) · 🟡 Breadth (role/domain) · ⚪ Niche. Tier drives both *whether* it ships and *how deep* it goes.
3. **No overlapping Areas.** Object-oriented design was merged into `system-design` (LLD) rather than kept as a peer — that is the model for resolving overlap: merge, don't cross-reference two half-areas.

**Choosing a Group**
4. A Group is a *subject* — 4–14 Topics that a learner would study as one sitting-block sequence. Fewer than 3 Topics means it should merge into a sibling; more than ~15 means it should split.
5. Groups are **ordered for learning** inside the Area (fundamentals → advanced). `regen_v3.py` reads that order from the `## Group:` sequence in the brief — alphabetical is fallback only.

**Choosing a Topic**
6. **One coherent idea, one sitting** — "Normalization", "TLB & Page Tables". Not a textbook chapter, not a single definition.
7. **Non-overlapping within and across Areas.** Deliberate cross-links (bare topic slug) instead of re-teaching.
8. **Level-tagged** — beginner / intermediate / advanced, set in the brief and carried into `topic.json`.
9. **Depth is per-Topic, not per-Area quota.** The wave-2 bar: 9–16 slides, 4–6 MCQs, 3–5 interview questions with 900–1800 char answers spanning fresher→staff. An Area with fewer Topics but each at the bar beats a wide, shallow Area.

---

## 3. Artifact 1 — the Area→Group map

[briefs/area-group-map.md](briefs/area-group-map.md) — one table per Area listing its Groups, slug, tier and one-line scope. This is the **pruning surface**: decisions about what ships happen here, before any Topic work.

```markdown
## Area N — <Title> `<area-slug>` 🟢

| Group | slug | Tier | Scope |
|---|---|---|---|
| Storage & Indexing | `storage-indexing` | 🟢 | B-trees, LSM, heap/clustered, index design |
```

`regen_v3.py` parses the `## Area N — … \`slug\`` sequence for **area ordering**, so the numbering here is load-bearing — renumber deliberately.

---

## 4. Artifact 2 — the expanded Area Brief

One file per Area at `briefs/expanded/<area-slug>.md`. This is what an authoring agent is handed. It goes **two levels below the Group**: every Topic, plus that Topic's slide outline.

```markdown
# Area: <Title> (<area-slug>)

Slide tags: `[concept]` `[diagram]` `[code]` `[compare]` `[pitfall]`. MCQs + interview
questions attach at topic level (separate files), not listed here.

## Group: <Group Title> (<group-slug>)

### Topic: <Topic Title> (<topic-slug>, beginner)
<One line: what this Topic actually teaches.>
- [concept] <the specific idea this slide carries>
- [diagram] <what the diagram shows>
- [compare] <A vs B, and the axis of comparison>
- [pitfall] <the mistake this slide inoculates against>
- [code] <the snippet and what it demonstrates>
```

Rules:
- **Slide bullets are the scope contract.** "The four key types and how they enforce identity" — not "Keys". An outline bullet that could belong to three different Topics is a bug.
- Slugs are kebab-case, unique **within the area**, stable — they are folder names and cross-link targets. Renaming one after authoring breaks links; don't.
- Group slugs and order must match [briefs/area-group-map.md](briefs/area-group-map.md) exactly.
- Topic count is whatever the subject needs. Do not pad a Group to a round number.
- MCQs and interview questions are **not** listed in the brief — the authoring agent derives them.

---

## 5. Gates

**Gate 1 — curriculum.** Human reviews the Area→Group map (does this Area ship? these Groups?) and then the expanded brief's Topic list + outlines. Coverage, overlap, ordering, scope. This is the cheap place to fix scope; fixing it after authoring costs an entire re-run.

**Gate 2 — content.** Per [prompts/authoring-agent-v3-area.md](prompts/authoring-agent-v3-area.md), the authoring agent may add up to **2 missing Topics per Group** if the brief has a real gap; anything beyond that comes back here.

**Gate 3 — mechanical.** `python3 tools/validate_v3.py <area>` must report **0 errors** (char-band lines are advisory WARNs), then `python3 tools/regen_v3.py` to rebuild `content/index.json` + `bundle.json.gz`. Never hand-edit those two.

---

## 6. Handoff to authoring

- **New Area:** map row → expanded brief → gate 1 → one authoring agent per Group (not per Topic; per-Topic fans out too wide and loses cross-topic consistency) → validate → single regen at the end.
- **Remediation:** update the brief to describe the Area as it *should* be, then re-run affected Groups in remediation mode. Slugs stay fixed.
- Regenerate `index.json` / `bundle.json.gz` **once** at the end of a wave, not per Topic.

---

## 7. Current state — audit (2026-08-06)

Measured from `content/`, `briefs/expanded/` and `tools/validate_v3.py`, not from notes.

### 7.1 Authored — 16 of 16 Areas, 1331 of 1331 planned Topics (100%)

Every planned Area is authored. The curriculum backlog is closed; what remains is depth
remediation inside already-authored Areas, not missing content.

| Area | Groups | Topics | Slides | MCQs | IQs | slides/topic | IQ/topic | IQ answer chars |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `web-frontend` | 8 | 65 | 742 | 372 | 251 | 11.4 | 3.9 | 1480 |
| `engineering-craft` | 9 | 67 | 763 | 393 | 269 | 11.4 | 4.0 | 1436 |
| `databases` | 11 | 43 | 483 | 251 | 171 | 11.2 | 4.0 | 1231 |
| `languages-compilers` | 7 | 53 | 575 | 292 | 213 | 10.8 | 4.0 | 1580 |
| `data-structures-algorithms` | 18 | 134 | 1446 | 718 | 505 | 10.8 | 3.8 | 1457 |
| `operating-systems` | 10 | 62 | 668 | 339 | 219 | 10.8 | 3.5 | 1334 |
| `system-design` | 54 | 473 | 5015 | 2065 | 1436 | 10.6 | 3.0 | 1000 |
| `data-engineering` | 7 | 48 | 502 | 264 | 192 | 10.5 | 4.0 | 1445 |
| `interview-prep` | 4 | 29 | 303 | 153 | 114 | 10.4 | 3.9 | 1274 |
| `security` | 7 | 42 | 438 | 249 | 172 | 10.4 | 4.1 | 1461 |
| `mobile` | 5 | 37 | 369 | 218 | 148 | 10.0 | 4.0 | 1611 |
| `computer-networks` | 11 | 40 | 397 | 149 | 128 | 9.9 | 3.2 | 1920 |
| `cs-theory-math` | 5 | 28 | 258 | 135 | 112 | 9.2 | 4.0 | 1563 |
| `ai-ml` | 12 | 68 | 622 | 354 | 208 | 9.1 | 3.1 | 1700 |
| `cloud-devops-sre` | 10 | 61 | 555 | 292 | 184 | 9.1 | 3.0 | 1646 |
| `computer-architecture` | 12 | 81 | 731 | 401 | 259 | 9.0 | 3.2 | 1536 |
| **Total** | **190** | **1331** | **13867** | **6645** | **4581** | 10.4 | 3.4 | 1344 |

Bar = wave-2 spec: ≥9 slides, 4–6 MCQs, 3–5 IQs at 900–1800 chars. **Every Topic now meets the
slide floor and the interview-question floor** — the "Topics <9 slides" column is gone because it
is zero everywhere.

### 7.2 Pending

None. All 16 briefs in `briefs/expanded/` are fully authored.

### 7.3 What is correct

- **Schema compliance is clean:** `validate_v3.py` reports **0 errors** across all 1331 Topics.
- **The interview-question bar is met everywhere.** Every Topic in the repo now ships ≥3
  interview questions (4581 total, 3.4/Topic average). The "~230 Topics need an IQ pass"
  debt from the 2026-07-30 audit is closed.
- **The slide floor is met everywhere.** 0 Topics below 9 slides (was 308); 13867 slides,
  10.4/Topic. The four Areas that carried the debt — `computer-architecture`, `system-design`,
  `ai-ml`, `cloud-devops-sre` — all now sit at 9.0–10.6 slides/Topic.
- **Diagram debt is fully closed.** 0 `<<< Image:` placeholders remain and all **1238 SVGs**
  parse as well-formed XML with `--dg-*` theming. This includes the 7 `system-design/uml`
  slides the last audit flagged as unmarked, and the 106→223 placeholder backlog.
- **Cross-links resolve.** 0 dangling bare-slug links and 0 path-style `](../…)` links repo-wide.
- **Glossary references resolve.** 372 of 380 terms carry `relatedTopicIds`, 0 dangling — the
  51 stale v2 slugs left by the schema migration are remapped. The 8 unlinked terms (Count-Min
  sketch, Cuckoo filter, RUM conjecture, varint, zero-copy, …) are genuine corpus gaps.
- **MCQ answer keys audited.** 923 prioritized questions checked against independently derived
  answers; 9 defects found and fixed (see §7.4.5 for what that says about method).
- **`index.json` / `bundle.json.gz` are current** — `regen_v3.py --check` exits 0 on a clean tree.

### 7.4 What is incorrect / owed

1. **Three duplicate Topic slugs**, surfaced as WARNs by `validate_v3.py`. Slugs double as
   Topic ids and as cross-link targets, so a collision makes every link to that slug ambiguous
   and makes the two Topics share an id:
   - `oltp-vs-olap` — `databases/data-warehousing` + `data-engineering/de-fundamentals`
   - `on-call-and-incident-response` — `cloud-devops-sre/sre` + `engineering-craft/debugging`
   - `handling-being-stuck` — `data-structures-algorithms/coding-interview-strategy` + `interview-prep/coding-playbook`

   Each pair is genuine near-duplicate content authored by different waves. This already
   produced one broken link (a Topic linking to itself). Decide per pair: delete one and
   redirect, or rename one id — renaming is app-visible and breaks saved progress/deeplinks.
2. **`system-design` interview questions hug the floor** — 456 of its 473 Topics sit at
   exactly 3 IQs, and its 1000-char answer average is the lowest in the repo (vs 1344 overall).
   It meets the bar; it is not at the depth of `databases` or `engineering-craft`.
3. **`computer-networks` IQ answers now run long** — 1920-char average, above the 1800 ceiling,
   after its normalization pass. Trim rather than extend.
4. **MCQ counts below the 4–6 band** in a tail of Topics. The slide-depth pass topped many up,
   but it was scoped to slides, so some Topics still sit at 3 MCQs. Advisory, not an error.
5. **What the answer-key audit taught (method note, so the next one is cheaper).** 923 Topics'
   worth of prioritized MCQs were checked; 9 were genuinely wrong. All 625 flags raised by a
   *lexical* heuristic — "the explanation's wording matches a different option than the key" —
   were false positives, because explanations legitimately spend their words saying why the
   WRONG options are wrong. Every real defect came from a **computational** question whose
   arithmetic nobody re-derived, or from an agent reading the file for an unrelated reason.
   One question's correct answer was not among its options at all (a FIFO page-fault count
   whose own explanation listed seven faults and then concluded "6").
   **Next audit: skip lexical scanning entirely; re-derive every numeric/traced question.**
   The remaining ~5700 non-flagged MCQs have still never been checked.

### 7.5 Focus balance — over- and under-focused

**Over-focused: `system-design` is 36% of all Topics (473 of 1331) across 54 Groups.** That is
down from 55% purely because the rest of the curriculum landed, not because anything moved.
Inside it, **15 `interview-*` Groups hold 202 Topics (15% of the repo)**, where each "Topic" is
a single interview question rendered as a full lesson.

The three problems from the last audit still stand and still want a decision:
- **Modality conflict.** Schema v3 already has a home for interview questions — `interview.json`.
- **Topical duplication.** `interview-hld-caching` (13) shadows `caching` (7); `interview-lld-oop`
  (14) shadows `oop-fundamentals` (7); `interview-lld-patterns` (14) shadows the pattern Groups (20).
- **Nav weight.** 54 Groups in one Area is far past the §2 guideline.

Recommendation unchanged: decide explicitly whether the `interview-*` Groups are (a) their own
Area — e.g. `system-design-interview`, returning `system-design` to ~271 Topics/39 Groups — or
(b) folded back into the concept Topics' `interview.json`.

**A correction the last audit got wrong:** deepening `system-design` was never blocked by that
decision. All 120 of its under-floor Topics were in the **concept** Groups (api-design,
microservices, storage-scale, observability, sd-playbook); the 202 `interview-*` Topics were
already at or above the 9-slide floor. The depth work has since been done on that basis, so the
placement decision remains open with nothing waiting on it.

**Correctly focused:** `databases`, `operating-systems`, `engineering-craft` and `web-frontend` —
right size, at the depth bar, brief-aligned. They remain the reference model.

### 7.6 Roadmap

The depth backlog is closed. What remains is judgement calls and correctness, not volume.

1. **Resolve the three slug collisions** (§7.4.1) — needs a decision, then minutes of work.
2. **Decide the `interview-*` placement** (§7.5) — the largest open architectural question.
3. **Finish the MCQ answer-key audit** (§7.4.5): ~5700 questions unchecked. Re-derive every
   computational one; do not repeat the lexical scan.
4. Trim `computer-networks` IQ answers to the 1800 ceiling; top up the tail of Topics still at
   3 MCQs (§7.4.3, §7.4.4).
5. Optionally deepen `system-design` interview questions beyond the 3-question floor (§7.4.2).

---

## 8. Checklist for a finished Brief

- [ ] Area has a row in [briefs/area-group-map.md](briefs/area-group-map.md) with tier and Group list; area number set.
- [ ] Every Group has 4–14 Topics; Group order is the learning order.
- [ ] Every Topic passes the interview-relevance filter and is one sitting's worth.
- [ ] Every Topic has a slide outline with tagged bullets — the scope contract, not a restated title.
- [ ] No Topic overlaps a sibling or another Area; deliberate cross-links noted as bare slugs.
- [ ] Slugs kebab-case, unique in-area, stable; `level` set on every Topic.
- [ ] Reviewed at gate 1 before authoring starts.
