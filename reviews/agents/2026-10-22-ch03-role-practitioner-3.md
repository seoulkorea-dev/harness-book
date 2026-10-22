# 3장 역할 검토: 실무자 3차 읽기(2026-10-22, 이슈 #66)

- **대상:** src/chapters/ch03.html 전체, 그림 3-1(SVG 라벨 전부), 커밋 7381fcf. 원고를 먼저 처음부터 끝까지 읽었고, 기준 문서와 대조한 것은 그 뒤입니다. 파일은 하나도 고치지 않았고, 작업 트리도 깨끗합니다.
- **대조한 자료**
  - research/ch03-sources.md(C3-1~C3-11), research/ch03-10-sources.md(permission-modes 기록), research/ch01-sources.md S38과 S18 재확인
  - docs/AUTHOR_QUEUE.md Q-110, Q-118~Q-120
  - examples/expense-app/: check.py, acceptance/test_cr07.py, tests/test_basic.py, reference/ 아래 파일 4개(CLAUDE.example.md, settings.example.json, reviewer.example.md, tasks.example.json)
  - src/appendix/practice.html(실습 1~6의 모드와 종료 코드 서술), 2차 보고
- **공식 문서 확인(2026-10-22, WebFetch)**
  - code.claude.com/docs/en/permission-modes에서 확인한 내용
    - 대화형 세션은 v2.1.283 이상에서 auto 모드로 시작합니다.
    - Manual 모드의 설정 값은 `default`이고, 별칭으로 `manual`도 받습니다. 시작 옵션은 `claude --permission-mode default`입니다.
    - 금지 규칙은 모든 모드에서 막습니다.
    - 명령 내용에 일치하는 ask 규칙은 auto 모드에서도 확인을 요청합니다.
    - auto 모드의 분류기는 기본으로 다음을 허용합니다: "Pushing to any branch of the repository you're working in, including the default branch"
  - code.claude.com/docs/en/permissions에서 확인한 내용
    - Edit 규칙은 내장 편집 도구 전체에 적용됩니다. 파일을 직접 여는 Python 하위 프로세스에는 적용되지 않습니다.
    - 도구 이름만 적은 deny 규칙은 그 도구를 컨텍스트에서 없앱니다.
    - `./path`는 현재 폴더 기준이고, `/path`는 설정 파일 기준입니다.
    - `git -C . push`는 `Bash(git push *)`와 일치하지 않습니다.
- **실행한 명령과 출력 요지**
  - `(cd examples/expense-app && python check.py)`의 두 요약 줄입니다.
    `tests: 실행 3건, 실패 0건, 건너뜀 0건, project_code 시험 0건`
    `acceptance: 실행 5건, 실패 3건, 건너뜀 0건(정한 수 5건)`
    실패한 시험은 test_1, test_2, test_3이고 종료 코드는 1입니다. test_4와 test_5는 구현 전에도 통과합니다(Q-118대로).
  - `python tools/check_all.py`는 빌드, 금칙어, 번호, 구조, 문체, 그림 안 이름, 검수 규칙을 모두 통과했습니다. check_tasks의 결과는 "요약: 공백 1건(작업 2)"로 Q-118대로입니다.
- **고칠 문장 비율:** 6 ÷ 189 = **3.2%**(1차 34.1%, 2차 8.0%). 표와 그림 지적 4건은 따로 셉니다.
  - 절별: 머리 0, spec 0, example 3, files 3, fail 0, check 0, principle 0

## 총평(3개 이내)

1. **2차 지적은 거의 다 반영됐고, 본문, 실습 규칙 문서, tasks.json, 그림이 같은 규칙을 말합니다(R17).**
   - 반영된 것: 완료 판정, 검토, commit 승인의 순서, 수정 요청 때 통과 값을 false로 되돌리는 규칙, 중단 셈(작업 단위 끝의 check.py만 셈), 작업 2와 3의 공백을 사람의 commit 확인으로 보완한다는 서술
   - 그 밖에 반영된 것: Edit 규칙의 적용 범위(Edit, Write), 시험 id, 허용한 시험 명령 경로, curl, git diff 전달, 그림의 되돌림 점선
   - 반영되지 않은 것: 작업 5의 통과 값을 실제로 지키는 장치(tasks.json 전체가 수정 허용 범위인 문제)
2. **남은 실무상 공백은 auto 모드 하나입니다(높음).**
   - 본문은 "수동 모드라면"으로 조건을 밝혔지만, auto 모드에서 무엇이 달라지는지는 쓰지 않았습니다.
   - 문서에 따르면 auto 분류기는 작업 중인 저장소로의 push를 기본으로 허용합니다. 그래서 `git -C . push` 같은 우회 명령을 사람도 분류기도 막지 않습니다.
   - 표 3-6 4행의 "commit 확인이 보완"은 push 우회에는 성립하지 않습니다. commit 확인은 push를 보지 않습니다.
   - 실습 파일과 부록도 모드를 정하지 않습니다. 그래서 최신 버전 독자는 auto 모드에서 실습합니다.
3. **나머지는 문장 단위의 정밀도 문제입니다.** 단언이 조금 넘친 곳 하나(작업 4 "꾸밀 수 없습니다"), 기준 폴더 설명이 서로 엇갈리는 곳 하나(./ 경로와 훅의 현재 폴더), 판정 방법 서술이 작업 3과 맞지 않는 곳 하나입니다.

## 발견

| 발견 | 위치(절과 문장 첫머리) | 근거 | 제안(고친 문장) | 확신 |
|---|---|---|---|---|
| auto 모드에서 무엇이 달라지는지 빠져 있습니다. 문서에 따르면 auto 분류기는 작업 중인 저장소의 어느 브랜치로든 push하는 것을 기본으로 허용합니다. 그래서 금지 규칙과 일치하지 않는 `git -C . push`는 auto 모드에서 확인 없이 실행될 수 있습니다. 확인 요청 규칙 `Bash(git commit *)`는 auto 모드에서도 확인을 요청합니다. | files "대화형 세션은 버전에 따라 Claude Code가 호출을 자동으로 판단하는 auto 모드로 시작하므로, 모드는…" | permission-modes("Pushing to any branch of the repository you're working in, including the default branch"가 기본 허용 목록에 있음, "Ask rules that match on a command's content … fall back to a permission prompt"), permissions 우회 명령 표, R4, R13 | 대화형 세션은 버전에 따라 분류기가 호출을 판단하는 auto 모드로 시작하며, 문서에 따르면 auto 모드는 작업 중인 저장소로의 push를 기본으로 허용하므로 다르게 작성한 push 명령은 막히지 않습니다. | 높음 |
| 본문은 "설정 파일의 defaultMode"로 모드를 정한다고 합니다. 그런데 바로 앞에 보인 설정 파일(settings.example.json)과 부록 실습에는 모드 설정이 없습니다(R17). 모드를 설정 파일에 둘지는 작가 확인 대상이므로, 본문에서는 시작 옵션만 구체적으로 밝힙니다. | files "…모드는 설정 파일의 defaultMode나 시작 옵션으로 정합니다." | settings.example.json(defaultMode 없음), practice.html 실습 2, 4("권한 모드에 따라 확인 화면 없이"), permission-modes(`claude --permission-mode default`, 별칭 manual) | 이 장의 실습 파일은 모드를 정하지 않으므로, 수동 모드로 진행하려면 claude --permission-mode manual로 시작하거나 설정 파일의 defaultMode에 default를 적습니다. | 높음 |
| 단언이 넘칩니다. 같은 장 files 절은 허용한 단위 테스트 명령과 훅이 에이전트가 작성한 시험 코드를 실행하고, 그 코드가 금지한 파일(acceptance/)을 바꿀 수 있다고 씁니다. 그러면 단위 테스트를 고쳐서 완료를 꾸미는 경로가 남습니다(R14). | example "작업 4는 사람이 작성한 수용 시험으로 완료를 판정하므로, 단위 테스트를 수정해도 완료를 꾸밀 수 없습니다." | ch03 files 절 "어느 모드에서든 허용한 단위 테스트 명령과 훅은…", permissions("arbitrary subprocesses … like a Python … script that opens files itself"), R14, R17 | 작업 4는 사람이 작성한 수용 시험으로 완료를 판정하므로, 단위 테스트의 판정을 바꾸는 것만으로는 완료를 꾸밀 수 없습니다(시험 코드가 다른 파일을 바꾸는 경로는 제품 파일로 옮기기 절에서 다룹니다). | 중간 |
| 2차 지적이 반영되지 않았습니다. 작업 5의 통과 값을 사람이 바꾼다는 것은 규칙 문서의 지시뿐입니다. tasks.json 전체가 수정 허용 범위이고, Edit 규칙은 JSON 항목 단위로 막지 못합니다. 작업 5의 통과 값이나 각 작업의 확인 방법 문구가 바뀌어도 막는 장치가 없습니다. | example "작업 1의 통과 값은 처음부터 true이고, 작업 2~4의 통과 값은 구현 에이전트가, 사람이 승인하는 작업 5의 통과 값은 사람이 변경합니다." | settings.example.json(tasks.json 금지 없음), CLAUDE.example.md "작업 5의 '통과' 값은 변경하지 않는다"(지시), R15, R16 | (뒤에 한 문장 추가) tasks.json은 에이전트가 수정할 수 있는 파일이므로, 작업 5의 통과 값과 확인 방법 문구가 바뀌지 않았는지는 사람이 commit 확인에서 tasks.json의 변경 내용으로 봅니다. | 중간 |
| 작업 3의 확인 방법(tests 실패 0건, project_code 시험 1건 이상)은 실패 목록이 아니라 요약 줄로 판정합니다. "실패 목록에 없는지"만으로는 작업 3의 둘째 조건을 볼 수 없습니다. | example "그래서 확인 방법은 검사 스크립트 출력의 실패 목록에 그 작업 단위가 맡은 시험이 없는지로 판정합니다." | tasks.example.json 작업 3, check.py 요약 줄(`project_code 시험 n건`) | 그래서 확인 방법은 검사 스크립트 출력의 요약 줄과 실패 목록에서 그 작업 단위가 맡은 시험만 보고 판정합니다. | 낮음 |
| 괄호 안 설명은 현재 폴더를 시작 폴더와 같다고 봅니다. 그런데 훅 문단은 세션이 하위 폴더로 옮겨 갈 수 있다고 씁니다. 문서는 `./path`를 "relative to current directory"로, `/path`를 "relative to the settings source"로 구분합니다. 두 문단을 함께 읽으면 금지 경로의 기준이 바뀔 수 있는지 독자가 판단할 수 없습니다(R17). | files "…./는 현재 폴더(Claude Code를 시작한 실습 폴더)를 기준으로 한 경로입니다." | permissions 경로 표, hooks("Handlers run in the current directory"), ch03 훅 문단, 2차 보고의 fact-checker 확인 요청(미확인) | ./는 현재 폴더를 기준으로 한 경로이며, 이 실습은 실습 폴더에서 Claude Code를 시작하고 그 폴더에서 작업한다고 전제합니다. (설정 파일 기준인 /acceptance/** 형식으로 바꿀지는 작가 확인) | 낮음 |

### 표, 그림(별도 4건)

| 발견 | 위치 | 근거 | 제안 | 확신 |
|---|---|---|---|---|
| commit 확인은 push 우회를 보지 못합니다. 그리고 auto 모드에서는 "수동 모드의 확인 요청"이 없고, 분류기가 push를 허용합니다. | 표 3-6 4행 방지 장치 "승인: 다르게 작성한 명령은 수동 모드의 확인 요청과 commit 확인이 보완" | permission-modes 기본 허용 목록, 위 files 첫 발견 | 강제: 확인 요청(git commit), 금지(git push). 승인: 다르게 작성한 명령은 수동 모드의 확인 요청이 보완(auto 모드에서는 push 우회가 허용될 수 있음) | 높음 |
| 수정 요청 경로에는 "통과 값 false"가 있지만, 앞으로 가는 경로에는 통과 값을 true로 바꾸는 단계가 없습니다. 그래서 본문("확인 방법을 충족하면 구현 에이전트가 통과 값을 변경하고…")과 그림의 수준이 다릅니다(R17). | 그림 3-1 "확인 충족 시" 화살표 라벨 | ch03 그림 설명 문단, CLAUDE.example.md 작업 순서 | 라벨을 "확인 충족 시(통과 값 true)"로 바꿉니다 | 중간 |
| "작성(사람 전용)"이 원본 자료도 포함합니다. 그런데 본문은 data/projects.csv를 인사 시스템이 하루 한 번 갱신한다고 씁니다. | 그림 3-1 수정할 수 없는 파일 영역, 사람(승인자) "작성(사람 전용)" | ch03 example "인사 시스템이 하루 한 번 갱신하는 data/projects.csv" | "작성(사람과 외부 시스템)", 또는 각주로 "원본 자료는 인사 시스템이 갱신" | 낮음 |
| 확인 표에 권한 모드 행이 없습니다(2차 지적이 작가 확인으로 남아 있음). 위 auto 발견을 고려하면 실무에서 가장 먼저 확인할 값입니다. | 표 3-7 | permission-modes, practice.html(모드 지정 없음) | 행 추가: "권한 모드 / 입력창 아래 모드 표시(Shift+Tab) / Manual(수동 모드로 진행할 때)". 실습과 연결할지는 practice-checker와 작가 확인 | 낮음 |

**사실이 맞는다고 확인한 새 문장과 수정 문장:**
- Edit 규칙의 적용 범위(Edit, Write, 그리고 Claude Code가 알아보는 파일 명령)
- 도구 이름만 적은 deny 규칙이 도구를 컨텍스트에서 없앤다는 설명
- `git -C . push`가 규칙과 일치하지 않는다는 설명
- PostToolUse 훅이 종료 코드 2로 끝날 때의 동작과 unittest의 stderr 출력
- `$CLAUDE_PROJECT_DIR`
- --max-turns와 --max-budget-usd가 -p 전용이라는 설명
- tools 줄을 생략하면 하위 에이전트가 주 에이전트의 도구를 물려받는다는 설명
- 확인 요청 규칙이 auto 모드에서도 확인을 요청한다는 점(본문의 "commit은 확인 요청"은 모드와 관계없이 성립합니다)
- 구현 전 check.py 출력(test_1~3 실패, 종료 코드 1)

**작가 확인 후보:**
- 실습 설정에 defaultMode를 넣을지, 또는 부록에 `--permission-mode manual` 시작 옵션을 넣을지. 위 auto 발견 때문에 우선순위를 올리기를 권합니다.
- 금지 경로를 `/` 형식으로 바꿀지
- 표 3-6에 tasks.json 변경 행을 더할지
- Q-118은 그대로 둡니다.
