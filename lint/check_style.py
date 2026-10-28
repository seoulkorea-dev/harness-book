"""B 배제어 경고 검사. 한자어 치환 후보를 출력만 하고 종료 코드는 항상 0이다.

치환 기준은 플레이북 6.3 어휘 선택을 따른다. 코드 상자 속 프롬프트도 검사한다. 뜻에 따라 바꿀 말이 다르므로
자동으로 고치지 않고, 위치와 문맥만 보여 준다.
"""
import glob
import re
import html
from collections import Counter

# 치환 대상 동사는 어간 뒤 모든 어미를 잡는다(관형형, 과거형, 연결형). 앞에 한글이 붙으면 다른 낱말(원고를, 덧붙이다)이라 제외
B = re.compile(
    r"(?<![가-힣])(?:쓰[고지기며면는]|써[도서야 ]|썼|씁|쓸 |쓴 |쓰십시오)"
    r"|(?<![가-힣])넣[고기어으을은었지는습]"
    r"|(?<![가-힣])(?:바꾸|바꿉|바꿔|바뀌|바꾼|바꿀|바꿨)"
    r"|(?<![가-힣])(?:고르|고릅|고른|골라|골랐|고를)"
    r"|(?<![가-힣])(?:고치|고칩|고친|고쳐|고칠|고쳤)"
    r"|(?<![가-힣])(?:붙이|붙입|붙인|붙일|붙여|붙였)"
    r"|(?<![가-힣])(?:틀리|틀린|틀릴|틀렸)"
    r"|알아채|잘하는|못하는|좋아지|나빠지|만들어 내|찾아내|(?<![가-힣])끄는"
)
# 정상 예외: 고르지 않다, 고르게(균등하다 뜻), 붙여 넣다, 읽기와 쓰기(권한 이름), 일부러 보인 나쁜 예(개선 전 프롬프트)
EXCEPT = re.compile(r"고르지 않|고르게|붙여 넣|읽기와 쓰기|나와\. 고쳐 줘|자기소개서 써 줘")
files = ["index.html"] + sorted(glob.glob("chapters/*.html")) + sorted(glob.glob("appendix/*.html"))
total = Counter()
for f in files:
    body = open(f, encoding="utf-8").read()
    # 표의 예제 열(작성 예제, 적용 예제, 요청 예제) 셀 속 프롬프트 말투도 "~해 줘"
    for t in re.findall(r"<table.*?</table>", body, flags=re.S):
        heads = re.findall(r"<th>(.*?)</th>", t)
        cols = [i for i, h in enumerate(heads) if h in ("작성 예제", "적용 예제", "요청 예제")]
        for row in re.findall(r"<tr>(.*?)</tr>", t, flags=re.S):
            cells = re.findall(r"<td[^>]*>(.*?)</td>", row, flags=re.S)
            for i in cols:
                if i < len(cells) and "십시오" in cells[i]:
                    total["표 예제 십시오"] += 1
                    print(f"경고 {f}: 표 예제 칸 '십시오' | {re.sub('<[^>]+>', '', cells[i])[:40]}")
    # 코드 상자 속 프롬프트 예제는 예외(플레이북 6.3 배제어). 줄 번호를 유지하도록 줄바꿈만 남긴다
    # 코드 상자 속 프롬프트 말투는 "~해 줘"(플레이북 15장). "십시오"가 남으면 따로 경고
    for m in re.finditer(r"<pre.*?</pre>", body, flags=re.S):
        # 입력 자료 태그(&lt;공지문&gt; 등) 안의 원문은 원래 문체를 유지하므로 제외
        k = re.sub(r"&lt;([^&/]+)&gt;.*?&lt;/\1&gt;", "", m.group(0), flags=re.S).count("십시오")
        if k:
            total["코드 상자 십시오"] += k
            print(f"경고 {f}: 코드 상자 속 '십시오' {k}건")
    # 본문 큰따옴표 안의 인용 프롬프트 말투도 "~해 줘"(코드 상자, 표 제외). 인용 프롬프트인지는 사람이 판단
    prose = re.sub(r"<(pre|table|svg)\b.*?</\1>", " ", body, flags=re.S)
    for q in re.findall(r'"([^"<>]*십시오[^"<>]*)"', re.sub(r"<[^>]+>", "", prose.replace("&quot;", '"'))):
        total["인용 십시오"] += 1
        print(f"경고 {f}: 큰따옴표 인용 '십시오' | {q[:40]}")
    for n, line in enumerate(body.split("\n"), 1):
        text = re.sub(r"<svg.*?</svg>|<[^>]+>", " ", line)
        for m in B.finditer(text):
            if EXCEPT.search(text[max(0, m.start() - 10):m.end() + 10]):
                continue
            total[m.group(0)] += 1
            print(f"경고 {f}:{n}: {m.group(0)} | {text[max(0, m.start() - 20):m.end() + 15].strip()}")
# 문장 원칙(2026-10-02, 길이 기준 2026-10-16 150자로 변경): 150자 넘는 문장, 문장 첫머리 "그리고, 다만, 또한, 특히"를 경고(표, 그림, 코드 상자, 참고 자료 서지 제외)
for f in files:
    if f.endswith("references.html"):
        continue
    body = re.sub(r"<(pre|table|svg|figure)\b.*?</\1>", " ", open(f, encoding="utf-8").read(), flags=re.S)
    for para in re.findall(r"<(?:p|li)\b[^>]*>(.*?)</(?:p|li)>", body, flags=re.S):
        text = html.unescape(re.sub(r"<[^>]+>", "", para)).strip()
        for sent in re.split(r"(?<=[.?!])\s+(?=[^)\s])", text):
            sent = sent.strip()
            if len(sent) > 150:
                total["150자 초과 문장"] += 1
                print(f"경고 {f}: 150자 초과({len(sent)}자) | {sent[:40]}")
            if re.match(r"(그리고|다만|또한|특히)[ ,]", sent):
                total["첫머리 접속어"] += 1
                print(f"경고 {f}: 첫머리 접속어 | {sent[:40]}")

# 이웃 문장 중복(2026-10-03, 60차): 같은 절 안에서 단어 겹침 65% 이상인 문장 쌍을 경고
# 요점 상자(첫 문단의 정리), 표, 그림, 코드 상자, 참고 자료, 용어 풀이는 제외. 의도된 대비 문장은 DUP_OK에 둔다
DUP_OK = [("짧은 자료는 구성 요소 뒤에 둡니다.", "긴 자료는 구성 요소 앞에 둡니다.")]
def _toks(x):
    return {w for w in re.findall(r"[가-힣A-Za-z0-9]+", x) if len(w) > 1}
for f in files:
    if f.endswith(("references.html", "terms.html")):
        continue
    body = open(f, encoding="utf-8").read()
    body = re.sub(r'<ul class="summary">.*?</ul>', " ", body, flags=re.S)
    body = re.sub(r'<p class="claim">.*?</p>', " ", body, flags=re.S)  # 주장 줄(D-104)은 첫 문단 둘째 문장과 같게 둠, 작가 확인 사항
    body = re.sub(r'<ol class="fn"[^>]*>.*?</ol>|<h2 id="refs">.*', " ", body, flags=re.S)  # 각주와 참고 자료(D-123)는 서지 형식이 겹침
    body = re.sub(r"<(pre|table|svg|figure)\b.*?</\1>", " ", body, flags=re.S)
    for sec in re.split(r"<h[23]\b", body):
        sents = []
        for para in re.findall(r"<(?:p|li)\b[^>]*>(.*?)</(?:p|li)>", sec, flags=re.S):
            text = html.unescape(re.sub(r"<[^>]+>", "", para)).strip()
            sents += [x.strip() for x in re.split(r"(?<=[.?!])\s+(?=[^)\s])", text) if len(_toks(x)) >= 5]
        for i in range(len(sents)):
            for j in range(i + 1, len(sents)):
                a, b = _toks(sents[i]), _toks(sents[j])
                if len(a & b) / min(len(a), len(b)) >= 0.65 and (sents[i], sents[j]) not in DUP_OK:
                    total["이웃 문장 중복"] += 1
                    print(f"경고 {f}: 이웃 문장 중복 | {sents[i][:30]} / {sents[j][:30]}")

if total:
    print("B 배제어 경고 합계:", sum(total.values()), dict(total.most_common()))

# 질문형 문장(플레이북 6.2, 2026-10-28): 절 첫 문장에 하나만 허용(점검 질문 절 제외). 판단이 필요하므로 실패가 아니라 경고만.
# 목록 항목(<li>)은 점검 질문 목록이므로 보지 않는다. check_all.py의 "문체"는 "경고 "로 시작하는 줄을 실패로 보므로, 이 경고는 "질문형 "으로 시작해 따로 보여 준다
Q_END = re.compile(r"(?:\?|까요\.|니까\.)$")
for f in files:
    if f.endswith(("references.html", "terms.html")):
        continue
    body = re.sub(r"<(pre|table|svg|figure|aside)\b.*?</\1>", " ", open(f, encoding="utf-8").read(), flags=re.S)
    for part in re.split(r"(?=<h[23]\b)", body):
        head = re.match(r"<h[23]\b[^>]*>(.*?)</h[23]>", part, flags=re.S)
        if not head:
            continue  # 장 첫머리(도입부)는 절이 아니므로 아래 문장 검사만 받음
        if "점검 질문" in head.group(1):
            continue
        first = True
        for para in re.findall(r"<p\b[^>]*>(.*?)</p>", part, flags=re.S):
            text = html.unescape(re.sub(r"<[^>]+>", "", para)).strip()
            for sent in re.split(r"(?<=[.?!])\s+(?=[^)\s])", text):
                sent = sent.strip()
                if sent and Q_END.search(sent) and not first:
                    print(f"질문형 {f}: 절 첫 문장 밖 | {sent[:40]}")
                if sent:
                    first = False
    # 장 첫머리(첫 절 제목 앞)의 질문형 문장
    lead = re.split(r"<h[23]\b", body, maxsplit=1)[0]
    for para in re.findall(r"<(?:p|li)\b[^>]*>(.*?)</(?:p|li)>", lead, flags=re.S):  # 도입부는 요약 목록도 봄(6.2)
        text = html.unescape(re.sub(r"<[^>]+>", "", para)).strip()
        for sent in re.split(r"(?<=[.?!])\s+(?=[^)\s])", text):
            if Q_END.search(sent.strip()):
                print(f"질문형 {f}: 장 첫머리 | {sent.strip()[:40]}")
