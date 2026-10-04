"""배포된 사이트를 실제로 받아 확인한다(GitHub Actions에서 실행).
확인: 모든 쪽 HTTP 200, 쪽 제목(title), 책 제목, 바닥글 날짜 없음, 사이트 안 링크 대상 존재,
      파비콘, 스타일시트, 스타일시트 안 글꼴 파일 응답 200.
실행: python tools/verify_site.py https://seoulkorea-dev.github.io/harness-book/
"""
import html, json, re, sys, urllib.error, urllib.request
from pathlib import Path
from urllib.parse import urljoin

BASE = sys.argv[1].rstrip("/") + "/"
ROOT = Path(__file__).resolve().parent.parent
site = json.loads((ROOT / "src" / "site.json").read_text(encoding="utf-8"))
BOOK = re.search(r'BOOK = "([^"]+)"', (ROOT / "tools" / "build.py").read_text(encoding="utf-8")).group(1)

def get(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers={"Cache-Control": "no-cache"}), timeout=30) as r:
        return r.status, r.read().decode("utf-8", "replace")

errors, pages = [], {}
for pid, meta in site["pages"].items():
    url = urljoin(BASE, meta["path"])
    try:
        status, body = get(url)
    except Exception as e:
        errors.append(f"열기 실패 {url}: {e}"); continue
    pages[meta["path"]] = body
    if status != 200: errors.append(f"HTTP {status} {url}")
    if BOOK not in body: errors.append(f"책 제목 없음 {url}")
    if "최종 업데이트" in body: errors.append(f"바닥글 날짜 남음 {url}")
    want = BOOK if pid == "index" else f"{meta['title']} | {BOOK}"
    got = re.search(r"<title>([^<]*)</title>", body)
    got = html.unescape(got.group(1)) if got else ""
    if got != want: errors.append(f"쪽 제목 불일치 {url}: {got!r}")
    print(f"title {meta['path']}: {got}")
for path, body in pages.items():
    for href in re.findall(r'href="([^"#:]+\.html)', body):
        target = urljoin(urljoin(BASE, path), href)[len(BASE):]
        if target not in pages and not any(target == r for r in site.get("redirects", {})):
            errors.append(f"사이트에 없는 쪽 링크 {path} -> {href}")
# 정적 자원(1차 검수 26번): 파비콘, 스타일시트, 스타일시트 안 url(...)
assets = set()
for path, body in pages.items():
    for m in re.finditer(r'<link rel="(?:icon|apple-touch-icon|stylesheet)" href="([^"]+)"', body):
        assets.add(urljoin(urljoin(BASE, path), m.group(1)))
for css in [a for a in sorted(assets) if a.endswith(".css")]:
    try:
        _, text = get(css)
        for u in re.findall(r'url\(["\']?([^"\')]+)["\']?\)', text):
            if not u.startswith("data:"): assets.add(urljoin(css, u))
    except Exception as e:
        errors.append(f"열기 실패 {css}: {e}")
for a in sorted(assets):
    try:
        with urllib.request.urlopen(urllib.request.Request(a, headers={"Cache-Control": "no-cache"}), timeout=30) as r:
            code = r.status
    except urllib.error.HTTPError as e:
        code = e.code
    except Exception as e:
        errors.append(f"열기 실패 {a}: {e}"); continue
    print(f"{code} {a[len(BASE):]}")
    if code != 200: errors.append(f"HTTP {code} {a}")
print(f"확인한 쪽 {len(pages)}, 자원 {len(assets)}, 오류 {len(errors)}")
for e in sorted(set(errors)): print(" -", e)
sys.exit(1 if errors else 0)
