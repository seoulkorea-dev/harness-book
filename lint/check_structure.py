"""원고 구조 검사 (STYLE.md 3절, CLAUDE.md 캡션 규칙). 위반이 없으면 출력 없음.
1. 캡션 설명(capnote)은 정확히 1줄
2. 절 제목(h2, h3) 바로 뒤에 그림이나 표를 두지 않음
3. 요약 그림은 캡션에서 가리키는 같은 절의 표보다 앞에 둠
4. 병합 셀(rowspan)이 있는 표에는 둘째 열 이후의 줄바꿈 금지 클래스(fit-2~)를 쓰지 않음
5. 장마다 참고 자료 항목과 본문 링크가 있고, 끊긴 링크가 없음
"""
import glob, os, re, sys

ROOT = __file__.rsplit('/lint/', 1)[0]
pages = ([f'{ROOT}/index.html'] + sorted(glob.glob(f'{ROOT}/chapters/*.html'))
         + sorted(glob.glob(f'{ROOT}/appendix/*.html')))
errors = []
for path in pages:
    s = open(path, encoding='utf-8').read()
    name = path[len(ROOT) + 1:]
    for m in re.finditer(r'<figcaption><b>([^<.]+)\.[^<]*</b>(.*?)</figcaption>', s, re.S):
        n = len(re.findall(r'<li>', m.group(2)))
        if n != 1:
            errors.append(f'{name}: {m.group(1)} 캡션 설명 {n}줄')
    for m in re.finditer(r'<(h2|h3)[^>]*>([^<]*)</\1>\s*<figure', s, re.S):
        errors.append(f'{name}: 절 "{re.sub(r"<[^>]+>", "", m.group(2))}" 제목 바로 뒤에 그림 또는 표')
    heads = [m.start() for m in re.finditer(r'<h2[\s>]', s)]
    section = lambda p: sum(1 for h in heads if h < p)
    pos = {m.group(1): m.start() for m in re.finditer(r'<figcaption><b>((?:표|그림) [0-9A-Z]+(?:-\d+)?)\.', s)}
    for m in re.finditer(r'<figcaption><b>(그림 [^<.]+)\.[^<]*</b>(.*?)</figcaption>', s, re.S):
        for ref in re.findall(r'표 [0-9A-Z]+-\d+', m.group(2)):
            if ref in pos and pos[ref] < m.start() and section(pos[ref]) == section(m.start()):
                errors.append(f'{name}: {m.group(1)}이 같은 절의 {ref}보다 뒤에 있음')
    for m in re.finditer(r'<table class="([^"]*)">.*?</table>', s, re.S):
        late = [c for c in m.group(1).split() if re.fullmatch(r'fit-[2-9]', c)]
        if late and 'rowspan' in m.group(0):
            cap = re.search(r'<figcaption><b>([^<.]+)\.', s[m.end():m.end() + 300])
            errors.append(f'{name}: {cap.group(1) if cap else "표"} 병합 셀이 있어 {" ".join(late)} 사용 불가')
    # 링크 규칙(61차): 참고 자료 링크는 항목 id로, 본문 문단의 장 링크는 절 앵커로(목차 표와 마치며 장 요약 문단 제외)
    _main = re.search(r'<main\b.*?</main>', s, re.S)
    _main = _main.group(0) if _main else s
    if 'http-equiv="refresh"' in s:
        _main = ''  # 이동 쪽은 새 쪽 맨 위로 안내하는 것이 목적이라 제외
    for m in re.finditer(r'href="[^"]*references\.html(#[^"]*)?"', _main):
        if not (m.group(1) or '').startswith('#ref-'):
            errors.append(f'{name}: 참고 자료 링크에 항목 id 없음')
    if not name.endswith(('index.html', 'epilogue.html')):
        body = re.sub(r'<table.*?</table>', ' ', _main, flags=re.S)
        for m in re.finditer(r'<a href="[^"#]*/(ch0\d|epilogue)\.html">([^<]*)</a>', body):
            errors.append(f'{name}: 앵커 없는 장 링크 {m.group(2)}')
    # 용어 풀이 표제어: 한글(원어) 또는 한글(원어, 약어). 괄호 붙임, 원어 각 단어 첫 글자 대문자(관사, 전치사, 접속사와 하이픈 뒤 제외), 약어는 뒤
    if name.endswith('terms.html'):
        SMALLW = {'a', 'an', 'the', 'of', 'in', 'on', 'to', 'for', 'and'}
        for dt in re.findall(r'<dt[^>]*>(.*?)</dt>', s):
            if re.search(r'[가-힣] \(', dt):
                errors.append(f'{name}: 표제어 괄호 앞 공백: {dt}')
            if re.search(r'\([A-Z]{2,6}, ', dt):
                errors.append(f'{name}: 표제어 약어가 원어보다 먼저: {dt}')
            m = re.search(r'\(([A-Za-z][^)]*)\)', dt)
            if m:
                words = m.group(1).split(',')[0].split(' ')
                bad = [w for i, w in enumerate(words) if w and w[0].islower() and not (i > 0 and w in SMALLW)]
                if bad:
                    errors.append(f'{name}: 표제어 원어 첫 글자 소문자: {dt}')
# 용어 풀이 표제어가 본문(표지, 장, 마치며)에 1회 이상 나오는지(2026-10-03, 64차)
import html as _html
_body = ''
for _f in ['index.html'] + sorted(glob.glob(f'{ROOT}/chapters/*.html')):
    _p = _f if _f.startswith('/') else f'{ROOT}/{_f}'
    _t = open(_p, encoding='utf-8').read()
    _m = re.search(r'<main\b.*?</main>', _t, re.S)
    _body += _html.unescape(re.sub(r'<[^>]+>', ' ', _m.group(0) if _m else _t))
# 용어 풀이 쪽이 있을 때만 검사(설계 단계에는 부록이 없음)
_tp = f'{ROOT}/appendix/terms.html'
_terms = open(_tp, encoding='utf-8').read() if os.path.exists(_tp) else ''
for _dt in re.findall(r'<dt[^>]*>(.*?)</dt>', _terms):
    _head = re.sub(r'<[^>]+>', '', _dt).split('(')[0].strip()
    if _head and _head not in _body:
        errors.append(f'appendix/terms.html: 본문에 없는 표제어 {_head}')

# 참고 자료 링크 검사(1차 검수 25번): 장마다 항목 1개 이상, 항목마다 본문 링크 1개 이상, 끊긴 링크 0, id 형식
_refp = f'{ROOT}/appendix/references.html'
_ref_ids = set(re.findall(r'id="(ref-[^"]+)"', open(_refp, encoding='utf-8').read())) if os.path.exists(_refp) else set()
for _f in sorted(glob.glob(f'{ROOT}/chapters/ch*.html')):
    _n = _f[len(ROOT) + 1:]
    _t = open(_f, encoding='utf-8').read()
    if 'http-equiv="refresh"' in _t:
        continue
    _ids = re.findall(r'id="(ref-[^"]+)"', _t)
    _local = re.findall(r'href="#(ref-[^"]+)"', _t)
    _remote = re.findall(r'href="[^"]*references\.html#(ref-[^"]+)"', _t)
    if not _ids and not _remote:
        errors.append(f'{_n}: 참고 자료 항목 없음')
    for _i in _ids:
        if not re.fullmatch(r'ref-[a-z]+-[0-9]{4}[a-z]?', _i):
            errors.append(f'{_n}: 참고 자료 id 형식 위반 {_i}')
        if _i not in _local:
            errors.append(f'{_n}: 본문 링크가 없는 참고 자료 항목 {_i}')
    for _h in _local:
        if _h not in _ids:
            errors.append(f'{_n}: 끊긴 참고 자료 링크 #{_h}')
    for _h in _remote:
        if _h not in _ref_ids:
            errors.append(f'{_n}: 끊긴 참고 자료 링크 references.html#{_h}')

print('\n'.join(errors), end='\n' if errors else '')
sys.exit(1 if errors else 0)
