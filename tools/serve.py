#!/usr/bin/env python3
"""CrackLoop content preview server — browse the data/ tree the way the app does.

  python3 tools/serve.py            # serve on http://localhost:8000
  python3 tools/serve.py 9000       # custom port
  PORT=9000 python3 tools/serve.py

Reads data/index.json + the content files and renders each learning topic
(blocks, inline MCQs, SVG diagrams) and each coding question the way a client
would. Stdlib only — no install, no build step. Light/dark toggle in the top bar.

The renderer is defensive: it self-heals the known nested image-path bug
(`assets/<slug>/x.svg` -> flat `assets/x.svg`) so diagrams show even before that
fix lands, and it renders `<<< Image: ... >>>` placeholders as a labelled slot.
"""
import json, os, re, html, sys, socket
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import unquote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")

# ------------------------------------------------------------------ data model
def load(rel):
    with open(os.path.join(DATA, rel), encoding="utf-8") as f:
        return json.load(f)

def build_model():
    idx = load("index.json")
    groups = sorted(idx["groups"], key=lambda g: g.get("order", 0))
    slug_to_route = {}          # topic slug -> (group-slug, topic-slug)
    for g in groups:
        g["topics"] = sorted(g["topics"], key=lambda t: t.get("order", 0))
        for t in g["topics"]:
            slug_to_route[t["id"]] = (g["slug"], t["id"])
    coding = {"topics": [], "questions": [], "byid": {}}
    cpath = os.path.join(DATA, "coding", "prep_manifest.json")
    if os.path.exists(cpath):
        cm = json.load(open(cpath, encoding="utf-8"))
        coding["topics"] = sorted(cm.get("topics", []), key=lambda t: t.get("order", 0))
        coding["questions"] = cm.get("questions", [])
        coding["byid"] = {q["id"]: q for q in coding["questions"]}
    return idx, groups, slug_to_route, coding

IDX, GROUPS, SLUG_ROUTE, CODING = build_model()

# ------------------------------------------------------------------ markdown
LEVEL_ORDER = {"beginner": 0, "intermediate": 1, "advanced": 2, "expert": 3}

def resolve_asset(topic_data_rel, rel):
    """Return a /data-relative path that exists, healing the nested-path bug."""
    cand = os.path.join(DATA, topic_data_rel, rel)
    if os.path.exists(cand):
        return f"{topic_data_rel}/{rel}"
    flat = "assets/" + os.path.basename(rel)
    if os.path.exists(os.path.join(DATA, topic_data_rel, flat)):
        return f"{topic_data_rel}/{flat}"
    return None

def _inline(s, topic_data_rel):
    s = html.escape(s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<!\*)\*(?!\*)([^*]+)\*(?!\*)", r"<em>\1</em>", s)

    def img(m):
        alt, path = m.group(1), m.group(2)
        data_rel = resolve_asset(topic_data_rel, path) if topic_data_rel else None
        if data_rel:
            return (f'<figure class="plate"><img src="/data/{data_rel}" alt="{alt}">'
                    f'<figcaption>{alt}</figcaption></figure>')
        return f'<div class="missing">missing image: {html.escape(path)}</div>'
    s = re.sub(r"!\[([^\]]*)\]\((assets/[^)]+)\)", img, s)

    def link(m):
        text, href = m.group(1), m.group(2)
        if href in SLUG_ROUTE:
            g, t = SLUG_ROUTE[href]
            return f'<a class="xlink" href="/t/{g}/{t}">{text}</a>'
        return f'<span class="xlink dead" title="unresolved link: {html.escape(href)}">{text}</span>'
    s = re.sub(r"(?<!\!)\[([^\]]+)\]\(([^)]+)\)", link, s)
    return s

def md_to_html(md, topic_data_rel=None):
    # image placeholders first (may span the block)
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
            out.append(f"<h{n} class=md-h>{_inline(h.group(2), topic_data_rel)}</h{n}>"); i += 1; continue
        if re.match(r"^\s*(---+|\*\*\*+)\s*$", ln):
            out.append("<hr>"); i += 1; continue
        if ln.strip().startswith("|") and i + 1 < len(lines) and set(lines[i+1].replace("|","").strip()) <= set("-: "):
            hdr = [c.strip() for c in ln.strip().strip("|").split("|")]
            rows = []; j = i + 2
            while j < len(lines) and lines[j].strip().startswith("|"):
                rows.append([c.strip() for c in lines[j].strip().strip("|").split("|")]); j += 1
            th = "".join(f"<th>{_inline(c, topic_data_rel)}</th>" for c in hdr)
            trs = "".join("<tr>" + "".join(f"<td>{_inline(c, topic_data_rel)}</td>" for c in r) + "</tr>" for r in rows)
            out.append(f'<div class="twrap"><table><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table></div>')
            i = j; continue
        if ln.strip().startswith(">"):
            quote = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                quote.append(re.sub(r"^\s*>\s?", "", lines[i])); i += 1
            out.append(f"<blockquote>{_inline(' '.join(quote), topic_data_rel)}</blockquote>"); continue
        if re.match(r"^\s*[-*] ", ln):
            items = []
            while i < len(lines) and re.match(r"^\s*[-*] ", lines[i]):
                items.append("<li>" + _inline(re.sub(r"^\s*[-*] ", "", lines[i]), topic_data_rel) + "</li>"); i += 1
            out.append("<ul>" + "".join(items) + "</ul>"); continue
        if re.match(r"^\s*\d+\. ", ln):
            items = []
            while i < len(lines) and re.match(r"^\s*\d+\. ", lines[i]):
                items.append("<li>" + _inline(re.sub(r"^\s*\d+\. ", "", lines[i]), topic_data_rel) + "</li>"); i += 1
            out.append("<ol>" + "".join(items) + "</ol>"); continue
        if ln.strip() == "":
            i += 1; continue
        out.append("<p>" + _inline(ln, topic_data_rel) + "</p>"); i += 1
    return "\n".join(out)

# ------------------------------------------------------------------ rendering
def chip(cls, text):
    return f'<span class="chip {cls}">{html.escape(str(text))}</span>'

def render_topic(group_slug, topic_slug):
    g = next((x for x in GROUPS if x["slug"] == group_slug), None)
    tmeta = next((t for t in g["topics"] if t["id"] == topic_slug), None) if g else None
    if not tmeta:
        return None
    data_rel = tmeta["dir"]
    topic = load(tmeta["topicFile"])
    mcqs = {}
    if tmeta.get("mcqFile"):
        for q in load(tmeta["mcqFile"]).get("blockMcqs", []):
            mcqs[q["id"]] = q

    from collections import Counter
    lc = Counter(b.get("level") for b in topic["blocks"])
    stats = "".join([
        f'<div class="stat"><b>{topic["blockCount"]}</b><span>blocks</span></div>',
        f'<div class="stat"><b>{len(mcqs)}</b><span>MCQs</span></div>',
        f'<div class="stat"><b>{topic.get("estReadMinutes","-")}</b><span>min read</span></div>',
        f'<div class="stat"><b>{lc.get("beginner",0)}/{lc.get("intermediate",0)}/{lc.get("advanced",0)}</b><span>beg/int/adv</span></div>',
    ])
    parts = [f'<header class="topic"><p class="kicker">{html.escape(g["name"])}</p>'
             f'<h1>{html.escape(topic["title"])}</h1>'
             f'<p class="summary">{html.escape(topic.get("summary",""))}</p>'
             f'<div class="stats">{stats}</div></header>']
    last = object()
    for b in topic["blocks"]:
        if b["sectionTitle"] != last:
            parts.append(f'<h2 class="eyebrow">{html.escape(str(b["sectionTitle"]))}</h2>')
            last = b["sectionTitle"]
        head = [chip(f'type type-{b["type"]}', b["type"])]
        if b.get("level"): head.append(chip(f'lvl-{b["level"]}', b["level"]))
        if b.get("subTitle"): head.append(f'<span class="sub">{html.escape(b["subTitle"])}</span>')
        quiz = ""
        for qid in b.get("mcqIds", []):
            q = mcqs.get(qid)
            if not q: continue
            opts = "".join(
                f'<li class="{"ok" if k==q["correctIndex"] else ""}"><span class="ok-k">{chr(65+k)}</span>{html.escape(o)}</li>'
                for k, o in enumerate(q["options"]))
            quiz += (f'<div class="quiz"><div class="qq">{html.escape(q["question"])}'
                     f'{chip("diff diff-"+q.get("difficulty","medium"), q.get("difficulty",""))}</div>'
                     f'<ul class="opts">{opts}</ul>'
                     f'<div class="expl"><span>Answer</span>{html.escape(q.get("explanation",""))}</div></div>')
        parts.append(f'<article class="card"><div class="chead">{"".join(head)}</div>'
                     f'<div class="body">{md_to_html(b["markdown"], data_rel)}</div>{quiz}</article>')
    return page("Learning", ("t", group_slug, topic_slug), "\n".join(parts))

def render_question(qid):
    q = CODING["byid"].get(qid)
    if not q: return None
    body = [f'<header class="topic"><p class="kicker">Coding · {html.escape(q.get("topic",""))}</p>'
            f'<h1>{html.escape(q["title"])}</h1><div class="chead">'
            f'{chip("diff diff-"+q.get("difficulty","medium"), q.get("difficulty",""))}'
            f'{chip("lvl-beginner", "★ most asked") if q.get("mostAsked") else ""}'
            f'{"".join(chip("type", c) for c in q.get("companies",[])[:4])}</div></header>']
    qpath = os.path.join(DATA, q["questionFile"])
    if os.path.exists(qpath):
        body.append(f'<article class="card"><div class="body">{md_to_html(open(qpath,encoding="utf-8").read())}</div></article>')
    for si, sol in enumerate(q.get("solutions", [])):
        head = (f'<div class="chead"><span class="sub" style="margin:0">{html.escape(sol.get("approach",""))}</span>'
                f'{chip("type", "time "+sol.get("time","?"))}{chip("type", "space "+sol.get("space","?"))}</div>')
        langs = sol.get("files", {})
        tabs = "".join(f'<button class="tab{" on" if li==0 else ""}" data-sol="{si}" data-lang="{L}">{L}</button>'
                       for li, L in enumerate(langs))
        panes = ""
        for li, (L, rel) in enumerate(langs.items()):
            p = os.path.join(DATA, rel)
            rendered = md_to_html(open(p, encoding="utf-8").read()) if os.path.exists(p) else "<p class=missing>missing</p>"
            panes += f'<div class="pane{" on" if li==0 else ""}" data-sol="{si}" data-lang="{L}">{rendered}</div>'
        body.append(f'<article class="card">{head}<div class="tabs">{tabs}</div>{panes}</article>')
    return page("Coding", ("q", qid), "\n".join(body))

# ------------------------------------------------------------------ shell / nav
def sidebar(active):
    kind = active[0] if active else ""
    out = ['<nav class="side"><input id="filter" placeholder="Filter…" autocomplete=off>']
    out.append('<div class="side-scroll">')
    out.append('<div class="sec-h">Learning content</div>')
    for g in GROUPS:
        out.append(f'<div class="grp" style="--gc:{g.get("color","#888")}">{html.escape(g["name"])}</div>')
        for t in g["topics"]:
            on = "on" if (kind == "t" and active[1] == g["slug"] and active[2] == t["id"]) else ""
            lvl = f'<i class="dot lvl-{t["level"]}"></i>' if t.get("level") else '<i class="dot"></i>'
            out.append(f'<a class="item {on}" href="/t/{g["slug"]}/{t["id"]}">{lvl}'
                       f'<span>{html.escape(t["title"])}</span><em>{t.get("blockCount","")}</em></a>')
    if CODING["questions"]:
        out.append('<div class="sec-h">Coding practice</div>')
        by_topic = {}
        for q in CODING["questions"]:
            by_topic.setdefault(q.get("topic", "misc"), []).append(q)
        for tp in sorted(by_topic):
            out.append(f'<div class="grp" style="--gc:#6C7A89">{html.escape(tp)}</div>')
            for q in by_topic[tp]:
                on = "on" if (kind == "q" and active[1] == q["id"]) else ""
                out.append(f'<a class="item {on}" href="/q/{q["id"]}"><i class="dot diff-{q.get("difficulty","")}"></i>'
                           f'<span>{html.escape(q["title"])}</span><em>{q.get("difficulty","")[:1].upper()}</em></a>')
    out.append("</div></nav>")
    return "".join(out)

def page(section, active, body):
    return (PAGE_TMPL
            .replace("%%TITLE%%", html.escape(section + " · CrackLoop preview"))
            .replace("%%SIDEBAR%%", sidebar(active))
            .replace("%%BODY%%", body))

def render_home():
    nt = sum(len(g["topics"]) for g in GROUPS)
    cards = "".join(
        f'<a class="home-card" href="/t/{g["slug"]}/{g["topics"][0]["id"]}" style="--gc:{g.get("color","#888")}">'
        f'<b>{html.escape(g["name"])}</b><span>{len(g["topics"])} topics</span></a>'
        for g in GROUPS if g["topics"])
    body = (f'<header class="topic"><p class="kicker">CrackLoop · local preview</p>'
            f'<h1>Content preview</h1>'
            f'<p class="summary">{IDX.get("topicCount", nt)} topics · {IDX.get("blockCount","?")} blocks · '
            f'{IDX.get("mcqCount","?")} MCQs · {len(CODING["questions"])} coding questions. '
            f'Pick a topic on the left, or a group below.</p></header>'
            f'<div class="home-grid">{cards}</div>')
    return page("Home", ("home",), body)

PAGE_TMPL = """<!doctype html><html lang=en><head><meta charset=utf-8>
<meta name=viewport content="width=device-width,initial-scale=1">
<title>%%TITLE%%</title>
<script>(function(){var t=localStorage.getItem('cl-theme');if(t)document.documentElement.setAttribute('data-theme',t);})();</script>
<style>__CSS__</style></head><body>
<div class="topbar"><a class="brand" href="/">CrackLoop <span>preview</span></a>
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
var f=document.getElementById('filter');
if(f)f.addEventListener('input',function(){
  var q=this.value.toLowerCase();
  document.querySelectorAll('.side .item').forEach(function(a){
    var hit=a.textContent.toLowerCase().indexOf(q)>=0; a.style.display=hit?'':'none';
  });
  document.querySelectorAll('.side .grp').forEach(function(g){
    var n=g.nextElementSibling, any=false;
    while(n&&n.classList.contains('item')){ if(n.style.display!=='none')any=true; n=n.nextElementSibling; }
    g.style.display=any?'':'none';
  });
});
document.querySelectorAll('.tab').forEach(function(b){
  b.addEventListener('click',function(){
    var s=b.dataset.sol,l=b.dataset.lang;
    document.querySelectorAll('.tab[data-sol="'+s+'"]').forEach(x=>x.classList.toggle('on',x===b));
    document.querySelectorAll('.pane[data-sol="'+s+'"]').forEach(p=>p.classList.toggle('on',p.dataset.lang===l));
  });
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
.grp{font-size:12.5px;font-weight:700;color:var(--ink);padding:10px 8px 4px;border-left:3px solid var(--gc,transparent);margin-top:4px}
.item{display:flex;align-items:center;gap:8px;text-decoration:none;color:var(--muted);font-size:13.5px;padding:6px 8px;border-radius:8px}
.item:hover{background:var(--ground);color:var(--ink)}
.item.on{background:var(--soft);color:var(--accent);font-weight:600}
.item span{flex:1;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.item em{font-style:normal;font-size:11px;color:var(--faint)}
.dot{width:7px;height:7px;border-radius:50%;background:var(--border2);flex:none}
.dot.lvl-beginner,.dot.diff-easy{background:var(--good)}
.dot.lvl-intermediate,.dot.diff-medium{background:var(--warn)}
.dot.lvl-advanced,.dot.diff-hard{background:var(--crit)}
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
.lvl-beginner{background:var(--good-bg);color:var(--good)}
.lvl-intermediate{background:var(--warn-bg);color:var(--warn)}
.lvl-advanced{background:var(--crit-bg);color:var(--crit)}
.diff-easy{background:var(--good-bg);color:var(--good)}
.diff-medium{background:var(--warn-bg);color:var(--warn)}
.diff-hard{background:var(--crit-bg);color:var(--crit)}
.sub{margin-left:auto;font-family:var(--fu);font-weight:600;font-size:14px;color:var(--ink);text-transform:none;letter-spacing:0}
.body>*:first-child{margin-top:0}.body>*:last-child{margin-bottom:0}
.body p{margin:0 0 14px}.body ul,.body ol{margin:0 0 14px;padding-left:22px}.body li{margin:5px 0}
.md-h{font-family:var(--fu);margin:18px 0 8px;line-height:1.25}
code{font-family:var(--fm);font-size:.85em;background:var(--code);padding:2px 6px;border-radius:5px}
pre{background:var(--pre-bg);color:var(--pre-ink);padding:16px 18px;border-radius:12px;overflow-x:auto;margin:0 0 14px;line-height:1.5}
pre code{background:none;padding:0;color:inherit;font-size:13px}
.twrap{overflow-x:auto;margin:0 0 14px}
table{border-collapse:collapse;width:100%;font-family:var(--fu);font-size:14px}
th,td{border:1px solid var(--border);padding:8px 12px;text-align:left;vertical-align:top}
th{background:var(--soft)}
blockquote{border-left:3px solid var(--accent);margin:0 0 14px;padding:4px 16px;color:var(--muted);background:var(--ground);border-radius:0 8px 8px 0}
.plate{margin:4px 0 14px;background:var(--plate);border:1px solid var(--border);border-radius:12px;padding:16px}
.plate img{max-width:100%;height:auto;display:block;margin:0 auto}
.plate figcaption{font-family:var(--fu);font-size:12px;color:#5A6B6A;text-align:center;margin-top:10px}
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
.tabs{display:flex;gap:6px;margin:0 0 12px;flex-wrap:wrap}
.tab{font-family:var(--fm);font-size:12px;cursor:pointer;background:var(--ground);color:var(--muted);border:1px solid var(--border2);border-radius:7px;padding:4px 10px}
.tab.on{background:var(--accent);color:#fff;border-color:var(--accent)}
.pane{display:none}.pane.on{display:block}
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
            if path.startswith("/data/"):
                return self._serve_static(path[len("/data/"):])
            parts = [p for p in path.strip("/").split("/") if p]
            if parts[0] == "t" and len(parts) == 3:
                html_out = render_topic(parts[1], parts[2])
                return self._send(html_out) if html_out else self._send(self._404(path), code=404)
            if parts[0] == "q" and len(parts) == 2:
                html_out = render_question(parts[1])
                return self._send(html_out) if html_out else self._send(self._404(path), code=404)
            return self._send(self._404(path), code=404)
        except Exception as e:  # a bad file shouldn't kill the server
            return self._send(f"<pre>error rendering {html.escape(path)}:\n{html.escape(repr(e))}</pre>", code=500)

    do_HEAD = do_GET

    def _serve_static(self, rel):
        safe = os.path.normpath(os.path.join(DATA, rel))
        if not safe.startswith(DATA) or not os.path.isfile(safe):
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
    host = f"http://localhost:{port}"
    print(f"CrackLoop preview → {host}")
    print(f"  {sum(len(g['topics']) for g in GROUPS)} topics · {len(CODING['questions'])} coding questions")
    print("  Ctrl-C to stop")
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        print("\nstopped")

if __name__ == "__main__":
    main()
