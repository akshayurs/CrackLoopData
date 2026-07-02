# Consuming CrackLoop content (v2)

How an app (or any client) loads and renders the content in this repo. This is the **data contract** — the source of truth for building a content loader.

> **Schema v2.** Content lives in a named-folder tree under `data/content/`, indexed by `data/index.json`. This replaced the old flat `data/topics/<id>.json` + `data/manifest.json` scheme. If you are migrating an old loader, see [Migrating a v1 loader](#migrating-a-v1-loader) at the end.

---

## 1. What ships

```
data/
  index.json          ← entry point: the registry of groups + topics
  bundle.json.gz      ← the whole tree, gzipped, for one-request sync
  roadmap.json        ← suggested learning order (phases of topic slugs)
  glossary.json       ← term definitions
  config.json         ← app feature flags (ads, etc.)
  content/
    <group-slug>/       e.g. databases, system-design, data-structures-algorithms
      <topic-slug>/     e.g. intro-to-dbms, normalization
        topic.json      the learning content (cards/blocks)
        mcq.json        the quiz bank for this topic
        assets/         SVG diagrams for this topic (if any)
```

Identifiers are **slugs**, not codes. A topic's `id` **equals** its folder name and its `slug` (e.g. `intro-to-dbms`). Groups are slugs too (`databases`). There is no `a01`/`b03` scheme.

---

## 2. How to fetch it

Two supported paths — **prefer the bundle**.

### A. Bundle (recommended — one request)
`bundle.json.gz` is a gzipped JSON map of the entire `data/` tree:

```json
{ "version": 1, "files": { "<relPath>": "<file contents as text>", ... } }
```

Steps:
1. Download `data/bundle.json.gz`.
2. Gunzip → parse JSON.
3. `files["index.json"]`, `files["content/databases/intro-to-dbms/topic.json"]`, etc. are the raw file texts (JSON strings, or SVG text for assets). Parse the JSON ones on demand.

Keys are POSIX-style relative paths matching `topicFile`/`mcqFile`/`dir` in the index. SVG assets appear as their own entries (text).

### B. Per-file (no bundle)
Fetch `index.json`, then fetch each topic's `topicFile` / `mcqFile` on demand from the raw repo URL. Fine for a web viewer; heavier (one request per file).

### Update detection
Re-sync when the bundle changes. Options: compare a stored hash of `bundle.json.gz`, or (if published as a GitHub Release) watch the latest release tag. Per-topic `checksum` / `mcqChecksum` in the index let you invalidate only changed topics.

---

## 3. `index.json` — the registry (your entry point)

```json
{
  "schemaVersion": 2,
  "topicCount": 75,
  "blockCount": 955,
  "mcqCount": 680,
  "groups": [
    {
      "slug": "databases",
      "name": "Databases",
      "order": 6,
      "color": "#00CEC9",
      "icon": "database",
      "topics": [
        {
          "id": "intro-to-dbms",
          "title": "Introduction to DBMS",
          "order": 1,
          "level": "beginner",
          "dir": "content/databases/intro-to-dbms",
          "topicFile": "content/databases/intro-to-dbms/topic.json",
          "mcqFile": "content/databases/intro-to-dbms/mcq.json",
          "blockCount": 12,
          "mcqCount": 8,
          "estReadMinutes": 8,
          "checksum": "sha256:…",
          "mcqChecksum": "sha256:…"
        }
      ]
    }
  ],
  "glossaryFile": "glossary.json",
  "roadmapFile": "roadmap.json",
  "configFile": "config.json"
}
```

Build your navigation from this alone:
- Sort `groups` by `order`; within each, sort `topics` by `order`.
- Show `group.name` as the section header, `topic.title` in the list.
- **`group.color`** (hex, e.g. `#00CEC9`) and **`group.icon`** (an icon name your app maps to a glyph) are the group's display accent. Both are optional — fall back to a neutral accent/icon when absent. They live in the data so branding can change without an app release.
- Load `topicFile` / `mcqFile` lazily when a topic is opened.
- `level`, `blockCount`, `mcqCount`, `estReadMinutes` are for list badges / filters without opening the file.
- `mcqFile` may be `null` (topic has no quiz).

---

## 4. `topic.json` — the learning content

```json
{
  "id": "data-models",
  "title": "Data Models",
  "group": "databases",
  "order": 3,
  "slug": "data-models",
  "summary": "One- or two-sentence hook.",
  "contentType": "learningTopic",
  "level": "beginner",
  "blockCount": 16,
  "estReadMinutes": 12,
  "blocks": [ /* ordered cards */ ]
}
```

A topic is an **ordered list of blocks (cards)**. Render blocks in `order`. Group consecutive blocks by `sectionNumber` / `sectionTitle` to draw section headings; `subTitle` (nullable) is the card's own sub-heading.

### Block shape
```json
{
  "id": "data-models-b03",
  "topicId": "data-models",
  "order": 3,
  "sectionNumber": 1,
  "sectionTitle": "The classic models",
  "subTitle": "Hierarchical",
  "type": "concept",
  "level": "beginner",
  "markdown": "…GitHub-flavored markdown…",
  "assets": [ { "alt": "…", "path": "assets/foo.svg" } ],
  "hasCode": false,
  "hasTable": false,
  "estReadSeconds": 62,
  "mcqIds": ["data-models-b03-q1"]
}
```

- **`markdown`** — render as GitHub-flavored markdown. Do **not** render `sectionTitle`/`subTitle` from inside the markdown; they come from the fields above.
- **`hasCode` / `hasTable`** — hints so you can lazy-load a code highlighter or table styler. They always match the markdown.
- **`mcqIds`** — the quiz questions tied to this card (look them up in `mcq.json` by `id`). Empty means no quiz for this card.
- **`estReadSeconds`** — for progress/TTS pacing.

### Block `type` → how to render
| `type` | Render intent |
|---|---|
| `overview` | Snapshot / summary card |
| `concept` | Standard explanation |
| `code` | Contains a fenced code block (`hasCode` = true) |
| `diagram` | Has (or should have) a diagram — see image placeholders |
| `compare` | Trade-off / comparison (often a table) |
| `pitfall` | Common mistakes / gotchas |
| `interview` | **Q&A card** — see below |

### `interview` blocks
Dedicated interview-prep cards. The markdown is one real interview question + a model answer:

```
⭐ **Q: SQL vs NoSQL — when would you choose each?**

<model answer, plain markdown>
```

- A leading `⭐` marks a most-asked question — surface it (badge/sort).
- Render the `**Q: …**` line as the question, the rest as the answer. `subTitle` is a short label for the question.
- These are **separate** from the MCQ quiz bank — open-ended, not multiple-choice.

### Images / diagrams — two cases
1. **Real SVG assets** (most migrated topics): markdown contains `![alt](assets/foo.svg)` and the block's `assets[]` lists `{alt, path}`. `path` is relative to the topic folder (`assets/foo.svg` → `content/<group>/<topic>/assets/foo.svg`, also a bundle key). Load and render the SVG.
2. **Placeholders** (newer topics, no image yet): markdown contains a literal token:
   ```
   <<< Image: a detailed prompt describing the diagram to generate >>>
   ```
   These are **intentional placeholders** (images not generated yet). Render them as a styled "diagram coming soon" slot, or hide them — do **not** show the raw token to users. The text after `Image:` is an AI-generation prompt, not user-facing copy.

### Cross-topic links
Markdown links use the **target topic's slug** as the href:
```
… see [normalization](normalization) for more.
```
Resolve `href` against `index.json` (it's a topic `id`) and navigate in-app. It is not a real URL.

---

## 5. `mcq.json` — the quiz bank

```json
{
  "topicId": "data-models",
  "blockMcqs": [
    {
      "id": "data-models-b03-q1",
      "blockId": "data-models-b03",
      "question": "…",
      "options": ["…", "…", "…", "…"],
      "correctIndex": 2,
      "explanation": "why the answer is right",
      "difficulty": "easy",
      "level": "beginner"
    }
  ]
}
```

- Exactly **4 `options`**; `correctIndex` is 0–3.
- Show `explanation` after the user answers.
- `blockId` ties a question to a card — use it for a per-card quiz, or pool all `blockMcqs` for a topic-level quiz.
- `difficulty` (`easy|medium|hard`) and `level` are for filtering/scoring.

---

## 6. The `level` field (the skip/filter feature)

`level` ∈ `beginner | intermediate | advanced | expert` appears on **topics, blocks, and MCQs**. Use it to let users skip material:

- **Topic level** — the topic's overall tier (for track filtering).
- **Block level** — lets a user inside a topic skip cards above/below their level.
- **MCQ level** — filter quiz difficulty by learner level.

Suggested UX: a level selector; show only content whose `level` is at or below the chosen tier (treat `beginner ⊂ intermediate ⊂ advanced ⊂ expert`), or exactly-matching — your choice.

> **Important:** `level` is **optional and may be `null`/absent** on older migrated topics (only the newer Databases topics are fully level-tagged so far). Treat missing `level` as "always show" — never hide unleveled content.

---

## 7. Other files

- **`roadmap.json`** — `{ phases: [ { title, topicIds: [<slug>, …] } ] }`. A suggested cross-group learning order. `topicIds` are topic slugs (resolve via the index).
- **`glossary.json`** — term → definition, some with links to topic slugs. *(Note: a few glossary links may still use the old `<code>-<slug>` form pending a fix — resolve defensively.)*
- **`config.json`** — app feature flags (e.g. `adsEnabled`). Read as-is.

---

## 8. Minimal loader (pseudocode)

```text
bundle = gunzipAndParse(fetch("data/bundle.json.gz")).files
index  = parseJson(bundle["index.json"])

for group in sortBy(index.groups, .order):
    for t in sortBy(group.topics, .order):
        listItem(group.name, t.title, t.level, t.estReadMinutes)

onOpen(topicMeta):
    topic = parseJson(bundle[topicMeta.topicFile])
    mcqs  = topicMeta.mcqFile ? parseJson(bundle[topicMeta.mcqFile]).blockMcqs : []
    for b in sortBy(topic.blocks, .order):
        if userLevel and b.level and not levelVisible(b.level, userLevel): continue
        renderCard(b.sectionTitle, b.subTitle, b.type, renderMarkdown(b.markdown))
        for id in b.mcqIds: renderQuiz(find(mcqs, .id == id))
```

---

## Migrating a v1 loader

If your loader was built for the old flat scheme, the changes are:

| v1 | v2 |
|---|---|
| `manifest.json` at root | **`index.json`** (nested `groups → topics`) |
| `topics/<id>.json`, `mcq/<id>.json` | **`content/<group>/<topic>/topic.json` + `mcq.json`** (paths given in the index) |
| topic id like `a01`, group letter `a` | **slug id** (`intro-to-dbms`), **slug group** (`databases`) |
| cross-links `[a08-trees-bst](a08-trees-bst.md)` | **`[trees-bst](trees-bst)`** (bare slug) |
| — | new **`level`** fields; new **`interview`** block type; **image placeholders** |

Concretely (Flutter app in `StudyAppTemplate`): the touch points are the sync layer that looks for `manifest.json` (`content_sync_service.dart`) and the repository that lists topics from its flat paths (`content_repository.dart`). Point both at `index.json` and the nested `topicFile`/`mcqFile`. The block/topic model classes already parse `group`/`id` as strings, so slugs need no model change.
