# ch03 fact-checker (2026-10-20, 3장 개정)

범위: src/chapters/ch03.html의 바뀐 문장. 문서 6개(permissions, hooks, sub-agents, commands, memory, agent-loop) 다시 확인, examples/expense-app/와 부록 practice.html 대조. 기록은 research/ch03-sources.md C3-8.

| 발견 | 위치 | 근거 | 제안 | 확신 | 심각도 |
|---|---|---|---|---|---|
| "아홉 항목 가운데 다섯 항목"이 표 3-5 원인 열(권한, 검증, 종료 조건, 역할, 승인 지점, 기록 여섯 개)과 맞지 않음 | fail 첫 문단 | 표 3-5 원인 열 | "다섯 가지 대표 실패"로 | 높음 | 필수 |
| "중단 규칙만 지시"가 예제와 어긋남. reviewer 요청 시점, 통과 값 변경 범위, 인계 메모 작성도 CLAUDE.md의 지시 | 표 3-5 뒤 문단 | CLAUDE.example.md 작업 순서, 중단 규칙 | 범위를 넓히거나 "만"을 뺌 | 높음 | 필수 |
| /context의 하위 에이전트 항목 표시는 문서로 확인하지 못함 | 표 3-6 검토 하위 에이전트 행 | Commands, context-window 문서 | 확인 기준을 reviewer.md의 tools 줄로 줄이는 안 검토 | 중간 | 참고(미확인) |
| /hooks 목록에 matcher가 보이는지 문서로 확인하지 못함 | 표 3-6 훅 행 | hooks 문서 /hooks 절 | "PostToolUse에 훅이 있고 선택하면 명령이 보임"으로 완화 | 중간 | 참고(미확인) |
| 훅 명령이 python 고정(python이 없으면 실패 신호) | 훅 단락, settings.example.json | CLAUDE.example.md 마지막 줄 | 실습 4에 한 줄(범위 밖) | 중간 | 참고 |
| 권한 규칙 읽는 법, PostToolUse 종료 코드 2, tools 상속, CLAUDE.md는 컨텍스트, 명령 설명, 표 3-6 권한 행, 사람 승인 범위, 실습 번호 대응, 수용 시험 대응, 예제 소개, 참고 자료 id | 여러 곳 | 문서와 예제 파일 | 없음 | 높음 | 일치 |

필수 2, 권장 0, 참고 3, 확인한 사실 문장 약 40개
