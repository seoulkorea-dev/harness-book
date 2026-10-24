# 실습 실행 기록

실행 환경(Pro 요금제 또는 API 키)이 정해지면 위에서부터 실행하고, 결과를 이 파일에 기록한다(D-074).

## 기준 상태 확인 (2026-10-16, 작성 채팅, Python 3)

```
$ python3 -m unittest discover tests -q
OK
$ python3 check.py
tests: 실행 3건, 실패 0건
acceptance: 실행 5건, 실패 3건
exit=1   (실패: test_1, test_2, test_3. CR 구현 전이므로 정상)
```

## 실습 1 새 흐름 확인 (2026-10-20, 작성 에이전트, Linux, Python 3.13.16, git 2.43.0)

부록 실습 1을 저장소 밖 폴더로 복사하는 흐름으로 바꾸며 실행했다. 저장소 폴더 밖의 새 폴더에 복사했으므로 상위 폴더에 CLAUDE.md와 .claude/가 없다.

```
$ cp -r harness-book/examples/expense-app expense-practice
$ cd expense-practice
$ git init
$ git add -A
$ git commit -m "실습 시작 상태"
$ git log --oneline
83d205a 실습 시작 상태
$ python3 -m unittest discover tests -q
----------------------------------------------------------------------
Ran 3 tests in 0.004s

OK
$ echo $?
0
$ python3 check.py
(앞부분: 단위 테스트 3건 OK, 수용 시험 test_1, test_2, test_3 FAIL과 AssertionError 출력)
Ran 5 tests in 0.006s

FAILED (failures=3)
tests: 실행 3건, 실패 0건
acceptance: 실행 5건, 실패 3건
$ echo $?
1
```

- commit 해시는 실행마다 다르다. git의 사용자 이름과 이메일이 설정되지 않은 환경에서는 commit 전에 git config로 설정해야 한다(이 기록은 명령 옵션으로 지정).

## 실행 대기 실습

| 부록 실습 | 내용 | 상태 | 기록할 것 |
|---|---|---|---|
| 실습 1 | 기준 상태 확인 | 확인함(2026-10-16, 2026-10-20 새 흐름) | 단위 테스트, check.py 출력 |
| 실습 2 | CLAUDE.md 작성, 수정 범위 질문 | 실행 전 | 질문과 응답 원문 |
| 실습 3 | settings.json 권한 설정, 금지 동작 요청 | 실행 전 | /permissions 화면 내용, 거부 메시지 원문 |
| 실습 4 | 훅과 검토 하위 에이전트 | 실행 전 | 훅 출력, reviewer 보고 원문 |
| 실습 5 | tasks.json, 세션 1(작업 2, 작업 3) | 실행 전 | check.py 출력, tasks.json 변경, commit 확인 요청 |
| 실습 6 | HANDOFF.md, 세션 2(작업 4) | 실행 전 | HANDOFF.md, check.py 출력, /usage |

실행할 때마다 날짜, 모델과 제품 버전, 요청 원문, 출력 원문, 재실행 시 차이를 함께 적는다.

## 검사 스크립트 보강 뒤 기준 상태 (2026-10-22, 작성 에이전트, Linux, Python 3.13.16, 3장 정비 PR #88)

check.py가 건너뜀, 수용 시험 수(5건), 이름에 project_code가 든 단위 시험 수를 함께 본다.

```
$ python check.py
tests: 실행 3건, 실패 0건, 건너뜀 0건, project_code 시험 0건
acceptance: 실행 5건, 실패 3건, 건너뜀 0건(정한 수 5건)
exit=1
$ python tools/check_tasks.py   (저장소 루트)
건너뜀	작업 1	결정 기록 D-012(사람이 판단하는 확인)
공백 있음	작업 2	python check.py의 수용 시험 4, 5 통과: 구현 전 상태에서도 통과(OK)
정상	작업 3	python check.py의 tests 실패 0건, project_code 시험 1건 이상: 구현 전 상태에서 실패(NO TESTS RAN)
정상	작업 4	python check.py의 수용 시험 1, 2, 3 통과: 구현 전 상태에서 실패(FAILED (failures=3))
건너뜀	작업 5	사람 승인(통과 값은 사람이 변경)(사람이 판단하는 확인)
요약: 공백 1건(작업 2)
```

## 실습 1 check.py 재확인 (2026-10-24, 작성 에이전트, Linux, Python 3)

현재 check.py의 요약 줄 형식(건너뜀, project_code 시험 건수 포함)으로 다시 실행했다.

```
$ python3 check.py
(앞부분: 단위 테스트 출력)
tests: 실행 3건, 실패 0건, 건너뜀 0건, project_code 시험 0건
(수용 시험 test_1, test_2, test_3 FAIL과 AssertionError 출력)
Ran 5 tests in 0.006s

FAILED (failures=3)
acceptance: 실행 5건, 실패 3건, 건너뜀 0건(정한 수 5건)
exit=1
```
