# TODO — session handoff (2026-07-30)

Pick this up cold. It says what is done, what is left, and the exact command or prompt to start each item. Written after a large authoring wave fully completed; **every number below was measured, not estimated**, with all agents finished and the index regenerated. Re-measure with §0 anyway if time has passed.

Specs you will need: [prompts/authoring-agent-v3-area.md](prompts/authoring-agent-v3-area.md) (how to author), [CURRICULUM.md](CURRICULUM.md) (what exists / what's planned), [.claude/CLAUDE.md](.claude/CLAUDE.md) (v3 layout + tooling).

---

## 0. First command of the next session

Re-measure before doing anything, so you are working from ground truth rather than this file.

```bash
cd /Users/akshayursm/Desktop/proj/CrackLoopData && python3 - <<'EOF'
import os,re,glob
tot=0
for f in sorted(glob.glob('briefs/expanded/*.md')):
    a=os.path.basename(f)[:-3]
    planned=len(re.findall(r'^### Topic:',open(f).read(),re.M))
    done=0
    for g in glob.glob(f'content/{a}/*/'):
        done+=sum(1 for t in os.listdir(g) if all(os.path.exists(f'{g}{t}/{x}') for x in ['topic.json','mcq.json','interview.json']))
    tot+=done
    print(f'{a:28} {done}/{planned}' + ('  <<' if done<planned else ''))
print('TOTAL',tot)
EOF
```

Then check for crash debris and schema health:

```bash
python3 tools/validate_v3.py 2>&1 | tail -3
```

A topic folder missing `mcq.json` or `interview.json` is a **hard validator error** — it means an agent died mid-topic. Finish those first (§3), never delete a folder that has a `topic.json`.

---

## 1. State as of this handoff

**1122 complete topics**, up from 856 at session start. **0 validator errors** repo-wide. `index.json` + `bundle.json.gz` were regenerated at the end of the session and `regen_v3.py --check` reports OK — so §2 is DONE unless you change content.

| Area | Complete / planned | Status |
|---|---|---|
| `system-design` | 473/473 | done (earlier wave) |
| `data-structures-algorithms` | **134/134** | **done this session** |
| `computer-architecture` | 81/81 | done (wave 1, below depth bar — see §6) |
| `ai-ml` | 68/68 | done (wave 1, below depth bar) |
| `operating-systems` | 62/62 | done (wave 2, at bar) |
| `cloud-devops-sre` | 61/61 | done (wave 1, below depth bar) |
| `engineering-craft` | **67/67** | **done this session** |
| `databases` | 43/43 | done (wave 2, at bar) |
| `computer-networks` | 40/40 | done (wave 1, below depth bar) |
| `cs-theory-math` | 28/28 | done (wave 1, below depth bar) |
| `web-frontend` | **65/65** | **done this session** |
| `languages-compilers` | 0/53 | **not started** |
| `data-engineering` | 0/48 | **not started** |
| `security` | 0/42 | **not started** |
| `mobile` | 0/37 | **not started** |
| `interview-prep` | 0/29 | **not started — author LAST** |

Nothing is committed. `git status` shows modified `CURRICULUM.md`, `briefs/expanded/system-design.md`, `content/index.json`, `content/bundle.json.gz`, four `system-design/uml` topics, and a large amount of untracked new content.

---

## 2. Do this first — it is mandatory before anything ships

```bash
python3 tools/regen_v3.py            # rebuild index.json + bundle.json.gz
python3 tools/regen_v3.py --check    # must print OK
```

`content/index.json` and `content/bundle.json.gz` are **generated**. The app reads them; new topics are invisible to the app until this runs. Never hand-edit either.

---

## 3. Finish partially-authored groups

**Nothing is partially authored.** Every group that had an agent finished cleanly at 0 errors. `data-structures-algorithms`, `engineering-craft` and `web-frontend` are all complete against their briefs.

If a future wave dies mid-run, run §0 to find short groups and use the §4 template with only the missing slugs listed.

---

## 4. Author the remaining areas

**This is the entire remaining content backlog — 209 topics across 5 areas.** Order by interview leverage: **`security` (42) → `data-engineering` (48) → `languages-compilers` (53) → `mobile` (37) → `interview-prep` (29)** (last: it summarizes the others, so it needs them to exist for cross-links).

Get each group's brief line range with:

```bash
python3 -c "
import re
f='briefs/expanded/security.md'   # change area
lines=open(f).read().split('\n')
gs=[(i+1,l) for i,l in enumerate(lines) if l.startswith('## Group:')]
gs.append((len(lines)+1,'END'))
for (s,l),(e,_) in zip(gs,gs[1:]):
    slug=re.findall(r'\(\`?([a-z0-9\-]+)\`?\)',l)[-1]
    n=sum(1 for x in lines[s-1:e-1] if x.startswith('### Topic:'))
    print(f'{slug}|lines {s}-{e-1}|{n} topics')
"
```

### Agent prompt template (proven this session)

One agent per group, `model: sonnet`. Substitute the bracketed parts:

> Author schema-v3 learning content in the CrackLoopData repo at /Users/akshayursm/Desktop/proj/CrackLoopData.
>
> Do this work YOURSELF — do not spawn subagents.
>
> FIRST read and follow exactly: `prompts/authoring-agent-v3-area.md`.
>
> AREA: `[area]`. GROUP: `[group]` — read ONLY lines [start]-[end] of `briefs/expanded/[area].md` using Read with offset/limit. Author all [N] topics in brief order: [slug list].
>
> REFERENCE EXEMPLAR — read all three files of `content/data-structures-algorithms/complexity/what-big-o-actually-claims/{topic.json,mcq.json,interview.json}` and match voice, depth, slide structure (open with an `overview` slide titled "Snapshot"), and interview-answer style (start with the answer, end with `**Testing:** …`, never repeat the question).
>
> Write ONLY under `content/[area]/[group]/`. Touch nothing else.
>
> One topic at a time: topic.json, then mcq.json, then interview.json — all three before starting the next topic, so a crash never leaves a half-written topic.
>
> Before treating a cross-link slug as nonexistent, CHECK DISK (`ls content/<area>/<group>/<slug>`) — `briefs/parts/_existing-slugs.txt` is a stale wave-start snapshot.
>
> Spread `correctIndex` evenly across 0-3. After each mcq.json, re-derive the correct option from your own `explanation` text and confirm `correctIndex` points at THAT option.
>
> Diagrams DEFERRED: `<<< Image: … >>>` inline, `assets: []`, no SVGs. Validate every 2-3 topics with `python3 tools/validate_v3.py [area]/[group]` to 0 errors. Char-band WARNs are advisory. Do NOT run `tools/regen_v3.py`.
>
> Final report under 20 lines: per-topic counts, correctIndex spread, final validator line, placeholder count, brief issues.

### Orchestration lessons — these cost real tokens this session

- **Cap concurrency at ~6 agents.** 20 simultaneous agents caused a mass failure: 12 died at once with "connection closed mid-response" or a 600s stall watchdog. The hard ceiling is 20 (`CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS`), but the practical ceiling is far lower.
- **Say "do this work yourself."** Four agents sub-delegated to children, paying an extra full context bootstrap each.
- **Track owners exactly.** Orphaned children of "failed" agents kept writing, so two agents raced on `heaps`, `sorting-searching`, `trees-bst`, and `coding-interview-strategy`. Nothing corrupted — agents detected concurrent writes and stood down — but a large share of the wave's tokens went to duplicate effort.
- **Verify files, not folders.** `heaps` looked like 8 finished topics for a while; they were 8 empty directories from a dead agent. Count topics by checking all three files exist and parse.

---

## 5. Known defects to fix

1. **`heaps` needs a review pass.** It was written by two racing agents, and one found genuine answer-key bugs in `priority-queues-in-practice` (two MCQs whose `correctIndex` pointed at a different option than the explanation defended). It fixed those two; the group had less coherent single-author attention than the rest. Spot-check all 8 topics.
2. **Cross-link backfill, repo-wide.** `briefs/parts/_existing-slugs.txt` is a wave-start snapshot, so multiple agents saw valid targets as missing and wrote plain text instead of links. Regenerate the snapshot, then sweep for cross-references that should be `[text](slug)`:
   ```bash
   find content -name topic.json -printf '%h\n' | sed 's|content/||' > briefs/parts/_existing-slugs.txt
   ```
3. **Two topics under the 9-slide depth floor:** `heaps/advanced-heap-variants` (8) and `stacks-queues/monotonic-deque` (8). Both are genuinely narrow subjects — acceptable, or pad if you want strict conformance.
4. **239 files carry `<<< Image: … >>>` placeholders** (was 0 before this wave; every new topic adds them by design). The SVG generation pass is `prompts/generate-pending-svgs.md`. Find them with `grep -rln '<<< Image:' content/`.
5. **Brief convention mismatch.** `briefs/expanded/web-frontend.md` marks interview material with "Interview angle: …" bullets instead of the spec's `(interview)` marker; agents had to be told explicitly. Normalize that brief, and check the unstarted areas' briefs for the same drift before authoring them.

---

## 6. Pre-existing debt (from the CURRICULUM audit, not caused by this wave)

1. **Interview-question normalization for the 5 wave-1 areas** — ~230 topics below the current bar. `ai-ml` 68/68 topics and `cs-theory-math` 28/28 have fewer than 3 interview questions; `computer-architecture` 60/81, `cloud-devops-sre` 45/61, `computer-networks` 29/40. Answers in networks/cloud/arch average under 800 chars against a 900–1800 target. Slide counts are short too (`computer-architecture` 77/81 topics under 9 slides).
2. **The `system-design` `interview-*` decision is still open.** 15 groups holding 202 topics model a single interview question as a whole topic, duplicating both the concept groups and the schema's own `interview.json`. Decide: split into its own area, or fold back into `interview.json`. See [CURRICULUM.md §7.5](CURRICULUM.md).
3. **Validator char bands are un-tuned.** ~1400 advisory WARNs in DSA alone, dominated by prose over target. The bands in `tools/validate_v3.py` predate the wave-2 depth bar; either raise them to match the bar or accept that the WARNs are noise. Deliberately not changed — it moves the quality contract every area was written against.
4. **Update [CURRICULUM.md §7](CURRICULUM.md)** — its audit table reflects 856 topics and is now stale.

---

## 7. Spec improvements to fold into `prompts/authoring-agent-v3-area.md`

These are all real failure modes observed in this wave, each caught by at least one agent:

- **Re-derive the answer key.** After writing `mcq.json`, re-read each `explanation` and confirm `correctIndex` points at the option that text defends. At least four agents caught themselves shipping a key pointing at the wrong option after rewording options — the spec's existing "count mechanically" advice does not catch this.
- **Complete all three files per topic before starting the next.** Makes a mid-run crash leave a clean boundary instead of an unvalidatable half-topic.
- **Check disk, not the slug snapshot**, before deciding a cross-link target doesn't exist.
- **JSON escaping remains the top mechanical failure.** Unescaped straight quotes and literal newlines inside markdown strings broke files in at least four groups. Recommend a `python3 -c "import json; json.load(open(...))"` check after every write.
- **Don't sub-delegate** unless the orchestrator says to.

---

## 8. Landing the work

Commit scope rule is strict — stage only task-relevant files, never blanket-add, and keep the legacy `data/` tree out of the commit.

Suggested split:

```bash
# 1. tooling/doc changes
git add CURRICULUM.md TODO.md prompts/authoring-agent-v3-area.md briefs/expanded/system-design.md
git commit -m "docs(curriculum): v3 rewrite with state audit + wave handoff"

# 2. content + regenerated artifacts (run regen FIRST)
python3 tools/regen_v3.py
git add content/data-structures-algorithms content/engineering-craft content/web-frontend \
        content/system-design/uml content/index.json content/bundle.json.gz
git commit -m "feat(content): author data-structures-algorithms area"
```

Pushing to `main` makes it live on the app's next content sync (basePath `content`), so run `python3 tools/validate_v3.py` (0 errors) and `python3 tools/regen_v3.py --check` (OK) before pushing.
