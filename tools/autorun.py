"""한 단위마다 새 세션으로 /next를 반복 실행한다(작가 요청 이슈 #22, 자가 복구와 상태 알림 이슈 #34).

사용: python tools/autorun.py [--once] [--max N] [--max-turns N] [--max-budget-usd X] [--unit-timeout M]
                              [--max-wait-hours H] [--retry-base S] [--apply-only] [--dry-run] [--selftest]
  --once             한 단위만 실행
  --max N            최대 단위 수(기본 20)
  --max-turns N      단위마다 claude -p의 턴 상한(기본 제한 없음)
  --max-budget-usd X 단위마다 비용 상한(기본 제한 없음)
  --unit-timeout M   단위마다 시간 상한(분, 기본 120). 넘으면 세션을 끝내고 실행 오류(시간 초과)로 봄
  --max-wait-hours H 사용량 한도가 풀리기를 기다리는 최대 시간(기본 6)
  --retry-base S     일시 오류 재시도 첫 간격(초, 기본 60, 두 배씩 늘려 3회)
  --apply-only       docs/staged-claude/의 설정 반영만 하고 끝냄(단위 실행 없음)
  --dry-run          상태만 확인하고 실행할 명령을 보여 줌(claude 실행, 상태 이슈, 설정 반영, 잠금 없음)
  --selftest         판정, 잠금, 설정 반영, 상태 알림, 다시 시작 인자, 멈춤 기록 시험(임시 저장소와 가짜 gh로)
  (--last-fail, --restarts는 자기 다시 시작 때 내부에서 넘기는 값)

설정 반영(docs/staged-claude/ → .claude/)
  에이전트가 .claude/를 바꿔야 할 때는 새 판을 docs/staged-claude/의 같은 경로(agents/<이름>.md, commands/<이름>.md,
  settings.json)에 두고 보통 PR로 editor 검수를 거쳐 병합한다. autorun은 시작할 때와 단위가 끝날 때마다 origin/main에
  그 폴더가 있으면 임시 작업 폴더(git worktree)에서 파일을 복사하고(허용 경로만), 폴더를 지우고, check_all 통과 뒤
  PR을 만들어 CI 통과(최대 20분) 후 병합한다. settings.json은 JSON 검사와 함께, 권한이 넓어지는 변경(deny나 ask 항목 삭제,
  allow 항목 추가, 훅이나 기본 모드 변경)이면 반영하지 않고 작가에게 알린다. 실패하면 되돌리고 작가에게 알린다.
  반영 PR은 editor 검수를 거친 파일의 기계적 복사라 editor 없이 병합한다(D-119).

자기 다시 시작
  단위가 끝난 뒤 작업 트리가 깨끗하면 main을 받아, 디스크의 tools/autorun.py가 실행 중인 판과 다르면 새 판을 자식
  프로세스로 실행하고(잠금을 넘겨줌, 남은 단위 수와 직전 실패 이유를 넘김, 다시 시작은 최대 3회) 그 종료 코드로 끝낸다.

상태 알림
  GitHub 이슈 "자동 실행 상태"(라벨 status, 없으면 만듦)에 단위마다 댓글(시각, 단위, 작업, PR, 결과, editor 결론, 비용).
  작가 조치가 필요한 멈춤일 때만 @seoulkorea-dev와 "작가가 할 일" 한 줄을 넣는다. GitHub는 자기 계정이 쓴 자기 언급에는
  알림을 보내지 않으므로, 환경 변수 AUTORUN_GH_TOKEN(별도 계정의 토큰)이 있으면 상태 댓글을 그 토큰으로 쓴다.

멈춤과 처리(판정 순서: 사용량 한도 → 단위 시간 초과 → 일시 오류 → 그 밖)
  사용량 한도: 출력의 재개 시각(못 읽으면 60분)까지 기다렸다가 같은 단위를 다시 실행, --max-wait-hours를 넘으면 멈춤
  일시 오류(네트워크, 연결, 과부하, 문맥 있는 5xx): 같은 단위를 3회까지 간격을 늘려 재시도, 넘으면 멈춤
  PR 설명 맨 위 "멈춤:"(굵게 쓴 "**멈춤:" 포함): 멈춤(이미 기록됨)
  같은 이유 2회 연속(단위 시간 초과, 검사 실패, CI 실패, 진전 없음): 멈춤. 재시도와 대기는 세지 않음
  그 밖의 실행 오류: 바로 멈춤
  할 일 없음(열린 요청 이슈, 열린 PR, 작업 목록이 모두 없음): 끝냄
  멈추면 이유를 HANDOFF.md "## 지금 상태"와 열린 PR 설명 맨 위에 적고(작업 트리가 깨끗할 때만, main에는 커밋하지 않음)
  상태 이슈에 작가 알림을 남긴다.

한 번에 하나만 실행
  logs/autorun.lock(pid, 시작, 마지막 갱신)을 배타 생성한다. 살아 있는 다른 프로세스의 잠금이 최근 갱신(단위 시간 상한 + 60분 안)
  이면 실행하지 않고, 아니면 낡은 잠금으로 지운다. 단위 시작과 끝, 대기 중 5분마다 갱신한다. 단위 세션은 "/next unit"으로 띄우며,
  /next는 인자가 unit이 아니고 잠금이 최근 갱신이면 "자동 실행 중"이라고만 답한다.
단위마다 시작, 끝, 작업, PR 번호, 결과를 logs/autorun.log에 남긴다(.gitignore).
"""
import argparse, atexit, datetime, hashlib, json, os, re, shutil, subprocess, sys, tempfile, time
from types import SimpleNamespace

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG = os.path.join(ROOT, "logs", "autorun.log")
LOCK = os.path.join(ROOT, "logs", "autorun.lock")
CO_AUTHOR = "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
STAGE = "docs/staged-claude"
CHECK_CMD = [sys.executable, "tools/check_all.py"]
CI_LIMIT_SEC = 20 * 60
STATUS_TITLE, STATUS_LABEL, AUTHOR = "자동 실행 상태", "status", "@seoulkorea-dev"
LIMIT_RE = re.compile(r"usage limit|rate limit|session limit|hit your [^\n.]*limit|limit reached|사용량 한도", re.I)
TRANSIENT_RE = re.compile(r"timed? ?out|ETIMEDOUT|ECONNRESET|ECONNREFUSED|ENOTFOUND|EAI_AGAIN|socket hang up|network error|"
                          r"connection error|fetch failed|overloaded|API Error:\s*5\d\d|HTTP\s*5\d\d|"
                          r"\b5\d\d\s+(?:Internal Server Error|Bad Gateway|Service Unavailable|Gateway Timeout)|\b529\b", re.I)
RESET_RE = re.compile(r"resets?\s+(?:at\s+)?(\d{1,2})(?::(\d{2}))?\s*([ap]m)?", re.I)
OWN_HASH = hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest()
SLEEP = time.sleep

def sh(cmd, check=False, cwd=None, timeout=None, env=None):
    # 목록은 셸 없이 실행(인용과 줄바꿈 문제 없음). 문자열은 셸로 실행하며, Windows에서는 cmd.exe라 Git Bash의 "/next" 경로 변환이 없음
    # stdin을 닫아 "no stdin data" 대기를 없앰
    try:
        r = subprocess.run(cmd, shell=isinstance(cmd, str), cwd=cwd or ROOT, capture_output=True, text=True, encoding="utf-8",
                           errors="replace", stdin=subprocess.DEVNULL, timeout=timeout, env=env)
    except subprocess.TimeoutExpired as e:
        r = SimpleNamespace(returncode=124, stdout=str(e.stdout or ""), stderr="시간 초과")
    if check and r.returncode != 0:
        raise RuntimeError(f"{cmd if isinstance(cmd, str) else ' '.join(cmd)}: {r.stderr.strip()}")
    return r

def gh(*a, check=True, cwd=None, timeout=None, token=None):
    return sh(["gh", *a], check, cwd, timeout, dict(os.environ, GH_TOKEN=token) if token else None)

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
    issues = json.loads(gh("issue", "list", "--label", "request", "--state", "open", "--json", "number,title").stdout or "[]")
    prs = json.loads(gh("pr", "list", "--json", "number,title,isDraft,headRefName,headRefOid,body,statusCheckRollup").stdout or "[]")
    sh(["git", "fetch", "-q", "origin", "main"])
    text = sh(["git", "show", "origin/main:HANDOFF.md"]).stdout
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
    """/next나 이전 실행이 남긴 멈춤 표시(열린 PR 설명 맨 위, 굵게 쓴 "**멈춤:"도 인정. PR #33에서 놓친 사례)"""
    for p in st["prs"]:
        m = re.match(r"\s*\**\s*멈춤\s*:\s*\**\s*(.*)", p.get("body") or "")
        if m:
            return f"PR #{p['number']}에 멈춤 표시: " + m.group(1).strip().strip("*").strip()
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

# ---------------- 잠금 ----------------
def pid_alive(pid):
    if not pid or pid <= 0:
        return False
    if os.name == "nt":
        r = subprocess.run(["tasklist", "/FI", f"PID eq {pid}", "/NH"], capture_output=True, text=True, errors="replace")
        return re.search(rf"\b{pid}\b", r.stdout) is not None
    try:
        os.kill(pid, 0); return True
    except OSError:
        return False

def read_lock():
    try:
        return json.load(open(LOCK, encoding="utf-8"))
    except Exception:
        return None

def write_lock(info):
    tmp = LOCK + ".tmp"
    json.dump(info, open(tmp, "w", encoding="utf-8")); os.replace(tmp, LOCK)

def lock_fresh(info, fresh_min):
    try:
        t = datetime.datetime.strptime(info.get("updated") or info.get("start"), "%Y-%m-%d %H:%M:%S")
    except Exception:
        return False
    return (datetime.datetime.now() - t).total_seconds() < fresh_min * 60

def acquire_lock(fresh_min=180, inherit_pid=None):
    """배타 생성. 살아 있고 최근 갱신된 다른 프로세스의 잠금이면 False, 낡은 잠금은 지우고 다시. inherit_pid는 다시 시작한 부모"""
    os.makedirs(os.path.dirname(LOCK), exist_ok=True)
    for _ in range(2):
        try:
            fd = os.open(LOCK, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
            with os.fdopen(fd, "w", encoding="utf-8") as f:
                json.dump({"pid": os.getpid(), "start": now(), "updated": now()}, f)
            return True
        except FileExistsError:
            info = read_lock() or {}
            pid = int(info.get("pid") or 0)
            if pid == os.getpid() or (inherit_pid and pid == inherit_pid):
                info.update(pid=os.getpid(), updated=now()); write_lock(info); return True
            if pid_alive(pid) and lock_fresh(info, fresh_min):
                return False
            try:
                os.remove(LOCK)
            except OSError:
                pass
    return False

def touch_lock():
    info = read_lock()
    if info and info.get("pid") == os.getpid():
        info["updated"] = now(); write_lock(info)

def release_lock():
    info = read_lock()
    if info and info.get("pid") == os.getpid():
        try: os.remove(LOCK)
        except OSError: pass

def wait(seconds):
    """기다리는 동안 5분마다 잠금 갱신"""
    left = seconds
    while left > 0:
        step = min(300, left); SLEEP(step); left -= step; touch_lock()

# ---------------- 상태 알림 ----------------
_status = {"no": None}

def status_issue():
    """"자동 실행 상태" 이슈 번호(없으면 라벨과 이슈를 만듦)"""
    if _status["no"]:
        return _status["no"]
    tok = os.environ.get("AUTORUN_GH_TOKEN")
    for i in json.loads(gh("issue", "list", "--label", STATUS_LABEL, "--state", "open", "--json", "number,title", token=tok).stdout or "[]"):
        if i["title"] == STATUS_TITLE:
            _status["no"] = i["number"]; return i["number"]
    gh("label", "create", STATUS_LABEL, "--color", "0284c7", "--description", "자동 실행 상태 알림", check=False, token=tok)
    r = gh("issue", "create", "--title", STATUS_TITLE, "--label", STATUS_LABEL, "--body",
           "tools/autorun.py가 단위마다 결과를 댓글로 남기는 이슈입니다(이슈 #34). 작가 조치가 필요한 멈춤에만 작가를 부릅니다.", token=tok)
    _status["no"] = int(re.search(r"/issues/(\d+)", r.stdout).group(1))
    return _status["no"]

def notify(text, todo=None):
    """상태 이슈에 댓글. todo가 있으면 작가를 부르고 작가가 할 일 한 줄. 실패해도 실행은 계속(로그에만)"""
    body = text + (f"\n\n{AUTHOR} 작가가 할 일: {todo}" if todo else "")
    try:
        n = status_issue()
        tmp = os.path.join(os.path.dirname(LOG), "status_body.md"); os.makedirs(os.path.dirname(tmp), exist_ok=True)
        open(tmp, "w", encoding="utf-8").write(body)
        gh("issue", "comment", str(n), "--body-file", tmp, token=os.environ.get("AUTORUN_GH_TOKEN"))
    except Exception as e:
        log(f"상태 알림 실패\t{e}")
    return body

def editor_verdict(text):
    t = str(text or "")
    return "병합 불가" if "병합 불가" in t else "병합 가능" if "병합 가능" in t else "-"

def unit_row(k, n, work, pr, result, out):
    cost = out.get("total_cost_usd")
    return ("| 시각 | 단위 | 작업 | PR | 결과 | editor | 비용 |\n|---|---|---|---|---|---|---|\n"
            f"| {now()} | {k}/{n} | {work} | {pr} | {result} | {editor_verdict(out.get('result'))} | {('%.2f달러' % cost) if cost else '-'} |")

# ---------------- 멈춤 분류 ----------------
def classify(out):
    """실패 종류(판정 순서: 한도 → 단위 시간 초과 → 일시 오류 → 그 밖). None은 실패 아님"""
    failed = out.get("timeout") or out.get("code") not in (0, None) or out.get("is_error")
    if not failed:
        return None
    # 한도와 일시 오류 문구는 실패한 실행에서만 봄(정상 보고에 그 말이 들어 있어도 멈추지 않게)
    res = str(out.get("result") or "") + " " + str(out.get("stderr") or "")
    if LIMIT_RE.search(res):
        return "limit"
    if out.get("timeout"):
        return "timeout"
    if TRANSIENT_RE.search(res):
        return "transient"
    return "error"

def failure_reason(out):
    """실행 결과에서 실패 이유를 뽑음(없으면 None)"""
    kind = classify(out)
    if kind is None:
        return None
    if kind == "timeout":
        return "실행 오류(시간 초과)"
    if kind == "limit":
        return "사용량 한도"
    res = re.sub(r"\s+", " ", str(out.get("result") or out.get("stderr") or "")).strip()
    if kind == "transient":
        return f"일시 오류({res[:80]})"
    sub = out.get("subtype") or f"종료 코드 {out.get('code')}"
    return f"실행 오류({sub}: {res[:80]})" if res else f"실행 오류({sub})"

def reset_wait(text, base=None, default_min=60):
    """한도 메시지의 재개 시각(예: "resets 7:30pm")까지 남은 초 + 2분. 이 컴퓨터의 현지 시각으로 읽고, 지났으면 다음 날. 못 읽으면 default_min분"""
    base = base or datetime.datetime.now()
    m = RESET_RE.search(str(text or ""))
    if not m:
        return default_min * 60
    h, mi, ap = int(m.group(1)), int(m.group(2) or 0), (m.group(3) or "").lower()
    if ap == "pm" and h < 12: h += 12
    if ap == "am" and h == 12: h = 0
    if h > 23 or mi > 59:
        return default_min * 60
    target = base.replace(hour=h, minute=mi, second=0, microsecond=0)
    if target <= base:
        target += datetime.timedelta(days=1)
    return int((target - base).total_seconds()) + 120

def unit_failure(out, before, after):
    """단위 하나의 실패 이유: 실행 오류, 검사 실패, CI 실패, 진전 없음 순"""
    return failure_reason(out) or check_failure() or ci_failure(after) or ("진전 없음(단위 전후 상태가 같음)" if snapshot(before) == snapshot(after) else None)

# ---------------- 멈춤 기록 ----------------
def record_stop(reason, st, dry=False, todo=None):
    """멈춘 이유를 HANDOFF.md 맨 위 '## 지금 상태'에 적고 커밋, push. 열린 PR이 있으면 그 브랜치와 설명에도. todo가 있으면 상태 이슈에 작가 알림"""
    log(f"멈춤\t{reason}")
    if dry:
        return
    if todo:
        notify(f"멈춤: {reason}", todo)
    if reason.startswith("할 일 없음"):
        return
    try:
        write_stop(reason, st)
    except RuntimeError as e:
        log(f"멈춤 기록 실패\t{e}")

def dirty(cwd=None):
    return bool(sh(["git", "status", "--porcelain", "--untracked-files=no"], True, cwd).stdout.strip())

def write_stop(reason, st):
    if dirty():
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

# ---------------- 설정 반영 ----------------
class ApplyError(Exception):
    def __init__(self, msg, todo="docs/staged-claude/의 파일을 확인해 고치거나 지운 뒤 다시 실행"):
        super().__init__(msg); self.todo = todo

def staged_plan(root):
    """docs/staged-claude/의 (원본, 대상) 목록과 허용 밖 경로. 폴더가 없으면 (None, [])"""
    base = os.path.join(root, *STAGE.split("/"))
    if not os.path.isdir(base):
        return None, []
    plan, bad = [], []
    for dp, _, fn in os.walk(base):
        for f in sorted(fn):
            src = os.path.join(dp, f); rel = os.path.relpath(src, base).replace("\\", "/"); parts = rel.split("/")
            if rel == "README.md":
                continue  # 폴더 설명은 반영하지 않음
            if rel == "settings.json":
                plan.append((src, ".claude/settings.json"))
            elif len(parts) == 2 and parts[0] in ("agents", "commands") and parts[1].endswith(".md"):
                plan.append((src, ".claude/" + rel))
            else:
                bad.append(rel)
    return plan, bad

def permission_widening(cur, new):
    """settings.json에서 권한이 넓어지는 변경: deny나 ask 삭제, allow 추가, 훅이나 기본 모드 변경"""
    cp, np = cur.get("permissions") or {}, new.get("permissions") or {}
    out = []
    for key, sign in (("deny", "-"), ("ask", "-"), ("allow", "+")):
        a, b = set(cp.get(key) or []), set(np.get(key) or [])
        diff = sorted(a - b) if sign == "-" else sorted(b - a)
        if diff:
            out.append(f"{key} {'삭제' if sign == '-' else '추가'}: {', '.join(diff)}")
    if cur.get("hooks") != new.get("hooks"):
        out.append("hooks 변경")
    if cp.get("defaultMode") != np.get("defaultMode"):
        out.append(f"defaultMode 변경({cp.get('defaultMode')} → {np.get('defaultMode')})")
    return "; ".join(out)

def wait_ci(pr, cwd):
    """PR의 CI가 끝날 때까지 기다림(최대 20분). 검사가 아직 없으면 잠시 뒤 다시"""
    deadline = time.monotonic() + CI_LIMIT_SEC
    while time.monotonic() < deadline:
        r = gh("pr", "checks", pr, "--watch", "--interval", "10", check=False, cwd=cwd, timeout=max(1, int(deadline - time.monotonic())))
        if "no checks reported" in (r.stdout + r.stderr).lower():
            SLEEP(10); continue
        return r.returncode == 0
    return False

def apply_staged():
    """origin/main에 docs/staged-claude/가 있으면 임시 작업 폴더에서 .claude/에 반영. 반환: None(할 것 없음), "반영", 실패 이유"""
    sh(["git", "fetch", "-q", "origin", "main"])
    if sh(["git", "cat-file", "-e", f"origin/main:{STAGE}"]).returncode != 0:
        return None
    wt = os.path.join(tempfile.mkdtemp(prefix="autorun-apply-"), "wt")
    br = "autorun-apply-" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    pr, merged, pushed = None, False, False
    try:
        sh(["git", "worktree", "add", "-q", "-b", br, wt, "origin/main"], True)
        plan, bad = staged_plan(wt)
        if bad:
            raise ApplyError("허용 밖 경로: " + ", ".join(bad))
        if not plan:
            raise ApplyError("반영할 파일 없음")
        for src, dst in plan:
            if dst.endswith("settings.json"):
                try:
                    new = json.load(open(src, encoding="utf-8"))
                except ValueError as e:
                    raise ApplyError(f"settings.json이 JSON이 아님({e})")
                cur_p = os.path.join(wt, ".claude", "settings.json")
                cur = json.load(open(cur_p, encoding="utf-8")) if os.path.exists(cur_p) else {}
                widen = permission_widening(cur, new)
                if widen:
                    raise ApplyError("settings.json 권한 확대라 자동 반영하지 않음: " + widen,
                                     "docs/staged-claude/settings.json의 권한 변경을 직접 확인해 .claude/settings.json에 반영하고 그 파일을 지움")
        for src, dst in plan:
            d = os.path.join(wt, *dst.split("/"))
            os.makedirs(os.path.dirname(d), exist_ok=True); shutil.copyfile(src, d)
        sh(["git", "rm", "-r", "-q", STAGE], True, wt)
        r = sh(CHECK_CMD, cwd=wt)
        if r.returncode != 0:
            raise ApplyError("check_all 실패: " + (r.stdout + r.stderr).strip()[-300:])
        sh(["git", "add", "--", *[dst for _, dst in plan]], True, wt)
        stat = sh(["git", "diff", "--cached", "--stat"], True, wt).stdout.strip()
        files = ", ".join(dst for _, dst in plan)
        sh(["git", "commit", "-q", "-m", f"설정 반영(docs/staged-claude → .claude): {files}\n\n{CO_AUTHOR}"], True, wt)
        sh(["git", "push", "-q", "-u", "origin", br], True, wt); pushed = True
        tmp = os.path.join(os.path.dirname(LOG), "apply_body.md"); os.makedirs(os.path.dirname(tmp), exist_ok=True)
        open(tmp, "w", encoding="utf-8").write(
            "tools/autorun.py가 main의 docs/staged-claude/를 .claude/에 반영했습니다(이슈 #34, D-119: editor 검수를 거친 파일의 기계적 복사).\n\n"
            f"- 반영: {files}\n- docs/staged-claude/ 삭제(이 PR 안에서)\n- check_all 통과\n\n```\n{stat}\n```")
        r = gh("pr", "create", "--base", "main", "--head", br, "--title", "설정 반영(docs/staged-claude → .claude)", "--body-file", tmp, cwd=wt)
        pr = re.search(r"/pull/(\d+)", r.stdout).group(1)
        if not wait_ci(pr, wt):
            raise ApplyError(f"CI 실패 또는 20분 초과(PR #{pr})", "반영 PR의 CI 결과를 확인하고 docs/staged-claude/를 고친 뒤 다시 실행")
        gh("pr", "merge", pr, "--merge", cwd=wt)
        merged = True
        log(f"설정 반영\tPR #{pr}\t{files}")
        notify(f"설정 반영: PR #{pr} 병합({files})")
        return "반영"
    except Exception as e:
        todo = getattr(e, "todo", "logs/autorun.log를 확인하고 docs/staged-claude/를 고친 뒤 다시 실행")
        if merged:
            reason = f"설정 반영 병합 뒤 단계 실패(되돌리지 않음): {e}"
        else:
            if pr:
                gh("pr", "close", pr, check=False, cwd=wt)
            reason = f"설정 반영 실패: {e}"
        log(reason)
        notify(reason, todo)
        return reason
    finally:
        sh(["git", "worktree", "remove", "--force", wt])
        sh(["git", "worktree", "prune"])
        sh(["git", "branch", "-q", "-D", br])
        if pushed:
            sh(["git", "push", "-q", "origin", "--delete", br])

# ---------------- 자기 다시 시작 ----------------
def sync_main():
    """작업 트리가 깨끗하면 main으로 옮겨 pull. 깨끗하지 않으면 False"""
    if dirty():
        return False
    sh(["git", "switch", "-q", "main"], True); sh(["git", "pull", "-q", "--ff-only", "origin", "main"], True)
    return True

def disk_hash():
    return hashlib.sha256(open(os.path.join(ROOT, "tools", "autorun.py"), "rb").read()).hexdigest()

def restart_argv(argv, remaining, last_fail, restarts):
    """다시 시작할 인자: --once, --max, --last-fail, --restarts를 빼고 남은 단위 수, 직전 실패, 다시 시작 횟수를 붙임"""
    out, skip = [], False
    for a in argv:
        if skip: skip = False; continue
        if a == "--once": continue
        if a in ("--max", "--last-fail", "--restarts"): skip = True; continue
        if a.startswith(("--max=", "--last-fail=", "--restarts=")): continue
        out.append(a)
    out += ["--max", str(remaining), "--restarts", str(restarts)]
    return out + (["--last-fail", last_fail] if last_fail else [])

def restart(remaining, last_fail, restarts):
    """새 판을 자식 프로세스로 실행하고 그 종료 코드를 돌려줌(잠금은 자식이 넘겨받음). 상한을 넘으면 None"""
    if restarts >= 3:
        notify("다시 시작하지 않음: 다시 시작이 3회를 넘음", "tools/autorun.py 변경이 반복되는지 확인하고 다시 실행")
        return None
    argv = [sys.executable, os.path.join(ROOT, "tools", "autorun.py")] + restart_argv(sys.argv[1:], remaining, last_fail, restarts + 1)
    log(f"다시 시작\ttools/autorun.py가 바뀜, 남은 단위 {remaining}")
    notify(f"다시 시작: tools/autorun.py가 main에서 바뀌어 새 판으로 이어서 실행(남은 단위 {remaining})")
    return subprocess.call(argv, cwd=ROOT, env=dict(os.environ, AUTORUN_PARENT_PID=str(os.getpid())))

# ---------------- 실행 ----------------
def run_unit(args):
    cmd = ['claude', '-p', '"/next unit"', '--permission-mode', 'acceptEdits', '--output-format', 'json']
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

def run_with_recovery(args, work):
    """일시 오류는 간격을 늘려 3회까지 재시도, 사용량 한도는 재개 시각까지 기다렸다가 다시 실행. (결과, 남은 문제) 반환"""
    tries, waited = 0, 0
    while True:
        touch_lock()
        out = run_unit(args)
        touch_lock()
        if out.get("dry"):
            return out, None
        kind = classify(out)
        text = str(out.get("result") or "") + " " + str(out.get("stderr") or "")
        if kind == "transient":
            if tries >= 3:
                return out, ("transient", "일시 오류가 재시도 3회 뒤에도 계속됨: " + failure_reason(out))
            secs = args.retry_base * 2 ** tries; tries += 1
            log(f"재시도\t{tries}/3\t{secs}초 뒤\t{failure_reason(out)}")
            notify(f"재시도 {tries}/3: {work}, {secs}초 뒤({failure_reason(out)})")
            wait(secs); continue
        if kind == "limit":
            secs = reset_wait(text)
            if waited + secs > args.max_wait_hours * 3600:
                return out, ("limit", f"사용량 한도: 재개까지 {secs // 60}분, 최대 대기 {args.max_wait_hours}시간 초과")
            waited += secs
            resume = (datetime.datetime.now() + datetime.timedelta(seconds=secs)).strftime("%m-%d %H:%M")
            log(f"대기\t사용량 한도\t{resume}까지")
            notify(f"대기: 사용량 한도, {resume}에 이어서 진행({work})")
            wait(secs); continue
        return out, None

def loop(args):
    live = not args.dry_run
    if live:
        apply_staged()
    if args.apply_only:
        return 0
    last_fail, n = args.last_fail, (1 if args.once else args.max)
    st = state()
    for k in range(n):
        mark = stop_mark(st)
        if mark:
            log(f"멈춤\t{mark}")  # 이미 PR에 기록된 멈춤이라 다시 적지 않음
            if live: notify(f"멈춤: {mark}", "PR 설명 맨 위의 멈춤 이유를 처리하고 그 줄을 지운 뒤 다시 실행")
            return 1
        work = next_work(st)
        if not work:
            record_stop("할 일 없음(열린 요청 이슈, 열린 PR, 작업 목록이 모두 없음)", st, not live)
            if live: notify("끝남: 할 일 없음(열린 요청 이슈, 열린 PR, 작업 목록이 모두 없음)")
            return 0
        log(f"시작\t{k + 1}/{n}\t{work}")
        out, problem = run_with_recovery(args, work)
        if out.get("dry"):
            log(f"실행할 명령(dry-run)\t{out['cmd']}"); return 0
        before, st = st, state()
        prs = json.loads(gh("pr", "list", "--state", "all", "--limit", "1", "--json", "number,state,title", check=False).stdout or "[]")
        last_pr = f"#{prs[0]['number']} {prs[0]['state']}" if prs else "-"
        log(f"끝\t{work}\tPR {last_pr}\t종료 코드 {out.get('code')}\t{out.get('subtype')}\t비용 {out.get('total_cost_usd')}\t{str(out.get('result'))[:300]!r}")
        if problem:
            kind, reason = problem
            notify(unit_row(k + 1, n, work, last_pr, "멈춤", out))
            record_stop(reason, st, todo="사용량 한도가 풀린 뒤 다시 실행" if kind == "limit" else "네트워크와 서비스 상태를 확인한 뒤 다시 실행")
            return 1
        reason = unit_failure(out, before, st)
        if reason and classify(out) == "error":
            notify(unit_row(k + 1, n, work, last_pr, "멈춤", out))
            record_stop(reason, st, todo="logs/autorun.log와 상태 이슈의 오류 원문을 확인하고 원인을 처리한 뒤 다시 실행")
            return 1
        if reason:
            log(f"실패\t{reason}")
            if reason == last_fail:
                notify(unit_row(k + 1, n, work, last_pr, "멈춤", out))
                record_stop(f"같은 이유로 2회 연속 실패: {reason}", st, todo="같은 실패의 원인(검사, CI, 진전 없음, 시간 초과)을 처리한 뒤 다시 실행")
                return 1
            notify(unit_row(k + 1, n, work, last_pr, f"실패 1회({reason}), 다음 단위 진행", out))
        else:
            notify(unit_row(k + 1, n, work, last_pr, "병합" if "MERGED" in last_pr else "진행", out))
        last_fail = reason
        apply_staged()
        remaining = n - k - 1
        if remaining > 0:
            try:
                synced = sync_main()
            except RuntimeError as e:
                synced = False; log(f"main 받기 실패\t{e}")
            if synced and disk_hash() != OWN_HASH:
                code = restart(remaining, last_fail, args.restarts)
                if code is not None:
                    return code
        st = state()
    log(f"끝남\t최대 단위 수 {n} 도달")
    if live: notify(f"끝남: 최대 단위 수 {n} 도달")
    return 0

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--once", action="store_true"); ap.add_argument("--max", type=int, default=20)
    ap.add_argument("--max-turns", type=int); ap.add_argument("--max-budget-usd", type=float)
    ap.add_argument("--unit-timeout", type=int, default=120)
    ap.add_argument("--max-wait-hours", type=float, default=6); ap.add_argument("--retry-base", type=int, default=60)
    ap.add_argument("--apply-only", action="store_true")
    ap.add_argument("--last-fail", default=None); ap.add_argument("--restarts", type=int, default=0)
    ap.add_argument("--dry-run", action="store_true"); ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    if args.selftest:
        return selftest()
    if not args.dry_run:
        parent = int(os.environ.get("AUTORUN_PARENT_PID") or 0) or None
        if not acquire_lock(args.unit_timeout + 60, parent):
            print("다른 autorun이 실행 중이라 끝냄(logs/autorun.lock)", flush=True); return 2
        atexit.register(release_lock)
    try:
        return loop(args)
    except KeyboardInterrupt:
        log("중단\tCtrl+C"); return 130

# ---------------- 시험 ----------------
def selftest():
    """가짜 상태와 임시 저장소, 가짜 gh로 시험(실제 로그, 저장소, GitHub는 건드리지 않음)"""
    global ROOT, LOG, LOCK, gh, CHECK_CMD, SLEEP, run_unit
    tmp = tempfile.mkdtemp(prefix="autorun-selftest-")
    LOG = os.path.join(tmp, "logs", "autorun.log"); LOCK = os.path.join(tmp, "logs", "autorun.lock")
    SLEEP = lambda s: None
    empty = {"issues": [], "prs": [], "tasks": []}
    # 작업 고르기와 멈춤 표시
    assert next_work(empty) is None
    assert next_work({"issues": [{"number": 30, "title": "b"}, {"number": 25, "title": "a"}], "prs": [{"number": 1, "title": "p"}], "tasks": ["t"]}) == "요청 이슈 #25 a"
    assert next_work({"issues": [], "prs": [{"number": 9, "title": "p", "body": ""}], "tasks": ["t"]}).startswith("열린 PR #9")
    assert next_work({"issues": [], "prs": [], "tasks": ["5장 개정"]}) == "작업 목록: 5장 개정"
    assert stop_mark({"prs": [{"number": 9, "body": "멈춤: editor 병합 불가 3회\n..."}]}) == "PR #9에 멈춤 표시: editor 병합 불가 3회"
    assert stop_mark({"prs": [{"number": 33, "body": "**멈춤: .claude/ 쓰기 권한 없음.** 설명"}]}).startswith("PR #33에 멈춤 표시: .claude/ 쓰기 권한 없음")
    assert stop_mark({"prs": [{"number": 1, "body": "## 진행\n멈춤: 아님"}]}) is None
    assert handoff_tasks("## 작업 목록\n- [x] a\n- [ ] b\n- [ ] c\n\n## 진행 기록\n") == ["b", "c"]
    # 멈춤 분류(판정 순서와 실제 로그 사례)
    assert classify({"code": 0, "is_error": False}) is None
    assert failure_reason({"code": 0, "result": "보고: usage limit, 502 판정 수정", "is_error": False}) is None
    assert classify({"code": 1, "result": "Claude usage limit reached"}) == "limit"
    assert classify({"code": 1, "subtype": "success", "result": "You've hit your session limit · resets 7:30pm (Asia/Seoul)"}) == "limit"
    assert classify({"code": 1, "timeout": True, "result": "usage limit reached"}) == "limit"  # 한도가 먼저
    assert classify({"code": 1, "timeout": True, "result": "partial"}) == "timeout"
    assert classify({"code": 1, "result": "API Error: 529 overloaded_error"}) == "transient"
    assert classify({"code": 1, "result": "API Error: 503 Service Unavailable"}) == "transient"
    assert classify({"code": 1, "stderr": "request timed out"}) == "transient"
    assert classify({"code": 1, "result": "검사 502건 실패"}) == "error"  # 문맥 없는 숫자는 일시 오류가 아님
    assert classify({"code": 1, "result": "x", "subtype": "error_max_turns"}) == "error"
    assert failure_reason({"code": 1, "result": "x", "subtype": "error_max_turns"}) == "실행 오류(error_max_turns: x)"
    assert failure_reason({"code": 1, "timeout": True}) == "실행 오류(시간 초과)"
    assert failure_reason({"code": 1, "result": "Claude usage limit reached"}) == "사용량 한도"
    base = datetime.datetime(2026, 10, 20, 18, 50)
    assert reset_wait("resets 7:30pm (Asia/Seoul)", base) == 40 * 60 + 120
    assert reset_wait("resets 6:00pm", base) == (23 * 60 + 10) * 60 + 120  # 지난 시각이면 다음 날
    assert reset_wait("resets 12am", base) == (5 * 60 + 10) * 60 + 120
    assert reset_wait("한도", base) == 60 * 60
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
    # 잠금: 살아 있고 최근 갱신된 다른 프로세스는 거부, 오래된 갱신이나 죽은 pid는 회수, 다시 시작은 넘겨받음
    os.makedirs(os.path.dirname(LOCK), exist_ok=True)
    other = subprocess.Popen([sys.executable, "-c", "import time; time.sleep(60)"])
    try:
        write_lock({"pid": other.pid, "start": now(), "updated": now()})
        assert acquire_lock() is False
        old = (datetime.datetime.now() - datetime.timedelta(hours=5)).strftime("%Y-%m-%d %H:%M:%S")
        write_lock({"pid": other.pid, "start": old, "updated": old})
        assert acquire_lock() is True  # 갱신이 오래된 잠금(pid 재사용 대비)
        write_lock({"pid": other.pid, "start": now(), "updated": now()})
        assert acquire_lock(inherit_pid=other.pid) is True and read_lock()["pid"] == os.getpid()  # 부모의 잠금 넘겨받기
    finally:
        other.kill(); other.wait()
    write_lock({"pid": other.pid, "start": now(), "updated": now()})
    assert acquire_lock() is True and read_lock()["pid"] == os.getpid()  # 죽은 pid
    touch_lock(); release_lock(); assert not os.path.exists(LOCK)
    # 자기 다시 시작 인자
    assert restart_argv(["--max", "20", "--unit-timeout", "90", "--restarts", "1"], 7, None, 2) == ["--unit-timeout", "90", "--max", "7", "--restarts", "2"]
    assert restart_argv(["--once", "--last-fail", "x"], 1, "진전 없음", 1) == ["--max", "1", "--restarts", "1", "--last-fail", "진전 없음"]
    # 가짜 gh: 호출 기록과 정해 둔 출력
    calls, outs, rc = [], {}, {}
    def fake_gh(*a, check=True, cwd=None, timeout=None, token=None):
        calls.append(a + (("token=" + token,) if token else ()))
        key = " ".join(a[:2])
        return SimpleNamespace(stdout=outs.get(key, ""), stderr="", returncode=rc.get(key, 0))
    gh = fake_gh
    # 상태 이슈: 없으면 만들고 댓글, 작가 알림에만 @, 토큰이 있으면 토큰으로
    outs["issue list"] = "[]"; outs["issue create"] = "https://github.com/x/y/issues/77\n"
    body = notify("단위 끝")
    assert ("issue", "create") == calls[-2][:2] and calls[-1][:3] == ("issue", "comment", "77") and AUTHOR not in body
    body = notify("멈춤: 사용량 한도", "한도가 풀린 뒤 다시 실행")
    assert calls[-1][:3] == ("issue", "comment", "77") and AUTHOR in body and "작가가 할 일: 한도가 풀린 뒤 다시 실행" in body
    assert sum(1 for c in calls if c[:2] == ("issue", "create")) == 1  # 이슈는 한 번만 만듦
    _status["no"] = None; outs["issue list"] = json.dumps([{"number": 5, "title": STATUS_TITLE}])
    os.environ["AUTORUN_GH_TOKEN"] = "bot"
    notify("다시 찾기"); assert calls[-1][:3] == ("issue", "comment", "5") and calls[-1][-1] == "token=bot"
    del os.environ["AUTORUN_GH_TOKEN"]
    assert editor_verdict("editor 2차 병합 가능") == "병합 가능" and editor_verdict("병합 불가 1회") == "병합 불가"
    # 권한 확대 판정
    cur = {"permissions": {"allow": ["Read"], "ask": ["Bash(git commit:*)"], "deny": ["Bash(git push origin main:*)"]}, "hooks": {"a": 1}}
    assert permission_widening(cur, cur) == ""
    assert "deny 삭제" in permission_widening(cur, {"permissions": {"allow": ["Read"], "ask": ["Bash(git commit:*)"]}, "hooks": {"a": 1}})
    assert "allow 추가: Bash(*)" in permission_widening(cur, {"permissions": dict(cur["permissions"], allow=["Read", "Bash(*)"]), "hooks": {"a": 1}})
    assert "hooks 변경" in permission_widening(cur, dict(cur, hooks={}))
    # 할 일 없음이면 바로 멈추고 이유를 로그에 남김(기록할 변경이 없어 커밋하지 않음)
    record_stop("할 일 없음(selftest)", empty)
    assert "할 일 없음(selftest)" in open(LOG, encoding="utf-8").read()
    # 임시 원격과 복제본
    remote, work = os.path.join(tmp, "remote.git"), os.path.join(tmp, "work")
    sh(["git", "init", "-q", "--bare", remote], True); sh(["git", "clone", "-q", remote, work], True)  # cwd는 있는 폴더(tmp)여야 함
    ROOT = work
    for c in (["config", "user.name", "selftest"], ["config", "user.email", "selftest@example.com"], ["symbolic-ref", "HEAD", "refs/heads/main"]):
        sh(["git", *c], True)
    def w(rel, text):
        p = os.path.join(ROOT, *rel.split("/")); os.makedirs(os.path.dirname(p), exist_ok=True); open(p, "w", encoding="utf-8").write(text)
    w("HANDOFF.md", "# 인계\n\n## 지금 상태\n- 이전\n"); w(".claude/commands/next.md", "옛 판\n"); w(".claude/settings.json", json.dumps(cur))
    sh(["git", "add", "-A"], True); sh(["git", "commit", "-q", "-m", "init"], True); sh(["git", "push", "-q", "-u", "origin", "main"], True)
    def stage(files, msg):
        sh(["git", "switch", "-q", "main"], True)
        for rel, text in files.items(): w(rel, text)
        sh(["git", "add", "--", *files], True); sh(["git", "commit", "-q", "-m", msg], True); sh(["git", "push", "-q"], True)
        sh(["git", "switch", "-q", "feature"], True)  # 사용자는 다른 브랜치에서 작업 중
    sh(["git", "switch", "-q", "-c", "feature"], True); w("메모.txt", "사용자 작업 중\n")  # 커밋하지 않은 파일
    def remote_branches():
        return [l.split("refs/heads/")[1] for l in sh(["git", "ls-remote", "--heads", "origin"], True).stdout.splitlines()]
    # 설정 반영 성공: 임시 작업 폴더에서 허용 경로 복사, 폴더 삭제, check_all, PR, CI, 병합. 사용자의 브랜치와 작업 트리는 그대로
    CHECK_CMD = [sys.executable, "-c", "pass"]
    stage({STAGE + "/commands/next.md": "새 판\n", STAGE + "/agents/editor.md": "editor 새 판\n", STAGE + "/settings.json": json.dumps(cur),
           STAGE + "/README.md": "설명\n"}, "stage")
    outs["pr create"] = "https://github.com/x/y/pull/88\n"; calls.clear()
    assert apply_staged() == "반영"
    assert [c[:2] for c in calls if c[0] == "pr"] == [("pr", "create"), ("pr", "checks"), ("pr", "merge")]
    assert sh(["git", "branch", "--show-current"], True).stdout.strip() == "feature" and os.path.exists(os.path.join(ROOT, "메모.txt"))
    assert "worktree" not in sh(["git", "worktree", "list"], True).stdout.split("\n", 1)[-1]  # 임시 작업 폴더 정리
    assert not [b for b in sh(["git", "branch"], True).stdout.split() if b.startswith("autorun-apply-")]
    # 실패 되돌림: 잘못된 JSON, 허용 밖 경로, 권한 확대, check_all 실패, CI 실패(병합이 가짜라 main에는 아직 폴더가 있음)
    cases = [({STAGE + "/settings.json": "{잘못된 JSON"}, "JSON이 아님", None),
             ({STAGE + "/settings.json": json.dumps(cur), STAGE + "/hooks/x.py": "print(1)\n"}, "허용 밖 경로", None),
             ({STAGE + "/hooks/x.py": None, STAGE + "/settings.json": json.dumps({"permissions": dict(cur["permissions"], deny=[]), "hooks": {"a": 1}})}, "권한 확대", None),
             ({STAGE + "/settings.json": json.dumps(cur)}, "check_all 실패", "check"),
             ({STAGE + "/agents/editor.md": "다시\n"}, "CI 실패", "ci")]
    for files, expect, mode in cases:
        if None in files.values():
            sh(["git", "switch", "-q", "main"], True)
            for rel in [r for r, t in files.items() if t is None]: sh(["git", "rm", "-q", rel], True)
            sh(["git", "commit", "-q", "-m", "rm"], True); sh(["git", "push", "-q"], True); sh(["git", "switch", "-q", "feature"], True)
            files = {r: t for r, t in files.items() if t is not None}
        stage(files, "bad stage " + expect)
        CHECK_CMD = [sys.executable, "-c", "import sys; print('금칙어 실패'); sys.exit(1)"] if mode == "check" else [sys.executable, "-c", "pass"]
        rc["pr checks"] = 1 if mode == "ci" else 0
        calls.clear(); res = apply_staged()
        assert res.startswith("설정 반영 실패") and expect in res, res
        assert not [c for c in calls if c[:2] == ("pr", "merge")]
        if mode == "ci":
            assert [c[:2] for c in calls if c[:2] == ("pr", "close")]
        assert AUTHOR in open(os.path.join(os.path.dirname(LOG), "status_body.md"), encoding="utf-8").read()
        assert sh(["git", "branch", "--show-current"], True).stdout.strip() == "feature"
        assert not [b for b in sh(["git", "branch"], True).stdout.split() if b.startswith("autorun-apply-")]
        assert not [b for b in remote_branches() if b.startswith("autorun-apply-")]
    rc.clear(); CHECK_CMD = [sys.executable, "-c", "pass"]
    # 멈춤 기록: 작업 트리가 더러우면 기록하지 않고, 깨끗하면 PR 브랜치에 HANDOFF.md만 커밋, push
    os.remove(os.path.join(ROOT, "메모.txt")); sh(["git", "switch", "-q", "main"], True); sh(["git", "pull", "-q"], True)
    sh(["git", "switch", "-q", "-c", "work"], True); sh(["git", "push", "-q", "-u", "origin", "work"], True); sh(["git", "switch", "-q", "main"], True)
    st = {"issues": [], "prs": [{"number": 7, "headRefName": "work", "body": "본문"}], "tasks": []}
    open(os.path.join(ROOT, "HANDOFF.md"), "a", encoding="utf-8").write("- 미완성\n")
    calls.clear(); record_stop("시험 이유 \"따옴표\" & 기호", st)
    assert not [c for c in calls if c[0] == "pr"] and "멈춤 기록 실패" in open(LOG, encoding="utf-8").read()
    sh(["git", "checkout", "--", "HANDOFF.md"], True)
    calls.clear(); record_stop("시험 이유 \"따옴표\" & 기호", st, todo="시험")
    assert calls[0][:2] == ("issue", "comment")  # 작가 알림이 먼저
    assert sh(["git", "branch", "--show-current"]).stdout.strip() == "work"
    assert "멈춤(autorun" in sh(["git", "show", "origin/work:HANDOFF.md"], True).stdout
    assert "멈춤" not in sh(["git", "show", "origin/main:HANDOFF.md"], True).stdout
    assert sh(["git", "show", "--numstat", "--format=", "HEAD"], True).stdout.split() == ["1", "0", "HANDOFF.md"]
    pe = [c for c in calls if c[:2] == ("pr", "edit")][0]
    assert pe[2] == "7" and open(pe[-1], encoding="utf-8").read().startswith('멈춤: 시험 이유 "따옴표" & 기호\n\n본문')
    # 재시도와 한도 대기(가짜 단위 실행)
    seq = [{"code": 1, "result": "API Error: 529 overloaded"}, {"code": 1, "result": "request timed out"}, {"code": 0, "is_error": False, "result": "끝"}]
    real_run = run_unit
    run_unit = lambda a: seq.pop(0)
    a = SimpleNamespace(retry_base=60, max_wait_hours=6)
    out, problem = run_with_recovery(a, "시험")
    assert problem is None and out["result"] == "끝" and "재시도\t2/3" in open(LOG, encoding="utf-8").read()
    seq[:] = [{"code": 1, "result": "overloaded"}] * 4
    out, problem = run_with_recovery(a, "시험"); assert problem[0] == "transient"
    seq[:] = [{"code": 1, "subtype": "success", "result": "You've hit your session limit · resets 7:30pm (Asia/Seoul)"}, {"code": 0, "is_error": False, "result": "끝"}]
    out, problem = run_with_recovery(SimpleNamespace(retry_base=60, max_wait_hours=48), "시험")  # 재개 시각까지 길어도 하루 안
    assert problem is None and "대기\t사용량 한도" in open(LOG, encoding="utf-8").read()
    seq[:] = [{"code": 1, "result": "usage limit reached"}]
    out, problem = run_with_recovery(SimpleNamespace(retry_base=60, max_wait_hours=0.5), "시험"); assert problem[0] == "limit"
    run_unit = real_run
    print("selftest 통과")
    return 0

if __name__ == "__main__":
    sys.exit(main())
