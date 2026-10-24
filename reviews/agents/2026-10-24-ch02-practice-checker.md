# Chapter 2 예제 실습 점검(practice-checker, 2026-10-24, PR #123)

요약: 필수 1, 권고 2, 참고 3. 파일 변경 없음(git status 비어 있음). 범위: 예제 절, 표 2-4~2-7, "예제에서는" 항목. 대조: docs/example-facts.md, examples/expense-app/reference/*, check.py, tools/check_tasks.py, 3, 6, 7장, 부록 실습.

| # | 위치 | 확인 결과와 근거 | 등급 | 제안 |
|---|---|---|---|---|
| 1 | 표 2-5 "파일을 수정할 때마다 단위 테스트 실행" 지시 수단 칸 | "없음(규칙 문서의 명령 절에는 단위 테스트 명령만 있음)"은 사실과 다름. reference/CLAUDE.example.md 명령 절에는 단위 테스트, 전체 검사(python check.py), 앱 실행, python3 안내가 있음 | 필수 | "없음(규칙 문서의 명령 절에는 명령만 적혀 있고, 수정할 때마다 실행하라는 지시는 없음)" |
| 2 | 표 2-4 역할 줄 운영 기준 칸 | 규칙 문서에 적는 것(false인 첫 단위만 수행, 작업 5 변경 금지)과 사람의 몫(수용 기준 확정, 작업 1 합의, 작업 5 승인, commit 확인, push)을 한 문장에 이어 써서 사람의 몫도 규칙 문서에 있는 것처럼 읽힘 | 권고 | 규칙 문서에 적는 것과 사람이 맡는 것(규칙 문서에는 적지 않음)을 나눔 |
| 3 | 3장 설정 코드 상자(ch03.html 64~96줄) | reference/settings.example.json의 python3 허용 두 항목이 없음(원본보다 짧음, 플레이북 15장, R17) | 권고 | 3장 정리 때 처리(장 밖) |
| 4 | 표 2-4, 2-5, 2-7 권한 | 허용, 확인 요청, 금지 9개와 규칙 글자가 settings.example.json과 같음 | 참고 | 없음 |
| 5 | JSON 형식과 훅 | json.load 두 파일 "json ok". 훅 PostToolUse, matcher Edit|Write, `python -m unittest discover tests -q || exit 2`가 표 2-4와 같음. 직접 실행 Ran 3 tests OK(rc 0). Claude Code 안의 훅 동작은 대화형이라 실행하지 못함 | 참고(검증 후 확정) | 부록 실습 4에서 확인 |
| 6 | 검사 스크립트 설명 | check.py 구현 전 출력 tests 실행 3건 실패 0건, acceptance 실행 5건 실패 3건, FAILED (failures=3), rc 1. 본문 설명과 같음 | 참고 | 없음 |
| 7 | R6, R7 | 작업 단위 사실은 example-facts, tasks.example.json, 6장 표 6-4, 3장 표 3-2와 같음. check_tasks 공백 2건(작업 2, 3)은 6장이 다룸. ch02는 작업 2, 3 완료 증명을 주장하지 않음 | 참고 | 없음 |

실행 명령: python tools/check_tasks.py(공백 2건, rc 1), python check.py(rc 1), python -m unittest discover tests -q(OK), json.load 두 파일(json ok), git status --short(비어 있음).
