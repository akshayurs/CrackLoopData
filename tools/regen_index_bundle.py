#!/usr/bin/env python3
"""Regenerate data/index.json (counts + checksums) and data/bundle.json.gz
from the content files, which are the source of truth.

Run after editing any topic.json / mcq.json / asset. Idempotent: topics you
didn't touch keep byte-identical index entries (checksum = sha256 of file bytes).

  python3 tools/regen_index_bundle.py            # regenerate both
  python3 tools/regen_index_bundle.py --check     # verify only, non-zero exit on drift

Contract (see CONSUMING.md):
  index entry.blockCount   = len(topic.blocks)
  index entry.mcqCount     = len(mcq.blockMcqs)      (0 when mcqFile is null)
  index entry.estReadMinutes = topic.estReadMinutes  (authored in the file)
  index entry.level        = topic.level             (null when omitted)
  index entry.checksum     = "sha256:" + sha256(topic.json bytes)
  index entry.mcqChecksum  = "sha256:" + sha256(mcq.json bytes)
  top-level topicCount/blockCount/mcqCount = sums
  bundle = gzip {"version":1,"files":{ <relpath>: <text>, ... }}
           every file under data/ except bundle.json.gz and .DS_Store
"""
import json, gzip, hashlib, os, sys, io

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")
INDEX = os.path.join(DATA, "index.json")
BUNDLE = os.path.join(DATA, "bundle.json.gz")

def sha(raw: bytes) -> str:
    return "sha256:" + hashlib.sha256(raw).hexdigest()

def rebuild_index(check=False):
    idx = json.load(open(INDEX))
    total_blocks = total_mcqs = total_topics = 0
    drift = []
    for g in idx["groups"]:
        for t in g["topics"]:
            total_topics += 1
            tpath = os.path.join(DATA, t["topicFile"])
            traw = open(tpath, "rb").read()
            topic = json.loads(traw)
            nblocks = len(topic["blocks"])
            new = {
                "blockCount": nblocks,
                "estReadMinutes": topic.get("estReadMinutes", t.get("estReadMinutes")),
                "level": topic.get("level"),
                "checksum": sha(traw),
            }
            nmcq = 0
            if t.get("mcqFile"):
                mraw = open(os.path.join(DATA, t["mcqFile"]), "rb").read()
                nmcq = len(json.loads(mraw).get("blockMcqs", []))
                new["mcqCount"] = nmcq
                new["mcqChecksum"] = sha(mraw)
            else:
                new["mcqCount"] = 0
            for k, v in new.items():
                if t.get(k) != v:
                    drift.append(f"{t['id']}.{k}: {t.get(k)} -> {v}")
                if not check:
                    t[k] = v
            total_blocks += nblocks
            total_mcqs += nmcq
    for k, v in (("topicCount", total_topics), ("blockCount", total_blocks), ("mcqCount", total_mcqs)):
        if idx.get(k) != v:
            drift.append(f"<root>.{k}: {idx.get(k)} -> {v}")
        if not check:
            idx[k] = v
    if not check:
        with open(INDEX, "w") as f:
            json.dump(idx, f, indent=2, ensure_ascii=False)
            f.write("\n")
    return drift, total_topics, total_blocks, total_mcqs

def rebuild_bundle():
    files = {}
    for root, _, names in os.walk(DATA):
        for fn in names:
            if fn in ("bundle.json.gz", ".DS_Store"):
                continue
            p = os.path.join(root, fn)
            rel = os.path.relpath(p, DATA).replace(os.sep, "/")
            files[rel] = open(p, encoding="utf-8").read()
    payload = {"version": 1, "files": {k: files[k] for k in sorted(files)}}
    raw = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    with open(BUNDLE, "wb") as fh:                       # mtime=0 => reproducible output
        with gzip.GzipFile(fileobj=fh, mode="wb", mtime=0) as gz:
            gz.write(raw)
    return len(files)

if __name__ == "__main__":
    check = "--check" in sys.argv
    drift, nt, nb, nm = rebuild_index(check=check)
    if check:
        if drift:
            print("DRIFT (index out of sync with content files):")
            for d in drift:
                print("  " + d)
            sys.exit(1)
        print(f"index in sync: {nt} topics / {nb} blocks / {nm} MCQs")
        sys.exit(0)
    print(f"index.json: {nt} topics / {nb} blocks / {nm} MCQs")
    if drift:
        print(f"  updated {len(drift)} field(s):")
        for d in drift:
            print("  " + d)
    nfiles = rebuild_bundle()
    print(f"bundle.json.gz: {nfiles} files")
