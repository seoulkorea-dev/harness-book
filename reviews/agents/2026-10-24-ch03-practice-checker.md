# 3장 실습 점검(practice-checker, 2026-10-24, 커밋 1024254)

결론: 필수 0, 권고 0, 참고 2. 확인을 요청한 5개 항목 모두 본문과 실습 파일이 일치했고, 고칠 원문은 없습니다.

| 번호 | 등급 | 위치 | 문제 | 근거(파일:행, 실행 출력) | 고칠 문안 |
|---|---|---|---|---|---|
| 1 | 참고 | ch03.html 138행(표 3-7 훅 행), 부록 실습 3, 4의 화면 확인 | /permissions, /hooks, Ctrl+O 오류 메시지 표시는 Claude Code 대화형 화면이라 실행하지 못했습니다. | 대화형 화면과 로그인이 필요합니다. 설정 파일 내용은 항목 3에서 원본과 글자까지 같음을 확인했습니다. | 검증 후 확정. 고칠 문안 없음 |
| 2 | 참고 | ch03.html 52행(그림 3-1 SVG) | 그림 해설의 규칙은 본문 46~47행, CLAUDE.example.md와 일치합니다. 그림 렌더링은 이 점검 범위가 아닙니다. | 해당 없음 | 고칠 문안 없음 |

**항목별 판정**

1. 종료 코드 0 조건 셋과 구현 전 출력: 일치(ch03 27행, 140행, check.py 3~5행, 28~35행).
   - 실제 출력은 `tests: 실행 3건, 실패 0건, 건너뜀 0건, project_code 시험 0건`, `acceptance: 실행 5건, 실패 3건, 건너뜀 0건(정한 수 5건)`, 종료 코드 1입니다.
   - 실패한 수용 시험은 test_1, test_2, test_3입니다. 표 3-7 첫 행(136행), 부록 실습 1(40행), docs/example-facts.md 10행과 같습니다.
   - 단위 테스트 명령(`python -m unittest discover tests -q`)의 출력은 `Ran 3 tests ... OK`로, 부록 실습 1의 "마지막 줄이 OK"와 같습니다.
2. 작업 2~4의 확인 방법: 설명과 같습니다.
   - `python tools/check_tasks.py` 결과는 작업 2 "공백 있음"(구현 전에도 통과, OK), 작업 3 "정상"(구현 전에 NO TESTS RAN으로 실패), 작업 4 "정상"(구현 전에 failures=3), 작업 1과 5는 "건너뜀"입니다. 요약은 "공백 1건(작업 2)"입니다. 본문 45행의 "작업 2는 구현 전에도 통과"와 같습니다.
   - 복사본에서 최소 구현을 한 결과는 다음과 같습니다.
     - 작업 2와 3을 구현한 뒤(service.py에 project_code 저장, tests에 project_code 시험 추가): tests 4건, 실패 0건, project_code 시험 1건. acceptance는 실패 3건이라 종료 코드 1입니다. 본문 46행의 "작업 2, 3을 마친 시점에는 전체가 종료 코드 1"과 같습니다.
     - 작업 4를 구현한 뒤(목록에 없는 코드 거부, select 항목, 목록 열): acceptance 실패 0건, 종료 코드 0입니다.
   - 아무것도 확인하지 않는 시험도 이름에 project_code만 있으면 셋째 조건을 충족한다는 본문 43행의 한계는 check.py 30~32행 구현과 일치합니다.
3. 코드 상자와 원본 비교: 일치합니다. `&amp;`를 `&`로 바꾼 뒤 diff를 떴습니다.
   - settings 상자와 settings.example.json은 python3 허용 두 줄(5~6행 부근)만 다릅니다. 이는 본문 75행이 생략했다고 밝힌 줄입니다.
   - reviewer 상자와 reviewer.example.md는 diff 출력이 없습니다.
4. CLAUDE.example.md: 모두 있습니다.
   - 본문 121행이 인용한 문장과 같은 취지의 줄이 "작업 순서" 절 3번째 줄에 있습니다. 내용은 "확인 방법을 충족하면 commit 전에 reviewer 하위 에이전트에게 바뀐 파일 목록과 변경 내용(git status, git diff 출력)을 넘겨 수용 기준 대조를 요청한다."입니다.
   - 중단 규칙: "그 단위의 확인 방법에 든 시험이 세 번 연속 실패하면(편집 뒤 훅의 실패는 세지 않음) 중단하고 HANDOFF.md를 작성한다."
   - 수정 요청 시 되돌림: "사람이 수정을 요청하면 그 단위의 '통과' 값을 false로 되돌리고 다시 작업한다."
   - 작업 5 통과 값 변경 금지, 수정 범위, 읽는 순서(docs/CR.md, DECISIONS.md, tasks.json, HANDOFF.md)도 표 3-3과 example-facts.md 25~30행과 같습니다.
5. 표 3-2, 3-3, 3-5와 tasks.example.json: 일치합니다.
   - 확인 방법 문구는 작업 2 "python check.py의 수용 시험 4, 5 통과", 작업 3 "python check.py의 tests 실패 0건, project_code 시험 1건 이상", 작업 4 "python check.py의 수용 시험 1, 2, 3 통과", 작업 1 "결정 기록 D-012", 작업 5 "사람 승인(통과 값은 사람이 변경)"입니다. 표 3-2 검증 행, 본문 46행, example-facts.md 17~21행과 같습니다.
   - 통과 시작 값은 작업 1만 true이고 나머지는 false입니다(본문 28행).
   - 수용 기준 5개(ch03 26행)는 docs/CR.md 10~14행과 같고, D-012는 DECISIONS.md 5행에 있습니다.
   - 부록 실습 3의 ask/deny 설명, 실습 5의 "작업 2, 3의 통과 값만 true" 및 commit 두 개, 실습 6의 작업 4와 종료 코드 0도 본문과 일치합니다.

**실행 기록**

모든 실행은 복사본 `/tmp/claude-0/-home-user-harness-book/4fa31d71-64a2-5605-bad4-d31a3ffd2331/scratchpad/ch03pc` 아래에서 했습니다.

- `python check.py` (examples/expense-app, 구현 전). 출력 끝부분:
  ```
  tests: 실행 3건, 실패 0건, 건너뜀 0건, project_code 시험 0건
  acceptance: 실행 5건, 실패 3건, 건너뜀 0건(정한 수 5건)
  exit=1
  ```
- `python tools/check_tasks.py` (복사본 루트). 출력 끝부분:
  ```
  건너뜀 작업 1 / 공백 있음 작업 2 / 정상 작업 3 / 정상 작업 4 / 건너뜀 작업 5
  요약: 공백 1건(작업 2)
  ```
- 복사본에서 작업 2와 3을 최소 구현한 뒤 `python check.py`:
  ```
  tests: 실행 4건, 실패 0건, 건너뜀 0건, project_code 시험 1건
  acceptance: 실행 5건, 실패 3건, 건너뜀 0건(정한 수 5건)
  exit=1
  ```
- 작업 4까지 최소 구현한 뒤 `python check.py`:
  ```
  tests: 실행 4건, 실패 0건, 건너뜀 0건, project_code 시험 1건
  acceptance: 실행 5건, 실패 0건, 건너뜀 0건(정한 수 5건)
  exit=0
  ```
- 코드 상자 두 개를 원본과 diff했습니다(ch03.html 76~109행과 113~120행을 추출). 결과는 위 항목 3과 같습니다.
- 원본 저장소에서 `python -m unittest discover tests -q`를 실행했고, 결과는 `Ran 3 tests ... OK`입니다.
- 실행 뒤 `git status --short` (/home/user/harness-book)는 출력이 없어 작업 폴더가 바뀌지 않았습니다. 복사본의 구현은 scratchpad 안에만 있습니다.

필수 수정 0, 편집 권고 0, 검증 후 확정 1(참고 1: 대화형 화면), 실행한 명령 약 10개
