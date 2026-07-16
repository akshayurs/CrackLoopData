# CURRICULUM — planning Study Areas and their Briefs

The **map-maker**, one layer above [AUTHORING.md](AUTHORING.md) (repo overview: [CLAUDE.md](CLAUDE.md)). It decides *what* content exists — the Study Areas and, inside each, the Topics — and produces a **Study Area Brief** per area. That Brief is the handoff artifact fed to an authoring agent, which then builds the whole area (Topics → Subtopics → Cards + MCQs + Interview Questions).

Vocabulary is fixed in [AUTHORING.md §0](AUTHORING.md): **Study Area → Topic → Subtopic → Card**.

```
CURRICULUM.md  →  Study Area Briefs  →  AUTHORING.md  →  content files
 (this doc)        (one per area)       (per area/topic)   (topic.json / mcq.json)
```

---

## 1. What a Study Area is

A top-level domain a candidate must know for interviews — e.g. **Databases**, **Data Structures & Algorithms**, **System Design**. It maps to a `group` in the data. It's big enough to hold 10–40 Topics and coherent enough to study as a track.

The catalog today (9): `data-structures-algorithms`, `system-design`, `cs-foundations`, `engineering-craft`, `modern-specialized`, `databases`, `computer-networks`, `computer-architecture`, `object-oriented-design`.

---

## 2. Principles for choosing Study Areas & Topics

1. **Interview-relevance is the filter.** Include a Study Area or Topic only if it shows up in real technical interviews (coding, system design, CS fundamentals, behavioral-adjacent craft). If it wouldn't help someone in the room, it doesn't belong. (Same **value filter** as authoring.)
2. **Complete but not overlapping.** Together the Study Areas should cover the interview landscape with minimal gaps; Topics within an area shouldn't duplicate each other or a neighbour area. Note deliberate cross-links instead of repeating.
3. **Ordered for learning.** Study Areas and their Topics get an `order` reflecting a sensible learning path (fundamentals before advanced).
4. **Right granularity.** A Topic is one sitting's worth of study (a coherent idea like "Normalization" or "Indexes"), not a whole textbook chapter and not a single definition. Split when a title spans clearly separate ideas; merge trivial fragments.
5. **Level-aware.** Note each Topic's rough tier (beginner / intermediate / advanced) so the track can be filtered.

---

## 3. The Study Area Brief (the handoff artifact)

One markdown file per Study Area, at `briefs/<study-area-slug>.md`. It is what an authoring agent reads to build the area. Each Topic entry carries a **deep description of what that Topic will teach** — the scope contract that keeps authors on-target and non-overlapping.

```markdown
# Study Area: <Title>

slug: <study-area-slug>
order: <n>
one-liner: <one sentence — what mastering this area gives a candidate>

## Description
<2–4 sentences: what this area covers, why it matters in interviews, who it's
for, and the level range. This frames every Topic below.>

## Topics
1. **<Topic Title>**  (slug: `<topic-slug>`, level: beginner, order: 1)
   <2–4 sentences: exactly what this Topic teaches and its boundaries — the
   sub-ideas it must cover, what it must NOT cover (belongs to another Topic),
   and the kinds of interview questions it should prepare the learner for.>

2. **<Topic Title>**  (slug: `<topic-slug>`, level: intermediate, order: 2)
   <…>
```

Rules for the Brief:
- **Topic descriptions are substantive**, not restated titles. "Normalization: teaches 1NF→BCNF with the anomaly each removes; boundary — functional dependencies are their own Topic; must prep 'explain normalization / when to denormalize' questions." — that level of specificity.
- Slugs are kebab-case, unique, stable (they become folder names and cross-link targets).
- Cover the area with the principles in §2; let the count be as large as the area needs.

---

## 4. Two-phase, with the curriculum approval gate

**Phase 1 — Propose.** The curriculum agent emits, for the Study Area(s) in scope:
- the area title + one-liner + description, and
- the **Topic list only** — each Topic's title, slug, level, and its deep description. No Cards, no content.

**→ Curriculum approval gate.** A human reviews the Topic list: right coverage? no gaps/overlap? good ordering? correct scope per Topic? Trim/add/redescribe here — this is the cheap place to fix scope.

**Phase 2 — Finalize Briefs.** Approved output is written to `briefs/<study-area-slug>.md`.

Then each Brief is handed to an authoring agent, which runs its **own** two-phase gate (outline → approve → write) per [AUTHORING.md §7](AUTHORING.md).

So there are two human gates: **curriculum** (what Topics exist) → **content** (what's in each Topic).

---

## 5. Handoff to authoring

- **New Study Area:** write its Brief here, then spawn one authoring agent per Topic (or per area), each given the Brief + the Topic it owns.
- **Existing Study Area (remediation):** first write/update its Brief to describe the area as it *should* be (reconciling the current Topic list against §2), then hand each Topic to an authoring agent in remediation mode ([AUTHORING.md §10](AUTHORING.md)).
- Parallelize across Topics; regenerate `index.json` / `bundle.json.gz` once at the end (`tools/regen_index_bundle.py`).

---

## 6. Checklist for a finished Brief
- [ ] Every Topic passes the interview-relevance value filter.
- [ ] Coverage of the area is complete; no two Topics overlap.
- [ ] Each Topic has a substantive scope description (sub-ideas + boundaries + target interview questions), not a bare title.
- [ ] Slugs are unique, kebab-case, stable; `order` set; `level` noted.
- [ ] Reviewed and approved at the curriculum gate before any authoring starts.
