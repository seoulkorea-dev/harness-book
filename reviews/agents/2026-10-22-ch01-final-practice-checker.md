# 1장 완성본 practice-checker(2026-10-22, PR #81, 실습 감수)
결과: 필수 수정 0, 편집 권고 2, 검증 후 확정 3. 예제 사실은 docs/example-facts.md, examples/expense-app/ 원본과 일치. tools/check_tasks.py 공백 2건(작업 2, 3)은 1장 문장과 모순 없음(3단계 몫). python check.py 결과는 example-facts 10행과 같음. 실행 뒤 git status 깨끗.

| # | 등급 | 위치 | 발견 | 처리 |
|---|---|---|---|---|
| 5 | 권고 | 확인 방법 | 실행 위치 | 반영("실습 폴더에서 Claude Code를 실행한 뒤") |
| 6 | 권고 | 표 1-9 기준 | 화면 서술 수준 | 보류 |
| 7~9 | 검증 후 확정 | /context, /permissions, /usage, SDK 종료 사유 | 대화형 화면이라 실행 못 함 | fact-checker가 문서로 확인, 실행 확인은 작가(Q-071과 같음) |
