"""한 단위마다 새 세션으로 /next를 반복 실행한다(작가 요청 이슈 #22).

사용: python tools/autorun.py [--once] [--max N] [--max-turns N] [--max-budget-usd X] [--dry-run] [--selftest]
  --once            한 단위만 실행
  --max N           최대 단위 수(기본 20)
  --max-turns N     단위마다 claude -p의 턴 상한(기본 제한 없음)
  --max-budget-usd X 단위마다 비용 상한(기본 제한 없음)
  --dry-run         상태만 확인하고 실행할 명령을 보여 줌(claude를 실행하지 않음)
  --selftest        멈춤 조건 판정 시험(가짜 상태로)

멈춤 조건
  1. 열린 요청 이슈, 열린 PR, HANDOFF 작업 목록의 빈 항목이 모두 없음(할 일 없음)
  2. /next가 PR 설명이나 HANDOFF.md 맨 위에 "멈춤:"을 적음(editor "병합 불가" 3회 등)
  3. 같은 이유의 실패가 2회 연속(검사, CI, 실행 오류)
  4. 사용량 한도나 실행 오류(종료 코드 0이 아니거나 결과가 오류)
멈추면 이유를 HANDOFF.md "## 지금 상태"에 적고 커밋, push한다(열린 PR이 있으면 그 브랜치와 PR 설명 맨 위에도). 할 일이 없어서 멈출 때는 기록할 변경이 없으므로 로그와 화면에만 남긴다.
단위마다 시작, 끝, 작업, PR 번호, 결과를 logs/autorun.log에 남긴다(.gitignore).
"""
import argparse, datetime, json, os, re, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG = os.path.join(ROOT, "logs", "autorun.log")

def sh(cmd, check=False):
    # stdin을 닫아 "no stdin data" 대기를 없앰. Windows에서는 cmd.exe로 실행되어 Git Bash의 "/next" 경로 변환이 없음
    r = subprocess.run(cmd, shell=True, cwd=ROOT, capture_output=True, text=True, encoding="utf-8", errors="replace", stdin=subprocess.DEVNULL)
    if check and r.returncode != 0:
        raise RuntimeError(f"{cmd}: {r.stderr.strip()}")
    return r

def now():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def log(line):
    os.makedirs(os.path.dirname(LOG), exist_ok=True)
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(f"{now()}\t{line}\n")
    print(line, flush=True)

def handoff_tasks(text):
    m = re.search(r"## 작업 목록\n(.*?)(\n## |\Z)", text, re.S)
    return [l[6:].strip() for l in (m.group(1).splitlines() if m else []) if l.startswith("- [ ] ")]

def state():
    """열린 요청 이슈, 열린 PR, HANDOFF 빈 항목"""
    issues = json.loads(sh("gh issue list --label request --state open --json number,title", True).stdout or "[]")
    prs = json.loads(sh("gh pr list --json number,title,isDraft,headRefName,body", True).stdout or "[]")
    sh("git fetch -q origin main")
    text = sh("git show origin/main:HANDOFF.md").stdout
    return {"issues": issues, "prs": prs, "tasks": handoff_tasks(text)}

def next_work(st):
    """/next가 고를 작업(1 요청 이슈의 가장 오래된 것, 2 열린 PR, 3 작업 목록 첫 항목)"""
    if st["issues"]:
        i = sorted(st["issues"], key=lambda x: x["number"])[0]
        return f"요청 이슈 #{i['number']} {i['title']}"
    if st["prs"]:
        p = sorted(st["prs"], key=lambda x: x["number"])[0]
        return f"열린 PR #{p['number']} {p['title']}"
    if st["tasks"]:
        return f"작업 목록: {st['tasks'][0]}"
    return None

def stop_mark(st):
    """/next가 남긴 멈춤 표시(PR 설명 맨 위 또는 HANDOFF 지금 상태 첫 줄)"""
    for p in st["prs"]:
        if (p.get("body") or "").lstrip().startswith("멈춤:"):
            return f"PR #{p['number']}에 멈춤 표시: " + p["body"].lstrip().splitlines()[0][3:].strip()
    return None

def record_stop(reason, st, dry=False):
    """멈춘 이유를 HANDOFF.md 맨 위 '## 지금 상태'에 적고 커밋, push. 열린 PR이 있으면 그 브랜치와 설명에도"""
    log(f"멈춤\t{reason}")
    if reason.startswith("할 일 없음") or dry:
        return
    pr = sorted(st["prs"], key=lambda x: x["number"])[0] if st["prs"] else None
    if pr:
        sh(f"git switch {pr['headRefName']}") ; sh("git pull -q --ff-only")
    else:
        br = "autorun-stop-" + datetime.datetime.now().strftime("%Y%m%d-%H%M")
        sh("git switch main"); sh("git pull -q --ff-only origin main"); sh(f"git switch -c {br}")
    p = os.path.join(ROOT, "HANDOFF.md"); t = open(p, encoding="utf-8").read()
    i = t.index("## 지금 상태\n") + len("## 지금 상태\n")
    t = t[:i] + f"- 멈춤(autorun, {now()}): {reason}\n" + t[i:]
    open(p, "w", encoding="utf-8").write(t)
    sh('git commit -q -am "autorun 멈춤 기록\n\nCo-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"')
    sh("git push -q -u origin HEAD")
    if pr:
        body = f"멈춤: {reason}\n\n" + (pr.get("body") or "")
        tmp = os.path.join(ROOT, "logs", "pr_body.md"); open(tmp, "w", encoding="utf-8").write(body)
        sh(f'gh pr edit {pr["number"]} --body-file "{tmp}"')
    else:
        sh(f'gh pr create --draft --base main --title "autorun 멈춤 기록" --body "멈춤: {reason}"')

def run_unit(args):
    cmd = ['claude', '-p', '"/next"', '--permission-mode', 'acceptEdits', '--output-format', 'json']
    if args.max_turns: cmd += ['--max-turns', str(args.max_turns)]
    if args.max_budget_usd: cmd += ['--max-budget-usd', str(args.max_budget_usd)]
    line = " ".join(cmd)
    if args.dry_run:
        return {"cmd": line, "dry": True}
    r = sh(line)
    out = {"cmd": line, "code": r.returncode, "stderr": r.stderr[-1000:]}
    try:
        j = json.loads(r.stdout)
        out.update({k: j.get(k) for k in ("result", "is_error", "subtype", "total_cost_usd", "session_id", "num_turns")})
    except Exception:
        out["result"] = r.stdout[-2000:]
    return out

def failure_reason(out):
    """실행 결과에서 실패 이유를 뽑음(없으면 None)"""
    res = str(out.get("result") or "") + " " + str(out.get("stderr") or "")
    if re.search(r"usage limit|rate limit|사용량 한도|limit reached", res, re.I):
        return "사용량 한도"
    if out.get("code") not in (0, None) or out.get("is_error"):
        sub = out.get("subtype") or f"종료 코드 {out.get('code')}"
        return f"실행 오류({sub})"
    return None

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--once", action="store_true"); ap.add_argument("--max", type=int, default=20)
    ap.add_argument("--max-turns", type=int); ap.add_argument("--max-budget-usd", type=float)
    ap.add_argument("--dry-run", action="store_true"); ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    if args.selftest:
        return selftest()
    last_fail, n = None, (1 if args.once else args.max)
    for k in range(n):
        st = state()
        mark = stop_mark(st)
        if mark:
            record_stop(mark, st, args.dry_run); return 1
        work = next_work(st)
        if not work:
            record_stop("할 일 없음(열린 요청 이슈, 열린 PR, 작업 목록이 모두 없음)", st); return 0
        log(f"시작\t{k + 1}/{n}\t{work}")
        out = run_unit(args)
        if out.get("dry"):
            log(f"실행할 명령(dry-run)\t{out['cmd']}"); return 0
        prs = json.loads(sh("gh pr list --state all --limit 1 --json number,state,title").stdout or "[]")
        last_pr = f"#{prs[0]['number']} {prs[0]['state']}" if prs else "-"
        log(f"끝\t{work}\tPR {last_pr}\t종료 코드 {out.get('code')}\t{out.get('subtype')}\t비용 {out.get('total_cost_usd')}\t{str(out.get('result'))[:300]!r}")
        reason = failure_reason(out)
        if reason == "사용량 한도":
            record_stop(reason, state()); return 1
        if reason:
            if reason == last_fail:
                record_stop(f"같은 이유로 2회 연속 실패: {reason}", state()); return 1
            last_fail = reason
        else:
            last_fail = None
    log(f"끝남\t최대 단위 수 {n} 도달")
    return 0

def selftest():
    """가짜 상태로 멈춤 판정을 시험"""
    empty = {"issues": [], "prs": [], "tasks": []}
    assert next_work(empty) is None
    assert next_work({"issues": [{"number": 30, "title": "b"}, {"number": 25, "title": "a"}], "prs": [{"number": 1, "title": "p"}], "tasks": ["t"]}) == "요청 이슈 #25 a"
    assert next_work({"issues": [], "prs": [{"number": 9, "title": "p", "body": ""}], "tasks": ["t"]}).startswith("열린 PR #9")
    assert next_work({"issues": [], "prs": [], "tasks": ["5장 개정"]}) == "작업 목록: 5장 개정"
    assert stop_mark({"prs": [{"number": 9, "body": "멈춤: editor 병합 불가 3회\n..."}]}).startswith("PR #9에 멈춤 표시")
    assert handoff_tasks("## 작업 목록\n- [x] a\n- [ ] b\n- [ ] c\n\n## 진행 기록\n") == ["b", "c"]
    assert failure_reason({"code": 1, "result": "Claude usage limit reached"}) == "사용량 한도"
    assert failure_reason({"code": 1, "result": "x", "subtype": "error_max_turns"}) == "실행 오류(error_max_turns)"
    assert failure_reason({"code": 0, "result": "ok", "is_error": False}) is None
    # 할 일 없음이면 바로 멈추고 이유를 로그에 남김(기록할 변경이 없어 커밋하지 않음)
    before = os.path.getsize(LOG) if os.path.exists(LOG) else 0
    record_stop("할 일 없음(selftest)", empty)
    assert os.path.getsize(LOG) > before
    print("selftest 통과")
    return 0

if __name__ == "__main__":
    sys.exit(main())
