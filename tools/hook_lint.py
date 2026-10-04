"""Claude Code PostToolUse 훅: 원고(src/)를 고치면 빌드와 lint를 바로 실행한다.
문제가 있으면 종료 코드 2와 함께 오류를 stderr로 보내 Claude가 즉시 고치게 한다.
"""
import json, subprocess, sys

data = json.load(sys.stdin)
path = (data.get("tool_input") or {}).get("file_path", "")
if "/src/" not in path.replace("\\", "/") and not path.replace("\\", "/").startswith("src/"):
    sys.exit(0)

steps = [
    ["python", "tools/build.py"],
    ["python", "lint/check_numbers.py"],
    ["python", "lint/check_structure.py"],
    ["python", "lint/check_style.py"],
]
errors = []
for cmd in steps:
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    out = (r.stdout + r.stderr).strip()
    if r.returncode != 0 or any(l.startswith("경고 ") for l in out.splitlines()):
        errors.append(f"[{' '.join(cmd)}] exit={r.returncode}\n{out[-1500:]}")
g = subprocess.run("git grep -nE -f lint/banned.txt -- index.html chapters appendix",
                   shell=True, capture_output=True, text=True, encoding="utf-8", errors="replace")
if g.stdout.strip():
    errors.append("[금칙어]\n" + g.stdout[-1500:])
if errors:
    print("\n\n".join(errors), file=sys.stderr)
    sys.exit(2)
sys.exit(0)
