"""그림, 표 번호 검사. 문제가 없으면 아무것도 출력하지 않고 종료 코드 0을 돌려준다.

검사 항목
1. 페이지 안에서 그림, 표 번호가 각각 1부터 빠짐없이 순서대로 매겨졌는지
2. 장 번호-순번 형식(예: 표 3-1)이 여러 페이지에서 중복되지 않는지
3. 본문이 가리키는 번호가 실제로 있는지
4. 다른 쪽 번호 참조에는 링크가 걸려 있고, 같은 쪽 번호 참조에는 링크가 없는지
6. 파일과 번호 접두가 맞는지(chapters/chNN.html은 NN, 부록 prompts=부1, terms=부2, references=부3)
5. 번호 뒤 조사가 마지막 숫자의 받침과 맞는지(0, 1, 3, 6, 7, 8 뒤에는 은, 이, 을, 과, 나머지 숫자 뒤에는 는, 가, 를, 와)

표지(index.html)는 번호와 캡션을 두지 않으므로 검사하지 않는다.
"""
import glob
import re
import sys

files = sorted(glob.glob("chapters/*.html")) + sorted(glob.glob("appendix/*.html"))
CAP = re.compile(r"<figcaption><b>((그림|표) (?:([0-9A-Z]+|부[0-9]+)-)?([0-9]+))\.")
REF = re.compile(r"(?:그림|표) (?:[0-9A-Z]+|부[0-9]+)-[0-9]+")
errors = []
owner = {}

for f in files:
    html = open(f, encoding="utf-8").read()
    seq = {}
    for full, kind, prefix, n in CAP.findall(html):
        seq.setdefault((kind, prefix), []).append(int(n))
        if prefix:
            if full in owner:
                errors.append(f"중복 번호: {full} ({owner[full]}, {f})")
            owner[full] = f
    for (kind, prefix), nums in seq.items():
        if nums != list(range(1, len(nums) + 1)):
            errors.append(f"순서, 누락 이상: {f} {kind} {prefix or ''} {nums}")

for f in files:
    html = open(f, encoding="utf-8").read()
    body = re.sub(r"<(figcaption|pre|svg)[^>]*>.*?</\1>", "", html, flags=re.S)
    linked = set(re.findall(r"<a [^>]*>((?:그림|표) (?:[0-9A-Z]+|부[0-9]+)-[0-9]+)</a>", body))
    plain = re.sub(r"<a [^>]*>.*?</a>", "", body, flags=re.S)
    plain = re.sub(r"<[^>]+>", " ", plain)
    for r in sorted(set(REF.findall(re.sub(r"<[^>]+>", " ", body)))):
        if r not in owner:
            errors.append(f"없는 번호 참조: {f} {r}")
    for r in sorted(set(REF.findall(plain))):
        if owner.get(r) != f:  # 다른 쪽 참조는 링크가 있어야 함
            errors.append(f"링크 없는 번호 참조: {f} {r}")
    for r in sorted(linked):
        if owner.get(r) == f:  # 같은 쪽 참조는 링크를 걸지 않음
            errors.append(f"같은 쪽 번호 링크: {f} {r}")

# 5. 번호 뒤 조사: 마지막 숫자를 읽었을 때 받침이 있으면 은/이/을/과, 없으면 는/가/를/와
BATCHIM = set("013678")
PAIR = {"은": "는", "는": "은", "이": "가", "가": "이", "을": "를", "를": "을", "과": "와", "와": "과"}
WITH = set("은이을과")
ROEURO = re.compile(r"((?:표|그림) (?:(?:[0-9A-Z]+|부[0-9]+)-)?(\d+)|Chapter (\d+))(?:</a>)?(으로|로)(?![가-힣])")
JOSA = re.compile(r"((?:표|그림) (?:(?:[0-9A-Z]+|부[0-9]+)-)?(\d+))(?:</a>)?([은는이가을를과와])(?![가-힣])")
for f in files + ["index.html"]:
    body = open(f, encoding="utf-8").read()
    for m in JOSA.finditer(body):
        need_with = m.group(2)[-1] in BATCHIM
        if (m.group(3) in WITH) != need_with:
            errors.append(f"조사 오류: {f} {m.group(1)}{m.group(3)} → {m.group(1)}{PAIR[m.group(3)]}")
    for m in re.finditer(r"(Chapter (\d+))(?:</a>)?([은는이가을를과와])(?![가-힣])", body):
        if (m.group(3) in WITH) != (m.group(2)[-1] in BATCHIM):
            errors.append(f"조사 오류: {f} {m.group(1)}{m.group(3)} → {m.group(1)}{PAIR[m.group(3)]}")
    # 로/으로: 마지막 숫자가 0, 3, 6(영, 삼, 육)이면 "으로", 1, 7, 8(ㄹ 받침)과 받침 없는 2, 4, 5, 9는 "로"
    for m in ROEURO.finditer(body):
        d = (m.group(2) or m.group(3))[-1]
        need = "으로" if d in "036" else "로"
        if m.group(4) != need:
            errors.append(f"조사 오류: {f} {m.group(1)}{m.group(4)} → {m.group(1)}{need}")

# 6. 파일과 번호 접두, figure id 일치
APPX = {"appendix/prompts.html": "부1", "appendix/terms.html": "부2", "appendix/references.html": "부3"}
FIG = re.compile(r'<figure[^>]*\bid="([^"]*)"[^>]*>.*?<figcaption><b>(그림|표) ([0-9A-Z]+|부[0-9]+)-([0-9]+)\.', re.S)
for f in files:
    m = re.match(r"chapters/ch0*([0-9]+)\.html$", f)
    want = m.group(1) if m else APPX.get(f)
    if want is None:
        continue
    body = open(f, encoding="utf-8").read()
    for g in FIG.finditer(body):
        fid, kind, pre, num = g.groups()
        if pre != want:
            errors.append(f"파일과 번호 접두 불일치: {f} {kind} {pre}-{num} (기대 {want}-)")
        exp = ("tbl" if kind == "표" else "fig") + f"-{pre}-{num}"
        if fid != exp:
            errors.append(f"id와 캡션 번호 불일치: {f} id={fid} 캡션={kind} {pre}-{num} (기대 id={exp})")

idx = open("index.html", encoding="utf-8").read()
if "<figcaption" in idx:
    errors.append("표지에 캡션이 있음: index.html")

for e in errors:
    print(e)
sys.exit(1 if errors else 0)

