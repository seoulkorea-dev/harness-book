# 3장 역할 검토: 실무자 2차 읽기(2026-10-22, 이슈 #66)

- **대상:** src/chapters/ch03.html 전체, 커밋 5cd7b1b. 원고를 먼저 처음부터 끝까지 읽었고, 기준 문서와 대조한 것은 그 뒤입니다. 파일은 하나도 고치지 않았습니다.
- **대조한 자료**
  - research/ch03-sources.md(C3-1~C3-11), research/ch03-10-sources.md 63행, research/ch01-sources.md S38, research/bibliography.json
  - docs/example-facts.md, docs/AUTHOR_QUEUE.md Q-118
  - examples/expense-app/: check.py, acceptance/test_cr07.py, tests/test_basic.py, reference/ 아래 파일 4개, README.md
  - src/appendix/practice.html(실습 2, 4), REVIEW_RULES.md(R1~R17), 1차 보고(…-practitioner-1.md)
- **공식 문서 확인(2026-10-22, WebFetch):** code.claude.com/docs/en/ 아래 permissions, hooks, cli-reference, permission-modes
- **실행한 명령과 출력 요지**
  - examples/expense-app에서 `python check.py`를 실행했습니다. 출력의 두 요약 줄은 다음과 같습니다. 그 밖에는 unittest가 실패한 test_1~3의 이름과 traceback만 나옵니다.
    ```
    tests: 실행 3건, 실패 0건, 건너뜀 0건, project_code 시험 0건
    acceptance: 실행 5건, 실패 3건, 건너뜀 0건(정한 수 5건)
    exit=1
    ```
  - `python -m unittest discover tests -q 2>/dev/null`은 아무것도 출력하지 않았습니다. 같은 명령을 `1>/dev/null`로 실행하면 "Ran 3 tests … OK"가 나옵니다. 그래서 "unittest는 결과를 오류 출력에 쓴다"가 맞다고 확인했습니다.
  - `python tools/check_tasks.py`의 결과는 "요약: 공백 1건(작업 2)"이고 exit=1입니다. Q-118대로입니다.
  - `python tools/check_all.py`는 빌드, 금칙어, 번호, 구조, 문체, 그림 안 이름, 검수 규칙을 모두 통과했습니다.
- **고칠 문장 비율:** 14 ÷ 175 = **8.0%**(1차는 34.1%). 표, 그림, 코드 지적 6건은 따로 셉니다.
  - 절별: 머리 0, spec 2, example 6, files 6, fail 0, check 0, principle 0

## 총평(3개 이내)

1. **"사람이 확인한다"를 기댄 마지막 방어선이 지금 제품의 기본 시작 모드에서는 성립하지 않습니다(높음).**
   - files 절의 "권한 모드가 사람에게 묻는 기본 모드라면"과 표 3-6의 4행("기본 권한 모드의 확인 요청이 보완")은 사람에게 묻는 모드를 전제로 합니다.
   - 그런데 v2.1.283 이상의 대화형 세션은 auto 모드로 시작합니다. 이 책의 기록(research/ch03-10-sources.md 63행, ch01 S38)에도 그렇게 적혀 있습니다. 그래서 독자 대부분에게는 git -C . push 같은 우회 명령을 사람이 아니라 분류기가 판단합니다. 문서에 따르면 ask 규칙에 일치하는 명령은 auto 모드에서도 묻습니다.
   - 또 이 예제에는 금지 규칙과 확인 요청을 모두 피해 가는 경로가 하나 남아 있습니다.
     - 허용된 `python -m unittest *`와 편집 뒤 훅은 에이전트가 쓸 수 있는 tests/의 코드를 묻지 않고 실행합니다.
     - 그래서 시험 코드가 acceptance/를 직접 고치면, 모드와 관계없이 금지 규칙에도 확인 요청에도 걸리지 않습니다.
     - 실제 방어선은 commit 확인 때 사람이 보는 바뀐 파일 목록입니다.
2. **완료 판정과 검토의 관계가 문단끼리 어긋납니다(R14, R15, R16, 높음).**
   - 40행은 "작업 2는 수용 시험으로 판정하니 꾸밀 수 없다"고 하고, 42행은 "작업 2의 확인은 구현 전에도 통과한다"고 합니다.
   - 43행은 "검토 대조는 완료 판정에 들어가지 않는다"고 하는데, 40행과 42행은 작업 2와 3의 완료를 검토와 commit 확인으로 보완한다고 합니다.
   - 실행 순서상 통과 값을 true로 바꾼 다음에야 검토와 commit 확인이 이어지는데, 거절됐을 때 통과 값을 되돌리는 절차가 없습니다.
   - "세 번 연속 실패"를 무엇으로 세는지(편집마다 도는 훅인지, 작업을 마칠 때 돌리는 check.py인지)도 정하지 않았습니다.
3. **1차 지적은 대부분 반영됐습니다.**
   - 반영된 것: CR 표기 0건, #ref- 0건, 같은 장 링크 0건, 실패 표와 확인 표의 열 세트, Edit 금지 규칙의 적용 범위, git -C . push, $CLAUDE_PROJECT_DIR, 결과가 stderr로 간다는 설명, -p 전용, 작업별 완료 판정, 중단 범위, 검토 요청에 바뀐 파일 목록, 작업 3의 방어선, 삭제 대신 내용 약화 예시
   - 새로 쓴 문장 가운데 사실관계가 맞는 것: Edit 금지 규칙의 범위, git -C . push, 훅의 현재 폴더와 $CLAUDE_PROJECT_DIR, unittest의 stderr, --max-turns와 --max-budget-usd가 -p 전용이라는 것
   - 반영되지 않은 것: /agents 확인(낮음)

## 발견

| 발견 | 위치(절과 문장 첫머리) | 근거 | 제안(고친 문장) | 확신 |
|---|---|---|---|---|
| 승인 지점을 권한 규칙으로만 구현한다고 씁니다. 그런데 예제의 작업 5 승인(통과 값)은 규칙 문서의 지시로만 막습니다 | spec "승인 지점은 권한 규칙(Permission Rule)으로 구현하지만" | 표 3-3 승인 지점 행, CLAUDE.example.md "작업 5의 통과 값은 변경하지 않는다"(지시), R16 | 승인 지점은 주로 권한 규칙의 확인 요청으로 구현하지만, 사람이 어느 동작에서 개입할지는 업무에 따라 정합니다. | 중간 |
| 목록처럼 끝까지 다 든 것으로 읽힙니다. 스킬, MCP 설정 같은 다른 제품 파일도 있습니다 | spec "규칙 문서(CLAUDE.md), 권한 규칙과 훅(Hook)을 담는 설정 파일, 하위 에이전트(Subagent) 정의가 제품 파일입니다." | R1(범위), R13 | 이 장에서 다루는 제품 파일은 규칙 문서(CLAUDE.md), 권한 규칙과 훅(Hook)을 담는 설정 파일, 하위 에이전트(Subagent) 정의 셋입니다. | 낮음 |
| check.py가 셈하는 "이름"은 시험 함수 이름이 아니라 모듈.클래스.함수를 합친 id입니다. tests/test_project_code.py 안에 아무 시험이나 하나 있어도 1건으로 셉니다. 대소문자도 구분합니다 | example "…단위 테스트에 이름에 project_code가 든 시험이 1건 이상이어야 합니다." | check.py `UNIT_KEYWORD in i`(i는 item.id()), R8 | …단위 테스트에 시험 id(파일, 클래스, 함수 이름)에 project_code가 든 시험이 1건 이상이어야 합니다. | 중간 |
| 통과 값 변경에 주체를 정해 두었지만, 이를 강제하는 장치가 없습니다. tasks.json 전체가 수정 허용 범위라서 에이전트는 작업 5의 통과 값도, 각 작업의 "확인 방법" 문구도 바꿀 수 있습니다. Edit 규칙은 JSON 항목 단위로 막지 못합니다 | example "통과 값은 구현 에이전트가 변경하고, 사람이 승인하는 작업 5의 통과 값만 사람이 변경합니다." | settings.example.json(tasks.json 금지 없음), CLAUDE.example.md 수정 범위, R15, R16 | 통과 값은 구현 에이전트가 변경하고, 사람이 승인하는 작업 5의 통과 값만 사람이 변경합니다. tasks.json은 에이전트가 수정할 수 있는 파일이므로, 작업 5의 통과 값과 확인 방법 문구가 바뀌지 않았는지는 commit 확인에서 tasks.json의 변경 내용으로 봅니다. | 높음 |
| 42행과 모순됩니다. 작업 2의 수용 시험 4와 5는 구현 전에도 통과하므로, 꾸밀 필요조차 없습니다 | example "작업 2와 작업 4는 수용 시험으로 완료를 판정하므로, 단위 테스트를 수정해도 완료를 꾸밀 수 없습니다." | check_tasks.py "공백 있음 작업 2", Q-118, R14 | 작업 4는 사람이 작성한 수용 시험으로 완료를 판정하므로, 단위 테스트를 수정해도 완료를 꾸밀 수 없습니다. | 높음 |
| (1) check.py의 요약 줄은 수용 시험 건수만 보여 주므로, "시험 4와 5 통과"는 실패 목록에 test_4와 test_5가 없다는 것으로 미루어 알아야 합니다. (2) 작업 3의 확인 대상(단위 테스트)은 훅이 편집할 때마다 실행합니다. 그래서 "세 번 연속"을 훅 실행으로 세면 시험을 먼저 쓰는 정상적인 진행도 곧 중단 규칙에 걸립니다. 그림 3-1은 이미 검사 스크립트에서 중단으로 가는 화살표를 그렸으니, 본문을 그림에 맞춥니다 | example "그래서 완료는 검사 스크립트 출력에서 그 작업 단위가 맡은 시험이 통과했는지로 판정하고, 중단 규칙도…" | check.py 실행 출력(요약 줄과 FAIL 목록), settings 훅, 그림 3-1, R17 | 그래서 완료는 검사 스크립트 출력에서 그 작업 단위가 맡은 시험이 실패 목록에 없는지로 판정하고, 중단 규칙도 작업 단위를 마칠 때 실행한 검사 스크립트에서 확인 대상 시험이 세 번 연속 실패할 때만 적용합니다(편집 뒤 훅의 실패는 세지 않습니다). | 높음 |
| 40행과 42행은 작업 2와 3의 완료를 검토와 commit 확인으로 보완한다고 하는데, 이 문장은 검토가 완료 판정에 들어가지 않는다고 합니다. 통과 값을 true로 바꾼 뒤 검토나 commit 확인에서 거절되면 어떻게 하는지도 없습니다 | example "검토 하위 에이전트의 대조는 완료 판정에 들어가지 않고, commit 확인 전에 한 번 더 보는 절차입니다." | CLAUDE.example.md 작업 순서(통과 값 true, 검토 요청, commit의 순서), R14, R15 | 통과 값은 확인 방법으로 판정하지만, 작업 단위의 완료가 확정되는 것은 검토 대조 뒤 사람이 commit을 승인할 때입니다. 사람이 수정을 요청하면 구현 에이전트는 그 작업 단위의 통과 값을 false로 되돌리고 다시 작업합니다. | 높음 |
| "사람만 실행"은 넘친 표현입니다. 바로 뒤 files 절에서 우회 명령이 있다고 밝히고, auto 모드에서는 그 우회 명령을 분류기가 판단합니다 | example "변경 확정(git commit)은 실행 전에 사람의 확인을 받고, 원격 저장소 반영(git push)은 금지 규칙으로 막아 사람만 실행합니다." | permissions(Bash rule limits), permission-modes(대화형 세션은 auto로 시작), R1 | 변경 확정(git commit)은 실행 전에 사람의 확인을 받게 하고, 원격 저장소 반영(git push)은 금지 규칙으로 막아 사람이 실행합니다. 다르게 작성한 명령은 규칙과 일치하지 않으므로 뒤의 제품 파일 절에서 보완 방법을 다룹니다. | 중간 |
| Edit 규칙은 Write를 포함한 내장 편집 도구 전체에 적용되고, Write(경로) 규칙은 아예 쓰이지 않습니다. 그런데 훅의 matcher는 Edit\|Write로 둘을 나누어 적습니다. 그래서 독자는 deny 목록에 Write가 빠졌다고 오해하기 쉽습니다 | files "Edit는 파일 수정 도구, Bash는 명령 실행 도구입니다." | permissions("If you write a path rule for Write … never consults it. Use Edit(docs/**)"), C3-9 | Edit 규칙은 파일을 고치거나 새로 쓰는 내장 편집 도구(Edit, Write) 전체에 적용되고, Bash는 명령 실행 도구입니다. | 높음 |
| ./는 현재 폴더 기준입니다. 훅 문단은 세션이 하위 폴더로 옮겨 갈 수 있다는 이유로 $CLAUDE_PROJECT_DIR을 씁니다. 같은 이유라면 금지 경로도 설정 파일 기준인 /acceptance/** 형식이 더 안전합니다. 둘의 설명이 엇갈립니다 | files "…./는 현재 폴더를 기준으로 한 경로입니다" | permissions 경로 표("/path relative to the settings source", "./path relative to current directory") | …./는 현재 폴더(Claude Code를 시작한 실습 폴더)를 기준으로 한 경로입니다. (실습 파일을 /acceptance/** 형식으로 바꿀지는 작가 확인) | 중간 |
| (1) v2.1.283 이상의 대화형 세션은 auto 모드로 시작하므로 "사람에게 묻는 기본 모드"라는 전제가 독자 환경과 다릅니다. (2) 바로 앞 문장의 "스크립트가 파일을 직접 여는 경우"는 이 예제에서는 허용된 unittest 명령과 훅으로 일어나므로 확인 요청이 뜨지 않습니다 | files "권한 모드(Permission Mode)가 사람에게 묻는 기본 모드라면, 허용 목록에 없는 명령은 실행 전에 확인을 요청하므로…" | permission-modes("interactive … starting mode is auto with v2.1.283 or later", Manual = default), research/ch03-10-sources.md 63행, 실습 2 단계 6("권한 모드에 따라 확인 화면 없이"), settings allow, R4, R13 | 이 예제는 사람에게 묻는 수동(Manual, 설정 값 default) 권한 모드(Permission Mode)로 진행합니다. 대화형 세션은 버전에 따라 auto 모드로 시작하므로, 설정 파일의 permissions.defaultMode나 시작 옵션으로 모드를 정합니다<sup class="cite" data-ref="permission-modes"></sup>. 수동 모드에서는 허용 목록 밖의 명령이 실행 전에 확인을 요청하지만, 허용한 단위 테스트 명령과 훅은 에이전트가 쓴 시험 코드를 묻지 않고 실행합니다. 그래서 그 코드가 금지한 파일을 바꾸는 경우는 commit 확인에서 바뀐 파일 목록으로 확인합니다. | 높음 |
| 원인과 목적이 한 문장에 엉켜 있습니다("…실행되므로, …하려는 것입니다") | files "훅의 명령은 세션의 현재 폴더에서 실행되므로, 세션이 하위 폴더로 옮겨 가도 같은 시험을 실행하게 하려는 것입니다" | hooks("Handlers run in the current directory"), 문체 | 훅의 명령은 세션의 현재 폴더에서 실행되므로, 세션이 하위 폴더로 옮겨 가면 상대 경로 tests를 찾지 못해 명령 오류가 시험 실패처럼 전달됩니다. 그래서 먼저 프로젝트 폴더로 이동합니다. | 중간 |
| WebFetch와 WebSearch를 빼도 Bash의 curl 같은 명령은 남습니다. 이런 명령은 허용 목록 밖이라 확인 요청 대상이 되며, 이 역시 권한 모드에 따라 달라집니다 | files "웹 페이지를 가져오는 WebFetch와 웹을 검색하는 WebSearch는 … 이 형식의 금지 규칙으로 막습니다." | permissions(Restrict Bash network tools) | …이 형식의 금지 규칙으로 막습니다. curl처럼 웹에 접근하는 셸 명령은 허용 목록 밖이라 실행 전에 확인을 요청합니다. | 낮음 |
| git status 출력은 파일 이름만 보여 줍니다. 검토 하위 에이전트는 Read만으로는 무엇이 바뀌었는지 알 수 없습니다. git diff는 허용 목록에 있으므로 구현 에이전트가 그 출력을 넘길 수 있습니다 | files "그래서 규칙 문서의 작업 순서에 … 바뀐 파일 목록(git status 출력)과 함께…" | settings allow(Bash(git diff *)), reviewer.example.md | …바뀐 파일 목록(git status 출력)과 변경 내용(git diff 출력)을 함께… (CLAUDE.example.md도 같이 고칠지는 작가 확인) | 낮음 |

### 표, 그림, 코드(별도 6건)

| 발견 | 위치 | 근거 | 제안 | 확신 |
|---|---|---|---|---|
| "기본 권한 모드의 확인 요청이 보완"은 auto 모드로 시작하는 환경에서는 성립하지 않습니다 | 표 3-6 4행 방지 장치 | permission-modes, 위 files 발견과 같음 | 강제: 확인 요청(git commit), 금지(git push). 다르게 작성한 명령은 수동 모드의 확인 요청과 commit 확인이 보완 | 높음 |
| tasks.json의 통과 값과 확인 방법을 에이전트가 바꾸는 실패가 빠져 있습니다. 작업 5의 승인을 확정하는 일이 지시로만 지켜집니다 | 표 3-6(행 추가 또는 1행 보강) | R15, R16, settings(tasks.json 금지 없음) | 행 추가: 실패 유형 "작업 5의 통과 값이나 확인 방법 문구를 에이전트가 변경함", 원인 "승인 지점, 기록: 진행 기록 전체가 수정 허용 범위", 방지 장치 "지시: 작업 5의 통과 값은 변경하지 않음. 승인: commit 확인에서 tasks.json 변경 확인" | 중간 |
| 확인 표가 설정이 화면에 보이는지만 확인합니다. 권한 모드와, 금지 규칙이 실제로 거부하는지는 확인하지 않습니다 | 표 3-7 | R13, ch10 표 10-5(동작 확인 방식), 실습 2의 모드 주석 | 행 추가: "권한 모드 / 입력창 아래 모드 표시 / Manual(default)", "금지 동작 / acceptance/ 수정 요청 / 거부됨". 실습 3과 연결할지는 practice-checker 확인 | 중간 |
| 본문은 "사람은 … 승인하거나 수정을 요청합니다"라고 하는데, 그림에는 검토 대조나 commit 확인에서 파일 수정으로 돌아가는 경로가 없습니다. 통과 값을 되돌리는 일도 없습니다 | 그림 3-1 아래 흐름 | 47행, R17 | commit 확인에서 파일 수정으로 가는 점선 "수정 요청 시(통과 값 false)"를 더함 | 중간 |
| 검증 행이 작업 2의 공백을 드러내지 않아 본문 42행과 수준이 다릅니다 | 표 3-2 검증 행 | Q-118, R14, R17 | "작업 2, 4는 맡은 수용 시험 통과(작업 2는 구현 전에도 통과해 검토와 commit 확인으로 보완)…" | 중간 |
| 설정 예시에 권한 모드가 없어 auto 모드로 시작하는 환경에서 예제의 전제가 깨집니다. ./ 경로도 시작 폴더에 따라 달라집니다 | settings 코드 블록, reference/settings.example.json | permission-modes(permissions.defaultMode 우선), permissions 경로 표 | `"permissions": { "defaultMode": "default", … }`를 더하고, 금지 경로를 `Edit(/acceptance/**)` 형식으로 바꿀지 검토합니다. 실습 파일 변경이라 작가 확인 | 중간 |

**작가 확인 후보:** settings에 defaultMode를 둘지와 금지 경로 형식(/), CLAUDE.example.md의 검토 요청에 git diff를 넣을지, 표 3-6에 행을 더할지(대표 다섯 가지에서 여섯 가지로)입니다. Q-118은 그대로 둡니다.

**fact-checker가 확인할 것**
- Bash로 cd를 실행해 세션의 현재 폴더가 바뀔 때 ./ 금지 경로의 기준도 함께 바뀌는지(문서는 "relative to current directory"라고만 씁니다)
- 실습 환경 v2.1.302에서 대화형 세션이 처음에 어떤 모드로 시작하는지, 실행해서 RUNLOG.md에 남길 것
=== CLAUDE.example.md
# 경비 정산 미니 웹 앱: 변경 요청 사항(docs/CR.md) 구현

## 목적
재무팀이 월말 결산에서 프로젝트별 경비를 집계할 수 있도록, 정산 요청에 프로젝트 코드를 기록한다(docs/CR.md).

## 읽는 순서
1. docs/CR.md(수용 기준)
2. DECISIONS.md
3. tasks.json
4. HANDOFF.md(있으면)

## 작업 순서
- tasks.json에서 "통과"가 false인 첫 작업 단위만 수행한다. 작업 5의 "통과" 값은 변경하지 않는다.
- 작업 단위를 마치면 python check.py를 실행하고, 출력이 tasks.json에 적은 그 단위의 "확인 방법"을 충족하면 그 단위의 "통과" 값만 true로 변경한다. 다음 작업 단위가 맡은 수용 시험의 실패는 이 판정에 넣지 않는다.
- 확인 방법을 충족하면 commit 전에 reviewer 하위 에이전트에게 바뀐 파일 목록과 변경 내용(git status, git diff 출력)을 넘겨 수용 기준 대조를 요청한다.
- 완료 보고에는 python check.py의 출력 원문과 reviewer의 대조 보고를 포함한다.
- 대조 보고 뒤 그 단위의 변경을 commit한다(commit은 사람 확인 후). 사람이 수정을 요청하면 그 단위의 "통과" 값을 false로 되돌리고 다시 작업한다.

## 수정 범위
- 수정할 수 있음: expense/, app.py, tests/, tasks.json의 "통과" 값, HANDOFF.md
- 수정하지 않음: data/, acceptance/, check.py, CLAUDE.md, DECISIONS.md, .claude/
- 수용 시험이 실패하면 시험이 아니라 구현을 고친다.

## 중단 규칙
- 작업 단위를 마칠 때 실행한 check.py에서 그 단위의 확인 방법에 든 시험이 세 번 연속 실패하면(편집 뒤 훅의 실패는 세지 않음) 중단하고 HANDOFF.md를 작성한다.
- 세션을 마칠 때 HANDOFF.md에 현재 상태, 읽을 문서, 미결정, 다음 작업, 확인 명령을 적는다.

## 명령
- 단위 테스트: python -m unittest discover tests -q
- 전체 검사: python check.py
- 앱 실행: python app.py (http://localhost:8000)
- macOS, Linux에서 python 명령이 없으면 python3를 사용한다.
=== reviewer.example.md
---
name: reviewer
description: 변경 요청 사항(docs/CR.md)의 변경 내용을 수용 기준과 대조해 보고하는 검토 에이전트
tools: Read, Grep, Glob
---
docs/CR.md의 수용 기준을 읽고, 요청에 적힌 바뀐 파일의 코드와 테스트가
기준마다 충족, 미충족, 확인 불가 가운데 어디에 해당하는지
근거 파일과 줄 번호를 함께 보고해 줘. 파일은 수정하지 마.
=== settings.example.json
{
  "permissions": {
    "allow": [
      "Bash(python -m unittest *)",
      "Bash(python check.py)",
      "Bash(python3 -m unittest *)",
      "Bash(python3 check.py)",
      "Bash(git status)",
      "Bash(git diff *)"
    ],
    "ask": [
      "Bash(git commit *)"
    ],
    "deny": [
      "Edit(./data/**)",
      "Edit(./acceptance/**)",
      "Edit(./check.py)",
      "Edit(./CLAUDE.md)",
      "Edit(./DECISIONS.md)",
      "Edit(./.claude/**)",
      "Bash(git push *)",
      "WebFetch",
      "WebSearch"
    ]
  },
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          { "type": "command", "command": "cd \"$CLAUDE_PROJECT_DIR\" && python -m unittest discover tests -q || exit 2" }
        ]
      }
    ]
  }
}
=== tasks.example.json
[
  {"id": "작업 1", "작업": "프로젝트 코드 조회 방식 합의", "완료 기준": "인사팀과 조회 방식과 갱신 주기 합의", "확인 방법": "결정 기록 D-012", "통과": true},
  {"id": "작업 2", "작업": "데이터 모델에 프로젝트 코드 항목 추가", "완료 기준": "정산 요청 데이터에 항목 추가, 기존 데이터 유지", "확인 방법": "python check.py의 수용 시험 4, 5 통과", "통과": false},
  {"id": "작업 3", "작업": "기존 단위 테스트 갱신", "완료 기준": "변경된 데이터 모델의 테스트 반영(project_code 시험 추가, 기존 시험 통과)", "확인 방법": "python check.py의 tests 실패 0건, project_code 시험 1건 이상", "통과": false},
  {"id": "작업 4", "작업": "정산 요청 화면에 선택 항목 추가", "완료 기준": "화면에서 프로젝트 코드 선택 가능, 목록에 없는 코드 거부", "확인 방법": "python check.py의 수용 시험 1, 2, 3 통과", "통과": false},
  {"id": "작업 5", "작업": "통합 테스트 시나리오 추가", "완료 기준": "프로젝트별 집계 시나리오 초안", "확인 방법": "사람 승인(통과 값은 사람이 변경)", "통과": false}
]
