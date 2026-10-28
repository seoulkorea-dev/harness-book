"""예제 작업 단위의 확인 방법이 구현 전에는 실패하는지 검사한다(플레이북 13장, 이슈 #66).

사용: python tools/check_tasks.py
examples/expense-app/는 변경 요청 사항을 구현하기 전 상태(기준 상태)다. reference/tasks.example.json의 각 작업 단위에서
확인 방법을 읽어 그 시험을 기준 상태에서 실행하고, 통과하면 "공백 있음"(아무것도 하지 않아도 완료로 판정됨)으로 보고한다.
사람이 판단하는 확인(결정 기록, 사람 승인)은 건너뛴다. 공백이 하나라도 있으면 종료 코드 1.
"""
import json, os, re, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APP = os.path.join(ROOT, "examples", "expense-app")
TASKS = os.path.join(APP, "reference", "tasks.example.json")

def run(args):
    r = subprocess.run([sys.executable, "-m", "unittest", *args], cwd=APP, capture_output=True, text=True, encoding="utf-8", errors="replace")
    tail = (r.stdout + r.stderr).strip().splitlines()
    ran_none = any(l.startswith("Ran 0 tests") for l in tail)  # 시험이 0건이면 통과로 보지 않음
    return r.returncode == 0 and not ran_none, (tail[-1] if tail else "")

def check_of(method):
    """확인 방법 문장 → 실행할 unittest 인자 목록(모두 통과해야 통과, 사람이 판단하는 확인이면 None)"""
    m = re.search(r"수용 시험 ([\d,\s]+) 통과", method)
    if m:
        args = ["acceptance.test_cr07"]
        for n in re.findall(r"\d+", m.group(1)):
            args += ["-k", f"test_{n}_"]
        return [args]
    if re.search(r"tests 실패 0건", method):
        runs = [["discover", "tests"]]
        k = re.search(r"(\w+) 시험 1건 이상", method)
        if k:  # 이름에 그 말이 든 단위 시험이 있어야 함(0건이면 unittest가 실패로 끝남)
            runs.append(["discover", "tests", "-k", k.group(1)])
        return runs
    return None

def main():
    tasks = json.load(open(TASKS, encoding="utf-8"))
    gaps, lines = [], []
    for t in tasks:
        method = t.get("확인 방법", "")
        runs = check_of(method)
        if runs is None:
            lines.append(f"건너뜀\t{t['id']}\t{method}(사람이 판단하는 확인)")
            continue
        results = [run(args) for args in runs]
        passed = all(p for p, _ in results)
        last = next((l for p, l in results if not p), results[-1][1])
        if passed:
            gaps.append(t["id"])
            lines.append(f"공백 있음\t{t['id']}\t{method}: 구현 전 상태에서도 통과({last})")
        else:
            lines.append(f"정상\t{t['id']}\t{method}: 구현 전 상태에서 실패({last})")
    print("\n".join(lines))
    print(f"요약: 공백 {len(gaps)}건" + (f"({', '.join(gaps)})" if gaps else ""))
    return 1 if gaps else 0

if __name__ == "__main__":
    sys.exit(main())
