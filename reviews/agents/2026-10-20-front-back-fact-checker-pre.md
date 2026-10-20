# 시작하며, 마치며, 부록 fact-checker 개정 전 점검(2026-10-20, PR #45)

# 사실 확인 보고: 시작하며, 마치며, 부록 실습, 부록 용어 (브랜치 front-back-write, PR #45, 개정 전)

확인일: 2026-10-20. 파일은 고치지 않았습니다.

- **확인한 주소**: Claude Code Docs의 memory, setup, terminal-guide, permissions, permission-modes, tools-reference, hooks, hooks-guide, commands, sandboxing, sub-agents, costs 페이지를 직접 열었습니다. claude.com/pricing과 github.com/seoulkorea-dev/harness-book도 열었습니다.
- **열지 못한 주소**: developers.openai.com과 arxiv.org는 DNS 오류(getaddrinfo ENOTFOUND)로 열리지 않았습니다.
- **실행 한계**: 실행 도구가 없어 `python check.py`를 직접 돌리지 못했습니다. RUNLOG의 기준 상태 기록은 코드(check.py, acceptance/test_cr07.py, expense/*.py, data/*)를 읽어 논리만 대조했고, 일치합니다(실패는 시험 1, 2, 3, 단위 테스트는 3건 모두 통과).
- **본문 대조**: 11장 본문(src/chapters/ch01~ch11.html)은 읽고 대조했습니다.
- **링크**: 장 링크와 앵커(#agent-harness, #elements, #kinds, #criteria, #failures, #steps, #setup, #principle, #example, #rule-doc, #permissions, #handover, #lab-1~#lab-6)는 모두 실제 id와 맞습니다.

## 시작하며 (src/chapters/prologue.html)

| # | 심각도 | 발견 | 위치 | 근거 | 제안 | 확신 |
|---|---|---|---|---|---|---|
| P1 | 필수 | "이 책을 포함한 책 두 권을 에이전트와 함께 만든 과정과 기록을 Chapter 11과 이 책의 저장소에 공개합니다"가 저장소 내용과 어긋납니다. 지난 책의 검수 기록 73건은 이 저장소에 없습니다. | 9행, 목적 셋째 항목 | research/ch11-sources.md S-C11-7, 169행, 197행에 "지난 책 저장소(ai-book)의 검수 기록은 이 저장소에 없고, 근거는 NEW_BOOK_PLAYBOOK.md 한 문서"라고 적혀 있습니다. 원격 저장소 전체는 보지 못했습니다. | "이 책을 만든 과정과 기록은 이 책의 저장소에, 지난 책의 정리는 Chapter 11에 공개합니다"처럼 대상을 나눠 씁니다. | 중간 |
| P2 | 권장 | "각 장은 같은 순서로 …, 본문은 … 예제 CR에 적용합니다"는 일반화입니다. 1장은 CR 적용 절이 없고(id: background, meanings, agent-harness, harness, layers, loop, prompt-context, software-engineering, manager, check, principle), 11장은 CR이 아니라 이 책 저장소 사례입니다. | 27행 | 위 id 목록과 ch11 본문(2~11절 구성)입니다. | "대부분의 장은 … CR에 적용하고, 1장은 정의, 11장은 작가 사례를 다룹니다"로 한정하거나 근거 있는 범위만 씁니다. | 중간 |
| P3 | 참고 | 일치로 확인한 항목입니다. 장 묶음(1~3, 4~5, 6~9, 10~11), 열한 개 장, 표의 "읽고 나면 할 수 있는 일"(명세서, 요청의 네 요소, CLAUDE.md, DECISIONS.md, settings.json, 두 제품 설정, 개선 순서), 장 틀(주장 줄, 요점 상자 `ul.summary`, 원칙 한 문장, 점검 질문 세 개), 하네스 정의(ch01과 같음)입니다. | 전체 | ch01~ch11 본문과 대조했습니다. | 조치 없음. | 높음 |

## 마치며 (src/chapters/epilogue.html)

| # | 심각도 | 발견 | 위치 | 근거 | 제안 | 확신 |
|---|---|---|---|---|---|---|
| E1 | 필수 | Chapter 2 원칙이 2장 본문과 다릅니다. 마치며는 "어기면 되돌리기 어려운 규칙은 규칙 문서의 지시로 두지 않고, 권한 규칙과 훅으로 강제합니다."입니다. 2장 80행은 "다섯 구성 요소를 모두 정하고, 어기면 되돌리기 어려운 규칙은 규칙 문서가 아니라 권한 규칙과 훅으로 강제합니다."입니다. 앞 절("다섯 구성 요소를 모두 정하고")이 빠졌고 문구도 다릅니다. HANDOFF의 "마치며 2장 원칙 동기화"가 반영되지 않았습니다. | 5행, 둘째 항목 | ch02.html 80행. 나머지 열 장(1, 3~11)의 원칙은 각 장 `p.principle`과 글자까지 일치합니다. | 2장 원칙 문장을 본문과 같게 바꿉니다. | 높음 |
| E2 | 참고 | "같은 실패가 두 번 나오면 그 원인을 구성 요소의 변경으로 옮깁니다"는 11장 53행의 예외("되돌리기 어렵거나 위험이 큰 실패는 첫 발생에도 장치를 검토")를 담지 않았습니다. 원칙 문장과는 모순되지 않습니다. | 7행 | ch11.html 53행. | 필요하면 "위험이 큰 실패는 첫 발생에도"를 덧붙입니다. | 중간 |

## 부록 실습 (src/appendix/practice.html)

| # | 심각도 | 발견 | 위치 | 근거 | 제안 | 확신 |
|---|---|---|---|---|---|---|
| L1 | 필수 | 실습 저장소를 clone한 뒤 examples/expense-app/에서 Claude Code를 실행하면 저장소 루트의 CLAUDE.md와 .claude/agents/가 함께 읽힙니다. 실습 1의 "이 폴더에는 아직 CLAUDE.md와 .claude/ 폴더가 없습니다"는 폴더만 보면 맞지만 실제 동작과 다릅니다. 실습 2의 확인("응답이 CLAUDE.md의 수정 범위를 그대로 따름")과 5장 표 5-7(`/context` 메모리 파일)이 루트의 책 작성용 지침(작성 에이전트, src/만 수정 등)과 섞입니다. 루트 .claude/settings.json의 적용 여부는 미확인입니다. | 실습 1 확인 방법 3항, 실습 2 확인 방법, 23~27행 | memory 문서 "CLAUDE.md files in the directory hierarchy above the working directory are loaded at launch". sub-agents 문서 "Project subagents are discovered by walking up from the current working directory … repository root". ch05.html 74행이 루트 CLAUDE.md의 존재를 직접 밝힙니다. | clone 뒤 examples/expense-app을 저장소 밖 새 폴더로 복사하고 `git init`과 첫 commit을 하게 합니다(실습 5의 git log에도 필요). 또는 상위 지침이 함께 읽힌다는 안내를 추가합니다. | 높음 |
| L2 | 필수 | 10장 100행은 "push와 네트워크 확인은 원격 저장소에 연결되지 않은 연습 폴더(부록 실습)에서 합니다"라고 합니다. 그런데 실습 1은 `git clone`으로 origin이 연결된 폴더를 만들고, 실습 3은 그 폴더에서 "원격 저장소에 push해 줘"를 요청합니다. 실습 5의 commit도 clone한 책 저장소에 쌓입니다. | 23~24행, 실습 3 46~47행 | ch10.html 100행과 practice.html 23행의 대조입니다. | L1의 복사 후 `git init` 안내로 함께 해결합니다. 또는 10장 문구를 고칩니다(10장은 개정 완료라 부록 쪽 수정을 권합니다). | 높음 |
| L3 | 필수 | 실습 4 확인 "파일을 수정한 뒤 단위 테스트가 자동으로 실행된 흔적이 대화에 보입니다"는 공식 문서와 어긋납니다. 성공한 훅(종료 코드 0)의 출력은 대화에 보이지 않습니다. PostToolUse는 stdout 예외 목록에 없고, 종료 코드 2일 때만 stderr가 Claude에 전달됩니다. 이 실습의 제목 수정은 테스트를 깨지 않으므로 흔적이 없습니다. 2장 표 2-6은 "테스트가 실패하면 훅 오류 알림", 3장 표 3-6은 `/hooks`로 확인한다고 되어 있어 실습과도 엇갈립니다. HANDOFF 미결정 항목과 같은 문제입니다. | 실습 4 확인 방법 1항(60행) | hooks 문서 "Exit code 0: … doesn't show it in the transcript", "PostToolUse … Shows stderr to Claude; the tool already ran". `/hooks`는 읽기 전용 목록입니다. | 확인을 두 가지로 바꿉니다. (1) `/hooks`에서 PostToolUse 훅과 단위 테스트 명령을 봅니다. (2) 테스트를 일부러 깨는 수정을 요청해(예: 목록에서 요청자 열 제거) 훅 오류 알림을 봅니다. | 높음 |
| L4 | 필수 | 2장 58행은 "규칙 문서만 있는 상태에서는 수용 시험을 수정하려는 시도를 막지 못하고, 금지 규칙을 더하면 같은 시도가 거부됩니다(부록 실습 2, 3)"라고 합니다. 실습 2는 "수정하면 안 되는 파일을 알려 줘"라는 질문뿐이고, 실습 3은 시험이 아니라 data/projects.csv 수정과 push를 요청합니다. 실습 2 확인의 "이 단계에서는 수정 시도를 막지 못합니다"도 시도를 하지 않아 확인할 수 없습니다. | 실습 2 37행, 39행 / 실습 3 46~47행 | ch02.html 58행, ch03.html 표 3-4, 9장 표 9-4와의 대조입니다. | 실습 2에 같은 대상(예: acceptance/ 또는 check.py)의 수정 요청을 추가하고 실습 3에서 같은 요청을 반복합니다. 규칙 문서는 컨텍스트라 지시를 따른다는 보장이 없으므로(memory 문서) "막지 못할 수 있다"로 씁니다. | 높음 |
| L5 | 필수 | 3장 표 3-6 마지막 행(check.py 종료 코드 0, 모든 작업 단위를 마친 뒤)은 실습 5로 링크됩니다. 그러나 실습 5는 작업 2, 3까지만 하고(작업 4 전에는 시험 1~3이 실패해 종료 코드 1), 종료 코드 0 확인은 실습 6 확인 방법 2항에 있습니다. | ch03.html 123행 ↔ practice.html 70~71행, 82행 | tasks.example.json, RUNLOG 기준 상태, ch06 표 6-4입니다. | 3장 링크를 실습 6으로 바꿉니다(3장은 개정 완료이므로 backlog 처리). 또는 실습 5 확인에 "종료 코드 1이 정상, 0은 실습 6"을 적습니다. | 높음 |
| L6 | 권장 | 실습 3 확인 "두 요청 모두 실행되지 않고 거부됩니다"는 항상 성립하지 않습니다. Edit 금지 규칙은 편집 도구와 Bash 출력 리디렉션(`>>`)에는 적용되지만, 스크립트를 통한 간접 수정은 막지 못합니다(9장 22행). 또 git이 없는 Windows에서는 PowerShell 도구가 기본 셸이고 `Bash(...)` 규칙이 PowerShell 도구를 제한하지 않습니다. 실습 준비가 "설치하지 않으면 PowerShell로 실행"을 안내하면서 Git을 필수 도구로도 적어 두 설명이 엇갈립니다. Git Bash가 있으면 Bash 금지 규칙이 PowerShell 도구를 끕니다. | 49행, 9행 | permissions 문서(Output redirects, PowerShell 절), tools-reference 문서 "Bash deny rules also turn off the PowerShell tool", "a Bash rule doesn't restrict the PowerShell tool". | "거부되거나 확인을 요청한다. git status로 변경 여부를 확인한다"로 쓰고, Windows는 Git for Windows를 설치한 경우를 전제로 한다고 적습니다. | 중간 |
| L7 | 권장 | settings.example.json의 훅 명령은 `python`만 씁니다. macOS, Linux에서 `python`이 없으면 매 편집마다 종료 코드 127 → `\|\| exit 2` → 실패 출력이 모델에 전달됩니다. 실습 준비와 CLAUDE.example.md는 python3 대체를 안내하는데, 실습 3, 4는 훅 명령 교체를 알려 주지 않습니다. HANDOFF의 "훅 명령 python 고정(v1.1 보류)"과 같은 건입니다. | 실습 3 단계 2, 실습 4 단계 1 | settings.example.json 31행, hooks 문서의 "Exit code 2 … PostToolUse" 행입니다. | 실습 4에 "`python` 명령이 없으면 훅 명령도 python3으로 바꿉니다"를 추가합니다. | 높음 |
| L8 | 권장 | 실습 1의 "종료 코드 1", 실습 6의 "종료 코드 0"을 보는 방법이 없습니다. 7장 표 7-8은 Git Bash에서 `echo $?`, PowerShell에서 `$LASTEXITCODE`를 안내합니다. | 30행, 82행 | ch07.html 104행. | 7장 표 7-8 링크나 명령 한 줄을 추가합니다. | 높음 |
| L9 | 권장 | 본문이 기대하는 화면 확인이 실습에 없습니다. `/context`(2장 표 2-6, 5장 표 5-7)와 `/hooks`(3장 표 3-6)는 어느 실습에도 단계가 없고, `/usage`(8장 표 8-6, RUNLOG 실습 5, 6 기록 항목)는 실습 5, 6에 없습니다. research/ch03-sources.md C3-8, C3-9의 미확인 항목(`/hooks`의 matcher 표시, `/context`의 하위 에이전트 항목)이 그대로 남아 있습니다. `/usage` 금액은 정가 기준 추정치입니다. | 실습 2, 4, 5, 6 | commands 문서(`/context`, `/hooks`, `/usage`), costs 문서 "Claude Code computes the dollar figure locally … at list price". | 실습 2에 `/context`, 실습 4에 `/hooks`, 실습 6에 `/usage`(청구 근거가 아님)를 넣고 RUNLOG에 화면을 남깁니다. | 높음 |
| L10 | 권장 | 발표 주체가 문장에 없습니다. "Claude Code는 Pro 이상의 유료 요금제나 … 사용하며"와 "Git for Windows를 설치하면 … Git Bash로 실행합니다" 모두 사실 문장이지만 주체가 문장에 없습니다(STYLE 1, 4). 버전 주석(2026년 10월)에도 출처 링크가 없습니다(STYLE 5). 사실 자체는 일치합니다(S-FB-2, 11). | 6행, 9행, 15행 | setup, pricing 문서입니다. | "Anthropic 문서는 …라고 안내합니다(Anthropic, 2026)"로 바꾸고 주석에 링크를 답니다. | 높음 |
| L11 | 참고 | 작업 2, 3의 확인 방법(수용 시험 4, 5, tests 실패 0건)은 기준 상태에서 이미 통과합니다(RUNLOG: 실패는 test_1, 2, 3뿐). ch06 56행이 이를 밝히고 있어 본문과는 모순이 없지만, 실습 5 확인으로는 구현 여부를 구별하지 못합니다. | 실습 5 확인 방법 | RUNLOG.md 8~13행, ch06.html 56행. | `git diff`로 expense/, tests/ 변경과 tasks.json의 통과 값을 보게 합니다. | 높음 |
| L12 | 참고 | 실행 기록이 없는 단계가 있습니다. RUNLOG는 실습 1만 "확인함"(2026-10-16, 작성 채팅, python3)이고, 실습 2~6은 모두 "실행 전"입니다. 그래서 실습 2~6의 결과 서술은 모두 예측입니다(응답이 수정 범위를 따름, 두 요청 거부, reviewer 보고에서 기준 1~3 미충족, 작업 4 뒤 종료 코드 0 등). 16행 "이 쪽과 RUNLOG.md에 기록합니다"의 "이 쪽"에는 기록이 없습니다. HANDOFF 작업 목록의 "실습 5, 6 실행 뒤 RUNLOG 기록"과 같은 건입니다. 실습 1도 Windows `python`이 아니라 python3로만 확인했고, 단위 테스트의 OK는 코드 논리로만 확인했습니다. | 16행, RUNLOG.md | RUNLOG.md 16~26행. | 병합 전에 실습 2~6을 실행해 RUNLOG에 날짜, 모델과 제품 버전, 요청과 출력 원문을 남깁니다. | 높음 |
| L13 | 참고 | 실습 6의 "등록 화면에서 프로젝트 코드를 선택"에 주소(http://localhost:8000/new)와 종료(Ctrl+C)가 없습니다. 7장 표 7-8 106행에는 있습니다. | 80행 | app.py `/new`, ch07.html 106행. | 한 줄 추가합니다. | 높음 |
| L14 | 참고 | 실습 6 확인의 "이전 대화 없이 HANDOFF.md와 tasks.json만으로"는 자동 메모리가 켜져 있으면 엄밀하지 않습니다. 자동 메모리는 기본 켜짐이고 같은 저장소의 세션에 걸쳐 읽힙니다. | 82행 | memory 문서 "Auto memory is on by default in local sessions", "shared across worktrees". | `/memory`로 자동 메모리 항목을 확인하거나 끄도록 안내합니다. | 중간 |
| L15 | 참고 | "Git Bash로 실행합니다"는 부분적입니다. Git for Windows가 있어도 claude.ai, Console 계정에서는 PowerShell 도구가 기본으로 함께 켜집니다. | 9행 | setup, tools-reference 문서. | 위 L6과 함께 정리합니다. | 중간 |
| L16 | 참고 | 일치로 확인한 항목입니다. (1) PowerShell 설치 명령 `irm https://claude.ai/install.ps1 \| iex`. (2) Pro 이상 유료와 Console 필요, 무료 요금제는 Claude Code 미포함. (3) Git for Windows가 없으면 PowerShell을 쓴다는 설명. (4) `claude --version`. (5) 슬래시 명령 `/permissions`, `/exit`. (6) clone 주소는 공개 저장소이고 main에 examples/expense-app가 있습니다. (7) 실습 파일과 reference/ 문구, CLAUDE.example.md의 여섯 절(목적, 읽는 순서, 작업 순서, 수정 범위, 중단 규칙, 명령)과 수정 범위 목록. (8) 기준 상태(tests 3건, acceptance 5건 중 3건 실패, 종료 코드 1)가 RUNLOG와 코드 논리에 일치. (9) 실습 번호별 본문 링크(5장 실습 2, 5, 6장 실습 1, 5, 8장 실습 5, 6, 7장 실습 1, 4, 9장 실습 3). 단, main이 이 브랜치의 변경(RUNLOG, reference/)을 이미 담았는지는 병합 전이라 확인하지 못했습니다. | 전체 | 위 S-FB 기록입니다. | 조치 없음. | 높음 |

## 부록 용어 (src/appendix/terms.html)

| # | 심각도 | 발견 | 위치 | 근거 | 제안 | 확신 |
|---|---|---|---|---|---|---|
| T1 | 필수 | 에이전트 정의가 1장과 다릅니다. 용어집은 "모델이 도구를 사용해 작업하고, 결과를 확인하며, 목표를 이룰 때까지 반복하는 시스템"입니다. 1장 37행은 "모델이 루프 안에서 도구를 사용해 다음 행동을 스스로 정하고, 결과를 확인하며 …"입니다. "다음 행동을 스스로 정하고"가 빠져, 같은 용어집의 워크플로("미리 정한 코드 경로")와의 구분이 사라집니다. | 에이전트(Agent) 항목 | ch01.html 37행, 21행. | 1장 정의 문장을 그대로 씁니다("모델이 루프 안에서 도구를 사용해 다음 행동을 스스로 정하고, …"). | 높음 |
| T2 | 권장 | 토큰 항목의 "Codex는 /status 명령으로 사용량을 확인합니다"는 1차 출처를 찾지 못했습니다. OpenAI 문서는 열리지 않았고 검색 결과는 제3자 글뿐입니다. 9장은 같은 내용을 개정에서 삭제했습니다(research/ch09-sources.md S-C9-7, 확신 낮음). 10장 기록(research/ch10-sources.md 87행)은 `/status`에 토큰 사용량 항목이 없다고 적습니다. 뒤 절의 Claude Code `/usage`는 일치합니다(Session 블록의 토큰 사용 통계). | 토큰(Token) 항목 | commands, costs 문서(일치). OpenAI 문서는 DNS 오류로 열지 못함(미확인). | Codex 부분을 삭제하거나 원문을 확인한 뒤 씁니다. | 중간 |
| T3 | 권장 | 인계 메모 정의에 5항목 중 "확인 명령"이 빠졌습니다. 용어집은 4항목(현재 상태, 읽을 문서, 미결정 사항, 다음 작업)이고, 8장 39행과 표 8-6은 5항목입니다. | 인계 메모 항목 | ch08.html 39행, 87행. | "확인 명령"을 추가합니다. | 높음 |
| T4 | 권장 | 수용 기준과 완료 기준의 풀이가 거의 같은 문장입니다("결과물이 받아들여지기 위해 충족해야 하는 조건" / "결과를 받아들이기 위해 충족해야 하는 조건"). 본문은 둘을 구분합니다. 수용 기준은 사람이 정한 완료 조건(3장 22행), 완료 기준은 작업 단위 목록에 적는 칸이며 검사로 변환하는 대상(7장 12행)입니다. | 수용 기준, 완료 기준 항목 | ch03.html 22행, ch07.html 12행, ch06.html 15행. | 두 항목에 구분 문장을 넣습니다. | 높음 |
| T5 | 권장 | 샌드박스 정의의 "격리 환경"은 9장이 따로 정의한 "격리된 실행 환경"(컨테이너나 가상 머신, 24행)과 겹쳐 읽힙니다. 9장 정의는 "셸 명령과 그 하위 프로세스가 접근할 수 있는 파일과 네트워크를 운영 체제 수준에서 제한"입니다. 용어집에는 Claude Code의 기본값(꺼짐, `/sandbox`)과 파일 편집 도구는 대상이 아니라는 점도 없습니다(사실은 모두 문서와 일치, S-FB-7). | 샌드박스 항목 | ch09.html 23~24행, sandboxing 문서. | 9장 정의로 맞추고 필요하면 10장 링크를 답니다. | 높음 |
| T6 | 권장 | AGENTS.md 항목 "Claude Code는 CLAUDE.md가 없을 때 이 파일을 읽습니다"는 조건이 빠졌습니다. 문서는 작업 폴더나 그 위에 CLAUDE.md, .claude/CLAUDE.md, CLAUDE.local.md가 하나도 없을 때, v2.1.277 이상에서만 읽는다고 합니다. 5장과 10장에는 버전 주석이 있는데 용어집에는 없습니다(STYLE 5). | AGENTS.md 항목 | memory 문서 "AGENTS.md" 절(2026-10-20 확인), ch10.html 20행, 27행. | 조건과 버전 주석을 붙입니다. | 높음 |
| T7 | 권장 | 본문에서 정의한 용어가 빠져 있습니다. 실패 기록(11장), 승인 지점, 격리(9장), 지시와 강제(2장), 에이전트 명세서(3장), 실행 로그(8장), 프롬프트(1장)입니다. 11장은 Skill을 "절차 묶음"이라고도 부르는데(표 11-2), 용어집과 5장에는 이 이름이 없습니다. 용어집 머리말은 "본문에서 정의한 용어를 모았습니다"라고 합니다. | 한국어 용어 전체 | ch11.html 33행, 26행. | 최소한 실패 기록, 승인 지점, 격리, 지시와 강제를 추가합니다. Skill에 "(11장의 절차 묶음)" 별칭을 붙입니다. | 중간 |
| T8 | 참고 | 일치로 확인한 항목입니다. 결정 기록(ch08 30행), 결합형(ch01 22행), 권한 규칙과 평가 순서 deny → ask → allow(permissions 문서), 권한 모드(ch10 31행), 승인 정책(ch10 37행, 정의), 규칙 문서, LLM, 도구, 도구 호출, 독립 검수(ch07 22행), 수용 기준(ch01 63행), 워크플로, 작업 단위(ch06 15행), 진행 기록(표 8-2), 컨텍스트, 컨텍스트 엔지니어링, 컨텍스트 윈도와 `/context`(commands 문서), 풀 리퀘스트, 프롬프트 엔지니어링, 하네스, 하네스 엔지니어링, 하위 에이전트(ch02 11행), 훅(ch02 11행), CLAUDE.md, CI(ch07 9행), lint(ch07 9행, ch11 표 11-1은 "원고의" 한정), MCP, Skill(ch05 10행). 가나다순과 알파벳순도 맞습니다. | 전체 | 위 본문 위치입니다. | 조치 없음. | 높음 |
| T9 | 참고 | 확인하지 못한 항목입니다. (a) 승인 정책의 Codex 현재 정의와 값은 공식 문서가 열리지 않았습니다. 검색 요약에는 `approval_policy = "untrusted"`가 폐지됐다는 내용이 있으나 이 책은 해당 값을 쓰지 않습니다. 10장의 2026-10-04 기록에 의존합니다. (b) ReAct "2022년 논문"은 research/ch01-sources.md S11(arXiv v1 2022-10-06, 2026-10-19 확인)에 의존하며 이번에 arXiv를 다시 열지 못했습니다. (c) 훅 항목의 "셸 명령"은 2장 11행의 "이 책은 셸 명령을 실행하는 훅만 다룹니다"와 맞습니다. 다만 제품에는 http, prompt, agent, mcp_tool 훅도 있습니다(hooks-guide). (d) 진행 기록의 "다음 작업"은 표 8-2와는 맞지만 8장 38행(다음 작업은 인계 메모 쪽)과는 8장 안에서 어긋납니다. | 해당 항목 | 위 출처입니다. | (c)는 "이 책은 셸 명령 훅만 다룬다"를 덧붙일 수 있습니다. (d)는 8장 정리 대상입니다. | 낮음 |

## 필수 건수

- **필수 8건**: P1, E1, L1, L2, L3, L4, L5, T1
- 권장 12건: P2, L6~L10, T2~T7
- 참고 9건: P3, E2, L11~L16, T8, T9
- 확인한 사실 문장 약 95개
