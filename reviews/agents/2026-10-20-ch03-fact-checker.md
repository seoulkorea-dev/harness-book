# ch03 fact-checker (2026-10-20, v1.0 보강)

범위: 주장 줄, CR 이름 변경 문장, reviewer 코드, 표 3-5, 표 3-6, 원칙과 점검 질문. 문서: Commands, Create custom subagents, Hooks reference(2026-10-20 확인). research/ch03-10-sources.md에 기록.

| 발견 | 위치 | 근거 | 제안 | 확신 | 심각도 |
|---|---|---|---|---|---|
| 현재 /agents는 하위 에이전트 관리를 Claude에게 요청하거나 .claude/agents/를 직접 편집하라는 안내만 출력. 목록과 도구를 보여 주는 화면은 v2.1.197 이전 동작(낡음) | 표 3-6 2행 | Commands(/agents), Create custom subagents | 확인 위치를 reviewer.md의 tools 줄과 /context의 하위 에이전트 항목으로 변경 | 높음 | 필수(반영) |
| 확인 방법, 실패와 막는 장치 절에 발표 주체와 참고 자료 링크 없음 | fail, check 절 | 형식 | Commands 문서 참고 자료 추가 | 중간 | 권장 |
| /permissions, 표 3-6 1행의 deny와 ask 목록, 기준 상태(5건 가운데 3건 실패, exit 1), 표 3-5 장치, CR 정보, reviewer 코드, 설정 코드, PostToolUse 종료 코드 2 설명은 예제 파일, 문서와 일치 | 표 3-5, 3-6, 예제 절, 제품 파일 절 | settings.example.json, RUNLOG.md, docs/CR.md, reviewer.example.md, Hooks reference | 없음 | 높음 | 일치 |
| 구현 완료 뒤 check.py 통과(exit 0) 실행 기록은 없음(코드 논리로는 일치) | 표 3-6 4행 | RUNLOG.md 실습 5, 6 "실행 전" | 실습 실행 뒤 RUNLOG 기록 | 중간 | 참고(미확인) |
| 중단 규칙은 CLAUDE.md 지침이라 강제 장치가 아님 | 표 3-5 2행 | Debug your configuration | "지침으로 정함" 한정 여부 작가 판단 | 중간 | 참고 |
| 수용 시험 파일 이름 test_cr07.py에 CR-07 잔재(본문은 파일 이름을 쓰지 않음) | examples/expense-app/acceptance/, docs/CR.md 15행 | D-104 작가 결정 | v1.1에서 작가가 변경 | 높음 | 참고 |

필수 1, 권장 1, 참고 2(조치 대상 기준), 확인한 사실 문장 12개
