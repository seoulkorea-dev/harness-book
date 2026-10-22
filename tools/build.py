"""src/ 의 본문 조각을 읽어 배포용 HTML을 만든다.

- 원고는 src/ 아래 HTML 조각(본문만)을 고친다. 루트의 index.html, chapters/, appendix/ 는 빌드 결과물이므로 직접 고치지 않는다.
- 목차와 페이지 정보는 src/site.json 에 있다.
- 빌드는 다른 쪽의 "표 3-1", "그림 8-1" 참조에만 링크를 건다. 같은 쪽 참조는 글자만 둔다. 없는 번호를 가리키면 멈춘다.
- 인용(BOOK_STANDARD.md 8절, D-131, 이슈 #66 08:28): 원고의 <a class="cite" data-ref="키">자료를 가리키는 낱말</a>을 부록 끝 "참고 문헌"
  쪽(site.json에서 generated)의 해당 항목 링크로 바꾼다. 본문에 번호를 표시하지 않는다. 참고 문헌 번호는 목차 순서로 처음 인용된 순서이고,
  항목마다 그 자료가 쓰인 곳(장 단위, 목차 순서)을 글자로 붙인다. 없는 키를 가리키면 멈춘다.
실행: python3 tools/build.py
"""
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
BOOK = "하네스 엔지니어링: 모델을 에이전트로 만드는 설계"
SUB = "프롬프트, 컨텍스트, 하네스로 에이전트 설계하기"

site = json.loads((SRC / "site.json").read_text(encoding="utf-8"))
NAV = site["nav"]
META = site["pages"]
ORDER = ["index"] + [pid for _, ids in NAV for pid in ids if pid != "index"]
BODY = {pid: (SRC / META[pid]["path"]).read_text(encoding="utf-8") for pid in ORDER if not META[pid].get("generated")}

# 인용: 본문 낱말 링크, 부록 끝 참고 문헌(번호는 처음 인용된 순서, 항목마다 쓰인 곳)
BIB = {k: v for k, v in json.loads((ROOT / "research" / "bibliography.json").read_text(encoding="utf-8")).items() if not k.startswith("_")}
CITE = re.compile(r'<a class="cite" data-ref="([^"]+)">(.*?)</a>', re.S)
CITE_NO, USED_IN = {}, {}
for _pid in ORDER:
    for _k, _ in CITE.findall(BODY.get(_pid, "")):
        if _k not in BIB:
            raise SystemExit(f"bibliography.json에 없는 자료 키: {META[_pid]['path']} {_k}")
        CITE_NO.setdefault(_k, len(CITE_NO) + 1)
        USED_IN.setdefault(_k, [])
        if _pid not in USED_IN[_k]:
            USED_IN[_k].append(_pid)
REF_PAGE = next((pid for pid in ORDER if META[pid].get("generated") == "references"), None)


def place(pid):
    m = re.match(r"Chapter (\d+)", META[pid]["nav"])
    return f"{m.group(1)}장" if m else META[pid]["nav"]


def bib_entry(e):
    if e["type"] == "web":
        text = f'{e["author"]}, “{e["title"]}”, 《{e["venue"]}》, ({e["accessed"]} 열람).'
    else:
        text = f'{e["author"]}, “{e["title"]}”, {e["venue"]}, {e["date"]}.'
    return html.escape(text, quote=False) + f' <a href="{html.escape(e["url"])}">{html.escape(e["url"])}</a>'


def cites(pid, body):
    if not REF_PAGE:
        return CITE.sub(lambda m: m.group(2), body)
    href = rel(META[pid]["path"], META[REF_PAGE]["path"])
    return CITE.sub(lambda m: f'<a class="cite" href="{href}#bib-{CITE_NO[m.group(1)]}">{m.group(2)}</a>', body)


if REF_PAGE:
    items = "".join(f'<li id="bib-{n}">{bib_entry(BIB[k])} <span class="bib-used">쓰인 곳: {", ".join(place(p) for p in USED_IN[k])}</span></li>'
                    for k, n in sorted(CITE_NO.items(), key=lambda x: x[1]))
    BODY[REF_PAGE] = (f'<h1>{META[REF_PAGE]["title"]}</h1>\n'
                      '<p class="lead">본문에서 점선 밑줄로 표시한 자료 이름이 가리키는 자료입니다. 번호는 시작하며부터 목차 순서로 처음 인용된 순서이고, 항목 끝의 쓰인 곳은 그 자료를 근거로 인용한 장입니다.</p>\n'
                      f'<ol class="bib">{items}</ol>\n')


def rel(frm, to):
    return "../" * frm.count("/") + to


def build_nav(cur):
    cp = META[cur]["path"]
    out = ['<nav class="sidenav" id="sidenav" aria-label="전체 목차">', "<h2>전체 목차</h2>", "<ul>"]
    for group, ids in NAV:
        out.append(f'<li class="group">{group}</li>')
        for pid in ids:
            cur_attr = ' aria-current="page"' if pid == cur else ""
            label = META[pid]["nav"]
            m = re.match(r"(Chapter \d+) (.+)$", label)
            if m:  # 장 번호와 제목을 두 줄로
                label = f'<span class="nav-num">{m.group(1)}</span><span class="nav-title">{m.group(2)}</span>'
            out.append(f'<li><a href="{rel(cp, META[pid]["path"])}"{cur_attr}>{label}</a></li>')
    out.append("</ul></nav>")
    return "\n".join(out)


def build_toc(body):
    items = re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', body, re.S)
    if not items:
        return ""
    lis = "\n".join(f'<li><a href="#{i}">{re.sub("<[^>]+>", "", t)}</a></li>' for i, t in items)
    return f'<aside class="pagetoc" aria-label="이 페이지"><h2>이 페이지</h2><ol>\n{lis}\n</ol></aside>'


def unique_markers(body):
    n = [0]

    def one(m):
        n[0] += 1
        svg = m.group(0)
        ids = set(re.findall(r'<marker id="([^"]+)"', svg))
        for old in ids:
            new = f"m{n[0]}-{old}"
            svg = svg.replace(f'id="{old}"', f'id="{new}"').replace(f"url(#{old})", f"url(#{new})")
        return svg
    return re.sub(r"<svg.*?</svg>", one, body, flags=re.S)


# 그림, 표 번호 참조 자동 연결 (장 번호-순번 형식만)
FIGMAP = {}
for pid in ORDER:
    for fid, num in re.findall(r'<figure class="fig[^"]*" id="([^"]+)">.*?<figcaption><b>((?:표|그림) [0-9A-Z]+-[0-9]+)\.', BODY[pid], re.S):
        if num in FIGMAP:
            raise SystemExit(f"중복 번호: {num}")
        FIGMAP[num] = (META[pid]["path"], fid)
REF = re.compile(r"(그림|표) ([0-9A-Z]+-[0-9]+)")


def link_refs(pid, body):
    cp = META[pid]["path"]
    out, depth_a, skip = [], 0, 0
    for tok in re.split(r"(<[^>]+>)", body):
        if tok.startswith("<"):
            t = tok.lower()
            if t.startswith("<a "):
                depth_a += 1
            elif t == "</a>":
                depth_a -= 1
            elif re.match(r"<(figcaption|pre|svg)[\s>]", t):
                skip += 1
            elif t in ("</figcaption>", "</pre>", "</svg>"):
                skip -= 1
            out.append(tok)
            continue
        if depth_a or skip:
            out.append(tok)
            continue

        def rep(m):
            key = m.group(0)
            if key not in FIGMAP:
                raise SystemExit(f"없는 번호 참조: {cp} {key}")
            path, fid = FIGMAP[key]
            if path == cp:  # 같은 쪽 참조는 바로 아래에 표, 그림이 있으므로 링크 없이 글자만
                return key
            return f'<a href="{rel(cp, path)}#{fid}">{key}</a>'
        out.append(REF.sub(rep, tok))
    return "".join(out)


def page(pid, body):
    m = META[pid]
    cp = m["path"]
    full_title = BOOK if pid == "index" else f"{m['title']} | {BOOK}"
    foot = f"{BOOK} — {SUB}"
    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light">
<title>{html.escape(full_title)}</title>
<meta name="description" content="{html.escape(m['desc'])}">
<link rel="stylesheet" href="{rel(cp, 'assets/style.css')}">
<link rel="icon" href="{rel(cp, 'assets/favicon.svg')}" type="image/svg+xml">
<link rel="icon" href="{rel(cp, 'assets/favicon-32.png')}" type="image/png" sizes="32x32">
<link rel="apple-touch-icon" href="{rel(cp, 'assets/apple-touch-icon.png')}">
</head>
<body>
<a class="skip" href="#main">본문으로 이동</a>
<header class="topbar">
<a class="brand" href="{rel(cp, 'index.html')}">{BOOK}</a>
<span class="spacer"></span>
<a class="navlink" href="#sidenav">전체 목차</a>
<a href="https://github.com/seoulkorea-dev/harness-book">저장소</a>
</header>
<div class="layout">
{build_nav(pid)}
<main id="main">
<article>
{body}
</article>
<footer class="site-foot">{foot}</footer>
</main>
{build_toc(body)}
</div>
</body>
</html>
"""


for pid in ORDER:
    body = link_refs(pid, unique_markers(cites(pid, BODY[pid])))
    out = ROOT / META[pid]["path"]
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page(pid, body), encoding="utf-8")
print("pages:", len(ORDER))

# 없어진 쪽의 이동 쪽: 안내 문장 1개, 새 위치 링크, meta refresh
for old, (new, label) in site.get("redirects", {}).items():
    href = rel(old, new)
    (ROOT / old).parent.mkdir(parents=True, exist_ok=True)
    (ROOT / old).write_text(f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta http-equiv="refresh" content="0; url={href}">
<title>이동한 쪽 | {BOOK}</title>
<link rel="canonical" href="{href}">
<link rel="icon" href="{rel(old, 'assets/favicon.svg')}" type="image/svg+xml">
</head>
<body>
<p>이 쪽의 내용을 옮겼습니다. 새 위치: <a href="{href}">{html.escape(label)}</a></p>
</body>
</html>
""", encoding="utf-8")
