"""작업 대시보드(이슈 #66 작가 요청 2026-10-22 15:00, D-129의 예외인 보고 장치).

GitHub 이슈 "작업 대시보드"의 본문을 매번 덮어써서 지금 상태를 보여 준다(댓글로 쌓지 않음).
같은 내용을 --write-file이면 DASHBOARD.md로도 쓴다(병합 전 마지막 커밋에서).

사용:
  python tools/dashboard.py start <에이전트> <작업>          에이전트 상태를 "진행 중"으로
  python tools/dashboard.py end <에이전트> <결과> [다음 작업]  에이전트 상태를 "완료"로
  python tools/dashboard.py now <단계> <작업> [PR]             "지금" 줄(단계 0~4, 지금 작업, 초안 PR)
  python tools/dashboard.py six <장> <PR>                      장의 여섯 확인 완료 기록(예: ch01 #80)
  python tools/dashboard.py stop <이유> <작가가 할 일>          멈춤 표시(이슈 댓글로 작가 알림)
  python tools/dashboard.py resume                             멈춤 표시 지움
  python tools/dashboard.py refresh [--write-file]             장별 표와 오늘 병합 PR만 다시 계산
공통 옵션: --dry(이슈를 고치지 않고 본문만 출력), --write-file(DASHBOARD.md도 씀)
상태는 logs/dashboard.json(저장소에 올리지 않음)에 둔다.
"""
import datetime, glob, json, os, re, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "lint"))
import check_rules  # noqa: E402  R9, R10, R12 판정을 같은 기준으로 셈

STATE = os.path.join(ROOT, "logs", "dashboard.json")
FILE = os.path.join(ROOT, "DASHBOARD.md")
TITLE, LABEL, AUTHOR = "작업 대시보드", "dashboard", "@seoulkorea-dev"
KST = datetime.timezone(datetime.timedelta(hours=9))
AGENTS = ["작성 에이전트", "editor", "flow-reviewer", "fact-checker", "reader-expert", "researcher",
          "reader-novice", "practice-checker", "production-checker", "자동 실행"]
PARTS = [("시작하며", ["src/chapters/prologue.html"])] + \
        [(f"{n}장", [f"src/chapters/ch{n:02d}.html"]) for n in range(1, 12)] + \
        [("마치며", ["src/chapters/epilogue.html"]), ("부록", ["src/appendix/practice.html", "src/appendix/terms.html"])]
STAGES = {"0": "0단계 작업 체계 동결", "1": "1단계 기준서", "2": "2단계 1장 완성본", "3": "3단계 나머지 장", "4": "4단계 작가 최종 검수"}
CR = re.compile(r"(?<![A-Za-z0-9_./-])CR(?![A-Za-z0-9_])(?!\.md)")  # check_rules R12와 같은 기준
ASSERT = re.compile(r"(?:이|가) 아니라|반드시|항상|결국|해야 합니다")

def now():
    return datetime.datetime.now(KST)

def stamp(t=None):
    return (t or now()).strftime("%m-%d %H:%M")

def run(cmd, check=False):
    r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if check and r.returncode != 0:
        raise RuntimeError(f"{' '.join(cmd[:3])} 실패: {(r.stderr or r.stdout).strip()[:300]}")
    return r

def load():
    st = {"now": {"stage": "", "work": "", "pr": ""}, "agents": {}, "six": {}, "stop": None, "issue": None, "updated": ""}
    if os.path.exists(STATE):
        st.update(json.load(open(STATE, encoding="utf-8")))
    for a in AGENTS:
        st["agents"].setdefault(a, {"status": "대기", "work": "", "start": "", "end": "", "result": "", "next": ""})
    return st

def save(st):
    os.makedirs(os.path.dirname(STATE), exist_ok=True)
    json.dump(st, open(STATE, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

# ---------- 장별 진행(저장소에서 계산) ----------
def part_row(name, paths):
    old = new = cr = same = bad = 0
    claim, pr = "", ""
    for p in paths:
        full = os.path.join(ROOT, *p.split("/"))
        if not os.path.exists(full):
            continue
        s = open(full, encoding="utf-8").read()
        old += s.count('href="#ref-') + len(re.findall(r'<sup class="fnref">', s))
        new += len(set(re.findall(r'<sup class="cite"[^>]*>.*?(\d+).*?</sup>', s, re.S)))
        cr += len(CR.findall(check_rules.text_of(check_rules.strip_code(s))))
        _, fails, _ = check_rules.check_file(full)
        same += sum(1 for f in fails if f.startswith("R10"))
        bad += len({f.split()[1] for f in fails if f.startswith("R9")})
        m = re.search(r'<p class="claim">(.*?)</p>', s, re.S)
        if m:
            claim = "단정형" if ASSERT.search(check_rules.text_of(m.group(1))) else "아님"
        log = run(["git", "log", "--first-parent", "origin/main", "-1", "--format=%s", "--", p]).stdout.strip()
        n = re.search(r"Merge pull request #(\d+)|\(#(\d+)\)$", log)  # 병합 커밋과 squash 병합 제목
        pr = max(pr, f"#{n.group(1) or n.group(2)}", key=lambda x: int(x[1:] or 0)) if n else pr
    return [name, str(old), str(new), str(cr), str(same), str(bad), claim or "-", "", pr or "-"]

def merged_today():
    day = now().strftime("%Y-%m-%d")
    r = run(["gh", "pr", "list", "--state", "merged", "--search", f"merged:>={day}T00:00:00+09:00", "--limit", "50",
             "--json", "number,title,mergedAt,files"])
    rows = []
    for p in sorted(json.loads(r.stdout or "[]"), key=lambda x: x["mergedAt"]):
        t = datetime.datetime.fromisoformat(p["mergedAt"].replace("Z", "+00:00")).astimezone(KST)
        parts = [n for n, paths in PARTS if any(f["path"] in paths for f in p.get("files", []))]
        rows.append([t.strftime("%H:%M"), f"#{p['number']} {p['title']}", ", ".join(parts) or "장 변경 없음"])
    return rows

# ---------- 본문 ----------
def table(head, rows):
    out = ["| " + " | ".join(head) + " |", "|" + "---|" * len(head)]
    out += ["| " + " | ".join(c.replace("|", "/") for c in r) + " |" for r in rows]
    return "\n".join(out)

def render(st, parts, merged):
    n = st["now"]
    lines = [f"# {TITLE}", "",
             "이 본문은 tools/dashboard.py가 매번 덮어씁니다(댓글로 쌓지 않음). 같은 내용이 병합 때마다 DASHBOARD.md에 남습니다.", "",
             "## 지금",
             f"- 단계: {STAGES.get(n['stage'], n['stage'] or '-')}",
             f"- 지금 작업: {n['work'] or '-'}" + (f"(초안 PR {n['pr']})" if n["pr"] else ""),
             f"- 마지막 갱신: {st['updated']}(한국 시간)", ""]
    if st.get("stop"):
        s = st["stop"]
        lines += ["## 멈춤", f"- {s['time']} 이유: {s['reason']}", f"- 작가가 할 일: {s['todo']}", ""]
    rows = []
    for a in AGENTS:
        x = st["agents"][a]
        rows.append([a, x["status"], x["work"] or "-", x["start"] or "-", x["end"] or "-", x["result"] or "-", x["next"] or "-"])
    lines += ["## 에이전트 상태", table(["에이전트", "상태", "지금 작업", "시작", "끝", "결과", "다음 작업"], rows), ""]
    prow = []
    for r in parts:
        key = {"시작하며": "prologue", "마치며": "epilogue", "부록": "appendix"}.get(r[0], f"ch{int(r[0][:-1]):02d}" if r[0].endswith("장") else r[0])
        r[7] = st["six"].get(key, "아니오")
        prow.append(r)
    lines += ["## 장별 진행(저장소에서 계산)",
              table(["장", "옛 인용 수", "새 인용 번호 수", "\"CR\" 수", "같은 장 링크 수", "표 체계 위반 표 수", "주장 줄", "여섯 확인", "마지막 정비 PR"], prow),
              "",
              "- 옛 인용: 본문의 #ref- 링크와 문단 아래 각주 번호(D-123). 새 인용: 기준서의 책 전체 번호(sup.cite, 1단계에서 정함)",
              "- \"CR\": lint/check_rules.py R12와 같은 기준(코드와 파일 경로 제외, \"CR이\", \"CR은\"도 셈). 같은 장 링크는 R10, 표 체계 위반은 R9 기준",
              "- 주장 줄: \"아니라\", \"반드시\", \"항상\", \"결국\", \"해야 합니다\"가 있으면 단정형. 마지막 정비 PR: 그 파일을 바꾼 마지막 병합 PR", ""]
    lines += ["## 오늘 병합된 PR(한국 시간)", table(["시각", "PR", "바뀐 장"], merged) if merged else "- 없음", ""]
    return "\n".join(lines)

# ---------- 이슈 ----------
def issue_number(st):
    if st.get("issue"):
        return st["issue"]
    r = run(["gh", "issue", "list", "--label", LABEL, "--state", "open", "--json", "number,title"])
    for i in json.loads(r.stdout or "[]"):
        if i["title"] == TITLE:
            st["issue"] = i["number"]; return i["number"]
    run(["gh", "label", "create", LABEL, "--color", "0284c7", "--description", "작업 대시보드"])
    r = run(["gh", "issue", "create", "--title", TITLE, "--label", LABEL, "--body", "준비 중"], check=True)
    st["issue"] = int(r.stdout.strip().rstrip("/").split("/")[-1])
    run(["gh", "issue", "pin", str(st["issue"])])
    return st["issue"]

def publish(st, body, dry, write_file):
    if write_file:
        open(FILE, "w", encoding="utf-8", newline="\n").write(body + "\n")
    if dry:
        print(body); return
    n = issue_number(st)
    tmp = os.path.join(ROOT, "logs", "dashboard-body.md")
    open(tmp, "w", encoding="utf-8").write(body)
    run(["gh", "issue", "edit", str(n), "--body-file", tmp], check=True)
    print(f"대시보드 갱신: 이슈 #{n}, {st['updated']}")

def main(argv):
    dry = "--dry" in argv
    write_file = "--write-file" in argv
    args = [a for a in argv if a not in ("--dry", "--write-file")]
    if not args:
        print(__doc__); return 2
    cmd, rest = args[0], args[1:]
    st = load()
    t = stamp()
    if cmd == "start" and len(rest) >= 2:
        a = st["agents"].setdefault(rest[0], {})
        a.update(status="진행 중", work=" ".join(rest[1:]), start=t, end="", result="")
    elif cmd == "end" and len(rest) >= 2:
        a = st["agents"].setdefault(rest[0], {})
        a.update(status="완료", end=t, result=rest[1], next=rest[2] if len(rest) > 2 else "")
    elif cmd == "now" and len(rest) >= 2:
        st["now"] = {"stage": rest[0], "work": rest[1], "pr": rest[2] if len(rest) > 2 else ""}
    elif cmd == "six" and len(rest) == 2:
        st["six"][rest[0]] = f"완료({rest[1]})"
    elif cmd == "stop" and len(rest) == 2:
        st["stop"] = {"time": t, "reason": rest[0], "todo": rest[1]}
    elif cmd == "resume":
        st["stop"] = None
    elif cmd != "refresh":
        print(__doc__); return 2
    for a in AGENTS:  # 새 에이전트 이름이 들어와도 기본 칸은 채움
        st["agents"].setdefault(a, {})
    for x in st["agents"].values():
        for k in ("status", "work", "start", "end", "result", "next"):
            x.setdefault(k, "대기" if k == "status" else "")
    st["updated"] = now().strftime("%Y-%m-%d %H:%M")
    run(["git", "fetch", "-q", "origin", "main"])
    parts = [part_row(n, p) for n, p in PARTS]
    body = render(st, parts, [] if dry else merged_today())
    publish(st, body, dry, write_file)
    save(st)
    if cmd == "stop" and not dry:
        run(["gh", "issue", "comment", str(st["issue"]), "--body", f"{AUTHOR} 멈춤: {rest[0]}. 작가가 할 일: {rest[1]}"])
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
