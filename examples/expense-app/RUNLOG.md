# 실습 실행 기록

실행 환경(Pro 요금제 또는 API 키)이 정해지면 위에서부터 실행하고, 결과를 이 파일에 기록한다(D-074).

## 기준 상태 확인 (2026-10-16, 작성 채팅, Python 3)

```
$ python3 -m unittest discover tests -q
OK
$ python3 check.py
tests: 실행 3건, 실패 0건
acceptance: 실행 5건, 실패 3건
exit=1   (실패: test_1, test_2, test_3. CR-07 구현 전이므로 정상)
```

## 실행 대기 실습

| 순서 | 실습 | 상태 | 기록할 것 |
|---|---|---|---|
| 1 | 하네스 없이 요청(CLAUDE.md, .claude/가 없는 복사본에서 "CR-07을 구현해 줘") | 실행 전 | 수정한 파일, 테스트 실행 여부, data/ 변경 여부 |
| 2 | 세션 1: CR-07-2, CR-07-4 | 실행 전 | /permissions 화면, 거부와 확인 요청, check.py 출력, 훅 출력, HANDOFF.md, /usage |
| 3 | 세션 2: HANDOFF.md로 시작, CR-07-3, CR-07-4, CR-07-5 초안 | 실행 전 | check.py 출력, reviewer 보고, /usage |
| 4 | python app.py로 화면 확인, CR-07-5 승인 판단 | 실행 전 | 승인 판단 |

실행할 때마다 날짜, 모델과 제품 버전, 요청 원문, 출력 원문, 재실행 시 차이를 함께 적는다.
