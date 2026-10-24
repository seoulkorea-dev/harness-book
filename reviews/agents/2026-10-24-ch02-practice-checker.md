# 2장 실습 점검(practice-checker, 2026-10-24, 커밋 74dba5a)

결론: 필수 1, 권고 2, 참고 3. 원고와 실습 파일은 수정하지 않았고, 실행은 scratchpad 복사본에서 했습니다.

| 번호 | 등급 | 위치 | 문제 | 근거 | 고칠 문안 |
|---|---|---|---|---|---|
| 1 | 필수 | ch02.html:83 (표 2-5 다섯째 줄, 지시 수단 칸) | "규칙 문서의 명령 절에는 단위 테스트 명령만 있음"이 참고본과 다릅니다. 명령 절에는 명령이 네 줄 있습니다. | reference/CLAUDE.example.md의 `## 명령` 절: 단위 테스트(`python -m unittest discover tests -q`), 전체 검사(`python check.py`), 앱 실행(`python app.py`), python3 안내. | "없음(규칙 문서의 명령 절은 단위 테스트 명령을 알려 줄 뿐, 파일을 수정할 때마다 실행하라는 규칙은 없음)". 표의 뜻은 "수정할 때마다 실행하라는 지시가 없다"이므로 이렇게 고치면 참고본과 맞습니다. |
| 2 | 권고 | ch02.html:100 (표 2-7 역할 행) | "규칙 문서에 사람이 승인할 작업이 적혀 있으며"를 참고본에서 직접 확인하기 어렵습니다. 참고본에는 "작업 5의 통과 값은 변경하지 않는다"만 있고, 작업 5가 사람 승인 작업이라는 말은 없습니다. 같은 이유로 표 2-6 첫 줄(91행)의 "규칙 문서에 사람이 승인할 작업 단위(작업 5) 명시"도 "승인"이라는 말이 없어 약합니다. 사람이 승인한다는 사실은 tasks.example.json의 작업 5 "작업"과 "확인 방법" 칸에 있습니다. | CLAUDE.example.md 작업 순서 첫 줄. tasks.example.json 작업 5: "사람 승인(통과 값은 사람이 변경)". | 둘 중 하나로 정합니다. (a) 확인 기준을 "규칙 문서에 통과 값을 변경하지 않는 작업 단위(작업 5)가 적혀 있으며"로 바꿉니다. (b) 참고본에 승인 문구를 더합니다(이 경우 docs/example-facts.md와 부록도 같이 고칩니다). |
| 3 | 권고 | ch02.html:103 (표 2-7 기록 행) | "통과 값을 true로 변경한 작업 단위(작업 2~4)마다 commit이 하나씩 있음"은 구현 전에는 판정할 수 없습니다. 이 기준은 실습 5, 6을 마친 뒤에만 확인됩니다. docs/example-facts.md는 RUNLOG가 "실행 전"이라고 적습니다. | 현재 tasks.json이 없고 reference/tasks.example.json의 통과 값은 모두 false(작업 1만 true)입니다. | 표 아래나 본문에 "이 항목은 실습 5, 6 뒤에 확인합니다"를 한 구절 더합니다. |
| 4 | 참고 | ch02.html:87 vs practice.html #lab-2, #lab-3 | 본문 87행(질문에서 말한 89행 근처)이 부록과 맞습니다. 실습 2는 CLAUDE.md만 두고 "acceptance/test_cr07.py의 첫 번째 시험을 삭제해 줘"를 요청하며, "규칙 문서는 지시이므로 … 막지 못할 수 있으며"라고 적습니다. 실습 3은 settings.json의 deny를 더해 acceptance/ 삭제, data/projects.csv 행 추가, push 세 요청이 모두 거부되는지 봅니다. 수정할 부분은 없습니다. | practice.html:45~54(실습 2), 55~(실습 3). 실습 3 확인 방법의 마지막 항목은 "스크립트를 통한 간접 수정은 막지 못할 수 있음"으로, 본문 64행 및 87행과 일치합니다. 대화형 동작은 실행하지 못했습니다. | 없음 |
| 5 | 참고 | 표 2-4(69~75행) vs reference/ | 표 2-4와 설정 참고본이 글자까지 같습니다. 허용은 `python -m unittest *`, `python check.py`, `git status`, `git diff *`입니다. python3 변형은 표에서 하나로 묶어 쓴 것으로 봅니다. 확인 요청은 `git commit *`입니다. 금지는 `Edit(./data/**)`, `Edit(./acceptance/**)`, `Edit(./check.py)`, `Edit(./CLAUDE.md)`, `Edit(./DECISIONS.md)`, `Edit(./.claude/**)`, `Bash(git push *)`, `WebFetch`, `WebSearch`입니다. 훅은 PostToolUse, matcher `Edit\|Write`, `python -m unittest discover tests -q \|\| exit 2`로, 단위 테스트를 실행하고 실패하면 종료 코드 2입니다. reviewer는 `tools: Read, Grep, Glob`이고 파일을 수정하지 않습니다(reviewer.example.md). 표 2-5의 규칙 문서 항목도 참고본에 모두 있습니다. 수정 범위 절에 acceptance/, check.py, data/가 있고, 작업 순서에 사람 확인 뒤 commit과 reviewer 대조가 있고, 중단 규칙에 "세 번 연속 실패"가 있습니다. 규칙 문서는 여섯 절이며 docs/example-facts.md와 같습니다. | 없음 | 없음 |
| 6 | 참고 | 표 2-7 검증 행, check.py | 표 2-7 검증 행의 "폴더별 실행 건수와 실패 건수" 기준은 실행으로 확인했고 맞습니다. 구현 전 출력은 `tests: 실행 3건, 실패 0건` / `acceptance: 실행 5건, 실패 3건`이고 종료 코드는 1입니다. acceptance를 비운 복사본에서는 `NO TESTS RAN`, `acceptance: 실행 0건, 실패 0건`이 나오고 종료 코드는 1입니다(수용 시험 0건이면 실패). 구현 후 통과는 구현이 없어 확인하지 못했습니다(검증 후 확정). | 아래 실행 기록 | 없음 |

R6 참고: tools/check_tasks.py는 작업 2와 작업 3을 "공백 있음"으로 판정했습니다. 두 작업은 구현 전에도 통과하는 확인입니다. 이는 docs/example-facts.md의 "정비 예정"과 같고 6장 정비 대상입니다. 2장은 이 두 작업의 확인을 주장하지 않으므로 2장의 필수 사항은 아닙니다. 다만 66행의 "작업 2~4를 에이전트가 하나씩 구현"은 사실과 맞습니다.

검증 후 확정(실행하지 못함): /context, /permissions, /hooks, /mcp와 data/ 수정 거부, 훅 오류 화면은 Claude Code 대화형 화면이라 실행하지 못했습니다. 따라서 표 2-7의 해당 기준은 "설정 뒤 통과"를 확인하지 못했습니다. 설정 참고본의 JSON 구조는 읽어서 확인했습니다.

실행 기록 (scratchpad 복사본: /tmp/claude-0/-home-user-harness-book/4fa31d71-64a2-5605-bad4-d31a3ffd2331/scratchpad/w/expense-app):
- `python check.py` (구현 전)
  - tests: `Ran 3 tests ... OK`
  - acceptance: `Ran 5 tests ... FAILED (failures=3)`. 실패한 시험은 test_1_form_offers_project_codes(name="project_code" 없음), test_2_unknown_code_rejected_with_reason(거부되지 않음), test_3_list_shows_project_code(PRJ-2602 없음)입니다.
  - 마지막 두 줄: `tests: 실행 3건, 실패 0건` / `acceptance: 실행 5건, 실패 3건`, 종료 코드 1. 시험 4, 5는 통과해 docs/example-facts.md와 같습니다.
- 복사본에서 acceptance/test_*.py를 삭제하고 `python check.py`: `Ran 0 tests ... NO TESTS RAN`, `acceptance: 실행 0건, 실패 0건`, 종료 코드 1.
- 저장소에서 `python tools/check_tasks.py`
  - 작업 1: 건너뜀
  - 작업 2: 공백 있음(OK)
  - 작업 3: 공백 있음(OK)
  - 작업 4: 정상(FAILED failures=3)
  - 작업 5: 건너뜀
  - 요약: 공백 2건(작업 2, 작업 3)
- 실행 뒤 `git status --short`: 출력 없음(작업 폴더 변경 없음), 브랜치 ch02-playbook.

필수 수정 1, 편집 권고 2, 검증 후 확정 1(대화형 화면 항목 묶음), 실행한 명령 6개
