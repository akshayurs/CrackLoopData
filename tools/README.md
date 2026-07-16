# CrackLoop content toolkit

Three dependency-free Python scripts (stdlib only — no `pip install`, no build step) for authoring, previewing, and validating the content in `data/`. Requires **Python 3.8+**.

| Script | Does | Run |
|---|---|---|
| [`serve.py`](serve.py) | Local preview server — browse content the way the app does | `python3 tools/serve.py` |
| [`validate_content.py`](validate_content.py) | Contract + quality-bar checker (the gate for generated content) | `python3 tools/validate_content.py --all` |
| [`regen_index_bundle.py`](regen_index_bundle.py) | Rebuild `index.json` counts/checksums + `bundle.json.gz` | `python3 tools/regen_index_bundle.py` |

The quality bar these enforce is defined in [`../AUTHORING.md`](../AUTHORING.md).

---

## `serve.py` — preview server

A local web app that reads `data/index.json` + the content files and renders every **learning topic** (blocks, inline MCQs, SVG diagrams) and every **coding question** (problem + multi-language solutions) the way a client would. Use it to read content, sanity-check formatting, and judge depth.

### Start it

```bash
python3 tools/serve.py            # http://localhost:8000
python3 tools/serve.py 9000       # custom port as an argument
PORT=9000 python3 tools/serve.py  # or via env var
```

It prints the URL and a content count, then serves until you press **Ctrl-C**. Open the URL in any browser. It binds to `127.0.0.1` only (local machine).

### Use it

- **Left sidebar** — all 9 groups and their topics (from `index.json`), then the coding-practice questions grouped by topic. The colored dot shows `level` (green = beginner, amber = intermediate, violet = advanced) for topics, or `difficulty` for questions; the number is the block count / difficulty initial.
- **Collapsible groups** — each group is an accordion (click the header to expand/collapse); the number on the header is its topic count. Groups start collapsed and the group of the currently-open topic auto-expands, so you never scroll past hundreds of items to find one.
- **Filter box** (top of sidebar) — type to filter topics live; matching groups auto-expand, and clearing the box restores the collapsed state.
- **Click a topic** — renders its blocks in order: section eyebrows, per-card type + level chips, the sub-title, markdown (tables, code, blockquotes), embedded SVG diagrams, and the inline MCQs with the correct option marked and the explanation shown.
- **Cross-links** inside content (bare topic slugs) are clickable and navigate in-app; unresolved links render as dotted, non-clickable text so you can spot them.
- **Coding question** — the problem statement plus each solution approach with its time/space complexity and a **language tab switcher** (python / javascript / java / cpp / sql).
- **Light / dark toggle** — the button in the top bar; your choice is remembered (localStorage) and applied on load with no flash. It respects your OS theme until you override it.
- **Responsive** — below 900px the sidebar collapses behind the **☰** button.

### What it handles for you

- **Self-heals the nested image-path bug:** if a block references `assets/<slug>/x.svg` but the file lives flat at `assets/x.svg`, the server finds and renders it anyway, so diagrams show even before that fix lands. Genuinely missing images render a visible "missing image" note.
- **Image placeholders** (`<<< Image: … >>>`) render as a labelled "diagram not yet generated" slot with the generation prompt tucked in a `<details>` — never shown as raw text.
- One malformed file returns a 500 page for that route only; the server keeps running.

> The server renders whatever is in your working tree right now — it reads the files live on each request, so edits show on refresh with no restart.

---

## `validate_content.py` — the gate

Checks learning-content topics against the data contract and the quality bar.

```bash
python3 tools/validate_content.py databases/intro-to-dbms   # one topic
python3 tools/validate_content.py --all                     # every topic
```

- **ERRORS** (process exits non-zero) are contract violations that would make a client mis-render or crash: invalid JSON, wrong `blockCount`, non-contiguous block order, a 4-option rule broken, a dangling MCQ reference, a broken image path, a malformed interview card, a bad cross-link. **Gate generated content on zero errors.**
- **WARNINGS** (exit stays zero) are quality-bar misses: average block too thin, too few blocks, too few interview cards, low MCQ coverage, no level layering. Treat these as a review queue, not a hard fail.

Thresholds live at the top of the script (`MIN_AVG_BLOCK_CHARS`, `MIN_BLOCKS`, …) — tune them there.

---

## `regen_index_bundle.py` — rebuild the derived files

`index.json` (counts + checksums) and `bundle.json.gz` are **generated** from the content files, which are the source of truth. Never hand-edit them.

```bash
python3 tools/regen_index_bundle.py           # rebuild both
python3 tools/regen_index_bundle.py --check    # verify only; non-zero exit on drift
```

Run it after editing any `topic.json`, `mcq.json`, or asset. It recomputes each topic's `blockCount`, `mcqCount`, `estReadMinutes`, `level`, and both checksums (`sha256:` of the file bytes), plus the top-level totals, then rebuilds the bundle (gzip of every file under `data/` except the bundle itself). Topics you didn't touch keep byte-identical index entries, so the git diff stays minimal. Use `--check` in CI or a pre-commit hook to catch a stale index/bundle.

---

## End-to-end authoring loop

```bash
# 1. Author or generate  data/content/<group>/<slug>/{topic.json,mcq.json} (+ assets/*.svg)
# 2. Gate it — must be 0 errors
python3 tools/validate_content.py <group>/<slug>
# 3. Preview it
python3 tools/serve.py            # open the topic, read it, judge depth
# 4. Rebuild the derived files
python3 tools/regen_index_bundle.py
# 5. Confirm nothing drifted
python3 tools/regen_index_bundle.py --check
```

See [`../AUTHORING.md`](../AUTHORING.md) for the depth bar, section arc, block-type rules, and the LLM prompt template used to scale this across all topics.
