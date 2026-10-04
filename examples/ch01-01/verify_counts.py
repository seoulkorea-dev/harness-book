"""주간 보고서 초안의 완료 건수, 작업 목록, 미해결 이슈를 원본 자료와 대조합니다.
실행: python verify_counts.py [보고서 경로]  (기본: output/weekly-report-2026-10-02.md)
"""
import csv, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
report = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "output" / "weekly-report-2026-10-02.md"
tasks = list(csv.DictReader(open(ROOT / "data" / "completed-tasks.csv", encoding="utf-8")))
issues = list(csv.DictReader(open(ROOT / "data" / "open-issues.csv", encoding="utf-8")))
done = [t["작업번호"] for t in tasks if t["상태"] == "완료"]
open_ids = [i["이슈번호"] for i in issues if i["상태"] == "미해결"]
closed_ids = [i["이슈번호"] for i in issues if i["상태"] != "미해결"]

if not report.exists():
    print(f"검증 실패: 보고서 파일 없음 {report}"); sys.exit(1)
text = report.read_text(encoding="utf-8")
errors = []
m = re.search(r"이번 주 완료\s*(\d+)\s*건", text)
stated = int(m.group(1)) if m else None
print(f"원본 완료 작업 {len(done)}건: {', '.join(done)}")
print(f"보고서에 적힌 완료 건수: {stated if stated is not None else '없음'}")
if stated != len(done):
    errors.append(f"완료 건수 불일치(보고서 {stated}, 원본 {len(done)})")
for tid in [t["작업번호"] for t in tasks]:
    if tid not in text: errors.append(f"진행 현황에 없는 작업 {tid}")
mi = re.search(r"^#+[^\n]*이슈[^\n]*$", text, re.M)
issue_part = text[mi.end():] if mi else ""
issue_part = re.split(r"^#+ ", issue_part, maxsplit=1, flags=re.M)[0]
table_rows = [l for l in issue_part.splitlines() if l.strip().startswith("|")]
in_table = {i for i in open_ids + closed_ids if any(i in l for l in table_rows)}
for i in open_ids:
    if i not in in_table: errors.append(f"이슈 표에 없는 미해결 이슈 {i}")
for i in closed_ids:
    if i in in_table: errors.append(f"이슈 표에 해결된 이슈 포함 {i}")
print(f"원본 미해결 이슈 {len(open_ids)}건: {', '.join(open_ids)}")
if errors:
    print("검증 실패"); [print(" -", e) for e in errors]; sys.exit(1)
print("검증 통과")
