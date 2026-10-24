요약: 필수 0, 권고 3, 참고 3. 실행은 python tools/check_tasks.py 1회와 파일 읽기(sed, grep, wc)만 했고, 실행 뒤 git status는 변경 없음(출력 없음)입니다.

핵심 판정: 규칙 문서 발췌 두 절(읽는 순서, 수정 범위)은 reference/CLAUDE.example.md와 글자까지 같습니다. 줄 수 32줄(wc -l 32), 여섯 절 이름, 요청 문장, 권한 항목도 원본과 같습니다. 실습 2에서 Claude Code를 직접 띄우는 단계(/context 화면, 두 요청의 응답)는 실행 못 함(대화형 화면)이라 검증 후 확정입니다.

| # | 위치 | 확인 결과와 근거 | 등급 | 제안 |
|---|---|---|---|---|
| 1 | ch05 72~81행 코드 상자 | 읽는 순서 절 5줄과 수정 범위 절 3줄 중 2줄이 원본(CLAUDE.example.md 5~10행, 17~19행)과 글자 단위로 같습니다. 본문이 "여섯 절 가운데 두 절의 발췌"라고 밝혔습니다. 다만 수정 범위 절의 셋째 줄 "수용 시험이 실패하면 시험이 아니라 구현을 고친다."를 표시 없이 뺐습니다. | 권고 | 코드 상자 끝에 "(수정 범위 절의 나머지 한 줄은 생략)"을 쓰거나 셋째 줄을 넣습니다. |
| 2 | ch05 표 5-7 "컨텍스트를 차지하는 항목", 실습 2 5단계 | 장은 "/context(접혀 있으면 /context all)"이고 부록은 "/context를 입력해 메모리 파일 항목에 CLAUDE.md가 있는지 확인"까지만 적습니다. 확인 대상(메모리 파일 항목)과 명령은 같지만 all 안내가 부록에 없습니다. | 권고 | 부록 5단계에 "목록이 접혀 있으면 /context all"을 한 구절 추가합니다(부록 쪽 수정). |
| 3 | ch05 표 5-7 "규칙의 실제 준수" | 장은 "commit 뒤 git show --stat HEAD(commit 전이면 git status)"입니다. 부록은 실습 2에서 git status와 git restore acceptance/, 실습 5에서 git status, git diff HEAD -- tasks.json, git diff HEAD~2 --stat을 씁니다. practice.html에 git show --stat이 없어(grep 0건) 장의 확인 방법이 실습 어디에서도 실행되지 않습니다. | 권고 | 장을 부록의 git diff HEAD~2 --stat 방식에 맞추거나, 실습 5 확인 방법에 git show --stat HEAD를 추가합니다. |
| 4 | ch05 표 5-7 "규칙 문서의 길이", "읽는 순서" | wc -l CLAUDE.md는 부록 실습 2에 단계가 없습니다. "수용 기준 문서를 먼저 읽는지"를 보는 단계도 없습니다. 직접 실행해 본 wc -l reference/CLAUDE.example.md는 32이며 본문 수치와 같습니다. | 참고 | 실습 2 확인 방법에 wc -l CLAUDE.md 한 줄을 추가하는 것을 검토합니다. 읽는 순서는 실습 5 첫 요청 직후 화면에서 확인함을 한 줄 적습니다. |
| 5 | ch05 표 5-5, 5-6, 72행 | 예제 사실이 docs/example-facts.md와 settings.example.json과 같습니다. 일치한 항목은 훅(편집 뒤 단위 테스트, 종료 코드 2), 금지 경로 6개, 요청 문장(실습 5의 96행 요청과 동일), 첫 읽기 docs/CR.md, 중단 규칙의 HANDOFF.md 항목 5개입니다. | 참고 | 조치 없음. |
| 6 | R6 확인 방법 공백 | python tools/check_tasks.py 결과: 작업 2와 3은 공백 있음(구현 전에도 통과), 작업 4는 정상(FAILED failures=3), 작업 1과 5는 건너뜀, 요약 "공백 2건". ch05는 작업 단위 확인을 다루지 않고 예제에서 "다음 작업 단위"만 언급하며, 공백의 필수 대상은 ch06입니다. R14 점검 대상(작업 완료 기준과 근거)은 ch05 예제에 없습니다. | 참고 | ch05 조치 없음. ch06에서 공백 2건을 다뤄야 합니다. |

실행한 명령 요약
- python tools/check_tasks.py → 위 출력(요약: 공백 2건(작업 2, 작업 3))
- sed, grep, wc -l, cat -A으로 ch05.html, CLAUDE.example.md, settings.example.json, practice.html, example-facts.md 대조 (모두 읽기 전용)
- git status --short → 출력 없음(작업 폴더 변경 없음)

필수 수정 0, 편집 권고 3, 참고 3, 검증 후 확정 1(실습 2 Claude Code 대화형 화면 재현), 실행한 명령 6개