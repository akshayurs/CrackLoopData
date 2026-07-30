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

**Authored so far (8 areas, 856 topics, 125 groups):** `ai-ml`, `cloud-devops-sre`,
`computer-architecture`, `computer-networks`, `cs-theory-math`, `system-design` (473),
`databases` (43), `operating-systems` (62) — 8112 slides, 3653 MCQs, 2222 interview Qs.
Source of truth for what to write: `briefs/expanded/<area>.md` (16 live briefs; 8 authored).
**Still unauthored:** `data-structures-algorithms` (134), `engineering-craft` (67),
`web-frontend` (65), `languages-compilers` (53), `data-engineering` (48), `security` (42),
`mobile` (37), `interview-prep` (29).

**Wave 2 (2026-07-30) raised the depth bar** — `databases` + `operating-systems` were authored to
`prompts/authoring-agent-v3-area.md` (area-agnostic; supersedes the system-design-only
`authoring-agent-v3-group.md`): 9–16 slides/topic, 4–6 MCQs, **3–5 interview questions/topic with
900–1800 char answers spanning fresher→staff**, and agents may add up to 2 missing topics/group.
Use that spec for every future area.

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

- `tools/validate_v3.py` **exists and is the gate** (`python3 tools/validate_v3.py [<area>[/<group>]]`,
  0 errors required; char-band lines are advisory WARNs and run high by design since the wave-2 depth
  bar). `tools/validate_content.py` and `tools/regen_index_bundle.py` are **v2** — they do NOT
  understand the v3 tree.
- `CONSUMING.md` / `AUTHORING.md` / `CURRICULUM.md` still describe v2 layout.
- The `data/` tree = legacy v2, intentionally **held back** (in-flight image-path fix branch). Don't commit it.
- **Interview-Q inconsistency across the 5 pre-system-design areas** (density + answer length):
  computer-architecture ~2–3/topic, cloud/theory ~1/topic, answers often <700 char. `databases`,
  `operating-systems` and `system-design` are at the current bar. A normalization pass over the
  older five is still owed.
- **106 deferred diagrams** repo-wide are `<<< Image: … >>>` placeholder tokens, not SVGs
  (`grep -rn '<<< Image:' content/`). Wave 2 added 65 (OS) + 41 (databases). All three consumers
  strip them safely; `prompts/generate-pending-svgs.md` is the follow-up pass.
- Two authoring defects wave-2 agents produced that need watching: **path-style cross-links**
  (`](../group/topic)` instead of a bare slug — the validator's link regex silently skips them) and
  **slides that restate an `(interview)` seed** (8 found and removed in memory/virtual-memory).

## App linkage

The app (`StudyAppTemplate`, flavor `crackloop`) fetches from `github.com/akshayurs/CrackLoopData`
branch `main`, basePath `content`. Pushing to `main` = live on next app content sync.
Commit scope rule (strict): stage only task-relevant files; never blanket-add; keep `data/` out.
