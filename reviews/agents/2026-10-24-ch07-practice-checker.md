# 7장 실습 점검(practice-checker)

# 7장 예제, 실패 표, 확인 표와 부록 실습 4 감수 보고

요약: 필수 3, 권고 3, 참고 5. 원고와 실습 파일은 고치지 않았습니다.

| 번호 | 위치 | 원문 | 확인 결과(실행한 명령과 출력) | 고친 문안 | 등급 |
|---|---|---|---|---|---|
| 1 | ch07.html 75~85행(예제 절의 check.py 코드 블록) | 코드 블록이 `print(f"{folder}: 실행 {count}건, 실패 {failed}건")`을 출력하고, 종료 조건은 `all(count > 0 and failed == 0 ...)`입니다. | 실제 examples/expense-app/check.py(1~37행)와 다릅니다. 실제 파일은 건너뜀을 세고, tests 줄에 project_code 시험 수를 붙이고, acceptance 줄에 "(정한 수 5건)"을 붙입니다. 종료 조건은 건너뜀 0건, 수용 시험 정확히 5건 실행, project_code 시험 1건 이상입니다. 본문 코드대로면 출력이 "tests: 실행 3건, 실패 0건"이 되어, 바로 아래 89~90행 출력 블록과 맞지 않습니다. 본문은 "발췌"라고 하면서 줄임 표시도 없습니다. | 두 가지 중 하나로 고칩니다. (a) 코드를 실제 파일의 핵심부(26~37행)로 교체합니다. (b) 간략화한 코드임을 밝히고 출력 형식 차이를 설명합니다. 권장은 (a)입니다. 82~86행 설명에는 건너뜀 0건, 수용 시험 정한 수(5건), project_code 시험 1건 이상의 세 조건을 더합니다. 3장 27행의 종료 코드 0 조건 세 가지와 같아집니다. | 필수 |
| 2 | ch07.html 88행(출력 해설) | "구현을 마치면 둘째 줄이 'acceptance: 실행 5건, 실패 0건'이 되고, 종료 코드는 0이어야 합니다." | 실제 출력 형식은 "acceptance: 실행 5건, 실패 0건, 건너뜀 0건(정한 수 5건)"입니다. 종료 코드 0이 되려면 첫 줄 tests도 project_code 시험 1건 이상이어야 하는데, 이 조건이 빠져 있습니다. 작업 3을 하지 않고 작업 4만 끝내면 둘째 줄은 맞아도 종료 코드는 1입니다. | "구현을 마치면 acceptance 줄이 '실행 5건, 실패 0건, 건너뜀 0건(정한 수 5건)'이 되고, tests 줄의 project_code 시험이 1건 이상이며 실패 0건이면 종료 코드가 0입니다." | 필수 |
| 3 | ch07.html 전체(예제 절, 확인 표). 앞 장 약속은 ch06.html 77행 | ch06 77행이 "확인 방법을 구현 전에는 실패하는 검사로 만드는 방법은 Chapter 7의 완료 기준을 검사로 변환에서 다룹니다"라고 약속합니다. | `python tools/check_tasks.py` 출력은 `공백 있음 작업 2 ... 구현 전 상태에서도 통과(OK)`, 요약은 "공백 1건(작업 2)"입니다. 작업 3과 4는 정상(각각 NO TESTS RAN, FAILED (failures=3))입니다. 그런데 ch07에는 "작업 2"나 "공백"이라는 말이 한 번도 없고, 표 7-6과 표 7-8은 작업 단위별 확인 방법을 다루지 않습니다. 약속이 이행되지 않았습니다. R6에 따르면 공백이 있는 작업 단위를 다루는 장의 필수 사항입니다. docs/example-facts.md는 이 공백의 해소를 작가 확인 Q-118로 남겨 두었습니다. | 예제 절에 한두 문장을 더하거나 criteria 절에서 사례로 짧게 다룹니다. 예시는 이렇습니다. "작업 2의 확인 방법(수용 시험 4, 5)은 구현 전에도 통과하므로 완료를 증명하지 못합니다. 구현 전에 실패하는 확인(예: 데이터 모델의 project_code 항목을 확인하는 시험 추가)이나 검토 하위 에이전트의 대조로 보완합니다." 수용 시험 추가는 acceptance/가 사람 소유 파일이라 작가 확인(Q-118)이 필요하므로, 본문에는 보완 방법만 쓰고 실습 파일 변경은 AUTHOR_QUEUE로 넘깁니다. | 필수 |
| 4 | ch07.html 105행(표 7-8 첫 행, 판정 근거) | 확인 기준: "tests와 acceptance의 실행 건수가 0보다 크고, 두 줄 모두 실패 0건" | check.py의 통과 조건은 이보다 엄격합니다. 건너뜀 0건, acceptance 5건, project_code 시험 1건 이상이 더 필요합니다. 표 7-8의 이 행만 읽고 판정하면 건너뜀이 있거나 project_code 시험이 0건인 출력도 통과로 판정합니다. 종료 코드 행(106행)이 0을 요구해 최종 판정은 막히지만, 출력 원문 행만 보면 R14의 "기준 전체 증명"이 약합니다. 구현 전 실패는 실제로 성립합니다. 실행 결과 tests 줄은 project_code 시험 0건, acceptance 줄은 실패 3건이고 종료 코드는 1입니다. | "tests와 acceptance의 실패가 0건이고 건너뜀이 0건, acceptance는 정한 수(5건)만큼 실행, tests의 project_code 시험 1건 이상" | 권고 |
| 5 | ch07.html 89~90행(기준 상태 출력 두 줄) | `tests: 실행 3건, 실패 0건, 건너뜀 0건, project_code 시험 0건` / `acceptance: 실행 5건, 실패 3건, 건너뜀 0건(정한 수 5건)` | 임시 복사본(`/tmp/claude-0/-home-user-harness-book/4fa31d71-64a2-5605-bad4-d31a3ffd2331/scratchpad/ep`)에서 `python check.py 2>/dev/null; echo "exit=$?"`를 실행했습니다. 출력 두 줄이 본문, 부록 실습 1(42~44행), 3장 27~28행과 글자 그대로 같습니다. 종료 코드는 `exit=1`입니다. 단위 테스트는 `Ran 3 tests ... OK`입니다. | 변경 없음 | 참고(통과) |
| 6 | ch07.html 66~72행(표 7-6, 수용 시험 1~5와 acceptance/test_cr07.py) | 수용 기준 다섯 가지와 "수용 시험 1~5(check.py로 실행)" | test_1_form_offers_project_codes, test_2_unknown_code_rejected_with_reason, test_3_list_shows_project_code, test_4_existing_requests_still_listed, test_5_project_source_unchanged가 기준 1~5와 1대 1로 대응합니다. 본문 66행의 서술과 docs/example-facts.md 9행도 같습니다. 본문 73행의 "수용 시험 1은 HTML에 선택 항목이 있는지만 본다"는 test_1이 `name="project_code"`와 코드 세 개의 문자열 포함만 확인하는 것과 같습니다. 6장 작업 5, 승인자, 통과 값 서술(ch06 65~74행)과도 맞습니다. | 변경 없음 | 참고(통과) |
| 7 | ch07.html 92~93행, 부록 실습 3, 4와 reference/settings.example.json | 금지 규칙: 수용 시험과 check.py. 훅: 편집 뒤 단위 테스트, 실패 시 종료 코드 2 | settings.example.json의 deny는 data, acceptance, check.py, CLAUDE.md, DECISIONS.md, .claude, git push, WebFetch, WebSearch입니다. 훅은 `PostToolUse`, matcher `Edit\|Write`, 명령 `cd "$CLAUDE_PROJECT_DIR" && python -m unittest discover tests -q \|\| exit 2`입니다. docs/example-facts.md 32~36행과 일치합니다. 부록 실습 4 1단계("reference의 hooks 부분 추가", python3 대체 안내)와도 맞습니다. 본문 93행의 "단위 테스트만 실행하므로 수용 시험은 check.py로 확인"도 맞습니다. 훅이 단위 테스트만 실행하는 것도 맞습니다. reviewer.example.md는 `tools: Read, Grep, Glob`로 3장 118~121행과 같고, 실습 4의 `cp reference/reviewer.example.md .claude/agents/reviewer.md`도 맞습니다. 훅의 `\|\| exit 2`는 unittest 실패 시 2로 끝납니다. | 변경 없음 | 참고(통과) |
| 8 | 부록 practice.html 87행(실습 4의 첫 요청), 89행 | "expense/views.py의 목록 표에서 요청자 열을 빼 줘" → 훅 작동 | 임시 복사본에서 views.py의 요청자 th와 td를 제거하고 `python -m unittest discover tests -q`를 실행했습니다. `FAILED (failures=1)`(test_list_shows_requesters)로 훅이 실제로 실패를 내는 시나리오입니다. 이 단계는 Claude Code 대화형이라 훅 실행과 모델 응답은 실행 못 함(검증 후 확정은 아닙니다. 실습 4는 응답 예상이라고 부록 21행이 이미 밝혔습니다). | 변경 없음 | 참고(통과) |
| 9 | ch07.html 103행, 부록 practice.html 5, 27~33행(폴더 이름과 명령) | "명령은 실습 폴더(expense-practice)에서 실행합니다" | 부록의 `cp -r harness-book/examples/expense-app expense-practice`와 `cd expense-practice`가 같은 이름입니다. 종료 코드 확인은 Git Bash `echo $?`, PowerShell `$LASTEXITCODE`로 맞습니다. 부록 34행에 PowerShell용 Copy-Item이 있고, 7장 106행과 부록 40행의 종료 코드 안내가 일치합니다. 다만 ch07 103행에는 "부록 실습 1에서 만든 폴더"라는 안내가 없습니다. 부록 실습 1은 `git init`과 commit을 하므로 `git status` 행(107행)은 그 폴더에서만 의미가 있습니다. | 103행에 "(부록 실습 1에서 복사해 git init한 폴더)"를 덧붙입니다. | 권고 |
| 10 | ch07.html 108행(표 7-8 화면 동작) | `python app.py` 후 http://localhost:8000/new 열기, Ctrl+C로 종료 | 서버 실행과 브라우저 접속은 환경 제한(네트워크, 대화형)으로 실행 못 함. `/new` 경로는 정적으로 확인하지 않았습니다. 구현 전에는 test_1이 실패하므로 화면에 선택 항목이 없을 것이라는 추정만 가능합니다(구현 전 실패 성립은 시험 1로 간접 확인). | app.py에서 `/new` 라우트를 확인하고, 필요하면 실습 5 구현 뒤에 작가가 한 번 확인하세요. | 권고(검증 후 확정) |
| 11 | ch07.html 107행, 부록 practice.html 54, 73, 89행(git status) | "변경된 파일 목록에 acceptance/ 폴더와 check.py가 없음" | 이 확인은 구현 전에도 통과하는 보호 장치용 확인입니다(완료 기준이 아니라 보호 확인이므로 R14 위반은 아닙니다). 훅이나 `Edit` 금지가 간접 수정은 막지 못한다는 본문(92행)과 짝이 맞습니다. 다만 사람이 commit 뒤에 확인하면 목록에 안 보이므로 "마지막 commit 이후 변경 없음, 또는 commit 후라면 git diff <기준 commit> -- acceptance check.py"를 넣는 편이 정확합니다. | "git status로 작업 중, git diff HEAD~N 으로 commit 후 확인" 정도의 보완 | 참고 |
| 12 | ch07.html 97~100행(표 7-7) | 실패 네 가지와 방지 장치 | 방지 장치가 모두 본문과 실습 파일에 존재합니다. check.py는 `run.testsRun > 0`과 정한 수 5건 검사로 0건 실행을 실패 처리합니다. "수용 시험 파일을 통째로 지우면 실패, 내용을 약하게 바꾸는 것은 못 잡음"은 example-facts.md 11행과 일치하며, 본문 92~93행이 git status와 commit 확인으로 보완한다고 밝히고 있습니다. | 변경 없음 | 참고(통과) |

## 실행한 명령과 출력 원문(끝 몇 줄)

임시 복사본(`/tmp/claude-0/-home-user-harness-book/4fa31d71-64a2-5605-bad4-d31a3ffd2331/scratchpad/ep`)에서 실행했습니다. 원본은 수정하지 않았습니다.

```
$ python check.py 2>/dev/null; echo "exit=$?"
tests: 실행 3건, 실패 0건, 건너뜀 0건, project_code 시험 0건
acceptance: 실행 5건, 실패 3건, 건너뜀 0건(정한 수 5건)
exit=1

$ python -m unittest discover tests -q
Ran 3 tests in 0.004s
OK

$ (views.py의 요청자 열을 제거한 임시 복사본) python -m unittest discover tests -q
Ran 3 tests in 0.004s
FAILED (failures=1)

$ python tools/check_tasks.py
건너뜀 작업 1 결정 기록 D-012(사람이 판단하는 확인)
공백 있음 작업 2 python check.py의 수용 시험 4, 5 통과: 구현 전 상태에서도 통과(OK)
정상 작업 3 python check.py의 tests 실패 0건, project_code 시험 1건 이상: 구현 전 상태에서 실패(NO TESTS RAN)
정상 작업 4 python check.py의 수용 시험 1, 2, 3 통과: 구현 전 상태에서 실패(FAILED (failures=3))
건너뜀 작업 5 사람 승인(통과 값은 사람이 변경)(사람이 판단하는 확인)
요약: 공백 1건(작업 2)
```

실행 뒤 `git status --short`(/home/user/harness-book): 출력 없음. 작업 폴더에 변경이 없습니다.

실행 못 함: Claude Code 대화형 화면(훅 실제 발동, /hooks, /permissions, reviewer 호출)과 `python app.py` 서버, 브라우저 확인. 이유는 대화형이거나 네트워크, 서버 실행이 제한된 환경이기 때문입니다.

필수 수정 3, 편집 권고 3, 검증 후 확정 1(권고 10과 겹침), 실행한 명령 9개

(요약 줄의 "참고 5"는 위 표의 참고 등급 행 5, 6, 7, 8, 12 중 통과 확인 항목과 11행을 합친 것입니다. 번호 5, 6, 7, 8, 11, 12가 참고이고 실제로는 6건입니다. 권고는 4, 9, 10으로 3건입니다.)
