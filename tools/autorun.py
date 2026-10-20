"""한 단위마다 새 세션으로 /next를 반복 실행한다(작가 요청 이슈 #22).

사용: python tools/autorun.py [--once] [--max N] [--max-turns N] [--max-budget-usd X] [--unit-timeout M] [--dry-run] [--selftest]
  --once            한 단위만 실행
  --max N           최대 단위 수(기본 20)
  --max-turns N     단위마다 claude -p의 턴 상한(기본 제한 없음)
  --max-budget-usd X 단위마다 비용 상한(기본 제한 없음)
  --unit-timeout M  단위마다 시간 상한(분, 기본 120). 넘으면 세션을 끝내고 실행 오류(시간 초과)로 봄
  --dry-run         상태만 확인하고 실행할 명령을 보여 줌(claude를 실행하지 않음)
  --selftest        멈춤 조건 판정과 멈춤 기록 시험(가짜 상태와 임시 저장소로)

멈춤 조건
  1. 열린 요청 이슈, 열린 PR, HANDOFF 작업 목록의 빈 항목이 모두 없음(할 일 없음)
  2. 열린 PR 설명 맨 위에 "멈춤:"이 있음(/next가 editor "병합 불가" 3회 등으로 적음). 이미 기록된 멈춤이라 다시 적지 않음
  3. 같은 이유의 실패가 2회 연속: 실행 오류, 검사 실패(.claude/last_check_failed.txt), CI 실패, 진전 없음(단위 전후로 이슈, PR과 그 커밋, 작업 목록이 같음)
  4. 사용량 한도(1회로 멈춤)
멈추면 이유를 HANDOFF.md "## 지금 상태"에 적고 HANDOFF.md만 커밋, push한다(열린 PR이 있으면 그 브랜치와 PR 설명 맨 위에, 없으면 새 브랜치와 초안 PR). 작업 트리에 커밋하지 않은 변경이 있거나 브랜치 이동이 실패하면 기록하지 않고 로그와 화면에만 남긴다. main에는 커밋하지 않는다. 할 일이 없어서 멈출 때는 기록할 변경이 없으므로 로그와 화면에만 남긴다.
다시 시작: 멈춤 이유를 처리하고 PR 설명 맨 위 "멈춤:" 줄을 지운 뒤(autorun 멈춤 기록 PR이면 닫은 뒤) 다시 실행한다.
단위마다 시작, 끝, 작업, PR 번호, 결과를 logs/autorun.log에 남긴다(.gitignore).
"""
import argparse, datetime, json, os, re, subprocess, sys, tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG = os.path.join(ROOT, "logs", "autorun.log")
CO_AUTHOR = "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"

def sh(cmd, check=False):
    # 목록은 셸 없이 실행(인용과 줄바꿈 문제 없음). 문자열은 셸로 실행하며, Windows에서는 cmd.exe라 Git Bash의 "/next" 경로 변환이 없음
    # stdin을 닫아 "no stdin data" 대기를 없앰
    r = subprocess.run(cmd, shell=isinstance(cmd, str), cwd=ROOT, capture_output=True, text=True, encoding="utf-8", errors="replace", stdin=subprocess.DEVNULL)
    if check and r.returncode != 0:
        raise RuntimeError(f"{cmd if isinstance(cmd, str) else ' '.join(cmd)}: {r.stderr.strip()}")
    return r

def gh(*a):
    return sh(["gh", *a], True)

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
    """열린 요청 이슈, 열린 PR(커밋과 CI 결과 포함), HANDOFF 빈 항목"""
    issues = json.loads(sh("gh issue list --label request --state open --json number,title", True).stdout or "[]")
    prs = json.loads(sh("gh pr list --json number,title,isDraft,headRefName,headRefOid,body,statusCheckRollup", True).stdout or "[]")
    sh("git fetch -q origin main")
    text = sh("git show origin/main:HANDOFF.md").stdout
    return {"issues": issues, "prs": prs, "tasks": handoff_tasks(text)}

def first_pr(st):
    return sorted(st["prs"], key=lambda x: x["number"])[0] if st["prs"] else None

def next_work(st):
    """/next가 고를 작업(1 요청 이슈의 가장 오래된 것, 2 열린 PR, 3 작업 목록 첫 항목)"""
    if st["issues"]:
        i = sorted(st["issues"], key=lambda x: x["number"])[0]
        return f"요청 이슈 #{i['number']} {i['title']}"
    if st["prs"]:
        p = first_pr(st)
        return f"열린 PR #{p['number']} {p['title']}"
    if st["tasks"]:
        return f"작업 목록: {st['tasks'][0]}"
    return None

def stop_mark(st):
    """/next나 이전 실행이 남긴 멈춤 표시(열린 PR 설명 맨 위)"""
    for p in st["prs"]:
        if (p.get("body") or "").lstrip().startswith("멈춤:"):
            return f"PR #{p['number']}에 멈춤 표시: " + p["body"].lstrip().splitlines()[0][3:].strip()
    return None

def snapshot(st):
    """진전 판정용: 이슈 번호, PR 번호와 head 커밋, 작업 목록"""
    return json.dumps([sorted(i["number"] for i in st["issues"]), sorted((p["number"], p.get("headRefOid")) for p in st["prs"]), st["tasks"]])

def ci_failure(st):
    """작업 대상 PR(가장 오래된 열린 PR)의 실패한 CI 검사 이름"""
    p = first_pr(st)
    bad = sorted(c.get("name") or c.get("context") or "?" for c in ((p or {}).get("statusCheckRollup") or [])
                 if (c.get("conclusion") or c.get("state") or "").upper() in ("FAILURE", "ERROR", "TIMED_OUT", "CANCELLED"))
    return f"CI 실패(PR #{p['number']}: {', '.join(bad)})" if bad else None

def check_failure():
    """종료 훅이 남긴 검사 실패(.claude/last_check_failed.txt)의 첫 줄"""
    p = os.path.join(ROOT, ".claude", "last_check_failed.txt")
    if not os.path.exists(p):
        return None
    first = next((l.strip() for l in open(p, encoding="utf-8", errors="replace") if l.strip()), "")
    return f"검사 실패({first[:80]})"

def record_stop(reason, st, dry=False):
    """멈춘 이유를 HANDOFF.md 맨 위 '## 지금 상태'에 적고 커밋, push. 열린 PR이 있으면 그 브랜치와 설명에도"""
    log(f"멈춤\t{reason}")
    if reason.startswith("할 일 없음") or dry:
        return
    try:
        write_stop(reason, st)
    except RuntimeError as e:
        log(f"멈춤 기록 실패\t{e}")

def write_stop(reason, st):
    if sh(["git", "status", "--porcelain", "--untracked-files=no"], True).stdout.strip():
        raise RuntimeError("작업 트리에 커밋하지 않은 변경이 있어 기록하지 않음(git status로 확인)")
    pr = first_pr(st)
    if pr:
        br = pr["headRefName"]
        sh(["git", "fetch", "-q", "origin", br], True); sh(["git", "switch", br], True); sh(["git", "pull", "-q", "--ff-only", "origin", br], True)
    else:
        br = "autorun-stop-" + datetime.datetime.now().strftime("%Y%m%d-%H%M")
        sh(["git", "switch", "main"], True); sh(["git", "pull", "-q", "--ff-only", "origin", "main"], True); sh(["git", "switch", "-c", br], True)
    cur = sh(["git", "branch", "--show-current"], True).stdout.strip()
    if cur != br or cur == "main":
        raise RuntimeError(f"현재 브랜치가 {cur!r}라 기록하지 않음(기대 {br!r})")
    # newline=""로 원래 줄 끝을 그대로 둠(Windows에서 파일 전체가 CRLF로 바뀌지 않게)
    p = os.path.join(ROOT, "HANDOFF.md"); t = open(p, encoding="utf-8", newline="").read()
    m = re.search(r"## 지금 상태(\r?\n)", t)
    if not m:
        raise RuntimeError('HANDOFF.md에 "## 지금 상태"가 없음')
    open(p, "w", encoding="utf-8", newline="").write(t[:m.end()] + f"- 멈춤(autorun, {now()}): {reason}{m.group(1)}" + t[m.end():])
    sh(["git", "add", "HANDOFF.md"], True)
    sh(["git", "commit", "-q", "-m", f"autorun 멈춤 기록: {reason}\n\n{CO_AUTHOR}"], True)
    sh(["git", "push", "-q", "-u", "origin", br], True)
    tmp = os.path.join(os.path.dirname(LOG), "pr_body.md"); os.makedirs(os.path.dirname(tmp), exist_ok=True)
    if pr:
        open(tmp, "w", encoding="utf-8").write(f"멈춤: {reason}\n\n" + (pr.get("body") or ""))
        gh("pr", "edit", str(pr["number"]), "--body-file", tmp)
    else:
        open(tmp, "w", encoding="utf-8").write(f"멈춤: {reason}\n\nautorun이 멈춘 이유를 HANDOFF.md에 기록했습니다.")
        gh("pr", "create", "--draft", "--base", "main", "--head", br, "--title", "autorun 멈춤 기록", "--body-file", tmp)

def run_unit(args):
    cmd = ['claude', '-p', '"/next"', '--permission-mode', 'acceptEdits', '--output-format', 'json']
    if args.max_turns: cmd += ['--max-turns', str(args.max_turns)]
    if args.max_budget_usd: cmd += ['--max-budget-usd', str(args.max_budget_usd)]
    line = " ".join(cmd)
    if args.dry_run:
        return {"cmd": line, "dry": True}
    p = subprocess.Popen(line, shell=True, cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.DEVNULL, text=True, encoding="utf-8", errors="replace")
    try:
        so, se = p.communicate(timeout=args.unit_timeout * 60)
    except subprocess.TimeoutExpired:
        # shell=True라 셸 아래의 claude까지 끝냄
        if os.name == "nt": subprocess.run(["taskkill", "/F", "/T", "/PID", str(p.pid)], capture_output=True)
        else: p.kill()
        so, se = p.communicate()
        return {"cmd": line, "code": p.returncode, "timeout": True, "stderr": (se or "")[-1000:], "result": (so or "")[-2000:]}
    out = {"cmd": line, "code": p.returncode, "stderr": (se or "")[-1000:]}
    try:
        j = json.loads(so)
        out.update({k: j.get(k) for k in ("result", "is_error", "subtype", "total_cost_usd", "session_id", "num_turns")})
    except Exception:
        out["result"] = (so or "")[-2000:]
    return out

def failure_reason(out):
    """실행 결과에서 실패 이유를 뽑음(없으면 None)"""
    if out.get("timeout"):
        return "실행 오류(시간 초과)"
    if out.get("code") not in (0, None) or out.get("is_error"):
        # 한도 문구는 실패한 실행에서만 봄(정상 보고에 "usage limit"이 들어 있어도 멈추지 않게)
        res = str(out.get("result") or "") + " " + str(out.get("stderr") or "")
        if re.search(r"usage limit|rate limit|사용량 한도|limit reached", res, re.I):
            return "사용량 한도"
        sub = out.get("subtype") or f"종료 코드 {out.get('code')}"
        return f"실행 오류({sub})"
    return None

def unit_failure(out, before, after):
    """단위 하나의 실패 이유: 실행 오류, 검사 실패, CI 실패, 진전 없음 순"""
    return failure_reason(out) or check_failure() or ci_failure(after) or ("진전 없음(단위 전후 상태가 같음)" if snapshot(before) == snapshot(after) else None)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--once", action="store_true"); ap.add_argument("--max", type=int, default=20)
    ap.add_argument("--max-turns", type=int); ap.add_argument("--max-budget-usd", type=float)
    ap.add_argument("--unit-timeout", type=int, default=120)
    ap.add_argument("--dry-run", action="store_true"); ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    if args.selftest:
        return selftest()
    last_fail, n = None, (1 if args.once else args.max)
    st = state()
    for k in range(n):
        mark = stop_mark(st)
        if mark:
            log(f"멈춤\t{mark}"); return 1  # 이미 PR에 기록된 멈춤이라 다시 적지 않음
        work = next_work(st)
        if not work:
            record_stop("할 일 없음(열린 요청 이슈, 열린 PR, 작업 목록이 모두 없음)", st); return 0
        log(f"시작\t{k + 1}/{n}\t{work}")
        out = run_unit(args)
        if out.get("dry"):
            log(f"실행할 명령(dry-run)\t{out['cmd']}"); return 0
        before, st = st, state()
        prs = json.loads(sh("gh pr list --state all --limit 1 --json number,state,title").stdout or "[]")
        last_pr = f"#{prs[0]['number']} {prs[0]['state']}" if prs else "-"
        log(f"끝\t{work}\tPR {last_pr}\t종료 코드 {out.get('code')}\t{out.get('subtype')}\t비용 {out.get('total_cost_usd')}\t{str(out.get('result'))[:300]!r}")
        reason = unit_failure(out, before, st)
        if reason == "사용량 한도":
            record_stop(reason, st); return 1
        if reason:
            log(f"실패\t{reason}")
            if reason == last_fail:
                record_stop(f"같은 이유로 2회 연속 실패: {reason}", st); return 1
        last_fail = reason
    log(f"끝남\t최대 단위 수 {n} 도달")
    return 0

def selftest():
    """가짜 상태로 멈춤 판정을, 임시 저장소로 멈춤 기록을 시험(실제 로그, 저장소, GitHub는 건드리지 않음)"""
    global ROOT, LOG, gh
    tmp = tempfile.mkdtemp(prefix="autorun-selftest-")
    LOG = os.path.join(tmp, "logs", "autorun.log")
    empty = {"issues": [], "prs": [], "tasks": []}
    assert next_work(empty) is None
    assert next_work({"issues": [{"number": 30, "title": "b"}, {"number": 25, "title": "a"}], "prs": [{"number": 1, "title": "p"}], "tasks": ["t"]}) == "요청 이슈 #25 a"
    assert next_work({"issues": [], "prs": [{"number": 9, "title": "p", "body": ""}], "tasks": ["t"]}).startswith("열린 PR #9")
    assert next_work({"issues": [], "prs": [], "tasks": ["5장 개정"]}) == "작업 목록: 5장 개정"
    assert stop_mark({"prs": [{"number": 9, "body": "멈춤: editor 병합 불가 3회\n..."}]}).startswith("PR #9에 멈춤 표시")
    assert handoff_tasks("## 작업 목록\n- [x] a\n- [ ] b\n- [ ] c\n\n## 진행 기록\n") == ["b", "c"]
    assert failure_reason({"code": 1, "result": "Claude usage limit reached"}) == "사용량 한도"
    assert failure_reason({"code": 1, "result": "x", "subtype": "error_max_turns"}) == "실행 오류(error_max_turns)"
    assert failure_reason({"code": 1, "timeout": True}) == "실행 오류(시간 초과)"
    assert failure_reason({"code": 0, "result": "ok", "is_error": False}) is None
    assert failure_reason({"code": 0, "result": "보고: usage limit 판정 수정", "is_error": False}) is None
    # 진전 없음, CI 실패, 검사 실패
    pr_a = {"number": 9, "headRefOid": "a1", "body": "", "statusCheckRollup": [{"name": "check", "conclusion": "SUCCESS"}]}
    pr_b = dict(pr_a, headRefOid="b2")
    pr_f = dict(pr_b, statusCheckRollup=[{"name": "check", "conclusion": "FAILURE"}])
    s_a, s_b, s_f = ({"issues": [], "prs": [p], "tasks": ["t"]} for p in (pr_a, pr_b, pr_f))
    ok = {"code": 0, "is_error": False}
    ROOT = tmp
    assert unit_failure(ok, s_a, s_a) == "진전 없음(단위 전후 상태가 같음)"
    assert unit_failure(ok, s_a, s_b) is None
    assert unit_failure(ok, s_a, s_f) == "CI 실패(PR #9: check)"
    os.makedirs(os.path.join(tmp, ".claude")); open(os.path.join(tmp, ".claude", "last_check_failed.txt"), "w", encoding="utf-8").write("\ncheck_all 실패: 금칙어\n")
    assert unit_failure(ok, s_a, s_b) == "검사 실패(check_all 실패: 금칙어)"
    os.remove(os.path.join(tmp, ".claude", "last_check_failed.txt"))
    # 할 일 없음이면 바로 멈추고 이유를 로그에 남김(기록할 변경이 없어 커밋하지 않음)
    record_stop("할 일 없음(selftest)", empty)
    assert "할 일 없음(selftest)" in open(LOG, encoding="utf-8").read()
    # 멈춤 기록: 임시 원격과 복제본에서 main이 아닌 PR 브랜치에 HANDOFF.md만 커밋, push
    remote, work = os.path.join(tmp, "remote.git"), os.path.join(tmp, "work")
    calls = []; gh = lambda *a: calls.append(a)
    sh(["git", "init", "-q", "--bare", remote], True); sh(["git", "clone", "-q", remote, work], True)  # cwd는 있는 폴더(tmp)여야 함
    ROOT = work
    for c in (["config", "user.name", "selftest"], ["config", "user.email", "selftest@example.com"], ["symbolic-ref", "HEAD", "refs/heads/main"]):
        sh(["git", *c], True)
    open(os.path.join(ROOT, "HANDOFF.md"), "w", encoding="utf-8").write("# 인계\n\n## 지금 상태\n- 이전\n")
    sh(["git", "add", "HANDOFF.md"], True); sh(["git", "commit", "-q", "-m", "init"], True); sh(["git", "push", "-q", "-u", "origin", "main"], True)
    sh(["git", "switch", "-q", "-c", "work"], True); sh(["git", "push", "-q", "-u", "origin", "work"], True); sh(["git", "switch", "-q", "main"], True)
    st = {"issues": [], "prs": [{"number": 7, "headRefName": "work", "body": "본문"}], "tasks": []}
    open(os.path.join(ROOT, "HANDOFF.md"), "a", encoding="utf-8").write("- 미완성\n")  # 작업 트리가 더러우면 기록하지 않음
    record_stop("시험 이유 \"따옴표\" & 기호", st)
    assert not calls and "멈춤 기록 실패" in open(LOG, encoding="utf-8").read()
    sh(["git", "checkout", "--", "HANDOFF.md"], True)
    record_stop("시험 이유 \"따옴표\" & 기호", st)
    assert sh(["git", "branch", "--show-current"]).stdout.strip() == "work"
    assert "멈춤(autorun" in sh(["git", "show", "origin/work:HANDOFF.md"], True).stdout
    assert "멈춤" not in sh(["git", "show", "origin/main:HANDOFF.md"], True).stdout
    assert sh(["git", "show", "--numstat", "--format=", "HEAD"], True).stdout.split() == ["1", "0", "HANDOFF.md"]  # HANDOFF.md 한 줄만 추가
    assert calls and calls[0][:3] == ("pr", "edit", "7")
    assert open(calls[0][-1], encoding="utf-8").read().startswith('멈춤: 시험 이유 "따옴표" & 기호\n\n본문')
    print("selftest 통과")
    return 0

if __name__ == "__main__":
    sys.exit(main())
