# 시작하며, 마치며, 부록 사실 확인 2차(fact-checker)

# 사실 확인 보고: 시작하며, 마치며, 부록 실습, 부록 용어 (브랜치 front-back-write, PR #45, 개정 후)

확인일: 2026-10-20. 파일은 고치지 않았습니다.

## 확인 범위와 한계
- **직접 열어 확인한 주소**: Claude Code Docs의 commands, hooks, hooks-guide, quickstart, cli-reference, security, permissions, permission-modes, memory, context-window, costs, setup, tools-reference, sandboxing, terminal-guide. claude.com/pricing. github.com/seoulkorea-dev/harness-book의 루트, examples/expense-app, reference/ 목록과 main의 tasks.example.json, RUNLOG.md.
- **열지 못한 주소**: developers.openai.com, arxiv.org, git-scm.com은 DNS 오류(getaddrinfo ENOTFOUND)로 열리지 않았습니다. 이 주소에 의존하는 문장은 미확인으로 처리했습니다.
- **본문 대조**: src/chapters/ch01~ch11.html에서 해당 문장과 앵커를 읽고 대조했습니다. 앵커 id는 모두 실제 id와 맞습니다(ch01#meanings, #layers, #loop, #agent-harness, #harness, #prompt-context / ch02#components, #tool-scope, #instruct-enforce / ch03#spec, #example / ch04#elements / ch05#rule-doc, #kinds, #resource / ch06#split, #multi-agent, #selection / ch07#criteria, #methods, #check / ch08#session, #kinds, #decisions, #handover, #logs / ch09#approval, #permissions, #isolation, #cost / ch10#criteria, #rule-docs, #perm-claude, #perm-codex / ch11#failures, #this-book, #this-book-grow, #steps).
- **실행 한계**: 실행 도구가 없어 `python check.py`를 직접 돌리지 못했습니다. check.py, tests/test_basic.py, acceptance/test_cr07.py, app.py, views.py, CLAUDE.example.md, reviewer.example.md, settings.example.json, tasks.example.json, CR.md, DECISIONS.md를 읽고 논리로만 대조했습니다.

## 개정 전 필수 8건의 해소 여부
| 개정 전 | 상태 | 확인 근거 |
|---|---|---|
| P1 책 두 권 기록 공개 | 해소 | 목적 셋째 항목이 "이 책의 저장소 / 앞선 책의 정리는 Chapter 11"로 나뉨. 공개 저장소 루트에 DECISIONS.md, FAILURES.md, reviews/, research/, CLAUDE.md가 있음(2026-10-20 확인). 단, 링크 앵커는 아래 P2. |
| E1 2장 원칙 | 해소 | 마치며 11개 원칙 문장이 ch01~ch11의 `p.principle`과 글자까지 같음(정규식으로 11개 모두 일치 확인). |
| L1 상위 CLAUDE.md, .claude 혼입 | 해소(문구는 아래 L4) | 실습 1이 저장소 밖 복사와 git init으로 바뀜. 저장소 루트에 CLAUDE.md와 .claude/가 실제로 있어 복사가 필요함. memory 문서 "above the working directory are loaded at launch". |
| L2 원격 연결된 폴더 | 해소 | 복사 폴더는 git init만 해서 원격이 없음. ch10.html 100행 "원격 저장소에 연결되지 않은 연습 폴더"와 맞음. |
| L3 훅 성공 출력 | 부분 해소 | "성공한 훅은 대화에 출력이 보이지 않음"은 hooks 문서와 일치. "실패하면 오류 알림이 대화에 보임"은 미확인(아래 L8). |
| L4 수정 시도 요청 | 해소 | 실습 2의 둘째 요청과 실습 3의 첫째 요청이 같은 대상(acceptance/test_cr07.py)이라 2장 58행과 맞음. 완화 문구("막지 못할 수 있으며")도 있음. |
| L5 종료 코드 0 위치 | 부록 쪽 해소 | 실습 5가 종료 코드 1을 정상, 0은 실습 6으로 적음. 단 ch03.html 123행(표 3-6)은 아직 `#lab-5` 링크(장 쪽, v1.1-backlog, 아래 L16). |
| T1 에이전트 정의 | 해소 | ch01.html 37행과 같음("다음 행동을 스스로 정하고"). |

개정 전 권장 중 해소: 인계 메모 5항목(ch08 39행), 수용 기준과 완료 기준 구분, 샌드박스(ch09 23~24행, 기본 꺼짐, 파일 편집 도구 제외), 토큰의 Codex `/status` 삭제, `python3` 대체 안내, localhost 주소와 Ctrl+C, 종료 코드 확인 명령(echo $?, $LASTEXITCODE), `/context`, `/hooks`, `/memory`, `/usage` 단계 추가, 발표 주체 문장("Anthropic 문서는 … 안내합니다"), 용어 보강(프롬프트, 실패 기록, 승인 지점, 격리, 지시와 강제, 에이전트 명세서, 실행 로그, 세션, Skill의 "절차 묶음").

---

## 시작하며 (src/chapters/prologue.html)
| # | 심각도 | 발견 | 위치 | 근거 | 제안 | 확신 |
|---|---|---|---|---|---|---|
| P1 | 필수 | 판정 불일치. "첫 문단 아래의 요점 상자는 그 장의 요점을 세 줄로 정리합니다"가 1장과 어긋납니다. 1장 요점 상자는 네 줄입니다. | 이 책의 활용법 34행 | ch01.html 4행 `ul.summary`의 li가 4개(ch02~ch11은 각 3개). | "세 줄"을 "몇 줄"로 바꾸거나 1장 예외(네 줄)를 덧붙입니다. 장 쪽을 줄이는 일은 작가 결정이라 이 PR에서는 시작하며를 고치는 쪽을 권합니다. | 높음 |
| P2 | 권장 | 링크가 문장 내용을 설명하지 않습니다. "앞선 책을 함께 만든 과정의 정리는 Chapter 11"의 링크가 `ch11.html#this-book`인데, 이 절은 "이 책 저장소의 하네스"입니다. 앞선 책의 정리는 `#failures`(5~17행)에 있습니다. | 목적 셋째 항목 9행 | ch11.html 5행, 18행 절 제목. | 링크를 `ch11.html#failures`로 바꿉니다. | 높음 |
| P3 | 참고 | 근거 없는 일반화 두 곳입니다. "도구와 기능은 계속 변경되어도 … 새 제품에도 같은 방식으로 적용할 수 있습니다", "에이전트에게 일을 맡기는 능력은 … 환경을 이렇게 설계하는 데서 나옵니다". 발표 주체와 출처가 없고, 10장이 비교하는 제품은 두 개뿐입니다(STYLE 1). | 이 책이 전하는 것 5~6행 | ch10.html, ch01.html 51행. | "이 책은 두 제품(Codex, Claude Code)에 같은 구성 요소를 적용해 보입니다"처럼 본문이 뒷받침하는 범위로 줄이거나 삭제합니다. | 중간 |
| P4 | 참고 | 일치로 확인한 항목입니다. 하네스 정의와 여섯 기능, 프롬프트와 컨텍스트 한 구절, 열한 개 장, 묶음 구성(1~3, 4~5, 6~9, 10~11), 구성 표와 "읽고 나면 할 수 있는 일" 표의 링크, 장 틀 예외(1장 표 1-8 증상별 원인 층, 11장 작가 두 책), 실패 표(2~10장의 `#fail`, 11장 표 11-1), 점검 질문 세 개, 원칙 한 문장, CR 소개(ch03.html 21행과 같은 표현, 첫 등장 규칙 충족), "버전 주석" 설명(STYLE 5와 일치), 공개 저장소. | 전체 | 위 본문 위치, GitHub 루트 목록. | 조치 없음. | 높음 |

## 마치며 (src/chapters/epilogue.html)
| # | 심각도 | 발견 | 위치 | 근거 | 제안 | 확신 |
|---|---|---|---|---|---|---|
| E1 | 권장 | 구조 서술이 모호합니다. "확인 방법은 각 장의 확인 방법 표에 있습니다. Chapter 1은 표 1-8의 증상별 원인 층으로 점검합니다"는 1장에 확인 방법 표가 없는 것처럼 읽힙니다. 1장의 확인 방법 표는 표 1-9이고(`#check`), 표 1-8은 `#manager` 절의 증상별 원인 표(점검 질문 3이 사용)입니다. | 장별 원인 첫 문단 4행 | ch01.html 116행, 133~139행, 143행. | "Chapter 1은 표 1-9로 확인하고, 표 1-8의 증상별 원인 층으로 점검합니다"로 씁니다. | 중간 |
| E2 | 참고 | 첫 문장 "설계할 것은 모델이 아니라"가 표 1-5와 어긋나게 읽힙니다. 표 1-5는 모델 층에도 설계 질문("어느 모델을 사용할지")을 둡니다. 1장 66행은 모델을 공급사가 제공하는 실행 엔진으로 봅니다. | lead 2행 | ch01.html 66행, 69~72행. | "설계할 것은 모델에 보내는 요청과 …"처럼 모델 선택과 충돌하지 않게 씁니다. | 낮음 |
| E3 | 참고 | 일치로 확인한 항목입니다. 열한 개 장별 원칙 문장이 각 장 본문과 글자까지 같습니다(2장 포함). 11장 개선 순서의 네 단계와 첫 발생 예외(ch11.html 53행의 "위험이 큰" 중 되돌리기 어려운 쪽), 결정 기록. | 5행, 7행 | 정규식 일치 11/11. | 조치 없음. | 높음 |

## 부록 실습 (src/appendix/practice.html)
| # | 심각도 | 발견 | 위치 | 근거 | 제안 | 확신 |
|---|---|---|---|---|---|---|
| L1 | 권장 | 설명이 일부만 맞습니다. "Git for Windows가 있으면 Claude Code는 셸 명령을 Git Bash로 실행하고, 이 경우 … 금지 규칙이 그대로 적용됩니다". Git Bash가 있어도 claude.ai와 Console 계정에서는 PowerShell 도구가 기본으로 함께 켜집니다. 금지 규칙이 유지되는 이유는 Bash 금지 규칙이 있으면 PowerShell 도구가 꺼지기 때문입니다. 결론은 맞고 이유 서술이 빠졌습니다. | 실습 준비 10행 | tools-reference 문서 PowerShell tool 절("on by default for claude.ai and Console accounts", "Bash deny rules also turn off the PowerShell tool"), setup 문서 Set up on Windows, 2026-10-20 확인. | "Git Bash를 쓰며, Bash 금지 규칙이 있으면 PowerShell 도구가 꺼져 금지 규칙이 유효합니다"로 바꿉니다. | 높음 |
| L2 | 권장 | 근거 없는 판단입니다. "요금이 정해진 Pro 요금제가 사용량을 예측하기 쉽습니다". 비용 문서는 구독 사용량이 요금제 한도 안에 포함된다고만 하고 예측 용이성은 말하지 않으며, 사용 크레딧으로 한도 이후에도 쓸 수 있다고 합니다. | 실습 준비 6행 | costs 문서 Plan usage breakdown, Add usage credits 절. | 삭제하거나 "Pro는 사용량이 요금제 한도 안에 포함된다고 Anthropic 문서가 안내합니다(…)"로 바꿉니다. | 중간 |
| L3 | 권장 | 참조 연결이 어긋납니다. "Pro 이상의 유료 요금제나 Claude Console의 API 키로 사용하며"의 인용이 Plans & pricing(2026a)뿐입니다. 요금제 부분(Free 미포함, Pro 포함)은 pricing과 일치하지만, Console 계정은 Set up(2026b)의 Authenticate 절에 있습니다. | 실습 준비 6행 | pricing("Claude Code is included in all paid plans"), setup 문서 Authenticate 절. | 인용에 2026b를 함께 답니다. | 높음 |
| L4 | 권장 | 일반화가 사용자 환경에 따라 틀릴 수 있습니다. "이 폴더와 그 위 폴더에는 아직 CLAUDE.md와 .claude/ 폴더가 없습니다". 실습 1이 안내하는 위치("홈 폴더처럼")의 상위 폴더는 Claude Code를 설치해 로그인하면 `~/.claude/`(사용자 설정, 사용자 CLAUDE.md 위치)가 생깁니다. 부모 폴더의 `.claude/settings.json`이 하위 폴더 세션에 적용되는지는 settings 문서에서 찾지 못했습니다(S-FB-14 c, 여전히 미확인). | 실습 1 확인 방법 4항 | memory 문서의 CLAUDE.md 계층, 사용자 범위 표. | "이 폴더에는 …"로 줄이고 "사용자 설정 폴더(~/.claude)는 모든 프로젝트에 적용된다"를 덧붙이거나, 위 폴더 서술을 뺍니다. | 중간 |
| L5 | 권장 | 실행 범위를 과대 표기합니다. "실습 1은 2026년 10월 20일에 실행해 기록했고". RUNLOG 2026-10-20 기록은 `cp -r`, `git init`, `git add`, `git commit`, `git log`, `unittest`, `check.py`, `echo $?`까지입니다(Linux, python3). `git clone`, `git config --global`, `python app.py`와 브라우저 확인, PowerShell의 `Copy-Item`과 `$LASTEXITCODE`, Git Bash 확인은 기록에 없습니다. 출력 예(FAILED (failures=3) 등 세 줄)는 RUNLOG 39~41행과 일치합니다. | 실습 준비 20행, 실습 1 | RUNLOG.md 16~46행. | "실습 1의 복사, git init, 첫 commit, 단위 테스트, check.py는 … 실행해 기록했습니다(Linux, python3)"처럼 범위를 밝힙니다. | 높음 |
| L6 | 권장 | 권한 모드를 밝히지 않아 확인 요청 화면이 나오지 않을 수 있습니다. v2.1.283 이상의 터미널은 auto로 시작하고, auto에서는 작업 폴더 안의 파일 수정이 자동 승인되며 판단은 분류기가 합니다. 그러면 실습 2의 "수정 확인을 묻는 화면이 나오면 거절", 실습 3의 "확인 요청이 나오면 거절"에 해당하는 화면이 없을 수 있고, 실습 2의 둘째 요청은 규칙 문서 외에는 막는 장치가 없어 실제로 시험이 삭제될 수 있습니다. 본문은 `git status`와 `git restore acceptance/`로 보호했고, 실습 3의 deny 규칙은 모든 모드에서 유효합니다. 부족한 것은 기대 화면 서술입니다. 같은 이유로 실습 3 확인의 "세 요청 모두 … 거부"도 스크립트 우회가 있으면 성립하지 않을 수 있습니다(바로 아래 4항이 완화함). | 실습 2 단계 6, 확인 2항, 실습 3 단계 4, 확인 2항 | permission-modes 문서(Which mode a session starts in, auto mode의 파일 수정, ask/deny 규칙), security 문서. 10장 버전 주석(ch10.html 33행)과 같은 내용. | 실습 준비나 실습 2에 "Claude Code 버전과 권한 모드에 따라 확인 화면이 나오지 않고 수정이 적용될 수 있다, 이때 git restore로 되돌린다"와 10장 버전 주석 링크를 한 줄 넣습니다. | 중간 |
| L7 | 권장 | 새로 쓴 제품 동작 문장에 발표 주체와 링크가 없습니다(STYLE 4). "처음에는 이 폴더를 신뢰하는지 묻는 화면"(security), "/context … 메모리 파일 항목"(commands, context-window), "/hooks"(hooks), "성공한 훅은 대화에 출력이 보이지 않으며"(hooks), "/memory"(commands, memory), "/usage … 정가 기준의 추정치"(costs). 사실은 모두 문서와 일치하지만 참고 자료는 2026a~c뿐입니다. | 실습 2 단계 4~5, 실습 4 확인 1항, 실습 6 단계 4와 확인 1항 | 각 문서(S-FB-6, 10, 15~19 아래 기록). | "Anthropic 문서에 따르면 …"로 주체를 밝히고 참고 자료에 Commands, Hooks, Security를 추가합니다. | 높음 |
| L8 | 참고 | 미확인 문장입니다. "테스트가 실패하면 훅의 오류 알림이 대화에 보이고". `|| exit 2`로 종료 코드 2가 나면 PostToolUse는 "Shows stderr to Claude; the tool already ran"만 문서에 있고, 사용자 화면에 `hook error` 알림이 뜨는지는 명시되지 않았습니다(`hook error` 알림이 명시된 경우는 종료 코드 0, 2 외의 비차단 오류와 SessionStart 등). "에이전트가 그 알림을 받습니다"는 일치합니다. 2장 표 2-6, 3장 표 3-6의 같은 서술도 같은 한계입니다. | 실습 4 확인 1항 | hooks 문서 Exit code 2 behavior per event, hooks-guide Fix common problems(Ctrl+O로 transcript 확인). 찾은 범위: hooks 문서 앞 200,000자, hooks-guide 전체. | 실행 전 서술이므로 "에이전트가 실패 출력을 받아 응답에서 테스트 실패를 언급합니다"로 줄이고, 실습 4 실행 때 화면을 RUNLOG에 남겨 확정합니다. | 중간 |
| L9 | 참고 | "/hooks 목록에 단위 테스트 명령이 등록된 훅이 보입니다"는 문서와 약간 다릅니다. 문서는 목록이 이벤트별로 훅을 보여 주고, 훅을 선택해야 실행 명령 전문이 보인다고 합니다(읽기 전용). 3장 표 3-6은 "선택하면 단위 테스트 명령이 보임"으로 맞습니다. | 실습 4 확인 1항 | hooks 문서 The /hooks menu 절, hooks-guide. | "PostToolUse 아래에 훅이 있고, 선택하면 단위 테스트 명령이 보입니다"로 3장과 맞춥니다. | 높음 |
| L10 | 참고 | `/context`가 CLAUDE.md 적재를 보여 준다는 서술은 일치합니다("including which CLAUDE.md and auto memory files loaded"). 다만 화면의 "메모리 파일" 항목 이름은 문서에서 찾지 못했고(S-FB-14 d, 실행 때 확인), 전체 화면(fullscreen)에서는 항목별 내역이 접히며 `/context all`로 펼친다고 합니다. | 실습 2 단계 5 | commands 문서 `/context [all]`, context-window 문서 끝 절. | 이 PR 범위에서는 조치 없음. 실습 2 실행 때 RUNLOG에 화면을 남깁니다. | 중간 |
| L11 | 참고 | 미확인입니다. "중괄호와 대괄호의 짝, … 어긋나면 Claude Code가 설정을 읽지 못합니다". settings 문서를 열지 않았습니다. `claude doctor`가 설정 파일 검증 오류를 보여 준다는 것(cli-reference)만 확인했습니다. | 실습 3 단계 2 | 찾은 범위: setup 문서의 `claude doctor`, cli-reference. | 실습 3 실행 때 증상을 RUNLOG에 남깁니다. | 낮음 |
| L12 | 참고 | 터미널 여는 법이 공식 안내와 다릅니다(오류는 아님). 공식은 Windows `Win + X`에서 Windows PowerShell, macOS `Cmd + Space`로 Spotlight에서 Terminal입니다. 책은 "시작 메뉴에서 PowerShell이나 Git Bash", "응용 프로그램의 유틸리티 폴더"라고 씁니다. 일반 지식으로는 맞지만 1차 출처로 확인한 문장이 아닙니다. | 실습 준비 10행 | terminal-guide 문서. | 공식 방법을 쓰거나 그대로 둡니다. | 높음 |
| L13 | 참고 | 미확인입니다. "--global은 이 컴퓨터의 모든 Git 저장소에 적용한다는 뜻입니다". git-scm 문서가 열리지 않아 확인하지 못했습니다. `--global`은 현재 사용자 범위(`~/.gitconfig`)라 "이 컴퓨터의 모든"보다 "현재 사용자의 모든"이 정확합니다(일반 지식, 1차 출처 미확인). | 실습 준비 16행 | git-scm.com DNS 오류. | git 문서 확인 뒤 "현재 사용자의 모든 Git 저장소"로 바꿉니다. | 낮음 |
| L14 | 참고 | 수정 범위 서술이 CLAUDE.example.md보다 좁습니다. 실습 5 본문의 "수정 범위 안(expense/, tests/, tasks.json)"은 CLAUDE.example.md 19~21행의 "expense/, app.py, tests/, tasks.json의 '통과' 값, HANDOFF.md"에서 app.py와 HANDOFF.md가 빠졌습니다. | 실습 5 단계 2 아래 문단 | reference/CLAUDE.example.md 19~21행. | "수정 범위(CLAUDE.md의 수정할 수 있음 목록)"로 바꾸거나 app.py를 넣습니다. | 높음 |
| L15 | 참고 | RUNLOG 표와 실습 본문이 다릅니다. RUNLOG "실습 5 … 기록할 것: check.py 출력, tasks.json 변경, commit 확인 요청, /usage"인데 실습 5 본문에는 `/usage` 단계가 없고 실습 6 단계 4에만 있습니다. | RUNLOG.md 56행 ↔ practice.html 87~92행 | 두 파일. | RUNLOG의 기록 항목을 실습 6으로 옮기거나 실습 5에 단계를 넣습니다. | 높음 |
| L16 | 참고 | 장 쪽 불일치가 남아 있습니다(알려진 backlog). ch03.html 123행 표 3-6의 "모든 작업 단위를 마친 뒤 종료 코드 0" 행이 `#lab-5`로 링크되지만 실습 5는 종료 코드 1이 정상이고 0은 실습 6입니다. ch02.html 58행은 "규칙 문서만 있는 상태에서는 … 막지 못하고"로 단정하지만 실습은 "막지 못할 수 있으며"입니다. | 실습 5 확인 1항, 실습 2 확인 2항 | ch03.html 123행, ch02.html 58행. | v1.1-backlog 항목으로 유지합니다. | 높음 |
| L17 | 참고 | 병합 전에는 clone에 이 PR의 변경이 없습니다. 지금 main에는 examples/expense-app(reference/ 네 파일, tasks.example.json 작업 1 true, RUNLOG.md 2026-10-16 기록만)이 있어 실습은 따라 할 수 있지만, 실습 준비 20행이 말하는 2026-10-20 기록은 병합 뒤에 clone에 들어옵니다. 저장소는 로그인 없이 열리는 공개 저장소입니다. | 실습 준비 20행 | github.com/seoulkorea-dev/harness-book(2026-10-20 확인). | 병합 뒤 한 번 더 확인합니다. | 높음 |

**실습에서 일치로 확인한 항목**: 실습 1의 출력 예 세 줄(RUNLOG 39~41행)과 확인 방법(unittest 마지막 줄 OK, tests 3건 통과, acceptance 5건 중 3건(test_1~3) 실패, 종료 코드 1). 앱 주소와 종료(app.py 40~41행, `/new` 라우트). `Copy-Item -Recurse`와 `cp -r`의 의미. tasks.example.json은 작업 1만 true, 나머지 false이고 키는 id, 작업, 완료 기준, 확인 방법, 통과(실습 5 본문과 일치). 작업 1은 D-012(DECISIONS.md, 2026-10-12)로 마침. 실습 5의 "첫 false 작업은 작업 2"는 CLAUDE.example.md 규칙과 일치. 실습 4의 첫 요청("요청자 열을 빼 줘")이 `test_list_shows_requesters`를 실제로 깨뜨림(views.py 13행, test_basic.py 31~34행). reviewer.md의 `tools: Read, Grep, Glob`. 기준 1~3 미충족이 실습 1의 test_1~3과 대응(CR.md). 훅 `|| exit 2`, `python3` 대체 안내. claude --continue(cli-reference: 현재 폴더의 가장 최근 대화). 첫 실행 로그인(quickstart, setup). 폴더 신뢰 확인(security: 신뢰하지 않은 폴더에서 시작할 때). `/permissions`(규칙과 출처 settings.json 표시), 평가 순서 deny → ask → allow, 편집 금지 규칙의 Bash 출력 리디렉션 검사. PowerShell 설치 명령. `/memory`(자동 메모리 항목 열람), 자동 메모리 기본 켜짐과 저장소 단위 공유. `/usage` 금액은 정가 기준 추정치이고 구독 사용자에게는 세션 금액이 청구 근거가 아님(costs). `/exit`. 막혔을 때 절의 항목.

## 부록 용어 (src/appendix/terms.html)
| # | 심각도 | 발견 | 위치 | 근거 | 제안 | 확신 |
|---|---|---|---|---|---|---|
| T1 | 필수 | 판정 불일치. 실패 기록 정의가 본문보다 좁습니다. 용어집은 "같은 종류가 두 번째로 나온 실패와 원인 구성 요소, 추가한 장치를 적은 문서"인데, 링크한 절(`#this-book-grow`)은 "같은 종류의 실패가 다시 나오거나 위험이 큰 실패가 나오면 … 실패 기록(FAILURES.md: 실패와 원인 구성 요소, 추가한 장치를 적은 문서)에 한 행을 남기고", 53행은 "위험이 큰 실패는 첫 발생도 올렸습니다"라고 합니다. | 실패 기록 항목 | ch11.html 33행, 53행. | 본문 정의를 그대로 씁니다. 예: "실패와 원인 구성 요소, 추가한 장치를 적은 문서입니다. 같은 종류가 다시 나온 실패와 위험이 큰 실패를 올립니다. 이 책의 저장소에서는 FAILURES.md입니다." | 높음 |
| T2 | 권장 | AGENTS.md 항목의 조건과 버전은 문서와 일치하지만 형식과 출처가 STYLE 4, 5에 맞지 않습니다. "(v2.1.277 이상, 2026년 10월 확인)"을 괄호 안에 넣었을 뿐 `aside.footnote`의 "버전 주석 (2026년 10월)"이 아니고, 발표 주체와 참고 자료 링크도 없습니다. 5장과 10장(ch10.html 27행)은 버전 주석 상자와 출처 링크를 씁니다. | AGENTS.md 항목 | memory 문서 AGENTS.md 절("Reading AGENTS.md directly requires Claude Code v2.1.277 or later", "reads AGENTS.md only when you have no CLAUDE.md … in your working directory or above"), ch10.html 20행, 27행. | 주석 상자로 옮기고 Anthropic 문서(ref 링크)를 답니다. 용어집에 참고 자료 절이 없으면 "(Chapter 10)" 링크로 대체하고 그 사실을 DECISIONS에 남깁니다. | 높음 |
| T3 | 권장 | 프롬프트 항목의 링크가 정의를 설명하지 않습니다. `ch04.html#elements`는 "요청의 네 요소"를 다루고, 프롬프트 정의는 ch01.html 20행과 `#layers`(66~67행)에 있습니다(4장 8행도 "Chapter 1에서 정의한 지시문"). 용어집 머리말은 "본문에서 처음 정의한 뜻"을 따른다고 합니다. | 프롬프트 항목 | ch01.html 67행, ch04.html 8행. | 링크를 `ch01.html#layers`로 바꿉니다. | 높음 |
| T4 | 권장 | 하위 에이전트 항목의 링크가 정의를 설명하지 않습니다. 정의 문장("특정 작업을 맡도록 별도로 정의한 에이전트")은 ch02.html 11행(`#components`)에 있고, `ch06.html#multi-agent`는 동작(컨텍스트, 비용)을 설명합니다. 훅 항목은 `ch02#components`로 맞게 연결돼 있습니다. | 하위 에이전트 항목 | ch02.html 11행, ch06.html 31~32행. | 링크를 `ch02.html#components`로 바꿉니다. | 중간 |
| T5 | 권장 | 완료 기준 정의가 4장의 용법을 담지 않습니다. 4장은 완료 기준을 "요청 한 건의 성공 기준"으로 먼저 정의합니다(요청의 네 요소 중 하나). 용어집은 "작업 단위 목록에 적는 완료 조건"만 씁니다(6장, 7장 용법과는 일치). | 완료 기준 항목 | ch04.html 7~8행, ch07.html 12행, ch06.html 15행. | "요청 한 건 또는 작업 단위 하나가 받아들여지기 위해 충족해야 하는 조건"처럼 두 용법을 합치고 4장 링크도 답니다. | 중간 |
| T6 | 참고 | 자동 메모리 정의가 2장과 문구가 다릅니다("작업 중에 알게 된 내용" ↔ "수정 요청과 선호"). 둘 다 memory 문서("notes Claude writes itself based on your corrections and preferences", 매 세션 앞 200줄 또는 25KB 적재)와 모순되지 않습니다. 링크가 없습니다. | 자동 메모리 항목 | ch02.html 11행, memory 문서. | 2장 문구에 맞추고 `ch02.html#components` 또는 ch08 링크를 답니다. | 높음 |
| T7 | 참고 | 미확인입니다. 승인 정책의 Codex 정의("동작 전에 멈추고 사용자에게 확인하는 시점을 정하는 설정, 금지는 규칙 파일")는 10장의 2026-10-04 기록(ch10.html 37행)과 같지만, OpenAI 문서가 열리지 않아 지금도 같은지 확인하지 못했습니다. 이 항목은 설정 값 이름을 쓰지 않아 폐지된 값 문제는 없습니다. | 승인 정책 항목 | developers.openai.com DNS 오류. | 병합 전 OpenAI 문서를 다시 열 수 있으면 확인합니다. | 중간 |
| T8 | 참고 | 미확인입니다. ReAct "2022년 논문" 서술은 research/ch01-sources.md S11의 기록(2026-10-19 확인)에 의존합니다. arxiv.org가 열리지 않았습니다. | ReAct 항목 | arxiv.org DNS 오류. | 기존 기록을 유지합니다. | 중간 |
| T9 | 참고 | 토큰 항목의 "한 단어가 여러 토큰으로 나뉘기도 합니다"는 1장 정의(ch01.html 7행)에 없는 추가 문장으로 출처가 없습니다. `/usage` 문장은 일치합니다. | 토큰 항목 | ch01.html 7행, commands 문서. | 출처를 달거나 삭제합니다. | 중간 |
| T10 | 참고 | 머리말은 "괄호 안의 장 링크로 본문의 설명을 찾아갈 수 있다"고 하지만 링크가 없는 항목이 일곱 개입니다(대규모 언어 모델, 도구, 도구 호출, 자동 메모리, 토큰, 풀 리퀘스트, MCP). 모두 본문에 정의가 있습니다(ch01 7·10·56행, ch02 11행). | 한국어 용어, 영어 용어 | 위 본문 위치. | 링크를 달거나 머리말을 "대부분의 항목"으로 완화합니다. | 높음 |
| T11 | 참고 | 진행 기록의 "다음 작업"은 표 8-2와 일치하지만 8장 38행(다음 작업은 인계 메모 쪽)과 8장 안에서 어긋납니다. 장 쪽 정리 대상입니다. | 진행 기록 항목 | ch08.html 25행, 38~39행. | 8장 backlog. | 높음 |

**용어에서 일치로 확인한 항목**: 격리(ch09 23행), 결정 기록(ch08 30행), 결합형(ch01 22행, 표 1-2), 권한 규칙과 평가 순서(permissions 문서 "deny, then ask, then allow"), 권한 모드(ch10 31~32행의 정의와 default·plan 설명, 기본값을 쓰지 않아 버전 문제 없음), 규칙 문서(ch02 11행, ch05), LLM·도구·도구 호출(ch01), 독립 검수(ch07 22행), 샌드박스(ch09 23~24행, sandboxing 문서: 셸 명령만 대상, 파일 도구·MCP·훅은 밖, 기본 꺼짐), 세션(ch08 3행), 수용 기준(ch01 63행, ch03 22행), 승인 지점(ch09 13·16행), 실행 로그(ch08 41~44행 네 종류), 에이전트(ch01 37행), 에이전트 명세서(ch03 요점 상자 아홉 항목), 워크플로(ch01 21행), 인계 메모(ch08 38~39행 다섯 항목), 작업 단위(ch06 15행), 지시와 강제(ch02 40행), 컨텍스트·컨텍스트 윈도(ch01 7행)·프롬프트·컨텍스트 엔지니어링·하네스 엔지니어링·하네스(ch01 51~55, 67, 95행), 풀 리퀘스트(ch01 56행), 훅(ch02 11행; hooks-guide의 http, prompt, agent, mcp_tool 형식은 "이 책은 셸 명령 훅만 다룹니다"로 한정), CI·lint(ch07), Skill의 "절차 묶음"(ch11 표 11-2), `/context`·`/usage`(commands 문서). 가나다순과 알파벳순.

---

## research/에 추가할 기록 문안 (research/front-back-sources.md)
공통: 게시일 없음(상시 갱신 문서), 확인일 2026-10-20, 작성 Anthropic(Claude Code Docs), 개정 후 대조(PR #45).

- **S-FB-15. Quickstart** (https://code.claude.com/docs/en/quickstart). 첫 실행에서 로그인 안내가 나오고(Pro, Max, Team, Enterprise, Console 계정, 브라우저 인증), `claude -c`는 현재 폴더의 가장 최근 대화를 이어 엽니다. Git for Windows가 없으면 PowerShell을 셸 도구로 씁니다. 사용처: 실습 준비, 실습 6, 막혔을 때.
- **S-FB-16. CLI reference** (https://code.claude.com/docs/en/cli-reference). `--continue`, `-c`는 현재 폴더의 가장 최근 대화를 불러옵니다. `claude doctor`는 설정 파일 검증 오류를 포함한 읽기 전용 진단을 출력합니다. 사용처: 실습 6, 막혔을 때.
- **S-FB-17. Security, Configure permissions** (https://code.claude.com/docs/en/security, /permissions). 신뢰하지 않은 폴더에서 시작하면 워크스페이스 신뢰 확인이 나옵니다. 프로젝트 `.claude/settings.json`의 allow 규칙은 신뢰를 수락한 뒤에만 적용되고 deny, ask는 영향을 받지 않습니다. 저장소 안에서는 저장소 루트 단위로 신뢰를 저장하고, 홈 폴더에서 시작하면 세션 동안만 유지합니다. 평가 순서는 deny → ask → allow이고 `/permissions`는 규칙과 출처 설정 파일을 보여 줍니다. 사용처: 실습 2, 3.
- **S-FB-18. Explore the context window, Commands** (https://code.claude.com/docs/en/context-window, /commands). `/context`는 어떤 CLAUDE.md와 자동 메모리 파일이 적재됐는지를 포함한 범주별 내역을 보여 주고, 전체 화면에서는 항목별 내역을 접으며 `all`로 펼칩니다. `/memory`는 CLAUDE.md 편집, 자동 메모리 켜고 끄기, 자동 메모리 항목 열람입니다. 화면의 "메모리 파일" 항목 이름은 문서에서 못 찾았고 실습 2 실행 때 확인합니다. 사용처: 실습 2, 6.
- **S-FB-19. Hooks reference, Automate actions with hooks** (https://code.claude.com/docs/en/hooks, /hooks-guide). `/hooks`는 읽기 전용 목록이고 이벤트별로 묶여 보이며, 훅을 선택하면 실행 명령 전문과 정의된 파일이 보입니다. 종료 코드 0이면 대부분의 이벤트에서 stdout이 transcript에 보이지 않습니다. PostToolUse의 종료 코드 2는 "Shows stderr to Claude; the tool already ran"입니다. 사용자 화면에 `hook error` 알림이 뜨는지는 PostToolUse에 대해 명시되지 않았습니다(미확인, 실습 4 실행 때 확인). 사용처: 실습 4.
- **S-FB-20. Choose a permission mode** (https://code.claude.com/docs/en/permission-modes). 터미널과 VS Code는 v2.1.283 이상에서 auto로 시작합니다. auto에서는 작업 폴더 안의 파일 수정이 자동 승인되고, 명시한 ask 규칙은 여전히 묻고, deny 규칙은 모든 모드에서 막습니다. 보호 경로(`.git`, `.claude` 등)는 분류기로 보냅니다. S-FB-8의 재확인입니다. 사용처: 실습 2, 3의 확인 화면 서술(L6).
- **S-FB-21. Set up, Tools reference, Terminal guide, Plans & pricing 재확인** (https://code.claude.com/docs/en/setup, /tools-reference, /terminal-guide, https://claude.com/pricing). Git for Windows는 선택 사항이고, 있으면 Bash 도구가 Git Bash를 쓰며 claude.ai와 Console 계정에서는 PowerShell 도구도 기본으로 함께 켜집니다. Git Bash가 있는 Windows에서 Bash 금지 규칙(범위 지정 포함)이 있으면 PowerShell 도구가 꺼집니다. 터미널 열기는 Windows `Win + X`, macOS `Cmd + Space`입니다. 인증은 Pro, Max, Team, Enterprise, Console이고 무료 claude.ai는 불포함이며, pricing은 Free 미포함, 모든 유료 요금제 포함입니다. `/usage` 세션 금액은 정가 기준 추정치이고 구독 사용자에게는 청구 근거가 아니라는 점을 costs 문서에서 재확인했습니다. 사용처: 실습 준비, 실습 6(L1~L3, L12).
- **S-FB-22. 실습 저장소 재확인** (https://github.com/seoulkorea-dev/harness-book). 작성 seoulkorea-dev. 로그인 없이 열리는 공개 저장소입니다. 루트에 CLAUDE.md, .claude/, DECISIONS.md, FAILURES.md, reviews/, research/가 있고, examples/expense-app에는 reference/(CLAUDE.example.md, reviewer.example.md, settings.example.json, tasks.example.json), RUNLOG.md(2026-10-16 기록만, 10-20 기록은 병합 전), tasks.example.json(작업 1 true)이 있습니다. 사용처: 시작하며 목적 셋째 항목, 실습 1.
- **S-FB-23. 미확인 기록(개정 후)**. (a) developers.openai.com, arxiv.org, git-scm.com이 DNS 오류로 열리지 않았습니다(승인 정책 Codex 정의, ReAct 연도, `git config --global` 범위). (b) 부모 폴더의 `.claude/settings.json`이 하위 폴더 세션에 적용되는지는 settings 문서를 열지 않아 확인하지 못했습니다. (c) 실습 3의 "설정 JSON 형식 오류 때 Claude Code가 설정을 읽지 못함" 증상. (d) PostToolUse 종료 코드 2의 사용자 화면 알림(S-FB-19). (e) `/context`의 "메모리 파일" 항목 이름(S-FB-18).

Sources: https://code.claude.com/docs/en/commands, /hooks, /hooks-guide, /quickstart, /cli-reference, /security, /permissions, /permission-modes, /memory, /context-window, /costs, /setup, /tools-reference, /sandboxing, /terminal-guide, https://claude.com/pricing, https://github.com/seoulkorea-dev/harness-book

---

## 필수 건수
- **필수 2건**: 시작하며 P1(요점 상자 "세 줄"이 1장과 불일치), 부록 용어 T1(실패 기록 정의가 11장보다 좁음)
- 권장 13건: P2, E1, L1~L7, T2~T5
- 참고 17건: P3, P4, E2, E3, L8~L17, T6~T11 (P4와 E3은 일치 확인 기록)
- 확인한 사실 문장 약 110개

(건수의 기준은 오류 지적에 쓴 번호입니다. 개정 전 필수 8건은 모두 해소 또는 부록 쪽 해소로 판정했고, 새 필수 2건은 개정 중 새로 생긴 문장에서 나왔습니다.)
