# CrackLoopData — repo guide

Read this first. It explains what this repo is, what we're trying to do, the vocabulary we use, and where every other doc fits.

## What this is

A **data-only repository**: the learning content and coding-question catalog for **CrackLoop**, an interview-prep app.

- **The app (Play Store) is the product.** It consumes this data.
- **The local website (`tools/serve.py`) is a dev/preview tool only** — for reading and reviewing content. When a choice trades off between the app and the preview (e.g. how SVGs are themed), optimize for the preview; the app is a separate concern.
- There is **no application code here** — just content (JSON + markdown + SVG) plus small Python tools.

## What we're doing (intention)

The v1 content is **flashcard-shallow** — short bullet lists that name things without teaching them. We are rebuilding it to a real learning bar and scaling that across all content with AI agents. The strategy:

1. **Perfect one exemplar** — the gold-standard Topic [data/content/databases/intro-to-dbms/](data/content/databases/intro-to-dbms/topic.json).
2. **Write the specs** — [CURRICULUM.md](CURRICULUM.md) (what content exists) and [AUTHORING.md](AUTHORING.md) (how to write it well).
3. **Scale with agents** — run the prompts in [prompts/](prompts/) to author new content and remediate old, gated by validation and human approval.

## Vocabulary (use these words)

| Level | Term | JSON key | Example |
|---|---|---|---|
| 1 | **Study Area** | `group` | Databases |
| 2 | **Topic** | `topic` (own file) | Introduction to DBMS |
| 3 | **Subtopic** | `sectionTitle` | "Why databases exist" |
| 4 | **Card** | `block` | one one-screen unit |
| — | **MCQ** | `blockMcqs[]` | multiple-choice question on a Card |
| — | **Interview Question** | Card `type:"interview"` | a real, asked question + answer |

Hierarchy: **Study Area → Topic → Subtopic → Card**. Separate track: **Coding Topic → Coding Question**. The JSON keys never change (app compatibility) — the terms above are our shared language.

## Document map

| Doc | Purpose | Read when |
|---|---|---|
| **CLAUDE.md** (this) | Repo overview + intentions + index | first |
| [CONSUMING.md](CONSUMING.md) | Read-side data contract — how a client loads/renders the data | building/​debugging a loader or the app |
| [CURRICULUM.md](CURRICULUM.md) | Plan Study Areas → produce a Study Area Brief per area | deciding *what* content exists |
| [AUTHORING.md](AUTHORING.md) | Write one Study Area's content to the quality bar | writing/​fixing content |
| [prompts/curriculum-agent.md](prompts/curriculum-agent.md) | Copy-paste prompt to run the curriculum step | scaling with agents |
| [prompts/authoring-agent.md](prompts/authoring-agent.md) | Copy-paste prompt to author/remediate a Topic | scaling with agents |
| [tools/README.md](tools/README.md) | The preview server + validation + regen tools | running the tooling |

## The two datasets

1. **Learning content** — `data/content/<study-area>/<topic>/{topic.json, mcq.json, assets/}`, indexed by `data/index.json`. This is the bulk. Full contract in [CONSUMING.md §1–7](CONSUMING.md).
2. **Coding-question catalog** — `data/coding/`, indexed by `data/coding/prep_manifest.json`. A separate schema ([CONSUMING.md §8](CONSUMING.md)).

## The content pipeline

```
CURRICULUM.md → Study Area Briefs → AUTHORING.md → content files → validate → regen
```
Two human approval gates: **curriculum** (what Topics exist) → **content** (each Topic's outline). Details in the two specs.

## The quality bar (one paragraph)

Every piece of content must pass the **value filter**: it ships only if the learner gains real, non-obvious understanding — no filler, obvious, or boring items. Counts are **topic-driven** (as many Cards/MCQs/Questions as the material needs, no quotas); each **Card is concise — one mobile screen** (prose char bands enforced), so depth comes from *more* Cards, not longer ones. The product is **interview-forward**: Interview Questions are real and commonly-asked, MCQ options are all substantive. Full rules in [AUTHORING.md](AUTHORING.md).

## Tools (`tools/`, stdlib Python, no install)

- `python3 tools/serve.py` — preview server; browse content app-style, light/dark toggle, adaptive diagrams.
- `python3 tools/validate_content.py <study-area>/<topic>` — contract + quality gate (0 errors required).
- `python3 tools/regen_index_bundle.py` — rebuild `index.json` counts/checksums + `bundle.json.gz`.

## Working conventions (important for AI)

- **Content files are the source of truth.** `data/index.json` and `data/bundle.json.gz` are **generated** — never hand-edit them; run `tools/regen_index_bundle.py`.
- **Always** run `tools/validate_content.py` after editing a Topic (0 errors), and regenerate the index/bundle before considering it done.
- **Commit scope:** stage only files relevant to the task; never blanket-add. Non-data doc/tool changes and `data/` content changes are landed separately (see below).
- **Images:** flat path `assets/x.svg` (never `assets/<slug>/x.svg`); adaptive `--dg-*` SVGs ([AUTHORING.md §6](AUTHORING.md)).

## Current state / gotchas (2026-07-16)

- The **gold-standard `data/` changes** (intro-to-dbms + regenerated `index.json`/`bundle.json.gz`) are **held back / uncommitted** to avoid colliding with an in-flight **image-path fix** branch that also regenerates those two files. Land plan: merge the image fix, then one regen captures both.
- **Known bug being fixed:** ~54 Topics reference images as `assets/<slug>/x.svg` (nested) while files sit flat at `assets/x.svg` → broken diagrams in-app. The preview server self-heals this; the data fix is in progress.
- **Coding catalog:** the manifest curates ~80 questions though ~179 question dirs exist on disk — the manifest is the source of truth for what to show.
- Old content is still v1-shallow; remediation to the bar is the ongoing agent work ([AUTHORING.md §10](AUTHORING.md)).
