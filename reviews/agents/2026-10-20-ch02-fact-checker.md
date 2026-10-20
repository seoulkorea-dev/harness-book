# ch02 fact-checker (2026-10-20, v1.0 보강)

범위: 주장 줄, 실패와 막는 장치(표 2-4), 확인 방법(표 2-5), 원칙과 점검 질문. 대조: ch03, examples/expense-app/reference/(settings, CLAUDE, tasks), check.py. 문서: Configure permissions, Hooks reference, Hooks guide(2026-10-20 확인). research/ch02-sources.md S23, S24에 기록.

| 발견 | 위치 | 근거 | 제안 | 확신 | 심각도 |
|---|---|---|---|---|---|
| 성공한 훅의 출력은 대화 기록에 나타나지 않음(디버그 로그로 감). 대화에는 차단이나 실패 때 hook error 알림만 보임. "대화 화면에 훅이 테스트를 실행한 흔적"은 불일치 | 표 2-5 검증 행 | Hooks reference(exit code와 출력) | /hooks(훅 등록)와 실패 때 알림으로 한정 | 높음 | 필수(반영) |
| Edit deny는 내장 수정 도구와 인식되는 Bash 명령은 막지만 Python 스크립트 같은 간접 쓰기는 막지 못함(샌드박스 필요) | 표 2-4 3, 5행 | Configure permissions(Read and Edit) | 막는 범위 한 문장 추가 여부 작가 판단 | 중간 | 권장 |
| 웹 접근 도구 deny, 사람이 변경하는 완료 표시, 작업 단위 목록과 인계 메모, 폴더별 건수, /permissions, /context, 수용 시험 설명은 예제 파일, 문서와 일치 | 표 2-4, 2-5 | settings.example.json, CLAUDE.example.md, tasks.example.json, check.py, research S20, S21 | 없음 | 높음 | 일치 |
| "작업 단위마다 commit 하나" 규칙이 ch03 명세에는 있으나 CLAUDE.example.md에는 없음 | 표 2-5 기록 행 | 예제 파일 대조 | 예제 규칙 문서에 한 줄 추가 여부 작가 확인 | 중간 | 권장 |
| 확인 방법 절에 발표 주체와 참고 자료 링크 없음(Commands, Debug, Hooks reference 항목 없음) | 확인 방법 절 | 형식 | 주체 표기와 참고 자료 추가 | 중간 | 권장 |
| 실패와 막는 장치 절에 참고 자료 링크 없음 | fail 절 | 형식 | ref-anthropic-2026a 한 번 링크 | 중간 | 권장 |
| 주장 줄은 1차 근거 없는 일반화(이 책의 주장) | 주장 줄 | research "근거가 부족한 곳" | 작가 판단 | 낮음 | 참고(미확인) |
| 표 2-4 실패는 관측 사례가 아닌 가상 시나리오 | 표 2-4 | RUNLOG.md | "생길 수 있는" 표현 유지 | 중간 | 참고 |
| ch03 설정의 ./data/** 같은 ./ 경로는 현재 디렉터리 기준이라 Claude Code를 examples/expense-app/에서 시작해야 의도대로 작동 | ch03 설정(범위 밖) | Configure permissions 경로 표 | ch03 점검 대상으로 전달 | 중간 | 참고 |

필수 1, 권장 4, 참고 2, 확인한 사실 문장 15개
