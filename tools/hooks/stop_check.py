"""Stop 훅: 작업을 끝내기 전에 전체 검사와 인계 문서 갱신을 확인한다.
- 저장소에 변경이 없으면 통과.
- 검사 실패 또는 원고를 바꿨는데 HANDOFF.md를 갱신하지 않았으면 종료 코드 2로 끝내지 못하게 한다.
- 같은 멈춤에서 두 번째 호출(stop_hook_active)이면 무한 반복을 막기 위해 통과시키고, 실패 내용을 .claude/last_check_failed.txt에 남긴다(다음 세션 시작 때 표시).
"""
import json, os, subprocess, sys
os.chdir(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))  # 저장소 루트 기준으로 실행(F-14)
data = json.load(sys.stdin)
again = bool(data.get("stop_hook_active"))
changed = subprocess.run("git status --porcelain", shell=True, capture_output=True, text=True).stdout.splitlines()
if not changed:
    sys.exit(0)
paths = [l[3:] for l in changed]
problems = []
r = subprocess.run("python tools/check_all.py", shell=True, capture_output=True, text=True, encoding="utf-8", errors="replace")
if r.returncode != 0:
    problems.append("[검사 실패]\n" + r.stdout[-2500:])
if any(p.startswith("src/") for p in paths) and not any(p.startswith("HANDOFF.md") for p in paths):
    problems.append("[인계] 원고(src/)를 바꿨는데 HANDOFF.md를 갱신하지 않았습니다.")
if not problems:
    if os.path.exists(".claude/last_check_failed.txt"):
        os.remove(".claude/last_check_failed.txt")
    sys.exit(0)
msg = "\n\n".join(problems)
if again:
    open(".claude/last_check_failed.txt", "w", encoding="utf-8").write(msg)
    sys.exit(0)
print(msg + "\n\n위 문제를 고친 뒤 끝내십시오.", file=sys.stderr)
sys.exit(2)
