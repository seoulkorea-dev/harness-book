"""검수 지침 반영 대조: 검수 문서의 "교체" 코드 상자 내용이 원고(src/ 등)에 있는지 확인한다.
사용: python tools/check_review.py reviews/<문서>.md
결과: 반영 n / m. 빠진 항목이 있으면 종료 코드 1.
"""
import glob, re, sys

def norm(s):
    return re.sub(r"\s+", " ", s).strip()

doc = open(sys.argv[1], encoding="utf-8").read()
FENCE = "`" * 3  # 문서 안에 백틱 세 개를 직접 쓰지 않으려고 만듦
blocks = re.findall(r"\*\*교체\*\*\s*\n" + FENCE + r"[a-z]*\n(.*?)" + FENCE, doc, re.S)
corpus = ""
for f in glob.glob("src/**/*.*", recursive=True) + glob.glob("*.md") + glob.glob("lint/*.py") + glob.glob("tools/*.py"):
    try:
        corpus += norm(open(f, encoding="utf-8").read()) + "\n"
    except (UnicodeDecodeError, IsADirectoryError):
        pass
missing = []
for i, b in enumerate(blocks, 1):
    if norm(b) and norm(b) not in corpus:
        missing.append((i, norm(b)[:80]))
print(f"반영 {len(blocks) - len(missing)} / {len(blocks)}")
for i, s in missing:
    print(f"  미반영 교체 {i}: {s}")
sys.exit(1 if missing else 0)
