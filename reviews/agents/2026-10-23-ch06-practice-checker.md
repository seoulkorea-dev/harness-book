# 6장 실습 감수(practice-checker, 2026-10-23, PR #98)

## 총평
예제 절, 표 6-4~6-6, 본문 JSON(작업 2, 3)은 tasks.example.json과 글자 그대로 같고, 본문의 실행 결과가 모두 재현됨. 필수 0, 권고 3.

## 실행한 명령과 결과(스크래치 lab/expense-practice)
1. 실습 1처럼 복사, git init, 첫 commit
2. python -m unittest discover tests -q → Ran 3 tests OK
3. python check.py → tests 3건 실패 0, acceptance 5건 실패 3, 종료 코드 1
4. python -m unittest discover acceptance -v → FAILED (failures=3)
5. cp reference/tasks.example.json tasks.json, git diff HEAD -- tasks.json → 빈 출력, git status ?? tasks.json(본문 주장과 같음)
6. tasks.json commit 뒤 작업 2 통과 값 true → git diff HEAD -- tasks.json에 그 한 줄만(표 6-6과 같음)
7. python tools/check_tasks.py → 공백 2건(작업 2, 작업 3), 본문과 표 6-5 마지막 행과 일치
8. 저장소 git status --short → 비어 있음

## 발견
| 발견 | 위치 | 제안 | 확신 | 등급 |
|---|---|---|---|---|
| 부록 실습 5에 tasks.json을 첫 단위 전에 commit하는 단계가 없음 | practice.html 실습 5 1단계 | 부록 정비 때 git add, commit과 확인 한 줄 | 높음 | 권고 |
| 본문 "작업 4 전에는 종료 코드 1"과 CLAUDE.example.md "통과하면"이 문자 그대로 부딪힘 | ch06 예제, 표 6-6 / CLAUDE.example.md 작업 순서 | 3장 #88이 CLAUDE.example.md를 고칠 때 "그 단위의 확인 방법에 적힌 시험이 통과하면"으로 | 높음 | 권고 |
| example-facts 작업 5 담당 열 "사람 승인"과 표 6-4 "승인자 승인", 완료 기준 칸의 작업 메모 | docs/example-facts.md 19행 | 맞추고 메모를 칸 밖으로 | 중간 | 권고 |

## 결론
필수 0, 권고 3.
