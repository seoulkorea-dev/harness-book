"""SessionStart 훅: 세션 시작 때 인계 문서, 최근 결정, 현재 브랜치를 컨텍스트로 보여 준다."""
import os, re, subprocess
os.chdir(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))  # 저장소 루트 기준으로 실행(F-14)
# 검사 도구, 에이전트, 스킬을 book-kit에서 가져온다(D-150). 저장소에는 두지 않는다
k = subprocess.run("python tools/sync_kit.py", shell=True, capture_output=True, text=True, encoding="utf-8", errors="replace")
if "book-kit 없음" in k.stdout:
    print("== 경고 ==\n" + k.stdout.strip() + "\n검사 도구, 에이전트, 스킬이 없습니다. 이 저장소 옆에 book-kit을 받아 두십시오.\n")
print("== 작업 공간 상태 ==")
b = subprocess.run("git branch --show-current", shell=True, capture_output=True, text=True).stdout.strip()
print(f"현재 브랜치: {b}" + ("  (main입니다. 작업 전에 작업 브랜치를 만드십시오)" if b == "main" else ""))
if os.path.exists(".claude/last_check_failed.txt"):
    print("\n== 지난 세션의 검사 실패 ==\n" + open(".claude/last_check_failed.txt", encoding="utf-8").read()[-1500:])
if os.path.exists("HANDOFF.md"):
    print("\n== HANDOFF.md ==\n" + open("HANDOFF.md", encoding="utf-8").read()[:4000])
if os.path.exists("DECISIONS.md"):
    rows = [l for l in open("DECISIONS.md", encoding="utf-8") if re.match(r"\| D-\d+", l)]
    print("\n== 최근 결정 10건 ==\n" + "".join(r[:200].rstrip() + "\n" for r in rows[-10:]))
