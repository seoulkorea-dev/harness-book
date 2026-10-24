# 5장 실습 점검(practice-checker, 2026-10-24, 커밋 0aac12e)

결론: 필수 0, 권고 1, 참고 3. 예제 절, 표 5-5·5-6·5-7, 부록 실습 2·3·5는 examples/expense-app/ 원본, docs/example-facts.md와 일치하고, 실행한 범위에서 설명과 다른 결과는 없었습니다. 원고와 실습 파일은 고치지 않았습니다.

| 번호 | 등급 | 위치 | 문제 | 근거 | 고칠 문안 |
|---|---|---|---|---|---|
| 1 | 편집 권고 | src/chapters/ch05.html:108 (표 5-7, 규칙의 실제 준수) | 확인 기준의 후반부 "tasks.json은 그 단위의 '통과' 값만 바뀜"을 git show --stat HEAD가 보여 주지 못합니다. --stat은 파일 이름과 줄 수만 보여 주므로 바뀐 줄이 "통과" 값인지는 알 수 없습니다. 파일 범위 확인은 --stat으로 충분합니다. 실습 5에도 "통과 값만 true" 확인용 명령은 없습니다(실습 5 따라 하기 1단계의 git diff HEAD -- tasks.json은 commit 전 변경을 보는 용도). | 복사본에서 재현: tasks.json의 작업 2 "통과"만 true로 바꾸고 CLAUDE.md를 추가해 commit한 뒤 git show --stat HEAD를 실행했습니다. 출력은 "CLAUDE.md \| 1 +", "tasks.json \| 2 +-", "2 files changed"였고, 바뀐 줄의 내용은 나오지 않았습니다. 작업 단위가 한 줄이므로 +-가 1줄씩이어야 한다는 간접 신호일 뿐입니다. | 원문(한 번만 나옴): "작업 단위의 commit 뒤 git show --stat HEAD(commit 전이면 git status)". 바꿀 문장: "작업 단위의 commit 뒤 git show --stat HEAD로 바뀐 파일을, git show HEAD -- tasks.json으로 바뀐 줄을 봄(commit 전이면 git status와 git diff -- tasks.json)". 실습 5 확인 방법의 "tasks.json에서 작업 2와 작업 3의 통과 값만 true로 변경되었습니다." 뒤에 "(git show HEAD -- tasks.json 또는 git diff HEAD~2 -- tasks.json으로 확인)"을 붙이면 표와 맞습니다. |
| 2 | 참고 | ch05.html 예제 절 코드 상자 | 문제 없음(요청하신 확인 1). 코드 상자는 CLAUDE.example.md 6~10행(읽는 순서)과 19~21행(수정 범위)에 글자까지 같습니다(파이썬 줄 단위 비교 True, True). 22행("수용 시험이 실패하면 구현을 고친다")을 뺀 것은 "두 절의 발췌"로 설명되어 문제 없습니다. 여섯 절(목적, 읽는 순서, 작업 순서, 수정 범위, 중단 규칙, 명령)과 32줄도 맞습니다. | wc -l CLAUDE.md는 32, splitlines 길이도 32, "^## " 헤더는 6개입니다. 표 5-5의 "여섯 절, 빈 줄 포함 32줄"과 같습니다. | 수정 없음 |
| 3 | 참고 | 표 5-5 작업 입력, 실습 5 | 문제 없음(요청하신 확인 2). 요청 문장 "CLAUDE.md의 규칙대로 tasks.json의 다음 작업 단위를 수행해 줘."가 표 5-5와 practice.html:97, 실습 6의 작업 5 요청과 글자까지 같습니다. "통과가 false인 첫 단위"는 CLAUDE.example.md:13과 같고, tasks.example.json에서 첫 false는 작업 2입니다. 실습 5 본문의 "작업 2" 설명과 맞습니다. | 같은 규칙이 example-facts.md "처리 규칙"에도 있습니다. | 수정 없음 |
| 4 | 참고 | 규칙 문서 수정 범위와 settings.example.json, 중단 규칙 | 문제 없음(요청하신 확인 4, 5). 수정하지 않음 6개 경로(data/, acceptance/, check.py, CLAUDE.md, DECISIONS.md, .claude/)가 deny의 Edit(./data/**), Edit(./acceptance/**), Edit(./check.py), Edit(./CLAUDE.md), Edit(./DECISIONS.md), Edit(./.claude/**)와 일대일로 같습니다. 수정할 수 있음과 겹치는 경로도 없어 본문 문장 "금지 규칙에도 들어 있어"는 맞습니다. 중단 규칙 26행은 "현재 상태, 읽을 문서, 미결정, 다음 작업, 확인 명령"을 같은 순서로 적게 하며, 본문(ch05.html:90)과 글자까지 같습니다. | 25행의 "세 번 연속 실패하면 중단하고 HANDOFF.md 작성"은 example-facts.md의 중단 항목과 같습니다. 본문 90행은 이 중 26행(세션 종료 시 기록)만 인용하는데, 설명으로는 문제 없습니다. | 수정 없음 |

범위 밖이지만 알아 둘 점(요청하신 범위 밖이라 등급을 매기지 않았습니다): check_tasks.py가 "공백 있음 작업 2"(수용 시험 4, 5는 구현 전에도 통과)를 보고합니다. 이미 example-facts.md에 R6 공백, Q-118로 적혀 있고 6장 정비 대상이어서 ch05의 필수 사항이 아닙니다. ch05는 작업 2를 "false인 첫 단위"로만 언급할 뿐 이 확인 방법을 근거로 쓰지 않습니다.

검증 후 확정(실행 못 함): 표 5-7의 /context(Memory files 항목), 작업 시작 직후의 읽기 순서 화면, 실습 2·3의 대화형 요청과 /permissions 화면, 실습 5의 실제 에이전트 동작은 Claude Code 대화형 화면이 필요해 이 환경에서 실행하지 못했습니다. RUNLOG.md도 실습 2~6이 "실행 전"입니다. 따라서 "실제로 지켜진다"는 판정은 하지 않았고, 파일 대조와 명령 재현으로만 확인했습니다.

표 5-7이 구현 전에는 실패하고 설정 뒤 통과하는지(요청하신 확인 3):
- wc -l: CLAUDE.md가 없는 상태에서는 파일이 없다는 오류로 실패합니다(복사본 expense-app에는 CLAUDE.md가 없었음). 예시를 복사한 뒤에는 32가 나와 200 미만입니다.
- git show --stat HEAD와 git status: 위 1번에서 재현했습니다. commit 전 git status는 " M tasks.json"과 "?? CLAUDE.md"를 보여 주고, 처음 만든 CLAUDE.md는 제외한다는 본문 설명과 같습니다.
- PowerShell 명령: 이 환경에 PowerShell이 없어 실행하지 못했습니다. 같은 값을 파이썬 splitlines로 대신 확인했는데 32였습니다. (Get-Content CLAUDE.md).Count도 줄 수를 세므로 같은 값이 예상되지만 실행으로 확인하지는 못했습니다.

실행 기록
작업 폴더: /tmp/claude-0/-home-user-harness-book/4fa31d71-64a2-5605-bad4-d31a3ffd2331/scratchpad/ch05pc (expense-app, tools, docs 복사본)
1. python3 tools/check_tasks.py (저장소 루트에서 실행). 출력 끝:
   건너뜀 작업 1 / 공백 있음 작업 2(수용 시험 4, 5는 구현 전에도 통과) / 정상 작업 3(NO TESTS RAN) / 정상 작업 4(failures=3) / 건너뜀 작업 5 / "요약: 공백 1건(작업 2)"
2. 복사본 expense-app에서 cp reference/CLAUDE.example.md CLAUDE.md 후 wc -l CLAUDE.md는 "32 CLAUDE.md", splitlines 길이는 32.
3. 복사본에서 python3 check.py. 끝 출력:
   "tests: 실행 3건, 실패 0건, 건너뜀 0건, project_code 시험 0건"
   "acceptance: 실행 5건, 실패 3건, 건너뜀 0건(정한 수 5건)" (test_1~3 FAIL), rc=1. RUNLOG와 example-facts의 구현 전 상태와 같습니다.
4. 복사본에서 python3 -m unittest discover tests -q는 "Ran 3 tests ... OK".
5. 발췌와 원본을 파이썬으로 비교했습니다. 읽는 순서는 6~10행, 수정 범위는 19~21행과 일치했습니다.
6. 임시 git 저장소에서 tasks.json 수정과 CLAUDE.md 추가 후 commit하고 git show --stat HEAD를 실행했습니다(1번 근거).
7. 읽기 명령: cat, sed, grep, cat -n, git status 등.
실행 후 /home/user/harness-book에서 git status --short는 출력이 없었고(변경 없음), 브랜치는 ch05-playbook입니다.

필수 수정 0, 편집 권고 1, 검증 후 확정 1(대화형 화면 항목 묶음), 실행한 명령 9개
