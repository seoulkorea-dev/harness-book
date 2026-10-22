# 1장 다시 만들기: practice-checker(실습 확인, 2026-10-22, PR #85)

판정 요약: 필수 0, 권장 3, 검증 후 확정 1

| 발견 | 위치 | 근거 | 제안 | 확신 |
|---|---|---|---|---|
| 통과: 예제 문단 사실(요청 내용, 재무팀, 다섯 작업 단위 이름과 순서, git commit 확인 요청, git push 금지, 순서 안내, 사람의 push)이 docs/example-facts.md, tasks.example.json, settings.example.json(ask Bash(git commit *), deny Bash(git push *)), CLAUDE.example.md와 일치 | meanings 예제 문단 | 파일 대조 | 없음 | 높음 |
| 권장: 표 1-9 /context는 부록 실습에 재현 단계가 없음(/permissions는 실습 3, /usage는 실습 6) | check 표 1-9 | grep 결과 | 부록 실습에 한 줄 또는 1장에 안내 | 중간 |
| 권장: 실습 폴더 이름(expense-practice)이 1장에 없음 | check 첫 문단 | practice.html 4~6행 | 이름 한 번 적기 | 낮음 |
| 권장: R6 공백 2건(작업 2, 3)이라 "완료 여부를 확인할 수 있는 크기"가 작업 2, 3에는 아직 성립하지 않음. R6 필수 장은 6장 정비 | meanings 예제 문단 | check_tasks.py | 6장 정비 전까지 유지 근거 기록 | 중간 |
| 검증 후 확정: /context, /permissions, /usage, Agent SDK 종료 사유는 이 환경에서 실행 불가 | check 표 1-9 | 대화형, 로그인 필요 | 실제 화면 확인 | 높음 |

실행 출력 원문(python tools/check_tasks.py)
```
건너뜀	작업 1	결정 기록 D-012(사람이 판단하는 확인)
공백 있음	작업 2	python check.py의 수용 시험 4, 5 통과: 구현 전 상태에서도 통과(OK)
공백 있음	작업 3	python check.py의 tests 실패 0건: 구현 전 상태에서도 통과(OK)
정상	작업 4	python check.py의 수용 시험 1, 2, 3 통과: 구현 전 상태에서 실패(FAILED (failures=3))
건너뜀	작업 5	사람 승인(통과 값은 사람이 변경)(사람이 판단하는 확인)
요약: 공백 2건(작업 2, 작업 3)
```
점검 질문 7(검증): 완료 기준 표 없음, R14 위반 없음. 8(일관성): 본문, 예제 사실, 실습 파일 일치.
