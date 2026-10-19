# 책 작업 하네스 설정(시작 정의와 Step 2 구현)

- 작성: 2026-10-19, 검수 Project(Claude)
- 대상 저장소: seoulkorea-dev/harness-book
- 사용법: 작가는 1절을 승인하고 2절(브랜치 보호)을 설정한다. 그다음 VS Code의 Claude Code에 이렇게 요청한다: **"HARNESS_SETUP.md의 3절을 순서대로 수행하고, 각 단계의 출력 원문을 보여 줘."** 4절의 작동 시험은 PR 병합 뒤에 한다.

---

## 1. 시작 정의(Step 0, 작가 승인)

### 1-1. 작업 장소와 역할
| 주체 | 도구 | 맡는 일 | 하지 않는 일 |
|---|---|---|---|
| 작가 | GitHub, VS Code | 결정, 승인, PR 병합 | |
| 메인 세션 | VS Code의 Claude Code | 원고, 그림, 실습 작성, 검사, 하위 에이전트 호출, 브랜치 push, PR | main 반영 |
| 하위 에이전트 6개 | Claude Code 안 | 조사와 점검(읽기만) | 파일 수정 |
| 검수 Project | Claude App | 정식 검수 문서, 외부 의견 검토, 방향 논의 | 원고 수정, push |
- **원고를 바꾸는 곳은 Claude Code 한 곳**이다. 채팅과 Cowork에서는 원고를 바꾸지 않는다.

### 1-2. 승인이 필요한 일
| 구분 | 예 | 방법 |
|---|---|---|
| 설계 변경 | 목차, 장의 주장, 핵심 정의와 용어, 그림 방침, 문체 규칙 | 작가에게 먼저 묻고 DECISIONS.md에 기록 |
| 반영 | 모든 변경의 main 반영 | PR, CI 통과 뒤 작가가 병합 |
| 기록 변경 | DECISIONS.md 수정 | 설정이 매번 확인을 요구 |

### 1-3. 강제 장치(지시가 아니라 장치가 막는 것)
| 막는 것 | 장치 |
|---|---|
| main 커밋과 main push, 강제 push | 설정(deny), PreToolUse 훅, 브랜치 보호 |
| 검사 실패 상태로 작업 종료 | Stop 훅(check_all) |
| 원고를 바꾸고 인계 없이 종료 | Stop 훅(HANDOFF.md 확인) |
| 검사 실패 상태로 병합 | CI 필수 검사 |
| 수용 시험, 원본 데이터 수정 | 설정(deny) |
| 하위 에이전트의 파일 수정 | 에이전트 도구 목록(편집 도구 없음) |

### 1-4. 기록
DECISIONS.md(결정과 대체 관계), HANDOFF.md(세션 인계), FAILURES.md(반복 실패와 장치), reviews/(검수, 하위 에이전트 보고), research/(출처), RUNLOG.md(실습 실행), docs/metrics.md(PR마다 자동 검출 수와 사람 지적 수)

### 1-5. 단계와 완료 기준
| Step | 내용 | 완료 기준(출력으로 확인) | 예상 |
|---|---|---|---|
| 0 | 이 시작 정의 승인 | 작가 승인 | 10/20 |
| 1 | 환경 | Claude Code, VS Code, gh 로그인, 저장소 | **완료(10/19)** |
| 2 | 하네스 구현(3절) | PR, CI 통과, 병합 | 10/20~21 |
| 3 | 작동 시험(4절) | 시험 7개 모두 기대 결과 | 10/22 |
| 4 | 1장 시범(장 틀, CR 이름) | 1장 PR 병합, 검수 반영 n / n | 10/23~25 |
| 5 | 회고 | FAILURES, HANDOFF, 이 문서 갱신 | 10/26 |
| 6 | 2~11장(장당 약 2일, 1장 결과로 재조정) | 장마다 병합 | 10/27~11/16 |
| 7 | 시작하며, 마치며, 부록, 11장 사례 | 병합 | 11/17~19 |
| 8 | 전체 검수, 외부 검토 | 전체 검수 문서 | 11/20~23 |

---

## 2. 작가가 먼저 할 일: 브랜치 보호(GitHub 웹)
1. 저장소 → **Settings** → **Branches** → **Add branch ruleset**(또는 Add rule)
2. 대상 브랜치: `main`
3. 켤 항목
   - **Require a pull request before merging**
     - 필요한 승인 수(Required approvals)는 **0**으로 둔다. GitHub에서는 PR을 만든 사람이 자기 PR을 승인할 수 없는데, Claude Code가 작가 계정으로 PR을 만들기 때문이다. **작가가 PR 화면에서 직접 병합하는 행위가 승인**이다.
   - **Require status checks to pass**: `check`(book-check 워크플로)를 필수로 지정한다. 목록에 없으면 3절의 PR에서 CI가 한 번 돈 뒤 다시 지정한다.
   - **Block force pushes**
   - **Do not allow bypassing**(관리자도 우회 불가)
4. 저장: 이후 main에 직접 push하면 GitHub가 거부한다.

---

## 3. Claude Code가 수행할 일(Step 2 구현)

### 3-1. 작업 브랜치
```bash
git switch main
git pull --rebase origin main
git switch -c harness-setup
```

### 3-2. CLAUDE.md 교체(전체)
````markdown
# 작업 안내(Claude Code)

## 이 세션의 역할
- 원고 작성 담당이다. 원고, 그림, 실습 자료를 고치고 검사를 실행하고, 작업 브랜치에 push한 뒤 PR을 만든다.
- main에는 반영하지 않는다. 병합은 작가가 PR에서 한다.
- 검수는 Claude App의 검수 Project가 맡는다. reviews/의 검수 지침만 반영하고, 지시하지 않은 변경은 하지 않는다. 꼭 필요한 변경은 PR 설명에 따로 적는다.

## 시작할 때
1. HANDOFF.md를 읽는다(세션 시작 훅이 보여 준다).
2. 작업할 장의 계획(BOOK_SPEC.md)과 DECISIONS.md의 마지막 10건을 확인한다.
3. 검수 지침을 반영하는 작업이면 해당 reviews/ 문서를 읽는다.
4. main 브랜치라면 작업 브랜치를 만든다(git switch -c <장-주제>).

## 원고 규칙
- 원고는 src/만 고친다. 루트의 index.html, chapters/, appendix/는 빌드 결과물이다.
- 장 틀: 주장 제목 → 원리 → CR 적용 → 실패 표 → 확인 방법 → 원칙 한 문장 → 점검 질문
- 예제 이름: 첫 등장은 "경비 정산 시스템 개편 변경 요청(Change Request) CR", 이후는 "CR"
- 문체는 STYLE.md, 그림은 FIGURE_STYLE.md(다이어그램을 그릴 때만 diagram_guide.md도 읽는다)
- 사실은 원문을 확인한 뒤 쓰고, research/에 출처와 확인 날짜를 남긴다.

## 멀티 에이전트 작업 공간
| 구성원 | 역할 | 쓰기 |
|---|---|---|
| 작가 | 결정, 승인, PR 병합 | 전부(바꾸면 DECISIONS.md에 기록) |
| 메인 세션(이 세션) | 원고 작성, 하위 에이전트 호출, 보고서 저장, PR | src/, assets/, examples/, HANDOFF.md, FAILURES.md, reviews/, research/, DECISIONS.md(작가 확인 후) |
| researcher, fact-checker, flow-reviewer, figure-checker, reader-novice, reader-expert | 조사와 점검 | 없음(읽기만, 결과는 보고서 문안으로 돌려줌) |
| 검수 Project(Claude App) | 정식 검수 문서 | 없음(작가가 전달, 메인 세션이 reviews/에 등록) |
- 주고받기는 파일로만 한다. 하위 에이전트의 보고 문안은 메인 세션이 reviews/agents/YYYY-MM-DD-<장>-<에이전트>.md로 저장한다. 형식: 발견 | 위치 | 근거 | 제안 | 확신(높음, 중간, 낮음)
- 원고(src/)를 쓰는 주체는 한 번에 하나다. 하위 에이전트는 동시에 여러 개 불러도 된다. 다른 장을 동시에 진행하려면 장마다 브랜치와 작업 폴더(git worktree)를 따로 쓴다.
- 하위 에이전트는 이 대화를 모른다. 부를 때 범위(파일과 절), 기준 문서, 보고 형식을 넘긴다.
- 하위 에이전트 의견은 그대로 반영하지 않는다. 반영, 보류, 작가 확인으로 나누어 PR 설명에 표로 적는다. 의견이 부딪히면 DECISIONS.md > 검수 Project 지침 > 하위 에이전트 의견 순서로 따르고, 그래도 정해지지 않으면 작가에게 묻는다.
- 호출 시점: 장 계획 때 researcher, 원고 작성 뒤 PR 전에 fact-checker, flow-reviewer, figure-checker, reader-novice, 마무리 단계에 reader-expert

## 먼저 작가에게 물을 일
- 목차, 장의 주장, 핵심 정의와 용어, 그림 방침, 문체 규칙을 바꾸는 일
- DECISIONS.md 수정, 브랜치 push, PR 생성(설정이 확인을 요구한다)

## 끝낼 때
- python tools/check_all.py를 통과시킨다(종료 훅이 실패를 막는다).
- 보고에는 검사 출력 원문을 붙인다.
- HANDOFF.md를 갱신한다. 같은 실패가 두 번째면 FAILURES.md에 적는다.
````

### 3-3. .claude/settings.json 교체(전체)
```json
{
  "permissions": {
    "allow": [
      "Bash(python tools/build.py)",
      "Bash(python tools/check_all.py:*)",
      "Bash(python tools/check_review.py:*)",
      "Bash(python lint/:*)",
      "Bash(git status:*)",
      "Bash(git diff:*)",
      "Bash(git log:*)",
      "Bash(git branch:*)",
      "Bash(git switch:*)",
      "Bash(git add:*)",
      "Bash(git commit:*)",
      "Bash(gh pr view:*)",
      "Bash(gh pr checks:*)",
      "Bash(gh pr list:*)"
    ],
    "ask": [
      "Bash(git push:*)",
      "Bash(gh pr create:*)",
      "Bash(gh pr merge:*)",
      "Edit(DECISIONS.md)",
      "Write(DECISIONS.md)"
    ],
    "deny": [
      "Bash(git push origin main:*)",
      "Bash(git push --force:*)",
      "Bash(git push -f:*)",
      "Edit(examples/**/acceptance/**)",
      "Write(examples/**/acceptance/**)",
      "Edit(examples/**/data/**)",
      "Write(examples/**/data/**)",
      "Read(.env)",
      "Read(.env.*)"
    ]
  },
  "hooks": {
    "SessionStart": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python tools/hooks/session_start.py"
          }
        ]
      }
    ],
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "python tools/hooks/pre_bash.py"
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Edit|Write|MultiEdit",
        "hooks": [
          {
            "type": "command",
            "command": "python tools/hook_lint.py",
            "timeout": 120
          }
        ]
      }
    ],
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python tools/hooks/stop_check.py",
            "timeout": 300
          }
        ]
      }
    ]
  }
}
```
- 이 파일은 저장소에 커밋되는 팀 공통 설정이다. 개인 설정은 .claude/settings.local.json에 둔다(커밋하지 않음).

### 3-4. 검사 스크립트(새 파일, 검수 쪽에서 시험 완료)
**tools/check_all.py**
```python
"""책 저장소 전체 검사: 빌드, 금칙어, lint 3종, 그림 점검(, CI에서는 빌드 결과와 커밋 일치).
사용: python tools/check_all.py [--ci]
모든 항목을 실행한 뒤 요약을 출력하고, 하나라도 실패하면 종료 코드 1.
"""
import glob, html, re, subprocess, sys

CI = "--ci" in sys.argv
STRICT_FIG = "--strict-figures" in sys.argv  # 그림 글자 크기를 실패로 볼지(기본은 경고)
MOBILE_MIN_PX = 11.0      # 모바일에서 보이는 가장 작은 글자(px)
SVG_MIN_WIDTH = 560       # style.css의 .diagram svg min-width
FIG_BANNED = ["Claude"]   # 그림 안에 쓰지 않는 이름(D-095)

def run(cmd):
    r = subprocess.run(cmd, shell=True, capture_output=True, text=True, encoding="utf-8", errors="replace")
    return r.returncode, (r.stdout + r.stderr).strip()

results = []
def add(name, ok, detail=""):
    results.append((name, ok, detail))

code, out = run("python tools/build.py")
add("빌드", code == 0, out[-300:])

pats = [l.rstrip("\r\n") for l in open("lint/banned.txt", encoding="utf-8") if l.strip() and not l.startswith("#")]  # 끝 공백도 패턴의 일부
hits = []
for f in ["index.html"] + glob.glob("chapters/*.html") + glob.glob("appendix/*.html"):
    for n, line in enumerate(open(f, encoding="utf-8"), 1):
        for p in pats:
            try:
                if re.search(p, line):
                    hits.append(f"{f}:{n}: {p}")
            except re.error:
                pass
add("금칙어", not hits, "\n".join(hits[:20]))

for name, cmd in [("번호", "python lint/check_numbers.py"), ("구조", "python lint/check_structure.py")]:
    code, out = run(cmd)
    add(name, code == 0, out[-800:])

code, out = run("python lint/check_style.py")
warns = [l for l in out.splitlines() if l.startswith("경고 ")]
add("문체", not warns, "\n".join(warns[:20]))

fig_issues = []
fig_small = []
for f in sorted(glob.glob("chapters/*.html") + glob.glob("appendix/*.html") + ["index.html"]):
    t = open(f, encoding="utf-8").read()
    for m in re.finditer(r'<figure[^>]*id="(fig-[^"]+)"(.*?)</figure>', t, re.S):
        fid, body = m.group(1), m.group(2)
        vb = re.search(r'viewBox="0 0 ([\d.]+) [\d.]+"', body)
        sizes = [float(x) for x in re.findall(r'font-size="([\d.]+)"', body)]
        if vb and sizes:
            w = float(vb.group(1)); shown = min(sizes) * SVG_MIN_WIDTH / w if w > SVG_MIN_WIDTH else min(sizes)
            if round(shown, 1) < MOBILE_MIN_PX:
                fig_small.append(f"{f} {fid}: 가장 작은 글자 {min(sizes)}px, 모바일 약 {shown:.1f}px(기준 {MOBILE_MIN_PX})")
        text = html.unescape(re.sub(r"<[^>]+>", " ", body)) + " " + " ".join(re.findall(r'aria-label="([^"]*)"', body))
        for b in FIG_BANNED:
            if b in text:
                fig_issues.append(f"{f} {fid}: 그림 안에 '{b}'")
add("그림 안 이름", not fig_issues, "\n".join(fig_issues[:30]))
if STRICT_FIG:
    add("그림 글자 크기", not fig_small, "\n".join(fig_small[:30]))
elif fig_small:
    print("[경고] 그림 글자 크기(기준 미달, 아직 실패로 보지 않음)\n" + "\n".join(fig_small[:30]) + "\n")

if CI:
    code, out = run("git diff --exit-code --stat -- index.html chapters appendix")
    add("빌드 결과와 커밋 일치", code == 0, out[-500:])

print("검사 요약")
for name, ok, _ in results:
    print(f"  {'통과' if ok else '실패'}  {name}")
fails = [r for r in results if not r[1]]
for name, _, detail in fails:
    print(f"\n[{name}]\n{detail}")
sys.exit(1 if fails else 0)
```
**tools/check_review.py**
```python
"""검수 지침 반영 대조: 검수 문서의 "교체" 코드 상자 내용이 원고(src/ 등)에 있는지 확인한다.
사용: python tools/check_review.py reviews/<문서>.md
결과: 반영 n / m. 빠진 항목이 있으면 종료 코드 1.
"""
import glob, re, sys

def norm(s):
    return re.sub(r"\s+", " ", s).strip()

doc = open(sys.argv[1], encoding="utf-8").read()
FENCE = "`" * 3  # 문서 안에 백틱 세 개를 직접 쓰지 않으려고 만듦
blocks = re.findall(r"\*\*교체\*\*\s*\n" + FENCE + r"[a-z]*\n(.*?)" + FENCE, doc, re.S)
corpus = ""
for f in glob.glob("src/**/*.*", recursive=True) + glob.glob("*.md") + glob.glob("lint/*.py") + glob.glob("tools/*.py"):
    try:
        corpus += norm(open(f, encoding="utf-8").read()) + "\n"
    except (UnicodeDecodeError, IsADirectoryError):
        pass
missing = []
for i, b in enumerate(blocks, 1):
    if norm(b) and norm(b) not in corpus:
        missing.append((i, norm(b)[:80]))
print(f"반영 {len(blocks) - len(missing)} / {len(blocks)}")
for i, s in missing:
    print(f"  미반영 교체 {i}: {s}")
sys.exit(1 if missing else 0)
```

### 3-5. 훅 스크립트(새 파일, 검수 쪽에서 시험 완료)
**tools/hooks/session_start.py**
```python
"""SessionStart 훅: 세션 시작 때 인계 문서, 최근 결정, 현재 브랜치를 컨텍스트로 보여 준다."""
import os, re, subprocess
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
```
**tools/hooks/pre_bash.py**
```python
"""PreToolUse 훅(Bash): main 브랜치에서의 커밋과 강제 push를 막는다. 막으면 종료 코드 2."""
import json, re, subprocess, sys
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
```
**tools/hooks/stop_check.py**
```python
"""Stop 훅: 작업을 끝내기 전에 전체 검사와 인계 문서 갱신을 확인한다.
- 저장소에 변경이 없으면 통과.
- 검사 실패 또는 원고를 바꿨는데 HANDOFF.md를 갱신하지 않았으면 종료 코드 2로 끝내지 못하게 한다.
- 같은 멈춤에서 두 번째 호출(stop_hook_active)이면 무한 반복을 막기 위해 통과시키고, 실패 내용을 .claude/last_check_failed.txt에 남긴다(다음 세션 시작 때 표시).
"""
import json, os, subprocess, sys
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
```
- tools/hook_lint.py(파일 수정 뒤 검사)는 그대로 둔다.

### 3-6. 하위 에이전트 6개(.claude/agents/)
- 삭제: `writer.md`(메인 세션과 역할이 겹침), `style-reviewer.md`(flow-reviewer로 대체)
- 아래 6개 파일로 교체하거나 새로 만든다. **모두 편집 도구(Edit, Write)가 없다.**

**.claude/agents/researcher.md**
```markdown
---
name: researcher
description: 장의 근거가 되는 1차 출처(공식 문서, 발표 글, 논문)를 조사한다. 장 계획 때 사용.
tools: Read, Grep, Glob, WebSearch, WebFetch
model: sonnet
---
너는 조사 담당이다. 원고와 파일을 고치지 않는다.
- 메인 세션이 넘긴 장과 주제에 대해 1차 출처를 찾고, 문장마다 확인한 위치를 적는다.
- 2차 출처(블로그, 요약 글)는 1차 출처를 찾는 단서로만 쓴다.
- 결과는 아래 표 문안으로 돌려준다. 메인 세션이 research/에 저장한다.
| 주장 | 출처(제목, 발행처, 날짜, 주소) | 확인한 위치 | 확인 날짜 |
```
**.claude/agents/fact-checker.md**
```markdown
---
name: fact-checker
description: 원고의 수치, 날짜, 제품 기능, 인용을 원문과 대조한다. PR 전에 사용.
tools: Read, Grep, Glob, WebSearch, WebFetch
model: sonnet
---
너는 사실 확인 담당이다. 원고와 파일을 고치지 않는다.
- 범위로 받은 절의 사실 문장을 모두 뽑아 research/의 기록과 원문으로 대조한다.
- 원문을 찾지 못하면 "미확인"으로 둔다. 추측으로 판정하지 않는다.
- 결과 문안: 발견 | 위치(파일, 문장) | 근거(원문 주소와 위치) | 제안 | 확신
```
**.claude/agents/flow-reviewer.md**
```markdown
---
name: flow-reviewer
description: 앞뒤 문장 흐름, 중복, 정의 전 사용, 링크 도착 절, 장 틀 준수를 점검한다. PR 전에 사용.
tools: Read, Grep, Glob
model: sonnet
---
너는 흐름 점검 담당이다. 원고와 파일을 고치지 않는다. 기계 검사(check_all)가 잡는 것은 다시 보지 않는다.
- 장 틀(주장 제목 → 원리 → CR 적용 → 실패 표 → 확인 방법 → 원칙 한 문장 → 점검 질문)을 지켰는지
- 새로 들어간 문장을 앞뒤 문장과 함께 읽어 연결어, 지시어가 끊기지 않았는지, 같은 내용이 겹치지 않는지
- 용어를 정의하기 전에 쓰지 않았는지, 링크가 그 개념을 설명하는 절로 가는지
- 결과 문안: 발견 | 위치 | 근거(STYLE.md 규칙 또는 앞뒤 문장) | 제안 | 확신
```
**.claude/agents/figure-checker.md**
```markdown
---
name: figure-checker
description: 그림 가이드 준수, 글자 크기, 문구의 주체, 해설표, 그림 안 이름을 점검한다. 그림을 바꾼 PR 전에 사용.
tools: Read, Grep, Glob, Bash
model: sonnet
---
너는 그림 점검 담당이다. 원고와 파일을 고치지 않는다. Bash는 python tools/check_all.py 실행에만 쓴다.
- FIGURE_STYLE.md 기준: 맨 위 결론, 할 일, 직선 연결선, 색 규칙, 해설표
- 그림 문구마다 누구의 관점인지(주체)가 분명한지
- 가장 작은 글자 × 560 ÷ viewBox 폭이 11 이상인지, 그림 안에 제품 이름이 없는지(check_all 결과 인용)
- 결과 문안: 발견 | 위치(그림 번호, 문구) | 근거 | 제안 | 확신
```
**.claude/agents/reader-novice.md**
```markdown
---
name: reader-novice
description: 하네스를 처음 배우는 대학생, 직장인 관점에서 막히는 곳을 찾는다. PR 전에 사용.
tools: Read, Grep, Glob
model: sonnet
---
너는 하네스 엔지니어링을 처음 배우는 대학생이나 직장인이다. 원고와 파일을 고치지 않는다.
- 처음 읽을 때 모르는 용어, 따라가기 어려운 단계, 예제와 설명이 이어지지 않는 곳을 적는다.
- 결과 문안: 막힌 곳 | 위치 | 왜 막혔는지 | 필요한 설명 | 확신
```
**.claude/agents/reader-expert.md**
```markdown
---
name: reader-expert
description: 에이전트를 실무에서 쓰는 개발자 관점에서 부정확하거나 얕은 곳을 찾는다. 마무리 단계에 사용.
tools: Read, Grep, Glob, WebSearch, WebFetch
model: sonnet
---
너는 코딩 에이전트를 실무에서 쓰는 개발자다. 원고와 파일을 고치지 않는다.
- 기술적으로 부정확하거나, 지나치게 단순하거나, 실무와 다른 곳을 근거와 함께 적는다.
- 결과 문안: 발견 | 위치 | 근거 | 제안 | 확신
```

### 3-7. 명령(.claude/commands/)
- 삭제: `reader-sim.md`(review-chapter에 포함)
- 아래 5개 파일로 교체하거나 새로 만든다.

**.claude/commands/plan-chapter.md**
```markdown
---
description: 장 계획: 조사와 개요를 만들고 작가 확인을 받는다
---
Chapter $ARGUMENTS의 계획을 세운다.
1. HANDOFF.md, BOOK_SPEC.md의 이 장 계획, DECISIONS.md 마지막 10건을 읽는다.
2. researcher 하위 에이전트에 장의 주장과 근거 조사를 맡기고, 결과를 research/에 저장한다.
3. 장 틀(주장 제목 → 원리 → CR 적용 → 실패 표 → 확인 방법 → 원칙 한 문장 → 점검 질문)에 맞춘 개요를 만든다.
4. 개요를 작가에게 보여 주고 확인을 받는다. 확인 전에는 원고를 쓰지 않는다.
```
**.claude/commands/write-chapter.md**
```markdown
---
description: 장 작성: 원고와 그림을 쓰고 점검한 뒤 PR을 만든다
---
Chapter $ARGUMENTS를 작성한다(작가가 확인한 개요 기준).
1. 작업 브랜치를 만든다(git switch -c ch$ARGUMENTS-write).
2. src/의 원고와 그림을 쓴다. 그림은 FIGURE_STYLE.md를 따른다.
3. python tools/check_all.py를 통과시킨다.
4. fact-checker, flow-reviewer, figure-checker, reader-novice를 동시에 부르고, 보고 문안을 reviews/agents/에 저장한다.
5. 의견을 반영, 보류, 작가 확인으로 나누어 반영하고 다시 check_all을 통과시킨다.
6. HANDOFF.md를 갱신하고 커밋한 뒤, 작가 확인을 받아 브랜치를 push하고 PR을 만든다. PR 설명에 check_all 출력 원문과 의견 분류 표를 넣는다.
```
**.claude/commands/apply-review.md**
```markdown
---
description: 검수 지침 반영: 지침대로 고치고 반영 n / n을 확인한다
---
검수 문서 $ARGUMENTS를 반영한다.
1. 문서를 읽고, "교체" 코드 상자의 내용만 옮긴다. 표의 이유 칸과 설명은 옮기지 않는다.
2. 지시하지 않은 변경은 하지 않는다.
3. python tools/check_all.py와 python tools/check_review.py $ARGUMENTS를 통과시킨다(반영 n / n).
4. 검수 문서를 reviews/에 별도 커밋으로 등록하고, HANDOFF.md를 갱신한다.
5. 작가 확인을 받아 같은 PR에 push하고, 출력 원문을 PR에 댓글로 남긴다.
```
**.claude/commands/handoff.md**
```markdown
---
description: 세션 인계: HANDOFF.md를 지금 상태로 갱신한다
---
HANDOFF.md를 갱신한다. 항목: 날짜, 브랜치와 열린 PR, 이번 세션에 한 일(커밋), 검사 결과(check_all 요약), 다음 할 일, 미결정, 주의할 점.
같은 실패가 두 번째 나왔으면 FAILURES.md에도 한 행을 추가한다.
```
**.claude/commands/review-chapter.md**
```markdown
---
description: PR 전 점검: 하위 에이전트 점검을 한 번에 실행한다
---
Chapter $ARGUMENTS에 대해 fact-checker, flow-reviewer, figure-checker, reader-novice를 동시에 부른다.
각 결과를 reviews/agents/YYYY-MM-DD-ch$ARGUMENTS-<에이전트>.md로 저장하고, 반영, 보류, 작가 확인으로 나눈 표를 보여 준다. 원고는 고치지 않는다.
```

### 3-8. 기록 파일(새 파일)
**HANDOFF.md**
```markdown
# 인계(HANDOFF)

- 갱신: 2026-10-19
- 브랜치: harness-setup(PR 예정)

## 지금 상태
- 작업 장소를 Claude Code(VS Code)로 옮기는 중. 하네스 설정(Step 2)을 반영하는 PR을 만드는 단계.
- 원고는 2026-10-19 결정(장 틀, CR 이름)에 따라 1장부터 다시 쓴다.

## 다음 할 일
1. Step 3 장치 작동 시험(HARNESS_SETUP.md 4절)
2. 1장 시범: /plan-chapter 1 → /write-chapter 1

## 미결정
- 그림 글자 크기 기준 미달 그림 8개(2-2, 4-2, 5-2, 6-2, 7-2, 8-2, 9-2, 11-1): 해당 장을 다시 쓸 때 고치고, 모두 고치면 check_all을 --strict-figures로 바꾼다.

## 주의할 점
- main에서 작업하지 않는다. 결정 기록 수정과 push는 작가 확인 후.
```
**FAILURES.md**
```markdown
# 실패 기록(FAILURES)

같은 실패가 두 번째 나오면 한 행을 추가하고, 원인이 된 구성 요소와 추가한 장치를 적는다.

| ID | 실패 | 반복 | 원인 구성 요소 | 추가한 장치 | 상태 |
|---|---|---|---|---|---|
| F-01 | 검수 지침이 일부만 반영되거나 반영 전 판이 들어감 | 생성형 AI 책과 이 책에서 여러 차례 | 검증 | check_review(반영 n / n), PR과 CI 필수 | 장치 추가 |
| F-02 | 검수 문서의 설명문, 이유가 원고에 섞임 | 여러 차례 | 역할 | 지침은 "교체" 코드 상자만 옮김(CLAUDE.md, /apply-review) | 장치 추가 |
| F-03 | 작가 승인 없는 큰 변경과 지시하지 않은 변경 | 2026-10-15 작성 세션 교체 | 권한 | main 반영 금지(설정, 훅, 브랜치 보호), push와 PR은 확인 | 장치 추가 |
| F-04 | 문장을 끼워 넣다가 앞뒤 연결이 끊기거나 같은 내용이 겹침 | 생성형 AI 책 26건 | 검증 | flow-reviewer, 이웃 문장 중복 점검 | 장치 추가 |
| F-05 | 장치(에이전트, 훅, Skill)를 설치만 하고 쓰지 않음 | 이 책 전체 기간 | 도구 | Step 3 작동 시험, 세션 시작 훅 | 장치 추가 |
| F-06 | 원고를 여러 곳(채팅, Cowork, 여러 세션)에서 고침 | 이 책 전체 기간 | 역할 | 원고를 쓰는 주체는 하나(멀티 에이전트 작업 공간 규칙) | 장치 추가 |
| F-07 | 세션을 바꾸며 미커밋 변경과 맥락이 사라짐 | 2026-10-15 | 기록 | HANDOFF.md, 종료 훅의 인계 확인 | 장치 추가 |
| F-08 | 그림 방침이 여러 번 바뀌어 재작업 | 2026-10-15~18 | 기록 | FIGURE_STYLE.md, 결정마다 대체 관계 기록 | 장치 추가 |
| F-09 | 그림 글자가 모바일에서 작음 | 그림 8개 | 검증 | check_all 그림 글자 크기 점검(경고에서 시작) | 진행 중 |
| F-10 | 핵심 정의와 용어가 집필 중 흔들림(하네스 정의, 세 설계 층) | 여러 차례 | 역할 | 정의와 용어 변경은 작가에게 먼저 물음(CLAUDE.md) | 장치 추가 |
| F-11 | 제품 기능 사실 오류(권한 모드 기본값, 승인 정책) | 이 책 2차 검수 | 검증 | fact-checker, research/ 출처 기록 | 장치 추가 |
| F-12 | 저장소에 없는 파일을 저장소 구성으로 설명 | 생성형 AI 책 README | 검증 | 저장소 구성은 git ls-files 기준 | 규칙 |
```
- reviews/agents/ 폴더를 만들고 빈 파일 `.gitkeep`을 둔다.
- .gitignore에 `.claude/settings.local.json`과 `.claude/last_check_failed.txt`를 추가한다.

### 3-9. CI 교체(.github/workflows/check.yml 전체)
```yaml
# PR과 main push마다 전체 검사를 실행한다. 브랜치 보호에서 이 검사를 필수로 지정한다.
name: book-check
on:
  pull_request:
  push:
    branches: [main]
jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: "3.12" }
      - name: 전체 검사(빌드, 금칙어, lint, 그림, 빌드 결과와 커밋 일치)
        run: python tools/check_all.py --ci
```

### 3-10. 결정 기록(DECISIONS.md, 작가 확인 후 다음 번호로 추가)
1. 원고 작업은 VS Code의 Claude Code에서만 한다. 검수 Project(Claude App)는 읽기와 검수 문서 작성만 하고, 채팅과 Cowork에서는 원고를 바꾸지 않는다.
2. 멀티 에이전트 작업 공간 규칙(CLAUDE.md의 같은 절)을 따른다. 하위 에이전트는 6개(researcher, fact-checker, flow-reviewer, figure-checker, reader-novice, reader-expert)이고 모두 읽기만 한다.
3. main 반영은 PR과 CI 통과 뒤 작가 병합으로만 한다(설정, 훅, 브랜치 보호로 강제).
4. 작업 종료 전 check_all 통과와 HANDOFF.md 갱신을 Stop 훅으로 강제한다. 반복 실패는 FAILURES.md에 기록한다.
5. 그림 글자 크기 점검은 경고로 시작하고, 미달 그림 8개를 고친 뒤 실패로 바꾼다(--strict-figures).

### 3-11. 검사, 커밋, PR
```bash
python tools/build.py
python tools/check_all.py
git add -A
git commit -m "chore: 책 작업 하네스 설정(CLAUDE.md, 설정과 훅, 하위 에이전트 6개, 명령 5개, check_all, check_review, HANDOFF, FAILURES, CI)"
git push -u origin harness-setup
gh pr create --base main --head harness-setup --title "책 작업 하네스 설정(Step 2)" --body-file HANDOFF.md
```
- push와 PR 생성은 설정에 따라 작가 확인을 요구한다.
- 보고: check_all 출력 원문, `git status --short`(비어 있어야 함), PR 주소, CI 결과(`gh pr checks`)

**검수 쪽 시험 결과(이 문서의 스크립트, 시험용 사본에서)**
```
check_all(현재 원고)            → 빌드, 금칙어, 번호, 구조, 문체, 그림 안 이름 모두 통과, exit 0
                                  [경고] 그림 글자 크기 미달 8개(2-2, 4-2, 5-2, 6-2, 7-2, 8-2, 9-2, 11-1)
check_all(원고에 금칙어 "잘 " 주입) → 금칙어 실패, exit 1
stop_check(원고 변경, HANDOFF 없음) → exit 2, "HANDOFF.md를 갱신하지 않았습니다"
stop_check(같은 멈춤 두 번째)       → exit 0, .claude/last_check_failed.txt 기록, 다음 세션 시작 때 표시
stop_check(변경 없음)              → exit 0
pre_bash: main에서 git commit      → exit 2 / git push --force → exit 2 / git push origin main, HEAD:main → exit 2
pre_bash: 작업 브랜치 commit, push   → exit 0 / git push origin main-fix → exit 0
check_review(11차 문서)            → 반영 9 / 11(이후 D-095로 바뀐 2건을 미반영으로 정확히 표시)
```
- 시험 중 발견해 고친 것: 금칙어 목록의 끝 공백("잘 ")을 지우면 "잘못"까지 잡는 오판이 생겨, 줄 끝 공백을 패턴의 일부로 유지하도록 고쳤다.

---

## 4. 작동 시험(Step 3, PR 병합 뒤 새 세션에서)
| # | 시험(Claude Code에 입력하거나 실행) | 기대 결과 |
|---|---|---|
| 1 | 새 세션 시작 | 세션 시작 훅 출력: 현재 브랜치, HANDOFF.md, 최근 결정 10건 |
| 2 | "CLAUDE.md의 역할과 멀티 에이전트 작업 공간 규칙을 요약해 줘" | 메인 세션 역할, 하위 에이전트 6개, 쓰기 범위 |
| 3 | main 브랜치에서 "아무 파일이나 고쳐 커밋해 줘" | PreToolUse 훅이 막음("main 브랜치에서는 커밋하지 않습니다") |
| 4 | "git push origin main을 실행해 줘" | 설정 deny 또는 훅이 막음 |
| 5 | 작업 브랜치에서 src/chapters/ch02.html에 "잘 되는"을 넣게 한 뒤 끝내기 | 파일 수정 뒤 훅이 경고, 끝낼 때 Stop 훅이 막음 |
| 6 | "flow-reviewer로 1장을 점검해 줘" | 하위 에이전트가 파일을 고치지 않고 보고 문안만 돌려줌 |
| 7 | GitHub 웹에서 main에 직접 push 시도(또는 작가 PC에서 `git push origin main`) | 브랜치 보호가 거부 |
- 결과(출력 원문)를 HANDOFF.md에 적고, 기대와 다른 항목은 FAILURES.md에 적는다. 시험 5의 변경은 되돌린다.

## 5. 미결정(작가)
1. 1절 시작 정의 승인
2. 2절 브랜치 보호 설정(승인 수 0, 작가 병합이 승인)
3. 3-10 결정 기록 5건 승인
