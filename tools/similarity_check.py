"""ai-book과 비교 대상 책의 유사도 측정 (검수 Agent 10차 측정과 같은 방법)

사용법:
  pip install scikit-learn
  git clone --depth 1 https://github.com/zakedu/genai-book.git ../genai-book
  python3 similarity_check.py --ab src --gb ../genai-book/docs [--out sim.json]

판정 구간(단위 점수): 일치율 0.95 이상 100, 0.80~0.95 90, 0.60~0.80 70, 그 밖 0
단위: 설명 문장, 표 행, 예제(코드 상자), 제목
"""
import re, glob, html, json, difflib, argparse, collections
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def norm(s): return re.sub(r'[\s\W_]+', '', s.lower())

def sents(text):
    out = []
    for para in re.split(r'\n+', text):
        para = para.strip()
        if not para: continue
        for s in re.split(r'(?<=[다요오죠음됨함])\.\s+|(?<=[.?!])\s+(?=[가-힣A-Z「"])', para):
            s = s.strip(' -*>#|')
            if len(norm(s)) >= 12: out.append(s)
    return out

def load_gb(root):
    units = []
    for f in sorted(glob.glob(root.rstrip('/') + '/**/*.md', recursive=True)):
        t = open(f, encoding='utf-8').read()
        t = re.sub(r'^---.*?---', '', t, flags=re.S)
        page = f[len(root.rstrip('/')) + 1:]
        for m in re.finditer(r'```.*?\n(.*?)```', t, re.S):
            if len(norm(m.group(1))) >= 12: units.append(dict(page=page, kind='예제', text=m.group(1).strip()))
        t = re.sub(r'```.*?```', '', t, flags=re.S)
        for h in re.findall(r'^#{1,4}\s+(.+)$', t, re.M): units.append(dict(page=page, kind='제목', text=h))
        for r in [l for l in t.split('\n') if l.strip().startswith('|') and not re.match(r'^\|[\s:|-]+\|?$', l.strip())]:
            cells = [c.strip() for c in r.strip().strip('|').split('|')]
            if len(norm(''.join(cells))) >= 8: units.append(dict(page=page, kind='표', text=' | '.join(cells)))
        body = '\n'.join(l for l in t.split('\n') if not l.strip().startswith('|') and not l.startswith('#'))
        body = re.sub(r'!\[.*?\]\(.*?\)|\[([^\]]*)\]\([^)]*\)', r'\1', body)
        body = re.sub(r'[*_`]', '', body)
        body = re.sub(r'^(!!!|\?\?\?)\s*\w+.*$', '', body, flags=re.M)
        for s in sents(body): units.append(dict(page=page, kind='설명', text=s))
    return units

def load_ab(root):
    units = []
    root = root.rstrip('/') + '/'
    for f in sorted(glob.glob(root + '**/*.html', recursive=True)):
        t = open(f, encoding='utf-8').read(); page = f[len(root):]
        t = re.sub(r'<svg.*?</svg>', '', t, flags=re.S)
        for m in re.finditer(r'<pre[^>]*>(.*?)</pre>', t, re.S):
            x = html.unescape(re.sub(r'<[^>]+>', '', m.group(1)))
            if len(norm(x)) >= 12: units.append(dict(page=page, kind='예제', text=x.strip()))
        t = re.sub(r'<pre.*?</pre>', '', t, flags=re.S)
        for m in re.finditer(r'<h[1-5][^>]*>(.*?)</h[1-5]>', t, re.S):
            units.append(dict(page=page, kind='제목', text=html.unescape(re.sub(r'<[^>]+>', '', m.group(1)))))
        for m in re.finditer(r'<tr[^>]*>(.*?)</tr>', t, re.S):
            cells = [html.unescape(re.sub(r'<[^>]+>', '', c)).strip() for c in re.findall(r'<t[hd][^>]*>(.*?)</t[hd]>', m.group(1), re.S)]
            if len(norm(''.join(cells))) >= 8: units.append(dict(page=page, kind='표', text=' | '.join(cells)))
        t = re.sub(r'<table.*?</table>|<h[1-5].*?</h[1-5]>|<figcaption.*?</figcaption>', '', t, flags=re.S)
        body = html.unescape(re.sub(r'<[^>]+>', '\n', re.sub(r'</?(b|a|i|em|strong|code)[^>]*>', '', t)))
        for s in sents(body): units.append(dict(page=page, kind='설명', text=s))
    return units

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--ab', default='src'); ap.add_argument('--gb', required=True); ap.add_argument('--out')
    a_ = ap.parse_args()
    g, a = load_gb(a_.gb), load_ab(a_.ab)
    gn, an = [norm(u['text']) for u in g], [norm(u['text']) for u in a]
    X = TfidfVectorizer(analyzer='char', ngram_range=(2, 3)).fit_transform(gn + an)
    S = cosine_similarity(X[len(g):], X[:len(g)])
    res = []
    for i, u in enumerate(a):
        best = (0, None)
        for j in S[i].argsort()[-8:][::-1]:
            r = difflib.SequenceMatcher(None, an[i], gn[j], autojunk=False).ratio()
            if r > best[0]: best = (r, j)
        r, j = best
        sc = 100 if r >= 0.95 else 90 if r >= 0.80 else 70 if r >= 0.60 else 0
        res.append(dict(page=u['page'], kind=u['kind'], text=u['text'], ratio=round(r, 3), score=sc,
                        gpage=g[j]['page'] if j is not None else None, gtext=g[j]['text'] if j is not None else ''))
    print('단위 | 개수 | 일치 | 근접 | 부분 | 독자 | 평균')
    for k in ['설명', '표', '예제', '제목']:
        rows = [x for x in res if x['kind'] == k]; c = collections.Counter(x['score'] for x in rows); n = len(rows) or 1
        print(f"{k} | {len(rows)} | {c[100]} | {c[90]} | {c[70]} | {c[0]} | {sum(x['score'] for x in rows)/n:.1f}")
    print('\n일치(0.95 이상) 목록')
    for x in sorted([x for x in res if x['score'] == 100], key=lambda x: x['page']):
        print(f"{x['page']} [{x['kind']}] {x['text'][:60]}  <->  {x['gpage']}")
    if a_.out: json.dump(res, open(a_.out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

if __name__ == '__main__':
    main()
