"""src/ 의 본문 조각을 읽어 배포용 HTML을 만든다.

- 원고는 src/ 아래 HTML 조각(본문만)을 고친다. 루트의 index.html, chapters/, appendix/ 는 빌드 결과물이므로 직접 고치지 않는다.
- 목차와 페이지 정보는 src/site.json 에 있다.
- 빌드는 다른 쪽의 "표 3-1", "그림 8-1" 참조에만 링크를 건다. 같은 쪽 참조는 글자만 둔다. 없는 번호를 가리키면 멈춘다.
실행: python3 tools/build.py
"""
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
BOOK = "하네스 엔지니어링(가제)"
SUB = "집필 준비 중"

site = json.loads((SRC / "site.json").read_text(encoding="utf-8"))
NAV = site["nav"]
META = site["pages"]
ORDER = [pid for _, ids in NAV for pid in ids]
BODY = {pid: (SRC / META[pid]["path"]).read_text(encoding="utf-8") for pid in ORDER}


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
    foot = f"{BOOK}: {SUB}."
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
    body = link_refs(pid, unique_markers(BODY[pid]))
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
