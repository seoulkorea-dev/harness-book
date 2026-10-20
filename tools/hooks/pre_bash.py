"""PreToolUse 훅(Bash): main 브랜치에서의 커밋과 강제 push를 막는다. 막으면 종료 코드 2."""
import os, json, re, subprocess, sys
os.chdir(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))  # 저장소 루트 기준으로 실행(F-14)
data = json.load(sys.stdin)
cmd = (data.get("tool_input") or {}).get("command", "")
branch = subprocess.run("git branch --show-current", shell=True, capture_output=True, text=True).stdout.strip()
if re.search(r"\bgit\s+commit\b", cmd) and branch == "main":
    print("main 브랜치에서는 커밋하지 않습니다. 작업 브랜치를 만든 뒤 커밋하십시오(git switch -c <브랜치>).", file=sys.stderr)
    sys.exit(2)
if re.search(r"\bgit\s+push\b.*(--force|\s-f\b)", cmd):
    print("강제 push는 하지 않습니다.", file=sys.stderr)
    sys.exit(2)
if re.search(r"\bgit\s+push\b.*\s(\S+:)?main(\s|$)", cmd) or (re.search(r"\bgit\s+push\b", cmd) and branch == "main"):
    print("main에는 push하지 않습니다. 작업 브랜치를 push하고 PR을 만드십시오.", file=sys.stderr)
    sys.exit(2)
sys.exit(0)
