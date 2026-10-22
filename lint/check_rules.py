"""REVIEW_RULES.md의 자동 검사(이슈 #66, D-127).

사용: python lint/check_rules.py
src/chapters/*.html, src/appendix/*.html을 검사한다. 장별 정비를 마친 장(lint/rules_applied.txt에 이름이 있음)은
"실패" 규칙을 어기면 실패, 아직 정비하지 않은 장은 경고만 낸다. "경고" 규칙은 모든 장에서 경고만 낸다.
  실패 규칙: R2 출처 없는 반론, R9 표 열 설계(실패 표와 확인 표의 열 이름, 열 수 4개 이하, 모호하거나 동사형이거나
             지시 표현이 든 열 이름, 열 이름 나열 설명 줄, 설명 줄의 "이 책"), R10 같은 장 링크와 괄호 절 참조,
             R11 인용(낱말 링크 a.cite의 자료 키, 같은 장 같은 자료는 한 번, 위첨자 번호 없음, 옛 표기 없음), R12 약어 CR과 (Change Request)
  경고 규칙: R1 단정 표현, R3 제품이 실험한 것처럼 읽히는 주어, R4 각주 없는 버전 번호
각주 형식(D-123): 본문 <sup class="fnref">n</sup>, 그 문단 바로 아래 <ol class="fn" start="n"><li>…</li></ol>
종료 코드: 실패가 하나라도 있으면 1.
"""
import glob, html, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APPLIED = os.path.join(ROOT, "lint", "rules_applied.txt")
BIB = {k for k in json.load(open(os.path.join(ROOT, "research", "bibliography.json"), encoding="utf-8")) if not k.startswith("_")}
FAIL_HEAD = ["실패 유형", "원인", "방지 장치"]  # BOOK_STANDARD 10절, D-124 갱신(이슈 #66 08:28)
CHECK_HEAD = ["확인 항목", "확인 방법", "확인 기준"]
# 표 열 설계 원칙(BOOK_STANDARD 10절): 모호한 열 이름, 동사형과 질문형, 지시 표현
VAGUE_HEAD = {"설명", "내용", "무엇인가", "예", "방법", "기준", "이유"}
VERB_HEAD = re.compile(r"(?:할|일할|하는|된) (?:때|것|쪽)$|할 것$|는가$|^적합한 ")
DEIXIS = re.compile(r"이 책|^(?:이|그) ")
R1_WORDS = re.compile(r"반드시|항상|결국|(?:이|가) 아니라")

def applied():
    if not os.path.exists(APPLIED):
        return set()
    return {l.strip() for l in open(APPLIED, encoding="utf-8") if l.strip() and not l.startswith("#")}

def text_of(s):
    return html.unescape(re.sub(r"<[^>]+>", " ", s))

def strip_code(s):
    return re.sub(r"<(pre|code)\b.*?</\1>", " ", s, flags=re.S)

def check_file(path):
    name = os.path.splitext(os.path.basename(path))[0]
    s = open(path, encoding="utf-8").read()
    fails, warns = [], []
    # R10 같은 장 링크(참고 자료 #ref-와 각주는 예외), 괄호 절 참조
    for m in re.finditer(r'href="([^"]*)"', s):
        h = m.group(1)
        if h.startswith("#") and not h.startswith("#ref-"):
            fails.append(f"R10 같은 장 링크 {h}")
        elif "#" in h and os.path.splitext(os.path.basename(h.split("#")[0]))[0] == name:
            fails.append(f"R10 같은 장 링크 {h}")
    for m in re.finditer(r"\([^()<>]{0,80}에서 다룸\)", text_of(s)):
        fails.append(f"R10 괄호 절 참조 {m.group(0)[:40]}")
    # R2 출처 없는 반론
    for m in re.finditer(r"[^.]{0,30}(?:라는|다는|는) 의견(?:이|도) 있습니다", text_of(s)):
        fails.append(f"R2 출처 없는 반론: {m.group(0).strip()[:50]}")
    # R12 약어 CR(코드와 파일 경로 예외), 영어 병기
    body = text_of(strip_code(s))
    for m in re.finditer(r"(?<![A-Za-z0-9_./-])CR(?![A-Za-z0-9_])(?!\.md)", body):
        fails.append(f"R12 약어 CR: {body[max(0, m.start() - 15):m.end() + 10].strip()}")
    if "(Change Request)" in body:
        fails.append("R12 영어 병기 (Change Request)")
    # R9 실패 표, 확인 표의 열 이름과 열 이름 나열 설명 줄
    for m in re.finditer(r'<figure class="fig" id="(tbl-[\d-]+)">(.*?)</figure>', s, re.S):
        tid, t = m.group(1), m.group(2)
        heads = [text_of(h).strip() for h in re.findall(r"<th[^>]*>(.*?)</th>", t, re.S)]
        cap = text_of((re.search(r"<b>(.*?)</b>", t, re.S) or [None, ""])[1]) if re.search(r"<b>(.*?)</b>", t, re.S) else ""
        if "실패와 막는 장치" in cap or "실패와 방지 장치" in cap or (heads and heads[0] in ("실패", "실패 유형")):
            if heads[:3] != FAIL_HEAD:
                fails.append(f"R9 {tid} 실패 표 열 이름 {heads[:3]}")
        if "확인 방법" in cap or (heads and heads[0] in ("확인할 것", "확인 항목")):
            if heads[:3] != CHECK_HEAD:
                fails.append(f"R9 {tid} 확인 표 열 이름 {heads[:3]}")
        if len(heads) > 4:
            fails.append(f"R9 {tid} 열 {len(heads)}개(최대 4개)")
        for h in heads:
            if h in VAGUE_HEAD:
                fails.append(f"R9 {tid} 모호한 열 이름 '{h}'")
            elif VERB_HEAD.search(h):
                fails.append(f"R9 {tid} 동사형이나 질문형 열 이름 '{h}'")
            elif DEIXIS.search(h):
                fails.append(f"R9 {tid} 지시 표현이 든 열 이름 '{h}'")
        for li in re.findall(r'<ul class="capnote">\s*<li>(.*?)</li>', t, re.S):
            parts = [p.strip() for p in re.split(r",\s*", text_of(li))]
            if len(parts) >= 2 and sum(1 for p in parts if p in heads) >= 2:
                fails.append(f"R9 {tid} 설명 줄이 열 이름을 나열: {text_of(li).strip()[:40]}")
            if DEIXIS.search(text_of(li).strip()):
                fails.append(f"R9 {tid} 설명 줄의 지시 표현: {text_of(li).strip()[:40]}")
    # R11 인용(D-131, 이슈 #66 08:28): 근거를 말하는 낱말을 <a class="cite" data-ref="키">로 링크, 같은 장에서 같은 자료는 처음 한 번만,
    # 위첨자 번호 없음, 옛 표기(문단 아래 각주, 장 끝 참고 자료, #ref- 링크) 없음
    if 'class="cite"' in s:
        cites = re.findall(r'<a class="cite" data-ref="([^"]+)">(.*?)</a>', s, re.S)
        for k, _ in cites:
            if k not in BIB:
                fails.append(f"R11 bibliography.json에 없는 자료 키 {k}")
        for k in sorted({k for k, _ in cites if [c for c, _ in cites].count(k) > 1}):
            fails.append(f"R11 같은 장에서 같은 자료를 두 번 이상 링크 {k}")
        for k, t in cites:
            if len(text_of(t).strip()) > 25:
                fails.append(f"R11 링크 낱말이 김(자료를 가리키는 말만): {text_of(t).strip()[:30]}")
        if '<sup class="cite"' in s:
            fails.append("R11 위첨자 인용 번호 남음(본문 낱말 링크로)")
        if re.search(r'<a class="cite"(?! data-ref=)', s):
            fails.append("R11 자료 키 없는 인용 링크(a.cite에는 data-ref만 씀, 주소는 빌드가 채움)")
        for pat, label in [('class="fnref"', "문단 아래 각주 번호"), ('<ol class="fn"', "문단 아래 각주"), ('<h2 id="refs">', "장 끝 참고 자료 절"), ('href="#ref-', "#ref- 링크")]:
            if pat in s:
                fails.append(f"R11 옛 인용 표기 남음: {label}")
        return name, fails, warns + r1_r4(s)
    if name in applied():
        fails.append("R11 규칙 적용 장은 새 인용 방식(a.cite 자료 키 낱말 링크)을 써야 함(D-131)")
    if 'href="#ref-' in s:
        fails.append(f"R11 본문의 참고 자료 링크 {s.count('href=\"#ref-')}곳")
    sups = [int(n) for n in re.findall(r'<sup class="fnref">(\d+)</sup>', s)]
    notes = []
    for m in re.finditer(r'<ol class="fn" start="(\d+)">(.*?)</ol>', s, re.S):
        notes += [int(m.group(1)) + i for i in range(len(re.findall(r"<li>", m.group(2))))]
    if sups and sups != list(range(1, len(sups) + 1)):
        fails.append(f"R11 위첨자 번호가 1부터 차례대로가 아님 {sups[:10]}")
    if sorted(sups) != sorted(notes):
        fails.append(f"R11 위첨자 {len(sups)}개와 각주 {len(notes)}개가 1:1이 아님")
    return name, fails, warns + r1_r4(s)

def r1_r4(s):
    warns = []
    # 경고: R1, R3, R4
    plain = text_of(strip_code(s))  # 주장 줄도 포함(D-126)
    n1 = len(R1_WORDS.findall(plain))
    if n1:
        warns.append(f"R1 단정 표현 후보 {n1}곳(반드시, 항상, 결국, 이 아니라)")
    for m in re.finditer(r"Claude Code는[^.]{0,60}(?:실험|보고했|밝혔)", plain):
        warns.append(f"R3 주어: {m.group(0)[:50]}")
    for p in re.findall(r"<p\b.*?</p>", s, re.S):
        if re.search(r"v\d+\.\d+\.\d+", text_of(p)) and "fnref" not in p and 'class="cite"' not in p:
            warns.append(f"R4 각주 없는 버전 번호: {re.search(r'v\d+\.\d+\.\d+', text_of(p)).group(0)}")
    return warns

def main():
    done = applied()
    files = sorted(glob.glob(os.path.join(ROOT, "src", "chapters", "*.html")) + glob.glob(os.path.join(ROOT, "src", "appendix", "*.html")))
    n_fail = 0
    counts = {}
    for f in files:
        name, fails, warns = check_file(f)
        strict = name in done
        for x in fails:
            if strict:
                print(f"실패 {name}: {x}"); n_fail += 1
            else:
                counts[name] = counts.get(name, 0) + 1
        for x in warns:
            print(f"경고 {name}: {x}")
    # 자료 목록(D-131): 같은 자료(제목이나 주소)에 키 둘 이상은 실패, 어느 장에서도 인용하지 않은 키는 경고
    bib = {k: v for k, v in json.load(open(os.path.join(ROOT, "research", "bibliography.json"), encoding="utf-8")).items() if not k.startswith("_")}
    seen = {}
    for k, v in bib.items():
        for field in ("title", "url"):
            key = (field, (v.get(field) or "").strip().rstrip("/").lower(), v.get("venue") if field == "title" else "")
            if key[1] in ("",):
                continue
            if key in seen:
                print(f"실패 bibliography: 같은 자료에 키 둘({seen[key]}, {k}, {field})"); n_fail += 1
            seen[key] = k
    used = set()
    for f in files:
        used |= set(re.findall(r'<a class="cite" data-ref="([^"]+)">', open(f, encoding="utf-8").read()))
    for k in sorted(set(bib) - used):
        print(f"경고 bibliography: 어느 장에서도 인용하지 않은 자료 {k}")
    if counts:
        print("정비 전 장의 실패 규칙 위반(경고): " + ", ".join(f"{k} {v}" for k, v in sorted(counts.items())))
    print(f"규칙 적용 장: {', '.join(sorted(done)) or '없음'}")
    return 1 if n_fail else 0

if __name__ == "__main__":
    sys.exit(main())
