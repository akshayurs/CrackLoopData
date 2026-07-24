#!/usr/bin/env python3
"""CrackLoop v3 content preview server — browse the repo-root content/ tree.

  python3 tools/serve_v3.py            # serve on http://localhost:8000
  python3 tools/serve_v3.py 9000       # custom port
  PORT=9000 python3 tools/serve_v3.py

The v2 preview (tools/serve.py) reads data/index.json + the data/ tree. This one
walks the v3 tree instead — content/<area>/<group>/<topic>/{topic.json, mcq.json,
interview.json, assets/*.svg} — reading the renamed v3 keys (slides[], mcqs[],
interviewQuestions[] in their own file). No index.json needed: the filesystem is
the source of truth. Stdlib only; light/dark toggle and adaptive --dg-* SVG
inlining carried over unchanged.
"""
import json, os, re, html, sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import unquote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT = os.path.join(ROOT, "content")

# ------------------------------------------------------------------ data model
def _pretty(slug):
    acronyms = {"nlp": "NLP", "llms": "LLMs", "iac": "IaC", "isa": "ISA",
                "ilp": "ILP", "mlops": "MLOps", "gpus": "GPUs", "ai": "AI",
                "ml": "ML", "cs": "CS", "cicd": "CI/CD", "sre": "SRE",
                "api": "API", "io": "I/O", "cpu": "CPU", "gpu": "GPU",
                "tlb": "TLB", "ip": "IP", "tls": "TLS", "cdn": "CDN",
                "hw": "HW", "e2e": "E2E", "peft": "PEFT", "rlhf": "RLHF",
                "rl": "RL", "cnn": "CNN", "rnn": "RNN", "gmm": "GMM",
                "pca": "PCA", "svm": "SVM", "knn": "kNN", "dbms": "DBMS"}
    return " ".join(acronyms.get(w, w.capitalize()) for w in slug.split("-"))

AREA_COLORS = ["#0C8F88", "#7A3AAE", "#C2571A", "#0E6FB8", "#0E8A55",
               "#B8305A", "#5A6B00", "#8A5A00", "#3A4AAE"]

def _read(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)

def build_model():
    """areas: [{slug,name,color,order, groups:[{slug,name, topics:[meta...]}]}]"""
    areas = []
    slug_to_route = {}     # topic slug -> (area, group, topic)
    if not os.path.isdir(CONTENT):
        return areas, slug_to_route
    for ai, area_slug in enumerate(sorted(os.listdir(CONTENT))):
        area_dir = os.path.join(CONTENT, area_slug)
        if not os.path.isdir(area_dir):
            continue
        groups = []
        for group_slug in sorted(os.listdir(area_dir)):
            group_dir = os.path.join(area_dir, group_slug)
            if not os.path.isdir(group_dir):
                continue
            topics = []
            for topic_slug in sorted(os.listdir(group_dir)):
                tdir = os.path.join(group_dir, topic_slug)
                tfile = os.path.join(tdir, "topic.json")
                if not os.path.isfile(tfile):
                    continue
                try:
                    t = _read(tfile)
                except Exception:
                    continue
                slides = t.get("slides", [])
                meta = {
                    "area": area_slug, "group": group_slug,
                    "slug": t.get("slug", topic_slug),
                    "id": t.get("id", topic_slug),
                    "title": t.get("title", _pretty(topic_slug)),
                    "level": t.get("level"),
                    "order": t.get("order", 0),
                    "slideCount": t.get("slideCount", len(slides)),
                    "dir": os.path.join(area_slug, group_slug, topic_slug),
                }
                topics.append(meta)
                slug_to_route[meta["slug"]] = (area_slug, group_slug, topic_slug)
                slug_to_route[meta["id"]] = (area_slug, group_slug, topic_slug)
            if topics:
                topics.sort(key=lambda m: (m["order"], m["title"]))
                groups.append({"slug": group_slug, "name": _pretty(group_slug),
                               "topics": topics})
        if groups:
            areas.append({"slug": area_slug, "name": _pretty(area_slug),
                          "color": AREA_COLORS[ai % len(AREA_COLORS)],
                          "order": ai, "groups": groups})
    return areas, slug_to_route

AREAS, SLUG_ROUTE = build_model()

# ------------------------------------------------------------------ markdown
def resolve_asset(topic_dir_rel, rel):
    """Return a /content-relative path that exists (flat assets/ only in v3)."""
    cand = os.path.join(CONTENT, topic_dir_rel, rel)
    if os.path.exists(cand):
        return f"{topic_dir_rel}/{rel}"
    flat = "assets/" + os.path.basename(rel)
    if os.path.exists(os.path.join(CONTENT, topic_dir_rel, flat)):
        return f"{topic_dir_rel}/{flat}"
    return None

def _inline(s, topic_dir_rel):
    s = html.escape(s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<!\*)\*(?!\*)([^*]+)\*(?!\*)", r"<em>\1</em>", s)

    def img(m):
        alt, path = m.group(1), m.group(2)
        data_rel = resolve_asset(topic_dir_rel, path) if topic_dir_rel else None
        if data_rel:
            try:
                raw = open(os.path.join(CONTENT, data_rel), encoding="utf-8").read()
            except Exception:
                raw = ""
            if raw.lstrip().startswith("<svg"):   # inline so it inherits the page's --dg-* theme tokens
                return f'<figure class="plate">{raw}<figcaption>{alt}</figcaption></figure>'
            return (f'<figure class="plate"><img src="/content/{data_rel}" alt="{alt}">'
                    f'<figcaption>{alt}</figcaption></figure>')
        return f'<div class="missing">missing image: {html.escape(path)}</div>'
    s = re.sub(r"!\[([^\]]*)\]\((assets/[^)]+)\)", img, s)

    def link(m):
        text, href = m.group(1), m.group(2)
        route = SLUG_ROUTE.get(href) or SLUG_ROUTE.get(href.split("/")[-1])
        if route:
            a, g, t = route
            return f'<a class="xlink" href="/t/{a}/{g}/{t}">{text}</a>'
        return f'<span class="xlink dead" title="unresolved link: {html.escape(href)}">{text}</span>'
    s = re.sub(r"(?<!\!)\[([^\]]+)\]\(([^)]+)\)", link, s)
    return s

def md_to_html(md, topic_dir_rel=None):
    md = re.sub(r"<<<\s*Image:\s*(.*?)>>>",
                lambda m: "\n\n@@PLACEHOLDER@@" + m.group(1).strip().replace("\n", " ") + "@@\n\n",
                md, flags=re.S)
    lines = md.split("\n"); out = []; i = 0
    while i < len(lines):
        ln = lines[i]
        if ln.startswith("@@PLACEHOLDER@@"):
            prompt = ln[len("@@PLACEHOLDER@@"):].rstrip("@")
            out.append(f'<div class="placeholder"><span>Diagram not yet generated</span>'
                       f'<details><summary>generation prompt</summary>{html.escape(prompt)}</details></div>')
            i += 1; continue
        if ln.startswith("```"):
            lang = ln[3:].strip(); j = i + 1; code = []
            while j < len(lines) and not lines[j].startswith("```"):
                code.append(lines[j]); j += 1
            out.append(f'<pre data-lang="{html.escape(lang)}"><code>{html.escape(chr(10).join(code))}</code></pre>')
            i = j + 1; continue
        h = re.match(r"^(#{1,6})\s+(.*)$", ln)
        if h:
            n = len(h.group(1))
            out.append(f"<h{n} class=md-h>{_inline(h.group(2), topic_dir_rel)}</h{n}>"); i += 1; continue
        if re.match(r"^\s*(---+|\*\*\*+)\s*$", ln):
            out.append("<hr>"); i += 1; continue
        if ln.strip().startswith("|") and i + 1 < len(lines) and set(lines[i+1].replace("|","").strip()) <= set("-: "):
            hdr = [c.strip() for c in ln.strip().strip("|").split("|")]
            rows = []; j = i + 2
            while j < len(lines) and lines[j].strip().startswith("|"):
                rows.append([c.strip() for c in lines[j].strip().strip("|").split("|")]); j += 1
            th = "".join(f"<th>{_inline(c, topic_dir_rel)}</th>" for c in hdr)
            trs = "".join("<tr>" + "".join(f"<td>{_inline(c, topic_dir_rel)}</td>" for c in r) + "</tr>" for r in rows)
            out.append(f'<div class="twrap"><table><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table></div>')
            i = j; continue
        if ln.strip().startswith(">"):
            quote = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                quote.append(re.sub(r"^\s*>\s?", "", lines[i])); i += 1
            out.append(f"<blockquote>{_inline(' '.join(quote), topic_dir_rel)}</blockquote>"); continue
        if re.match(r"^\s*[-*] ", ln):
            items = []
            while i < len(lines) and re.match(r"^\s*[-*] ", lines[i]):
                items.append("<li>" + _inline(re.sub(r"^\s*[-*] ", "", lines[i]), topic_dir_rel) + "</li>"); i += 1
            out.append("<ul>" + "".join(items) + "</ul>"); continue
        if re.match(r"^\s*\d+\. ", ln):
            items = []
            while i < len(lines) and re.match(r"^\s*\d+\. ", lines[i]):
                items.append("<li>" + _inline(re.sub(r"^\s*\d+\. ", "", lines[i]), topic_dir_rel) + "</li>"); i += 1
            out.append("<ol>" + "".join(items) + "</ol>"); continue
        if ln.strip() == "":
            i += 1; continue
        out.append("<p>" + _inline(ln, topic_dir_rel) + "</p>"); i += 1
    return "\n".join(out)

# ------------------------------------------------------------------ rendering
def chip(cls, text):
    return f'<span class="chip {cls}">{html.escape(str(text))}</span>'

def _find_topic(area_slug, group_slug, topic_slug):
    a = next((x for x in AREAS if x["slug"] == area_slug), None)
    if not a: return None, None, None
    g = next((x for x in a["groups"] if x["slug"] == group_slug), None)
    if not g: return a, None, None
    m = next((t for t in g["topics"] if t["slug"] == topic_slug or t["id"] == topic_slug), None)
    return a, g, m

def render_topic(area_slug, group_slug, topic_slug):
    a, g, meta = _find_topic(area_slug, group_slug, topic_slug)
    if not meta:
        return None
    data_rel = meta["dir"]
    topic = _read(os.path.join(CONTENT, data_rel, "topic.json"))
    slides = sorted(topic.get("slides", []), key=lambda s: s.get("order", 0))

    mcqs = {}
    mfile = os.path.join(CONTENT, data_rel, "mcq.json")
    if os.path.isfile(mfile):
        for q in _read(mfile).get("mcqs", []):
            mcqs.setdefault(q.get("slideId"), []).append(q)
        # also index by id so slide.mcqIds resolves regardless of slideId presence
    mcq_by_id = {}
    if os.path.isfile(mfile):
        for q in _read(mfile).get("mcqs", []):
            mcq_by_id[q.get("id")] = q

    interviews = []
    ifile = os.path.join(CONTENT, data_rel, "interview.json")
    if os.path.isfile(ifile):
        interviews = _read(ifile).get("interviewQuestions", [])

    from collections import Counter
    lc = Counter(s.get("level") for s in slides)
    mcq_total = len(mcq_by_id)
    stats = "".join([
        f'<div class="stat"><b>{topic.get("slideCount", len(slides))}</b><span>slides</span></div>',
        f'<div class="stat"><b>{mcq_total}</b><span>MCQs</span></div>',
        f'<div class="stat"><b>{len(interviews)}</b><span>interview Qs</span></div>',
        f'<div class="stat"><b>{topic.get("estReadMinutes","-")}</b><span>min read</span></div>',
        f'<div class="stat"><b>{lc.get("beginner",0)}/{lc.get("intermediate",0)}/{lc.get("advanced",0)}</b><span>beg/int/adv</span></div>',
    ])
    parts = [f'<header class="topic"><p class="kicker">{html.escape(a["name"])} · {html.escape(g["name"])}</p>'
             f'<h1>{html.escape(topic.get("title",""))}</h1>'
             f'<p class="summary">{html.escape(topic.get("summary",""))}</p>'
             f'<div class="stats">{stats}</div></header>']

    def render_mcq(q):
        opts = "".join(
            f'<li class="{"ok" if k==q.get("correctIndex") else ""}"><span class="ok-k">{chr(65+k)}</span>{html.escape(o)}</li>'
            for k, o in enumerate(q.get("options", [])))
        return (f'<div class="quiz"><div class="qq">{html.escape(q.get("question",""))}'
                f'{chip("diff diff-"+q.get("difficulty","medium"), q.get("difficulty",""))}</div>'
                f'<ul class="opts">{opts}</ul>'
                f'<div class="expl"><span>Answer</span>{html.escape(q.get("explanation",""))}</div></div>')

    last = object()
    for b in slides:
        if b.get("sectionTitle") != last:
            if b.get("sectionTitle"):
                parts.append(f'<h2 class="eyebrow">{html.escape(str(b["sectionTitle"]))}</h2>')
            last = b.get("sectionTitle")
        head = [chip(f'type type-{b.get("type","concept")}', b.get("type","concept"))]
        if b.get("level"): head.append(chip(f'lvl-{b["level"]}', b["level"]))
        if b.get("subTitle"): head.append(f'<span class="sub">{html.escape(b["subTitle"])}</span>')
        seen = set(); quiz = ""
        for qid in b.get("mcqIds", []):
            q = mcq_by_id.get(qid)
            if q and qid not in seen:
                seen.add(qid); quiz += render_mcq(q)
        for q in mcqs.get(b.get("id"), []):   # fallback: link by slideId
            if q.get("id") not in seen:
                seen.add(q.get("id")); quiz += render_mcq(q)
        parts.append(f'<article class="card"><div class="chead">{"".join(head)}</div>'
                     f'<div class="body">{md_to_html(b.get("markdown",""), data_rel)}</div>{quiz}</article>')

    if interviews:
        parts.append('<h2 class="eyebrow">Interview questions</h2>')
        for q in sorted(interviews, key=lambda x: (not x.get("mostAsked"), 0)):
            head = [chip("type type-interview", "interview")]
            if q.get("mostAsked"): head.append(chip("lvl-beginner", "★ most asked"))
            if q.get("level"): head.append(chip(f'lvl-{q["level"]}', q["level"]))
            if q.get("subTitle"): head.append(f'<span class="sub">{html.escape(q["subTitle"])}</span>')
            qtext = f'<p class="iq">{html.escape(q.get("question",""))}</p>'
            parts.append(f'<article class="card"><div class="chead">{"".join(head)}</div>'
                         f'<div class="body">{qtext}{md_to_html(q.get("answerMarkdown",""), data_rel)}</div></article>')

    return page("Learning", ("t", area_slug, group_slug, topic_slug), "\n".join(parts))

# ------------------------------------------------------------------ shell / nav
def _grp_block(title, color, count, is_open, items_html, cls="grp"):
    op = " open" if is_open else ""
    return (f'<div class="grp-block{op}" style="--gc:{color}">'
            f'<button class="{cls}" type="button">{html.escape(title)}'
            f'<em>{count}</em><i class="caret"></i></button>'
            f'<div class="grp-items">{items_html}</div></div>')

def sidebar(active):
    kind = active[0] if active else ""
    out = ['<nav class="side"><input id="filter" placeholder="Filter topics…" autocomplete=off>']
    out.append('<div class="side-scroll">')
    for a in AREAS:
        area_active = kind == "t" and active[1] == a["slug"]
        out.append(f'<div class="sec-h" style="color:{a["color"]}">{html.escape(a["name"])}</div>')
        for g in a["groups"]:
            group_active = area_active and active[2] == g["slug"]
            items = []
            for t in g["topics"]:
                on = "on" if (group_active and active[3] == t["slug"]) else ""
                lvl = f'<i class="dot lvl-{t["level"]}"></i>' if t.get("level") else '<i class="dot"></i>'
                items.append(f'<a class="item {on}" href="/t/{a["slug"]}/{g["slug"]}/{t["slug"]}">{lvl}'
                             f'<span>{html.escape(t["title"])}</span><em>{t.get("slideCount","")}</em></a>')
            out.append(_grp_block(g["name"], a["color"], len(g["topics"]),
                                  group_active, "".join(items)))
    out.append("</div></nav>")
    return "".join(out)

def page(section, active, body):
    return (PAGE_TMPL
            .replace("%%TITLE%%", html.escape(section + " · CrackLoop v3 preview"))
            .replace("%%SIDEBAR%%", sidebar(active))
            .replace("%%BODY%%", body))

def render_home():
    nt = sum(len(g["topics"]) for a in AREAS for g in a["groups"])
    ng = sum(len(a["groups"]) for a in AREAS)
    cards = ""
    for a in AREAS:
        first = a["groups"][0]["topics"][0]
        tcount = sum(len(g["topics"]) for g in a["groups"])
        cards += (f'<a class="home-card" href="/t/{a["slug"]}/{first["group"]}/{first["slug"]}" '
                  f'style="--gc:{a["color"]}"><b>{html.escape(a["name"])}</b>'
                  f'<span>{len(a["groups"])} groups · {tcount} topics</span></a>')
    body = (f'<header class="topic"><p class="kicker">CrackLoop · v3 local preview</p>'
            f'<h1>Content preview (v3)</h1>'
            f'<p class="summary">{len(AREAS)} areas · {ng} groups · {nt} topics. '
            f'Reads the repo-root <code>content/</code> tree directly. '
            f'Pick a topic on the left, or an area below.</p></header>'
            f'<div class="home-grid">{cards}</div>')
    return page("Home", ("home",), body)

PAGE_TMPL = """<!doctype html><html lang=en><head><meta charset=utf-8>
<meta name=viewport content="width=device-width,initial-scale=1">
<title>%%TITLE%%</title>
<script>(function(){var t=localStorage.getItem('cl-theme');if(t)document.documentElement.setAttribute('data-theme',t);})();</script>
<style>__CSS__</style></head><body>
<div class="topbar"><a class="brand" href="/">CrackLoop <span>v3 preview</span></a>
<button id="menu" aria-label="menu">☰</button>
<button id="theme" aria-label="toggle theme"><span class="tl">Light</span><span class="td">Dark</span></button></div>
<div class="layout">%%SIDEBAR%%<main class="main"><div class="main-in">%%BODY%%</div></main></div>
<script>__JS__</script></body></html>"""

JS = r"""
document.getElementById('theme').addEventListener('click',function(){
  var r=document.documentElement, cur=r.getAttribute('data-theme');
  if(!cur){cur=matchMedia('(prefers-color-scheme:dark)').matches?'dark':'light';}
  var next=cur==='dark'?'light':'dark';
  r.setAttribute('data-theme',next); localStorage.setItem('cl-theme',next);
});
document.getElementById('menu').addEventListener('click',function(){
  document.querySelector('.side').classList.toggle('open');
});
document.querySelectorAll('.side .grp').forEach(function(b){
  b.addEventListener('click',function(){ b.parentElement.classList.toggle('open'); });
});
var f=document.getElementById('filter');
if(f)f.addEventListener('input',function(){
  var q=this.value.toLowerCase().trim();
  document.querySelectorAll('.side .grp-block').forEach(function(blk){
    var any=false;
    blk.querySelectorAll('.item').forEach(function(a){
      var hit=!q||a.textContent.toLowerCase().indexOf(q)>=0;
      a.style.display=hit?'':'none'; if(hit&&q)any=true;
    });
    if(q){ blk.style.display=any?'':'none'; blk.classList.toggle('open',any); }
    else { blk.style.display=''; }
  });
  if(!q){
    document.querySelectorAll('.side .grp-block').forEach(b=>b.classList.remove('open'));
    var on=document.querySelector('.side .item.on');
    if(on)on.closest('.grp-block').classList.add('open');
  }
});
var cur=document.querySelector('.side .item.on');
if(cur)cur.scrollIntoView({block:'center'});
"""

CSS = r"""
:root{
  --ground:#F5F8F8;--card:#FFF;--ink:#14201F;--muted:#5A6B6A;--faint:#7C8C8A;
  --border:#E2E9E8;--border2:#CBD8D6;--accent:#0C8F88;--soft:#E3F3F1;
  --code:#F0F5F4;--plate:#FFF;--pre-bg:#12201E;--pre-ink:#CBD8D5;
  --good:#0E8A55;--good-bg:#E4F4EC;--warn:#9A6B00;--warn-bg:#FBF0DA;--crit:#7A3AAE;--crit-bg:#F1E8FB;
  --fb:"Charter","Iowan Old Style",Palatino,Georgia,serif;
  --fu:ui-sans-serif,system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;
  --fm:ui-monospace,"SF Mono",Menlo,Consolas,monospace;--side:300px;
}
@media(prefers-color-scheme:dark){:root{
  --ground:#0E1514;--card:#16201F;--ink:#E6EDEC;--muted:#93A3A1;--faint:#7B8A88;
  --border:#26322F;--border2:#33423F;--accent:#2FD6CC;--soft:#0F2624;
  --code:#1C2827;--plate:#F7FAFA;--pre-bg:#0A1211;--pre-ink:#C4D2CF;
  --good:#4ED08A;--good-bg:#12281E;--warn:#E0B155;--warn-bg:#2A2213;--crit:#C69BEA;--crit-bg:#231831;}}
:root[data-theme=light]{--ground:#F5F8F8;--card:#FFF;--ink:#14201F;--muted:#5A6B6A;--faint:#7C8C8A;--border:#E2E9E8;--border2:#CBD8D6;--accent:#0C8F88;--soft:#E3F3F1;--code:#F0F5F4;--plate:#FFF;--pre-bg:#12201E;--pre-ink:#CBD8D5;--good:#0E8A55;--good-bg:#E4F4EC;--warn:#9A6B00;--warn-bg:#FBF0DA;--crit:#7A3AAE;--crit-bg:#F1E8FB;}
:root[data-theme=dark]{--ground:#0E1514;--card:#16201F;--ink:#E6EDEC;--muted:#93A3A1;--faint:#7B8A88;--border:#26322F;--border2:#33423F;--accent:#2FD6CC;--soft:#0F2624;--code:#1C2827;--plate:#F7FAFA;--pre-bg:#0A1211;--pre-ink:#C4D2CF;--good:#4ED08A;--good-bg:#12281E;--warn:#E0B155;--warn-bg:#2A2213;--crit:#C69BEA;--crit-bg:#231831;}
:root{--dg-ink:#202124;--dg-muted:#5F6368;--dg-line:#5F6368;--dg-fill:#F1F3F4;--dg-stroke:#9AA0A6;--dg-accent:#0C8F88;--dg-accent-bg:#E3F3F1}
@media(prefers-color-scheme:dark){:root{--dg-ink:#E6EDEC;--dg-muted:#9AA0A6;--dg-line:#8FA09E;--dg-fill:#1C2827;--dg-stroke:#3A4A47;--dg-accent:#2FD6CC;--dg-accent-bg:#123330}}
:root[data-theme=light]{--dg-ink:#202124;--dg-muted:#5F6368;--dg-line:#5F6368;--dg-fill:#F1F3F4;--dg-stroke:#9AA0A6;--dg-accent:#0C8F88;--dg-accent-bg:#E3F3F1}
:root[data-theme=dark]{--dg-ink:#E6EDEC;--dg-muted:#9AA0A6;--dg-line:#8FA09E;--dg-fill:#1C2827;--dg-stroke:#3A4A47;--dg-accent:#2FD6CC;--dg-accent-bg:#123330}
*{box-sizing:border-box}
body{margin:0;background:var(--ground);color:var(--ink);font-family:var(--fb);font-size:17px;line-height:1.65;-webkit-font-smoothing:antialiased}
.topbar{position:sticky;top:0;z-index:20;display:flex;align-items:center;gap:12px;height:52px;padding:0 16px;background:var(--card);border-bottom:1px solid var(--border)}
.brand{font-family:var(--fu);font-weight:700;color:var(--ink);text-decoration:none;letter-spacing:-.01em}
.brand span{color:var(--accent);font-weight:600}
#theme{margin-left:auto}
.topbar button{font-family:var(--fu);font-size:13px;font-weight:600;cursor:pointer;background:var(--ground);color:var(--ink);border:1px solid var(--border2);border-radius:8px;padding:6px 12px}
#menu{display:none}
#theme .td{display:none}
:root[data-theme=dark] #theme .tl,html:not([data-theme]) #theme .td{display:none}
@media(prefers-color-scheme:dark){html:not([data-theme]) #theme .tl{display:none}html:not([data-theme]) #theme .td{display:inline}}
:root[data-theme=dark] #theme .td{display:inline}
.layout{display:grid;grid-template-columns:var(--side) 1fr;min-height:calc(100vh - 52px)}
.side{border-right:1px solid var(--border);background:var(--card);position:sticky;top:52px;height:calc(100vh - 52px);display:flex;flex-direction:column;font-family:var(--fu)}
#filter{margin:12px;padding:8px 10px;border:1px solid var(--border2);border-radius:8px;background:var(--ground);color:var(--ink);font-size:13px;font-family:var(--fu)}
.side-scroll{overflow-y:auto;padding:0 8px 24px}
.sec-h{font-size:11px;font-weight:700;letter-spacing:.09em;text-transform:uppercase;color:var(--faint);padding:14px 8px 6px}
.grp-block{margin-top:2px}
.grp{display:flex;align-items:center;gap:7px;width:100%;text-align:left;cursor:pointer;font-family:var(--fu);font-size:12.5px;font-weight:700;color:var(--ink);padding:8px;background:none;border:0;border-left:3px solid var(--gc,transparent);border-radius:0 6px 6px 0}
.grp:hover{background:var(--ground)}
.grp em{font-style:normal;font-size:11px;font-weight:600;color:var(--faint);margin-left:auto}
.caret{width:0;height:0;border-left:5px solid currentColor;border-top:4px solid transparent;border-bottom:4px solid transparent;opacity:.5;transition:transform .15s;flex:none}
.grp-block.open .caret{transform:rotate(90deg)}
.grp-items{display:none;padding-bottom:4px}
.grp-block.open .grp-items{display:block}
.item{display:flex;align-items:center;gap:8px;text-decoration:none;color:var(--muted);font-size:13.5px;padding:6px 8px;border-radius:8px}
.item:hover{background:var(--ground);color:var(--ink)}
.item.on{background:var(--soft);color:var(--accent);font-weight:600}
.item span{flex:1;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.item em{font-style:normal;font-size:11px;color:var(--faint)}
.dot{width:7px;height:7px;border-radius:50%;background:var(--border2);flex:none}
.dot.lvl-beginner{background:var(--good)}
.dot.lvl-intermediate{background:var(--warn)}
.dot.lvl-advanced{background:var(--crit)}
.main{overflow-x:hidden}
.main-in{max-width:760px;margin:0 auto;padding:40px 28px 96px}
.topic{border-bottom:1px solid var(--border);padding-bottom:24px;margin-bottom:8px}
.kicker{font-family:var(--fu);font-size:12px;letter-spacing:.09em;text-transform:uppercase;color:var(--accent);font-weight:600;margin:0 0 10px}
h1{font-family:var(--fu);font-weight:700;font-size:32px;line-height:1.14;margin:0 0 12px;letter-spacing:-.02em;text-wrap:balance}
.summary{font-size:18px;color:var(--muted);margin:0 0 20px;max-width:60ch}
.stats{display:flex;flex-wrap:wrap;gap:10px}
.stat{background:var(--ground);border:1px solid var(--border);border-radius:10px;padding:8px 14px;font-family:var(--fu)}
.stat b{display:block;font-size:20px;color:var(--accent);font-variant-numeric:tabular-nums}
.stat span{font-size:11px;color:var(--muted)}
.eyebrow{font-family:var(--fu);font-size:12px;font-weight:700;letter-spacing:.11em;text-transform:uppercase;color:var(--accent);margin:36px 0 4px}
.card{background:var(--card);border:1px solid var(--border);border-radius:16px;padding:22px 24px;margin:14px 0}
.chead{display:flex;align-items:center;gap:8px;margin-bottom:12px;flex-wrap:wrap;font-family:var(--fu)}
.chip{font-family:var(--fu);font-size:11px;font-weight:600;letter-spacing:.03em;padding:3px 9px;border-radius:100px;text-transform:uppercase;background:var(--border);color:var(--muted)}
.type-interview{background:var(--soft);color:var(--accent)}
.type-code{background:var(--good-bg);color:var(--good)}
.type-pitfall{background:var(--crit-bg);color:var(--crit)}
.type-diagram{background:var(--warn-bg);color:var(--warn)}
.type-compare{background:var(--warn-bg);color:var(--warn)}
.type-overview{background:var(--soft);color:var(--accent)}
.lvl-beginner{background:var(--good-bg);color:var(--good)}
.lvl-intermediate{background:var(--warn-bg);color:var(--warn)}
.lvl-advanced{background:var(--crit-bg);color:var(--crit)}
.diff-easy{background:var(--good-bg);color:var(--good)}
.diff-medium{background:var(--warn-bg);color:var(--warn)}
.diff-hard{background:var(--crit-bg);color:var(--crit)}
.sub{margin-left:auto;font-family:var(--fu);font-weight:600;font-size:14px;color:var(--ink);text-transform:none;letter-spacing:0}
.body>*:first-child{margin-top:0}.body>*:last-child{margin-bottom:0}
.body p{margin:0 0 14px}.body ul,.body ol{margin:0 0 14px;padding-left:22px}.body li{margin:5px 0}
.iq{font-family:var(--fu);font-weight:600;font-size:16px;color:var(--ink)}
.md-h{font-family:var(--fu);margin:18px 0 8px;line-height:1.25}
code{font-family:var(--fm);font-size:.85em;background:var(--code);padding:2px 6px;border-radius:5px}
pre{background:var(--pre-bg);color:var(--pre-ink);padding:16px 18px;border-radius:12px;overflow-x:auto;margin:0 0 14px;line-height:1.5}
pre code{background:none;padding:0;color:inherit;font-size:13px}
.twrap{overflow-x:auto;margin:0 0 14px}
table{border-collapse:collapse;width:100%;font-family:var(--fu);font-size:14px}
th,td{border:1px solid var(--border);padding:8px 12px;text-align:left;vertical-align:top}
th{background:var(--soft)}
blockquote{border-left:3px solid var(--accent);margin:0 0 14px;padding:4px 16px;color:var(--muted);background:var(--ground);border-radius:0 8px 8px 0}
.plate{margin:4px 0 14px;background:var(--card);border:1px solid var(--border);border-radius:12px;padding:16px}
.plate img,.plate svg{max-width:100%;height:auto;display:block;margin:0 auto}
.plate figcaption{font-family:var(--fu);font-size:12px;color:var(--muted);text-align:center;margin-top:10px}
.placeholder{border:1px dashed var(--border2);border-radius:12px;padding:18px;text-align:center;color:var(--muted);font-family:var(--fu);margin:0 0 14px}
.placeholder span{font-weight:600}
.placeholder details{margin-top:8px;font-size:12px;text-align:left}
.missing{color:var(--crit);font-family:var(--fu);font-size:13px}
.xlink{color:var(--accent);text-decoration:none;border-bottom:1px solid var(--border2)}
.xlink.dead{color:var(--muted);border-bottom:1px dotted var(--border2);cursor:help}
.quiz{margin-top:16px;border:1px solid var(--border);border-left:3px solid var(--accent);border-radius:10px;padding:14px 16px;background:var(--ground)}
.qq{font-family:var(--fu);font-weight:600;font-size:15px;display:flex;gap:8px;align-items:baseline;justify-content:space-between}
.opts{list-style:none;padding:0;margin:12px 0 0;font-family:var(--fu);font-size:14px}
.opts li{display:flex;gap:10px;align-items:baseline;padding:6px 0;color:var(--muted)}
.ok-k{font-weight:700;color:var(--faint);min-width:16px}
.opts li.ok{color:var(--good);font-weight:600}
.opts li.ok .ok-k{color:var(--good)}
.opts li.ok::after{content:"\2713";margin-left:auto;color:var(--good)}
.expl{font-family:var(--fu);font-size:13px;color:var(--muted);margin-top:12px;padding-top:10px;border-top:1px dashed var(--border)}
.expl span{font-weight:700;color:var(--accent);text-transform:uppercase;font-size:11px;letter-spacing:.05em;margin-right:8px}
.home-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:12px;margin-top:20px}
.home-card{text-decoration:none;background:var(--card);border:1px solid var(--border);border-left:4px solid var(--gc,var(--accent));border-radius:12px;padding:16px 18px;color:var(--ink)}
.home-card b{display:block;font-family:var(--fu);font-size:15px}
.home-card span{font-family:var(--fu);font-size:12px;color:var(--muted)}
@media(max-width:900px){
  #menu{display:block;order:-1}
  .layout{grid-template-columns:1fr}
  .side{position:fixed;left:0;top:52px;width:var(--side);z-index:15;transform:translateX(-100%);transition:transform .2s}
  .side.open{transform:none}
}
"""

PAGE_TMPL = PAGE_TMPL.replace("__CSS__", CSS).replace("__JS__", JS)

# ------------------------------------------------------------------ http
class Handler(BaseHTTPRequestHandler):
    def log_message(self, *a): pass

    def _send(self, body, ctype="text/html; charset=utf-8", code=200):
        data = body.encode("utf-8") if isinstance(body, str) else body
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        if self.command != "HEAD":
            self.wfile.write(data)

    def do_GET(self):
        path = unquote(self.path.split("?", 1)[0])
        try:
            if path == "/" or path == "":
                return self._send(render_home())
            if path.startswith("/content/"):
                return self._serve_static(path[len("/content/"):])
            parts = [p for p in path.strip("/").split("/") if p]
            if parts and parts[0] == "t" and len(parts) == 4:
                html_out = render_topic(parts[1], parts[2], parts[3])
                return self._send(html_out) if html_out else self._send(self._404(path), code=404)
            return self._send(self._404(path), code=404)
        except Exception as e:
            return self._send(f"<pre>error rendering {html.escape(path)}:\n{html.escape(repr(e))}</pre>", code=500)

    do_HEAD = do_GET

    def _serve_static(self, rel):
        safe = os.path.normpath(os.path.join(CONTENT, rel))
        if not safe.startswith(CONTENT) or not os.path.isfile(safe):
            return self._send("not found", ctype="text/plain", code=404)
        ct = ("image/svg+xml" if safe.endswith(".svg") else
              "application/json" if safe.endswith(".json") else
              "text/plain; charset=utf-8")
        with open(safe, "rb") as f:
            self._send(f.read(), ctype=ct)

    def _404(self, path):
        return page("Not found", ("home",),
                    f'<header class="topic"><h1>404</h1><p class="summary">No content at '
                    f'<code>{html.escape(path)}</code>. Pick something from the sidebar.</p></header>')

def main():
    port = int(sys.argv[1]) if len(sys.argv) > 1 else int(os.environ.get("PORT", "8000"))
    srv = ThreadingHTTPServer(("127.0.0.1", port), Handler)
    nt = sum(len(g["topics"]) for a in AREAS for g in a["groups"])
    print(f"CrackLoop v3 preview → http://localhost:{port}")
    print(f"  {len(AREAS)} areas · {nt} topics (from {CONTENT})")
    print("  Ctrl-C to stop")
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        print("\nstopped")

if __name__ == "__main__":
    main()
