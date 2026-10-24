# 6장 실습 점검(practice-checker, 2026-10-24, 커밋 655861f)

결론: 필수 2, 권고 0, 참고 2 (6장 예제 절, 표 6-4~6-6, 부록 실습 1, 5 점검)

| 번호 | 등급 | 위치 | 문제 | 근거(파일:행, 실행 출력) | 고칠 문안 |
|---|---|---|---|---|---|
| 1 | 필수 | src/chapters/ch06.html:91 (JSON 코드 상자, 작업 3) | 작업 3의 "완료 기준"이 원본보다 짧습니다. 괄호 "(project_code 시험 추가, 기존 시험 통과)"가 빠졌습니다. 코드 상자는 원본과 글자까지 같아야 합니다(플레이북 15장). 표 6-4(같은 절)에는 괄호가 있어 본문 안에서도 불일치합니다. | 원본 reference/tasks.example.json 작업 3: "완료 기준": "변경된 데이터 모델의 테스트 반영(project_code 시험 추가, 기존 시험 통과)". 원고 91행: "변경된 데이터 모델의 테스트 반영". 이 문자열은 원고에 한 번만 나옵니다(grep으로 확인). | 원문 `"완료 기준": "변경된 데이터 모델의 테스트 반영",` 를 `"완료 기준": "변경된 데이터 모델의 테스트 반영(project_code 시험 추가, 기존 시험 통과)",` 로 바꿉니다. |
| 2 | 필수 | src/appendix/practice.html 실습 5 "확인 방법" 둘째 항목 | "작업 2와 작업 3의 통과 값만 true로 변경되었습니다(git show HEAD -- tasks.json 또는 git diff HEAD~2 -- tasks.json …)"라고 했는데, 단위마다 commit한 뒤 git show HEAD -- tasks.json은 마지막 commit(작업 3)의 변경만 보여 줍니다. 작업 2의 변경은 나오지 않습니다. 임시 저장소에서 재현했습니다. | 작업 2 commit과 작업 3 commit 뒤 git show HEAD -- tasks.json 출력은 `-  "통과": false / +  "통과": true` 한 쌍(작업 3 한 곳)뿐이었습니다. git diff HEAD~2 -- tasks.json은 두 단위의 변경을 함께 보여 줍니다. 같은 확인 항목 셋째의 git diff HEAD~2 --stat은 이미 HEAD~2 기준입니다. | 원문 `(git show HEAD -- tasks.json 또는 git diff HEAD~2 -- tasks.json으로 확인)` 을 `(git diff HEAD~2 -- tasks.json으로 확인하고, git show HEAD -- tasks.json은 마지막 commit인 작업 3의 변경만 보여 줍니다)` 로 바꿉니다. |
| 3 | 참고 | ch06.html:84~100 (JSON 코드 상자 형식) | 원본은 항목마다 한 줄인 형식이고, 코드 상자는 항목을 여러 줄로 풀어 썼습니다. 키 이름과 값은 작업 3의 완료 기준(번호 1)을 빼면 같습니다. 본문이 "일부(작업 2, 3)"라 하므로 읽는 데 문제는 없지만, 글자까지 같게 하려면 한 줄 형식으로 적어야 합니다. | tasks.example.json 2~3행 형식과 대조. 작업 2와 작업 3의 id, 작업, 확인 방법, 통과 값은 일치합니다. | 작가 확인 사항입니다. 줄 구성이 달라도 되는지 정해 주세요. 현행 유지도 가능합니다. |
| 4 | 참고 | ch06.html 표 6-4 설명 문단 | 표 6-4는 "작업 단위 목록과 같은 순서와 문구"라고 하는데, 표의 "작업 1: 프로젝트 코드 …"는 원본의 id와 작업을 합친 표기이고 담당 열은 원본에 없습니다. 담당 열이 더한 것이라는 점은 본문이 이미 밝혔고, 값은 docs/example-facts.md의 담당과 일치합니다. | 수정 필요 없음 | 없음 |

## 점검 결과(항목별)
1. 표 6-4의 다섯 행(작업, 완료 기준, 확인 방법)은 tasks.example.json과 글자까지 같습니다. 표 6-4 작업 3 완료 기준의 괄호는 원본에 있습니다. JSON 코드 상자는 작업 2는 일치하고 작업 3만 불일치합니다(번호 1).
2. 기준 상태에서 python -B tools/check_tasks.py를 실행했습니다. 작업 2는 "공백 있음"(수용 시험 4, 5가 구현 전에도 통과)이고, 작업 3은 "NO TESTS RAN"으로 실패, 작업 4는 "FAILED (failures=3)"으로 실패합니다. 작업 1과 5는 건너뜁니다. 요약은 공백 1건(작업 2), 종료 코드 1입니다. 6장의 서술(작업 2는 구현 전에도 통과, 작업 3과 4는 실패)과 일치합니다. 수용 시험은 -v 실행에서 test_1~3 FAIL, test_4, 5 ok였습니다. 부록 실습 1의 기준 상태 서술(tests 3건 통과, acceptance 5건 중 3건 실패, 종료 코드 1, 출력 끝 3줄)도 일치합니다.
3. 임시 git 저장소에서 실습 5의 순서대로 재현했습니다. tasks.json을 commit하지 않은 상태의 git diff HEAD -- tasks.json은 출력이 0바이트이고 오류도 없었습니다. git status는 `?? tasks.json`입니다. 본문 서술과 일치합니다. 목록을 commit한 뒤 통과 값을 true로 바꾸면 git diff HEAD -- tasks.json이 그 변경을 보여 줍니다. 인자 없는 git diff는 스테이징하지 않은 변경을 보여 주고(49행), git diff --cached는 0행이었습니다. 단위마다 commit한 뒤 git log --oneline은 4건(실습 시작 상태, 작업 단위 목록 추가, 작업 2, 작업 3)이어서 표 6-6의 "작업 단위마다 commit 하나씩"과 맞습니다. 불일치는 번호 2뿐입니다.
4. reference/CLAUDE.example.md "작업 순서"에 "작업 5의 '통과' 값은 변경하지 않는다"가 있고, "수정 범위"에 "tasks.json의 '통과' 값"만 수정할 수 있다고 적혀 있습니다. 본문 서술("수정할 수 있는 항목(통과 값)과 갱신 주체를 규칙 문서에 지시로 적고")과 표 6-5의 두 방지 장치와 일치합니다.
5. "실습 폴더(expense-practice)"는 실습 1의 cp -r harness-book/examples/expense-app expense-practice와 일치합니다. "실습 5에서 reference/tasks.example.json을 복사해 만든 파일"도 실습 5 1단계(expense-practice/tasks.json으로 복사하고 commit)와 일치합니다. 6장이 말한 "목록을 만든 직후 첫 단위 전에 commit"도 실습 5 1단계에 있습니다.

## 실행 기록(복사본 /tmp/claude-0/-home-user-harness-book/4fa31d71-64a2-5605-bad4-d31a3ffd2331/scratchpad/ch06pc/)
- cp -r examples/expense-app → .../ch06pc/expense-practice (실행 전 __pycache__ 삭제), .../ch06pc/repo/examples/expense-app (check_tasks.py용)
- python check.py → tests 실행 3건 통과, acceptance: 실행 5건, 실패 3건, 건너뜀 0건(정한 수 5건), 종료 코드 1
- python -m unittest discover tests -q → Ran 3 tests, OK
- python -m unittest -v acceptance.test_cr07 → test_1~3 FAIL, test_4, 5 ok
- python -B tools/check_tasks.py(복사본 repo) → 위 2번의 출력, 종료 코드 1
- 임시 git 저장소에서 git init, add, commit, tasks.json 복사, git diff HEAD -- tasks.json(0바이트), git status, 통과 값 수정, git diff, git diff --cached, commit, git show HEAD -- tasks.json, git diff HEAD~2 -- tasks.json, git log --oneline
- 원본 저장소 /home/user/harness-book에서 git status --short는 출력이 없었습니다(변경 없음). 원고와 실습 파일은 고치지 않았습니다.
- 실행 못 함: Claude Code 대화형 화면(실습 5 요청 입력, 에이전트의 실제 작업 2, 3 구현)은 실행할 수 없어 "검증 후 확정"으로 둡니다. 통과 값 변경은 python으로 대신 만들어 재현했습니다. 이 재현에서는 json.dump가 서식을 바꿔 diff가 커졌지만, 이는 내 재현의 부작용이며 원고의 문제가 아닙니다.

필수 수정 2, 편집 권고 0, 참고 2, 검증 후 확정 1(대화형 부분), 실행한 명령 약 10개
