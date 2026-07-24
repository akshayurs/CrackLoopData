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
import json, gzip, hashlib, os, re, sys, subprocess

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

# Per-area accent: (AppIcons name, hex colour). Icon names must exist in the
# app's AppIcons registry.
AREA_META = {
    "ai-ml": ("sparkle", "#7A3AAE"),
    "cloud-devops-sre": ("cloud", "#0E6FB8"),
    "computer-architecture": ("chip", "#C2571A"),
    "computer-networks": ("network", "#0E8A55"),
    "cs-theory-math": ("function", "#B8305A"),
}

# Distinct group colours, cycled by global group index so groups within an area
# are visually distinguishable (harmonious across light/dark).
GROUP_PALETTE = [
    "#0C8F88", "#7A3AAE", "#C2571A", "#0E6FB8", "#0E8A55", "#B8305A",
    "#5A6BD8", "#B8860B", "#2A9D8F", "#9B2226", "#4C6EF5", "#D6336C",
    "#1098AD", "#7048E8",
]

# First matching keyword picks the group icon (AppIcons name); else the area icon.
GROUP_ICON_RULES = [
    (("security", "tls", "crypto", "auth", "attack", "vpn", "zero-trust", "mtls"), "security"),
    (("routing", "ip-", "-ip", "addressing", "dns", "transport", "link-", "wireless",
      "cdn", "load", "mesh", "gateway", "protocol", "network"), "network"),
    (("database", "sql", "-db", "storage-hardware"), "database"),
    (("cache", "virtual-memory"), "memory"),
    (("cpu", "pipeline", "datapath", "isa", "instruction", "register", "alu",
      "multicore", "ilp", "superscalar", "microarch"), "chip"),
    (("gpu", "accelerator", "simd", "vector", "perf", "power"), "speed"),
    (("serverless", "edge", "cloud"), "cloud"),
    (("container", "docker", "kubernetes", "k8s"), "layers"),
    (("cicd", "ci-cd", "iac", "infra"), "terminal"),
    (("observability", "monitoring", "logging", "tracing", "sre", "reliability",
      "incident", "alert", "chaos", "toil"), "analytics"),
    (("cost", "capacity"), "speed"),
    (("api",), "api"),
    (("nlp", "language", "text", "embedding", "bert", "transformer"), "model"),
    (("vision", "image", "cnn", "segmentation", "detection"), "devices"),
    (("llm", "generative", "diffusion", "prompt", "rag", "fine-tun", "rlhf",
      "applied-ai", "agent"), "sparkle"),
    (("reinforcement", "policy", "value-based"), "model"),
    (("recommender", "ranking", "collaborative"), "analytics"),
    (("mlops", "serving", "drift", "feature-store", "versioning"), "tools"),
    (("supervised", "unsupervised", "clustering", "regression", "classification",
      "ensemble", "boosting", "svm", "knn", "bias-variance", "deep-learning",
      "neural", "optimizer", "regulariz", "ml-"), "sparkle"),
    (("algebra", "linear", "probability", "statistic", "combinator", "graph",
      "number-theory", "recurrence", "calculus", "math"), "function"),
    (("automata", "turing", "complexity", "computation", "information", "theory"), "science"),
    (("logic", "proof", "set", "proposition", "discrete"), "function"),
]


def area_meta(area_slug):
    return AREA_META.get(area_slug, ("book", "#5F6368"))


def group_icon(area_slug, group_slug):
    s = group_slug.lower()
    for kws, icon in GROUP_ICON_RULES:
        if any(k in s for k in kws):
            return icon
    return area_meta(area_slug)[0]


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


def area_ranks():
    """Relevance order of areas, from `## Area N — … `<slug>`` in the map."""
    p = os.path.join(ROOT, "briefs", "area-group-map.md")
    ranks, rank = {}, 0
    if os.path.exists(p):
        for line in open(p, encoding="utf-8"):
            m = re.match(r"^##\s+Area\s+\d+.*`([a-z0-9-]+)`", line)
            if m:
                ranks[m.group(1)] = rank
                rank += 1
    return ranks


def group_ranks(area_slug):
    """Relevance order of an area's groups, from the `## Group: … (slug)`
    sequence in its expanded brief."""
    p = os.path.join(ROOT, "briefs", "expanded", f"{area_slug}.md")
    ranks, rank = {}, 0
    if os.path.exists(p):
        for line in open(p, encoding="utf-8"):
            m = re.match(r"^##\s+Group:.*\(([a-z0-9-]+)\)", line)
            if m:
                ranks[m.group(1)] = rank
                rank += 1
    return ranks


def build():
    groups = {}            # slug -> group dict
    files = {}             # bundle: content-rel path -> text
    gcount = 0             # global group index (for palette cycling)
    tot_topics = tot_slides = tot_mcqs = tot_iq = 0
    # Relevance ordering from the briefs; alphabetical only as a last resort.
    arank = area_ranks()
    alpha_areas = {a: i for i, a in enumerate(
        d for d in sorted(os.listdir(CONTENT)) if os.path.isdir(os.path.join(CONTENT, d)))}

    for area_slug in sorted(os.listdir(CONTENT)):
        area_dir = os.path.join(CONTENT, area_slug)
        if not os.path.isdir(area_dir):
            continue
        grank = group_ranks(area_slug)
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
            aicon, acolor = area_meta(area_slug)
            groups[gslug] = {
                "slug": gslug,
                "name": pretty(group_slug),
                "area": area_slug,
                "areaName": pretty(area_slug),
                "order": arank.get(area_slug, 900 + alpha_areas.get(area_slug, 0)) * 1000
                         + grank.get(group_slug,
                                     900 + sorted(os.listdir(area_dir)).index(group_slug)),
                "color": GROUP_PALETTE[gcount % len(GROUP_PALETTE)],
                "icon": group_icon(area_slug, group_slug),
                "areaColor": acolor,
                "areaIcon": aicon,
                "topics": topics,
            }
            gcount += 1

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


def add_aux(index, files):
    """Fold the migrated auxiliary datasets (glossary, remote config, coding
    catalog) into the manifest + bundle so the app reaches them under content/."""
    for aux, key in (("glossary.json", "glossaryFile"), ("config.json", "configFile")):
        p = os.path.join(CONTENT, aux)
        if os.path.exists(p):
            files[aux] = open(p, encoding="utf-8").read()
            index[key] = aux

    prep = os.path.join(CONTENT, "coding", "prep_manifest.json")
    if not os.path.exists(prep):
        return
    ptext = open(prep, encoding="utf-8").read()
    files["coding/prep_manifest.json"] = ptext
    pm = json.loads(ptext)
    refs = set()
    for t in pm.get("topics", []):
        if t.get("primerFile"):
            refs.add(t["primerFile"])
    for q in pm.get("questions", []):
        if q.get("questionFile"):
            refs.add(q["questionFile"])
        for s in q.get("solutions", []):
            if s.get("file"):
                refs.add(s["file"])
    missing = 0
    for rel_ in sorted(refs):
        fp = os.path.join(CONTENT, rel_)
        if os.path.exists(fp):
            files[rel_] = open(fp, encoding="utf-8").read()
        else:
            missing += 1
    index["codingManifest"] = "coding/prep_manifest.json"
    index["codingCount"] = len(pm.get("questions", []))
    if missing:
        print(f"  warning: {missing} coding files referenced but not found on disk")


def main():
    check = "--check" in sys.argv
    index, files = build()
    add_aux(index, files)
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
