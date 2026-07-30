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

## 7. Current state — audit (2026-07-30)

Measured from `content/` and `briefs/expanded/`, not from notes.

### 7.1 Authored (8 of 16 Areas — 856 of 1331 planned Topics, 64%)

| Area | Groups | Topics | Slides | MCQs | IQs | slides/topic | IQ/topic | IQ answer chars | Depth bar |
|---|---:|---:|---:|---:|---:|---:|---:|---:|:--|
| `databases` | 11 | 43 | 483 | 251 | 171 | 11.2 | 4.0 | 1244 | ✅ at bar |
| `operating-systems` | 10 | 62 | 668 | 339 | 219 | 10.8 | 3.5 | 1340 | ✅ at bar |
| `system-design` | 54 | 473 | 4835 | 1978 | 1360 | 10.2 | 2.9 | 981 | 🟡 near bar |
| `computer-networks` | 11 | 40 | 387 | 143 | 89 | 9.7 | 2.2 | 683 | 🟡 thin IQs |
| `cs-theory-math` | 5 | 28 | 239 | 115 | 28 | 8.5 | 1.0 | 1215 | ❌ IQ density |
| `cloud-devops-sre` | 10 | 61 | 461 | 227 | 105 | 7.6 | 1.7 | 773 | ❌ below bar |
| `ai-ml` | 12 | 68 | 495 | 275 | 80 | 7.3 | 1.2 | 1140 | ❌ IQ density |
| `computer-architecture` | 12 | 81 | 544 | 325 | 170 | 6.7 | 2.1 | 795 | ❌ below bar |
| **Total** | **125** | **856** | **8112** | **3653** | **2222** | 9.5 | 2.6 | — | |

Bar = wave-2 spec: ≥9 slides, 4–6 MCQs, 3–5 IQs at 900–1800 chars.

### 7.2 Pending (8 Areas — 475 Topics; briefs written, no content)

| Area | Groups | Topics | Tier | Priority |
|---|---:|---:|:--|:--|
| `data-structures-algorithms` | 18 | 134 | 🟢 | **1 — highest interview leverage, only Core area unauthored** |
| `engineering-craft` | 9 | 67 | 🟢 | 2 — git/testing/debugging/behavioral, universal |
| `web-frontend` | 8 | 65 | 🟡 | 3 — large candidate segment |
| `languages-compilers` | 7 | 53 | 🔵 | 4 |
| `data-engineering` | 7 | 48 | 🔵 | 5 |
| `security` | 7 | 42 | 🔵 | 6 |
| `mobile` | 5 | 37 | 🟡 | 7 |
| `interview-prep` | 4 | 29 | 🔵 | 8 — meta, overlaps others; author **last** |
| **Total** | **65** | **475** | | |

### 7.3 What is correct

- **Brief ↔ content alignment is essentially exact.** Every authored Area matches its brief's Group set and Topic count 1:1; the only slug drift is two Topics in `system-design/observability` (`observability-fundamentals` → `observability-in-system-design`, `distributed-tracing` → `distributed-tracing-design`). Fix by updating the brief, not the content.
- **Schema compliance is clean:** `validate_v3.py` reports **0 errors** across all 856 Topics.
- **Diagram debt is closed, not open.** The "106 deferred `<<< Image:` placeholders" in [.claude/CLAUDE.md](.claude/CLAUDE.md) is **stale** — 0 placeholder tokens remain; 804 SVGs are in place. Only **7** diagram slides lack an image, all in `system-design/uml`.
- **Path-style cross-link defect is gone** — 0 occurrences of `](../…)` remain (also stale in the notes).
- **Slide-type mix is healthy** repo-wide: ~50–60% concept, 7–15% pitfall, 7–13% compare, 6–19% diagram, 2–8% code.

### 7.4 What is incorrect / owed

1. **Interview-question debt in the 5 pre-wave-2 Areas.** `ai-ml` 68/68 Topics, `cs-theory-math` 28/28, `computer-architecture` 60/81, `cloud-devops-sre` 45/61 and `computer-networks` 29/40 have **fewer than 3** interview questions; `computer-networks` / `cloud-devops-sre` / `computer-architecture` average <800-char answers vs the 900–1800 band. **~230 Topics need an IQ pass.**
2. **Slide-count debt in the same Areas.** Below the 9-slide floor: `computer-architecture` 77/81, `ai-ml` 55/68, `cloud-devops-sre` 47/61, `cs-theory-math` 15/28, `system-design` 131/473, `computer-networks` 7/40. `databases` and `operating-systems`: 0.
3. **`index.json` is stale** — `python3 tools/regen_v3.py --check` reports DRIFT on a clean tree, so the committed index no longer matches what the generator produces. Regen and commit before the next wave.
4. **2595 advisory WARNs**, dominated by prose over the char band: 1212 concept, 371 IQ answers, 290 pitfall, 275 compare. Expected since the wave-2 depth bar — but the bands in `validate_v3.py` should be **re-tuned to the bar** so the signal is usable instead of ignored.
5. **7 diagram slides in `system-design/uml`** have neither image nor placeholder — nothing marks them as pending.
6. **`cs-theory-math` is under-built**: 5 Groups / 28 Topics is the thinnest Area, and at 1.0 IQ/Topic it reads as a stub. Either bring it to the bar or explicitly demote it to 🟡 breadth and freeze it.

### 7.5 Focus balance — over- and under-focused

**Over-focused: `system-design` is 55% of all authored Topics (473 of 856) across 54 Groups** — more than the other seven authored Areas combined. Inside it, **15 `interview-*` Groups hold 202 Topics (24% of the entire repo)**, where each "Topic" is a single interview question rendered as a full 11-slide lesson (`iv-hot-key-problem`, `iv-factory-vs-builder`, …).

That creates three problems worth a decision at the curriculum gate:
- **Modality conflict.** Schema v3 already has a home for interview questions — `interview.json`. Modelling them as Topics means the same question can exist twice (as a Topic *and* as an `interviewQuestions[]` entry on the concept Topic).
- **Topical duplication.** `interview-hld-caching` (13) shadows `caching` (7); `interview-lld-oop` (14) shadows `oop-fundamentals` (7); `interview-lld-patterns` (14) shadows the three pattern Groups (20). The concept coverage and the question coverage of the same material sit in separate nav branches.
- **Nav weight.** 54 Groups in one Area is far past the 4–14 Topics/Group, coherent-track guideline in §2.

Recommendation: keep the `interview-*` content (it is good and the format works), but decide explicitly whether it is (a) its own **Area** — e.g. `system-design-interview` — so `system-design` returns to ~271 Topics/39 Groups, or (b) folded back into the concept Topics' `interview.json`. Do not leave it undecided; it distorts every ratio in this table.

**Under-focused:** `data-structures-algorithms` — the single most-asked Area in the industry — has **0 Topics authored** while 202 system-design interview-question Topics ship. That is the biggest coverage gap in the repo. `engineering-craft` (67, 🟢 Core) is the second.

**Correctly focused:** `databases` and `operating-systems` — right size, at the depth bar, brief-aligned. They are the reference model for every future wave.

### 7.6 Roadmap

1. **Author `data-structures-algorithms`** (18 Groups / 134 Topics) to [prompts/authoring-agent-v3-area.md](prompts/authoring-agent-v3-area.md). Cross-link to the existing `content/coding/` catalog rather than re-teaching questions.
2. **Decide the `interview-*` placement** (§7.5) before that wave lands, so the index regen captures it.
3. **IQ + slide-depth normalization pass** over the five pre-wave-2 Areas (~230 Topics).
4. **Author `engineering-craft`, then `web-frontend`.**
5. Re-tune validator char bands; fill the 7 `uml` diagrams; regen and commit `index.json`.

---

## 8. Checklist for a finished Brief

- [ ] Area has a row in [briefs/area-group-map.md](briefs/area-group-map.md) with tier and Group list; area number set.
- [ ] Every Group has 4–14 Topics; Group order is the learning order.
- [ ] Every Topic passes the interview-relevance filter and is one sitting's worth.
- [ ] Every Topic has a slide outline with tagged bullets — the scope contract, not a restated title.
- [ ] No Topic overlaps a sibling or another Area; deliberate cross-links noted as bare slugs.
- [ ] Slugs kebab-case, unique in-area, stable; `level` set on every Topic.
- [ ] Reviewed at gate 1 before authoring starts.
