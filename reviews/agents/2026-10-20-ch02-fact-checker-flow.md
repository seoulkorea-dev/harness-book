# ch02 fact-checker 흐름 재점검 사실 확인(2026-10-20)
결과: 필수 1(+작가 확인 1), 권장 5, 참고 3. 출처 기록: research/ch02-sources.md "2026-10-20 ch02-flow 사실 확인"

| 발견 | 위치 | 근거 | 제안 | 확신 | 처리 |
|---|---|---|---|---|---|
| 1 CLAUDE.md는 세션 시작 때 읽음(하위 폴더는 필요할 때, AGENTS.md 대체) | 용어 문단 | memory 문서 | 유지 | 높음 | 유지 |
| 2 권한 규칙은 설정 파일에 적음 | 용어 문단 | permissions 문서 | 유지 | 높음 | 유지 |
| 3 필수: 훅은 셸 명령만이 아님(http, mcp_tool, prompt, agent), "판단과 관계없이"의 직접 근거는 debug-your-config | 용어 문단, 지시와 강제 둘째 문단 | hooks, debug-your-config | 범위 한정, 2026c 인용 | 중간 | 반영 |
| 4 금지 규칙은 제품이 적용, 규칙 문서는 모델이 따라야 함 | 지시와 강제 첫 문단 | permissions, memory | 유지 | 높음 | 유지(다음 문단이 인용) |
| 5 이름만 지정한 금지 규칙은 목록에서 제외 | tool-scope | permissions | 유지 | 높음 | 유지 |
| 6 "작업 단위마다 검사를 통과했는지"는 작업 1, 5에 맞지 않음 | CR 문단 | tasks.example.json | "완료 여부" | 높음 | 반영(3장 표 3-2도 같은 한계, 3장 재점검 때 확인) |
| 7 검증이 강제 묶음인 근거는 편집 뒤 훅 부분만 | 그림 2-1 | settings.example.json | 근거 한정 | 중간 | 보류(그림 묶음은 D-109 채택 시안, Q-041에 함께 적음) |
| 8a "막습니다"는 push에만 맞음(commit은 확인) | 그림 2-1 문단 | settings.example.json | "막거나 확인을 요청" | 높음 | 반영 |
| 8b "의견이 있습니다"의 출처 없음 | 실패와 막는 장치 첫 문단 | STYLE 1, 4 | 이 책의 정리로 | 중간 | 반영 |
| 9 작가 확인: "Claude Code는 최소한의 도구 집합을 권합니다(Rajasekaran 외, 2025)" 주체 | tool-scope | S34 | "Anthropic의 글" | 높음 | Q-039에 포함 |
| 10 인용 위치: 도구 정의가 공간을 차지(2026b), /context(2026c) | tool-scope | agent-loop, debug-your-config | 나눠 링크 | 높음 | 반영 |
| 11 사람 거절의 거부는 Agent SDK 문서만 확인 | tool-scope 넷째 문단 | Handle approvals | "Agent SDK 문서에 따르면" | 중간 | 반영 |
| 12~14 표 2-2, 2-6, 설정 값, 버전 주석 | | | 유지 | 높음 | 유지 |
