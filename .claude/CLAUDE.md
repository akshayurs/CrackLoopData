# CrackLoopData — .claude working notes (v3)

Session-handoff context for this **data repo**. The root [CLAUDE.md](../CLAUDE.md) describes
the original v2 intent; this file records the **v3 state** the content + tooling are now in.
Read this first when touching content or the generator.

## What shipped (v3)

The learning content was rebuilt clean-sheet to **schema v3** and lives at the **repo root**:

```
content/<area>/<group>/<topic>/
    topic.json       # { id, title, area, group, order, slug, summary, level, slideCount, estReadMinutes, slides[] }
    mcq.json         # { topicId, mcqs[] }            (renamed from v2 blockMcqs[]; each mcq has slideId)
    interview.json   # { topicId, interviewQuestions[] }   (pulled OUT of slides)
    assets/*.svg     # adaptive --dg-* SVGs, flat filenames
```

- **slides[]** = renamed v2 `blocks[]`. **mcqs[]** = renamed `blockMcqs[]` (key `slideId`, not `blockId`).
- Hierarchy: **area → group → topic → slides/mcqs/interviewQuestions**.

**Authored so far (5 areas, 278 topics):** `ai-ml`, `cloud-devops-sre`, `computer-architecture`,
`computer-networks`, `cs-theory-math` — 2126 slides, 1085 MCQs, 427 interview Qs, 238 SVGs.
Source of truth for what to write: `briefs/expanded/<area>.md` (17 areas have briefs; only 5 authored).

## Generated files — never hand-edit

`content/index.json` and `content/bundle.json.gz` are **generated** by `tools/regen_v3.py`.
Run it after ANY content edit:

```bash
python3 tools/regen_v3.py            # rebuild index.json + bundle.json.gz
python3 tools/regen_v3.py --check    # verify only (non-zero exit on drift)
```

What `regen_v3.py` does (all paths in index/bundle are **relative to `content/`** — the app's basePath):
- Emits **schemaVersion 3** index. Folds each **(area, group)** pair into ONE app-facing "group"
  with slug `"<area>__<group>"` (the app has one nav level; area is carried as metadata).
- Per-group **`icon`** (keyword heuristic → AppIcons name) + **`color`** (cycled palette);
  per-area **`areaIcon`** + **`areaColor`**. Edit `AREA_META` / `GROUP_PALETTE` / `GROUP_ICON_RULES` there.
- **Relevance ordering** (NOT alphabetical): area order from `briefs/area-group-map.md`
  (`## Area N — … \`slug\``), group order from each `briefs/expanded/<area>.md` (`## Group: … (slug)`
  sequence). Topics keep their authored `order`. Alphabetical is last-resort fallback only.
- **Bundle** = gzip `{"version":1,"files":{relpath:text}}` incl. every topic/mcq/interview JSON,
  every SVG, `index.json`, AND the migrated aux datasets (below).

## Aux datasets migrated into content/ (were v2-only under data/)

`glossary.json`, `config.json`, and the whole `coding/` catalog were **copied** from the legacy
`data/` tree into `content/` so the v3 app (basePath `content`) can reach them:
- `content/glossary.json`, `content/config.json` → referenced in the index (`glossaryFile`/`configFile`), bundled.
- `content/coding/` → `regen_v3.py` bundles `coding/prep_manifest.json` + only the files it references
  (primerFile/questionFile/solutions), ~104 files / 80 questions. Index gets `codingManifest`/`codingCount`.
- Caveats: glossary `relatedTopicIds` are **stale v2 topic slugs** (defs display fine, some links dangle);
  `data/coding` still exists too (dup, retires with data/).

## Preview

```bash
python3 tools/serve_v3.py            # http://localhost:8000 — walks content/, area→group→topic nav,
                                     # inlines adaptive --dg-* SVGs, light/dark, interview section
```

## Adaptive SVG diagrams

Authored with CSS custom props: `fill="var(--dg-fill, #F1F3F4)"` etc. (light-value fallback).
Tokens: `--dg-ink/muted/line/fill/stroke/accent/accent-bg`. The **preview** and the **app** both
theme these (the app's `cached_svg.dart` inlines `var()` since flutter_svg can't eval CSS vars).

## Still v2 / deferred (gotchas)

- `tools/validate_content.py` and `tools/regen_index_bundle.py` are **v2** — they do NOT understand
  the v3 tree. There is **no v3 validator yet**. Validation was deferred; agents self-checked.
- `CONSUMING.md` / `AUTHORING.md` / `CURRICULUM.md` still describe v2 layout.
- The `data/` tree = legacy v2, intentionally **held back** (in-flight image-path fix branch). Don't commit it.
- **Interview-Q inconsistency across areas** (density + answer length): computer-architecture invented
  ~2–3/topic (briefs had none); cloud/theory ~1/topic. Answer lengths vary (some >700 char). Needs a
  normalization pass + a `validate_v3.py`.

## App linkage

The app (`StudyAppTemplate`, flavor `crackloop`) fetches from `github.com/akshayurs/CrackLoopData`
branch `main`, basePath `content`. Pushing to `main` = live on next app content sync.
Commit scope rule (strict): stage only task-relevant files; never blanket-add; keep `data/` out.
