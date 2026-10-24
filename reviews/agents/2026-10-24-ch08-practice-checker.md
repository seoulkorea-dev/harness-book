# 8장 실습 점검(practice-checker)

## 요약: 필수 3, 권고 5, 참고 4

실행한 명령은 8개입니다. 원본은 건드리지 않고 임시 복사본(/tmp/claude-0/-home-user-harness-book/4fa31d71-64a2-5605-bad4-d31a3ffd2331/scratchpad/ep)에서 실행했고, `__pycache__`는 지우고 시작했습니다. 실행 뒤 `git status --short`는 출력이 없어 작업 폴더가 바뀌지 않았습니다.

### 실행 기록 (출력 끝부분)
- 복사본에서 `python check.py`의 출력 끝은 다음과 같습니다.
  ```
  FAILED (failures=3)
  acceptance: 실행 5건, 실패 3건, 건너뜀 0건(정한 수 5건)
  ```
  종료 코드는 1입니다. 첫 번째 실행에서 `| tail`을 거쳐 읽은 `exit=0`은 tail의 코드라서 무시했고, 따로 다시 실행해 1을 확인했습니다.
- 위 출력 위쪽에 있는 test_3 실패 메시지는 `AssertionError: 'PRJ-2602' not found in ...`입니다.
- `python -m unittest discover tests -q`는 `Ran 3 tests ... OK`였습니다.
- `python tools/check_tasks.py`(저장소 루트에서 실행)는 다음과 같이 출력했습니다.
  ```
  건너뜀 작업 1 / 공백 있음 작업 2(수용 시험 4, 5는 구현 전에도 통과) / 정상 작업 3(NO TESTS RAN) / 정상 작업 4(FAILED (failures=3)) / 건너뜀 작업 5
  요약: 공백 1건(작업 2)
  ```
- 읽기 확인한 파일은 DECISIONS.md, reference/CLAUDE.example.md, tasks.example.json, settings.example.json, RUNLOG.md, docs/example-facts.md, ch06 표 6-6, ch08-spec입니다.

### 일치를 확인한 것
- 결정 기록 코드 상자: 머리글, 구분선, D-012 행이 `examples/expense-app/DECISIONS.md`와 글자까지 같습니다. 표 제목 줄(`# 결정 기록`)만 빠졌습니다. D-015가 가상이라는 점은 본문 33행에 적혀 있습니다.
- 표 8-4: 갱신 주체와 읽는 순서가 규칙 문서와 맞습니다. 읽는 순서는 CR.md, DECISIONS.md, tasks.json, HANDOFF.md입니다. 수정 범위(HANDOFF.md는 수정 가능, DECISIONS.md와 CLAUDE.md는 수정 금지)와 작업 5의 통과 값을 사람이 바꾼다는 규칙도 맞습니다.
- 인계 메모의 "확인 명령" 설명: 작업 4 전에는 수용 시험 1~3이 실패하는 것이 실제 출력(failures=3)과 같습니다. 작업 5의 "사람이 승인한다"는 설명, 폴더 이름 expense-practice, `/new` 경로(app.py 21행)도 맞습니다.

| 번호 | 위치 | 원문 | 확인 결과(실행한 명령과 출력) | 고친 문안 | 등급 |
|---|---|---|---|---|---|
| 1 | ch08 인계 메모 코드 상자(70~74행)와 handover 절 41행 | 항목 정의는 "현재 상태: 최종 commit, 완료된 작업 단위, 진행 중인 작업 단위와 멈춘 이유"인데, 예의 현재 상태에는 최종 commit이 없음 | 정의 41행과 예 70행을 대조했습니다. 정의한 하위 요소가 예에서 빠졌습니다(R17). | `현재 상태: 최종 commit "작업 3 완료"(해시는 git log --oneline의 맨 위 줄). 작업 2, 3 완료(통과 값 true, 단위마다 commit). 진행 중인 작업 없음`. 또는 정의에서 "최종 commit"을 빼서 둘을 맞춥니다. | 필수 |
| 2 | ch08 인계 메모 70행, 표 8-6 진행 기록 행, 부록 lab-5 확인 | "작업 2 완료(통과 값 true)", "통과 값이 true가 된 작업(작업 2, 3)"을 작업 2의 완료 근거로 삼음 | `check_tasks.py`가 작업 2를 "공백 있음"으로 판정했습니다. 작업 2의 확인 방법(수용 시험 4, 5)은 구현 전에도 통과합니다. 작업 2의 완료 기준은 "정산 요청 데이터에 항목 추가"인데 이 기준을 증명하는 실행 근거가 없습니다(R6, R14). example-facts에도 Q-118이 작가 확인 대기로 있습니다. | 작가가 정해야 할 사안이라 고친 문안은 제안만 합니다. 작업 2에 구현 전 실패하는 시험(예: 저장한 요청에 project_code가 들어가는 단위 시험)을 추가하고 check.py를 그에 맞춰 조정하거나, 본문 문장을 "통과 값은 작업 2의 구현 증거가 아니다(공백, Q-118)"로 한정합니다. 확정 전까지 AUTHOR_QUEUE에 둡니다. | 필수 |
| 3 | 부록 lab-5 확인 방법 | "tasks.json에서 작업 2와 작업 3의 통과 값만 true로 변경되었습니다", `git diff HEAD~2 --stat`은 "수정 범위 안인지" 확인 | 두 확인 모두 작업 2의 새 요구(데이터 모델 항목 추가)를 증명하지 않습니다. 작업 2를 안 해도 통과 값 true와 수용 시험 4, 5 통과가 동시에 성립합니다(R14). | 한 줄을 더합니다. `작업 2의 구현은 git diff HEAD~2 -- expense/store.py expense/service.py에서 project_code 항목이 추가됐는지 직접 확인합니다. 수용 시험 4, 5 통과만으로는 증명되지 않습니다.` | 필수 |
| 4 | ch08 표 8-6 결정 기록 행 | "DECISIONS.md / D-012 한 건이 있음" | 구현 전부터 이미 충족되어 구현 전 실패 조건이 아닙니다(3.5). 실습 5, 6에는 DECISIONS.md를 바꾸는 단계가 없습니다. | 확인 기준을 "D-012 한 건이 있고, 에이전트가 수정하지 않음(`git diff HEAD~2 -- DECISIONS.md` 출력 없음). 대체 관계는 D-015를 직접 추가해 읽어 보는 선택 과제"로 바꿉니다. 또는 행 앞에 "기준 상태 확인"이라고 표시합니다. | 권고 |
| 5 | ch08 표 8-6 보관 기간 행 | "설정 파일의 cleanupPeriodDays / 확인에 필요한 기간 이상(없으면 기본 30일)" | 값이 없어도 "기본 30일"로 통과하므로 구현 전후 구분이 없습니다. 설정 파일 위치도 없고(research: 기본 30, 최솟값 1), 실습의 settings.example.json에도 이 키가 없습니다(grep으로 확인). | `사용자 설정 파일(Git Bash 등 macOS, Linux는 ~/.claude/settings.json, Windows는 %USERPROFILE%\.claude\settings.json)에서 cleanupPeriodDays 값을 확인합니다. 값이 없으면 기본 30일이므로, 완료 보고 확인에 30일이 모자라면 값을 정해 둡니다(예: 90).` | 권고 |
| 6 | ch08 76행, 표 8-6 세션 기록 행 | "사용자 폴더의 .claude/projects/ 아래 파일 ... 에서 python check.py 실행과 그 출력을 찾아 확인" | 찾는 방법과 Windows 경로가 없습니다. 구현 전에는 check.py 실행 기록이 없어 실패하고 뒤에는 통과하므로 방향은 맞습니다. 이 환경에서는 대화형 세션이 없어 실행하지 못했습니다(검증 후 확정). | `Git Bash, macOS, Linux: grep -l "python check.py" ~/.claude/projects/*/*.jsonl / PowerShell: Select-String -Path "$HOME\.claude\projects\*\*.jsonl" -Pattern "python check.py" -List` (하위 폴더 이름은 프로젝트 경로로 만들어짐) | 권고 |
| 7 | ch08 표 8-6 사용량 행 | "/usage / 사용량과 비용 추정치가 표시됨" | 세션을 시작하면 언제나 표시되므로 구현 전 실패 조건이 없습니다. 대화형 화면이라 실행하지 못했습니다(검증 후 확정). | 확인 기준을 "실습 6을 마친 세션에서 Session 항목의 토큰 사용량이 0이 아님"으로 바꿉니다(ch09 82행의 Session 항목 표현과 맞춤). | 권고 |
| 8 | ch08 표 8-6 진행 기록 행 | "git log --oneline과 tasks.json / 작업 2, 3마다 그 작업의 commit이 있음" | 실습 시작 상태 한 줄만 있으면 실패하고, 작업 단위 commit이 생기면 통과해 구현 전후 구분은 됩니다. 다만 `--oneline`은 메시지만 보여서 어느 작업의 commit인지는 메시지에 작업 번호가 있어야 알 수 있습니다. 이 규칙이 CLAUDE.md에 없습니다. | 확인 기준에 "(commit 메시지에 작업 번호가 있음)"을 더하거나, 규칙 문서의 commit 항목에 메시지 형식을 정합니다. | 권고 |
| 9 | ch08 인계 메모 확인 명령 줄 | "python check.py(acceptance의 시험 1~3이 아직 실패하는 것이 정상)" | 설명은 정확합니다. 종료 코드 1은 빠져 있고, 그 시점의 tests 줄은 "project_code 시험 1건 이상"이어야 합니다. 그 시점은 작업 3을 마친 상태라 실제 실행은 하지 못했습니다(검증 후 확정). | `확인 명령: python check.py(종료 코드 1이 정상. tests는 통과, acceptance 시험 1~3만 실패)` | 참고 |
| 10 | ch08 표 8-5 둘째 행, 표 8-6, 33행 | D-015는 가상이며 실습 폴더에는 D-012만 있음 | 본문 33행에 가상이라고 밝혀 R7 위반은 아닙니다. 표 8-5의 "방지 장치: D-015 예시"가 "실습 폴더에 있다"로 읽힐 수 있습니다. | `결정 기록에 새 결정과 대체 관계를 남김(가상의 D-015 예시)` | 참고 |
| 11 | ch08 76행, 표 8-6, 부록 lab-1·lab-6 | Windows | `cp -r`, `ls -a`, `echo $?`는 부록에서 Git Bash 기준 또는 PowerShell 대체 명령이 있습니다. `python app.py`와 `claude --continue`는 공통입니다. 8장 본문에서는 `.claude/projects/`의 Windows 위치와 PowerShell 검색 명령만 없습니다(6번 참고). | 6번 문안으로 처리합니다. | 참고 |
| 12 | 부록 lab-5, lab-6 전체 | `claude`, `/usage`, `/memory`, 훅, 확인 요청 화면 | 대화형 Claude Code와 계정 로그인이 필요해 실행하지 못했습니다. 각 단계의 서술이 파일 기준으로 모순되지 않는지만 대조했고 문제는 없었습니다. | 작가가 실제 실행 뒤 RUNLOG.md에 기록합니다(현재 "실행 전"). | 참고(검증 후 확정) |

### 판정
- 표 8-4, 결정 기록 코드 상자, `expense-practice` 이름, "시험 1~3 실패" 설명은 통과입니다.
- 필수 3건은 1번(인계 메모에 "최종 commit"이 빠짐), 2번과 3번(작업 2의 완료 근거 공백, R6·R14)입니다. 2번과 3번은 이미 알려진 Q-118과 같은 문제라, 6장 정비 결과에 맞춰 함께 처리하는 편이 좋습니다.

필수 수정 3, 편집 권고 5, 검증 후 확정 3(6, 7, 12번 계열), 실행한 명령 8개

(요약의 "참고 4"는 9~12번입니다. 참고 중 12번은 검증 후 확정에 해당하고, 6번과 7번의 대화형 부분도 그렇습니다.)
