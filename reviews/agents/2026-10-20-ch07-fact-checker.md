# ch07 fact-checker (2026-10-20, v1.0 보강)

범위: 주장 줄, CR 이름이 바뀐 세 문장, 표 7-4, 표 7-5, 원칙과 점검 질문. 대조: check.py, app.py, acceptance/test_cr07.py(읽기만), settings.example.json, 부록 실습. 문서: Define success criteria and build evaluations, Python unittest(2026-10-20 확인).

| 발견 | 위치 | 근거 | 제안 | 확신 | 심각도 |
|---|---|---|---|---|---|
| http://localhost:8000은 목록 화면이고 등록 화면은 /new | 표 7-5 4행 | app.py do_GET, 부록 실습 1 | 주소를 /new로 | 높음 | 필수(반영) |
| 수용 시험은 브라우저 화면이 아니라 등록 화면 함수의 HTML 출력에 project_code와 코드가 있는지만 확인 | 표 7-4 1행 | test_cr07.py test_1 | "HTML 출력을 확인하는 수용 시험"으로, 화면은 사람이 브라우저로 확인한다고 구분 | 높음 | 필수(반영) |
| 시작 폴더가 없으면 0건이 아니라 오류. 0건은 폴더는 있는데 test*.py 파일이 없을 때 | 표 7-4 3행 | unittest 문서(동작 미기재), check.py | 원인을 "시험 파일을 찾지 못해"로 | 중간 | 필수(반영, 미확인 단정 회피) |
| deny는 Edit 도구만 막고 Bash로 쓰는 변경은 막지 않음 | 표 7-4 2행 | settings.example.json | "Edit 도구로" 한정, git status 행과 연결 | 중간 | 권장 |
| 종료 코드 확인(echo $?, $LASTEXITCODE)과 check.py의 sys.exit(0/1), 실행 0건 실패 판정, LLM 채점 1~5점과 예시 답안, CR 이름 | 표 7-3, 7-5, 예제 절 | check.py, Anthropic 평가 문서 | 없음 | 높음 | 일치 |
| 수용 시험 파일 이름과 문서 문자열에 CR-07 잔재 | acceptance/test_cr07.py | D-104 작가 결정 | v1.1 작가 변경 | 높음 | 참고 |
| 새 절은 이 책 예제에 관한 문장이라 외부 출처 링크가 필요한 사실 없음 | 표 7-4, 7-5 | 형식 | 없음 | 중간 | 권장(조치 없음) |

필수 3, 권장 2, 참고 1, 확인한 사실 문장 10개
