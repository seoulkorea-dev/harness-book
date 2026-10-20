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
