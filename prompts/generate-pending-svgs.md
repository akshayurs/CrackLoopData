# Prompt — generate the deferred SVG diagrams

SVG authoring is **deliberately deferred** while content is being written, to save tokens.
An authoring agent writes the `diagram` slide's prose and leaves a placeholder token in the
markdown instead of drawing anything:

```
<<< Image: <a description of exactly what the diagram should show> >>>
```

The placeholder is the hand-off artifact — it carries everything needed to draw the SVG later.
`tools/serve_v3.py` renders it as a dashed **"Diagram not yet generated"** box with the prompt
in a collapsible, so nothing raw leaks into the preview, and `tools/validate_v3.py` lists each
one as a `PENDING` line (never an error).

## Find what's outstanding

```bash
grep -rn '<<< Image:' content/                      # everything
grep -rn '<<< Image:' content/system-design/        # one area
grep -rc '<<< Image:' content/*/*/*/topic.json | grep -v ':0'   # counts per topic
```

`python3 tools/validate_v3.py <scope>` also prints every placeholder with its prompt, plus a
total, under `PENDING`.

Two *other* kinds of broken diagram exist in the pre-v3 corpus — they show up as ERRORs from
the validator, not as placeholders, and are worth fixing in the same pass:

- **asset listed but not embedded** (~22) — the SVG is on disk and bundled, but the markdown
  never embeds it, so it silently never renders. One `![alt](assets/x.svg)` line fixes each.
- **image embedded but file missing** (~11) — the markdown points at an SVG that was never
  drawn. These need real authoring, at the exact filename already referenced.

---

## The prompt (copy-paste, set the scope)

> Generate the deferred SVG diagrams for `content/system-design/` in the CrackLoop data repo.
>
> **1. Find the work.** Run `grep -rn '<<< Image:' content/system-design/`. Each hit is one
> diagram to draw; the text after `Image:` is the generation prompt describing what it must show.
> Also run `python3 tools/validate_v3.py system-design` and note any ERROR of the form
> "asset listed but not embedded" or "image referenced but file is missing" — fix those in the
> same pass.
>
> **2. For each placeholder**, read the surrounding slide `markdown` in that topic's `topic.json`
> so the diagram matches what the prose actually explains, then author
> `content/<area>/<group>/<topic>/assets/<name>.svg`. Use a short, descriptive, flat filename
> (`assets/scale-cube.svg`, never `assets/<slug>/scale-cube.svg`).
>
> **3. Every colour must be a CSS custom property with a light-value fallback** so the diagram
> follows the page theme:
>
> | role | usage |
> |---|---|
> | text | `fill="var(--dg-ink, #202124)"` |
> | secondary text | `fill="var(--dg-muted, #5F6368)"` |
> | arrows / neutral lines | `stroke="var(--dg-line, #5F6368)"` (marker paths use `fill`) |
> | neutral box fill | `fill="var(--dg-fill, #F1F3F4)"` |
> | neutral border | `stroke="var(--dg-stroke, #9AA0A6)"` |
> | accent stroke | `stroke="var(--dg-accent, #0C8F88)"` |
> | accent fill | `fill="var(--dg-accent-bg, #E3F3F1)"` |
>
> **No raw hex outside a `var()` fallback** — not even for emphasis. Need a "bad path" or
> "failure" highlight? Use a dashed `--dg-accent` stroke and a text label, not red.
> Include a `viewBox`, `font-family="-apple-system, sans-serif"`, arrow markers in `<defs>`,
> labels of 2-3 words, and escape `>` / `&` in text (`-&gt;`, `&amp;`).
> Copy the conventions from
> `content/computer-networks/application-layer/dns-resolution/assets/dns-hierarchy.svg`.
>
> **4. Wire it up in BOTH places, with byte-identical flat paths** — replace the
> `<<< Image: ... >>>` token with the embed, and add the asset entry:
>
> - in the slide markdown: `![descriptive alt text](assets/<name>.svg)`
> - in that slide's `assets` array: `{"alt": "descriptive alt text", "path": "assets/<name>.svg"}`
>
> Listing without embedding means the diagram never renders — that bug already exists ~22 times
> in this repo. Do not add to it. Delete the placeholder token once the image is in place.
>
> **5. Apply the value filter.** If a slide doesn't genuinely need a diagram, don't draw one:
> remove the placeholder, change the slide's `type` from `"diagram"` to `"concept"`, and say so
> in your report.
>
> **6. Validate and report.**
> ```bash
> python3 tools/validate_v3.py system-design      # 0 errors required
> grep -rn '<<< Image:' content/system-design/    # should be empty when done
> ```
> Do NOT run `tools/regen_v3.py` — the orchestrator runs it once at the end.
> Report: SVGs authored, slides converted to `concept` instead, and anything still outstanding.

---

## Notes

- Work in batches by area or group; each SVG costs roughly 1-2k tokens.
- Regenerate the index/bundle **once** after a batch: `python3 tools/regen_v3.py`, then
  `python3 tools/regen_v3.py --check`.
- **Safe to ship to prod.** All three consumers handle the token, so placeholder-bearing
  content can go to `main` without waiting for the SVGs:
  - **app** — `app/lib/features/reader/widgets/block_markdown.dart` strips it via
    `RegExp(r'<<<\s*Image:.*?>>>', dotAll: true)` and renders
    `> 🖼️ *Diagram coming soon*`; the prompt never reaches users.
  - **preview** — `tools/serve_v3.py` renders a dashed "Diagram not yet generated" box with
    the prompt in a collapsible.
  - **validator** — reports it as `PENDING`, never an error.
