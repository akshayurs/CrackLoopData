#!/usr/bin/env python3
"""Regenerate the v3 manifest + bundle from the repo-root content/ tree.

The v3 content tree (content/<area>/<group>/<topic>/{topic.json,mcq.json,
interview.json,assets/*.svg}) has no directory listing over GitHub raw, so the
app needs a generated manifest to enumerate it. This emits:

  content/index.json      schemaVersion 3 manifest the app parses
  content/bundle.json.gz   gzip {"version":1,"files":{relpath:text}} — one
                           download of the whole set (topic/mcq/interview JSON +
                           every SVG asset), plus "index.json" itself

Paths in both are relative to content/ (the flavor's basePath). Each (area,
group) pair folds into one app "group" (slug "<area>__<group>"), with the area
carried as metadata so the app can still section/colour by area.

  python3 tools/regen_v3.py            # regenerate both
  python3 tools/regen_v3.py --check     # verify only, non-zero exit on drift
"""
import json, gzip, hashlib, os, sys, subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT = os.path.join(ROOT, "content")
INDEX = os.path.join(CONTENT, "index.json")
BUNDLE = os.path.join(CONTENT, "bundle.json.gz")

ACRONYMS = {"nlp": "NLP", "llms": "LLMs", "iac": "IaC", "isa": "ISA", "ilp": "ILP",
            "mlops": "MLOps", "gpus": "GPUs", "ai": "AI", "ml": "ML", "cs": "CS",
            "cicd": "CI/CD", "sre": "SRE", "api": "API", "io": "I/O", "cpu": "CPU",
            "gpu": "GPU", "tlb": "TLB", "ip": "IP", "tls": "TLS", "cdn": "CDN",
            "hw": "HW", "e2e": "E2E", "peft": "PEFT", "rlhf": "RLHF", "rl": "RL",
            "cnn": "CNN", "rnn": "RNN", "gmm": "GMM", "pca": "PCA", "svm": "SVM",
            "knn": "kNN", "dbms": "DBMS", "vpn": "VPN", "bgp": "BGP", "svd": "SVD"}

AREA_COLORS = {"ai-ml": "#0C8F88", "cloud-devops-sre": "#7A3AAE",
               "computer-architecture": "#C2571A", "computer-networks": "#0E6FB8",
               "cs-theory-math": "#0E8A55"}


def pretty(slug):
    return " ".join(ACRONYMS.get(w, w.capitalize()) for w in slug.split("-"))


def sha(raw: bytes) -> str:
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def rel(path):
    """content/-relative POSIX path used as index + bundle + cache key."""
    return os.path.relpath(path, CONTENT).replace(os.sep, "/")


def git_sha():
    try:
        return subprocess.check_output(
            ["git", "-C", ROOT, "rev-parse", "--short", "HEAD"],
            stderr=subprocess.DEVNULL).decode().strip()
    except Exception:
        return ""


def build():
    groups = {}            # slug -> group dict
    files = {}             # bundle: content-rel path -> text
    tot_topics = tot_slides = tot_mcqs = tot_iq = 0
    area_order = {a: i for i, a in enumerate(sorted(os.listdir(CONTENT)))
                  if os.path.isdir(os.path.join(CONTENT, a))}

    for area_slug in sorted(os.listdir(CONTENT)):
        area_dir = os.path.join(CONTENT, area_slug)
        if not os.path.isdir(area_dir):
            continue
        for group_slug in sorted(os.listdir(area_dir)):
            group_dir = os.path.join(area_dir, group_slug)
            if not os.path.isdir(group_dir):
                continue
            gslug = f"{area_slug}__{group_slug}"
            topics = []
            for topic_slug in sorted(os.listdir(group_dir)):
                tdir = os.path.join(group_dir, topic_slug)
                tfile = os.path.join(tdir, "topic.json")
                if not os.path.isfile(tfile):
                    continue
                traw = open(tfile, "rb").read()
                topic = json.loads(traw)
                slides = topic.get("slides", [])
                nslides = len(slides)
                files[rel(tfile)] = traw.decode("utf-8")

                entry = {
                    "id": topic.get("id", topic_slug),
                    "title": topic.get("title", pretty(topic_slug)),
                    "order": topic.get("order", 0),
                    "slug": topic.get("slug", topic_slug),
                    "level": topic.get("level"),
                    "group": gslug,
                    "dir": rel(tdir),
                    "topicFile": rel(tfile),
                    "slideCount": nslides,
                    "estReadMinutes": topic.get("estReadMinutes", 0),
                    "checksum": sha(traw),
                }

                mfile = os.path.join(tdir, "mcq.json")
                if os.path.isfile(mfile):
                    mraw = open(mfile, "rb").read()
                    nmcq = len(json.loads(mraw).get("mcqs", []))
                    entry["mcqFile"] = rel(mfile)
                    entry["mcqCount"] = nmcq
                    entry["mcqChecksum"] = sha(mraw)
                    files[rel(mfile)] = mraw.decode("utf-8")
                else:
                    entry["mcqFile"] = None
                    entry["mcqCount"] = 0

                ifile = os.path.join(tdir, "interview.json")
                niq = 0
                if os.path.isfile(ifile):
                    iraw = open(ifile, "rb").read()
                    niq = len(json.loads(iraw).get("interviewQuestions", []))
                    entry["interviewFile"] = rel(ifile)
                    entry["interviewCount"] = niq
                    entry["interviewChecksum"] = sha(iraw)
                    files[rel(ifile)] = iraw.decode("utf-8")
                else:
                    entry["interviewFile"] = None
                    entry["interviewCount"] = 0

                # SVG assets travel in the bundle so diagrams work offline.
                adir = os.path.join(tdir, "assets")
                if os.path.isdir(adir):
                    for a in sorted(os.listdir(adir)):
                        if a.endswith(".svg"):
                            ap = os.path.join(adir, a)
                            files[rel(ap)] = open(ap, encoding="utf-8").read()

                topics.append(entry)
                tot_topics += 1
                tot_slides += nslides
                tot_mcqs += entry["mcqCount"]
                tot_iq += niq

            if not topics:
                continue
            topics.sort(key=lambda t: (t["order"], t["title"]))
            groups[gslug] = {
                "slug": gslug,
                "name": pretty(group_slug),
                "area": area_slug,
                "areaName": pretty(area_slug),
                "order": area_order.get(area_slug, 0) * 1000
                         + sorted(os.listdir(area_dir)).index(group_slug),
                "color": AREA_COLORS.get(area_slug),
                "topics": topics,
            }

    index = {
        "schemaVersion": 3,
        "contentVersion": git_sha(),
        "commitSha": git_sha(),
        "topicCount": tot_topics,
        "slideCount": tot_slides,
        "mcqCount": tot_mcqs,
        "interviewCount": tot_iq,
        "groups": sorted(groups.values(), key=lambda g: g["order"]),
    }
    return index, files


def main():
    check = "--check" in sys.argv
    index, files = build()
    index_text = json.dumps(index, ensure_ascii=False, indent=2)
    files["index.json"] = index_text
    bundle_obj = {"version": 1, "files": files}
    bundle_bytes = gzip.compress(
        json.dumps(bundle_obj, ensure_ascii=False).encode("utf-8"), mtime=0)

    if check:
        old = open(INDEX, encoding="utf-8").read() if os.path.exists(INDEX) else ""
        if old.strip() != index_text.strip():
            print("DRIFT: content/index.json is stale — run tools/regen_v3.py")
            sys.exit(1)
        print("OK: index.json up to date")
        return

    with open(INDEX, "w", encoding="utf-8") as f:
        f.write(index_text)
    with open(BUNDLE, "wb") as f:
        f.write(bundle_bytes)
    print(f"v3 manifest → {rel(INDEX)}")
    print(f"  {index['topicCount']} topics · {index['slideCount']} slides · "
          f"{index['mcqCount']} MCQs · {index['interviewCount']} interview Qs · "
          f"{len(index['groups'])} groups")
    print(f"v3 bundle   → {rel(BUNDLE)}  ({len(files)} files, "
          f"{len(bundle_bytes)//1024} KB gzipped)")


if __name__ == "__main__":
    main()
