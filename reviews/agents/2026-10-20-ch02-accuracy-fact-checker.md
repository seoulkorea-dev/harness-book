# ch02 정확성 보강 fact-checker (2026-10-20, 이슈 #10)

확인 원문: agent-sdk/agent-loop, mcp, permissions, memory, costs, MCP 규약 Tools(revision 2026-07-28). 기록: research/ch02-sources.md S39, S25, S26, S30, S37 보강.

| 발견 | 위치 | 근거 | 제안 | 확신 | 심각도 |
|---|---|---|---|---|---|
| "입력 구성, 출력과 실행 환경 연결, 진행 제어"는 Chapter 1 정의 문구에 없고, #harness는 정의 절이 아님 | components 첫 문단 | ch01 #agent-harness, #harness | Chapter 1 용어로 쓰고 #agent-harness로 링크, 또는 정의 변경을 작가에게 | 중간 | 필수 |
| "뿐"의 범위: 권한 규칙 안에서만 맞음(MCP 지연 로드, 하위 에이전트 도구 목록도 노출을 줄임) | tool-scope 셋째 문단, 그림 2-2 "*" | permissions | "권한 규칙 가운데"로 한정 | 높음 | 권장 |
| 문서의 실행 주체는 "SDK", "harness"라는 말은 문서에 없음, 링크 위치 | tool-scope 셋째 문단 | agent-loop | 문서 표현과 이 책 용어를 나눔, 링크 앞당김 | 높음 | 권장 |
| 기록 문장의 링크는 API 수준(Chapter 1), 주장은 세션 수준 | 기록 항목 | memory, agent-loop | 2026a 링크 더함 | 높음 | 권장 |
| "확인은 승인 후"는 기본 모드 기준, 다른 모드는 미확인 | 그림 2-2 | permissions | 미확인 기록 | 낮음 | 참고 |
| 장 연결 문장(Chapter 4~6)은 책 구성 | components 첫 문단 | 범위 밖 | 편집자 확인 | - | 참고 |
| MCP 지연 로드는 규약이 아니라 Claude Code 기능, 거부 메시지 전달, 읽기 전용 동시 실행, 평가 순서, 이력 누적, 규칙 문서와 자동 메모리는 강제 아님, 참고 자료 id | 여러 곳 | mcp, MCP 규약, agent-loop, permissions, memory | 없음 | 높음 | 일치 |

필수 1, 권장 3, 참고 2, 확인한 사실 문장 15개
