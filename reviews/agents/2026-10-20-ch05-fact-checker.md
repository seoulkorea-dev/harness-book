# ch05 fact-checker (2026-10-20, v1.0 보강)

범위: 주장 줄, 실패와 막는 장치(표 5-3), 확인 방법(표 5-4), 원칙과 점검 질문. 문서: memory, costs, debug-your-config, commands, sub-agents, context-window(2026-10-20 확인). research/ch03-10-sources.md에 기록.

| 발견 | 위치 | 근거 | 제안 | 확신 | 심각도 |
|---|---|---|---|---|---|
| "Claude Code는 CLAUDE.md를 … 읽습니다"는 낡음. CLAUDE.md가 없고 AGENTS.md만 있으면 AGENTS.md를 읽음(v2.1.277 이상) | 규칙 문서 작성 절(기존 본문) | memory 문서 AGENTS.md 절 | 본문 유지, 버전 주석 추가 | 높음 | 필수(반영) |
| 문서는 "200줄 미만 목표", 책은 "200줄 이내" | 표 5-3 1행, 표 5-4 2행, 본문 | memory, costs | "200줄 미만(목표)" | 중간 | 권장 |
| /context는 전체화면 모드에서 분류를 접고 /context all로 펼침, 하위 폴더 규칙 문서는 시작 때 안 보임 | 표 5-4 1행 | commands, debug-your-config | 확인 기준에 덧붙임(선택) | 중간 | 권장 |
| "테스트 출력 때문에 앞의 지시를 놓친다"의 직접 근거 없음 | 표 5-3 4행 | 확인 범위 memory, costs, debug, context-window | "놓칠 수 있음"으로 한정, ref-rajasekaran-2025 링크 | 중간 | 권장(미확인) |
| 표 5-3, 5-4에 발표 주체와 참고 자료 링크 없음, 참고 자료에 Debug, Commands 문서 없음 | 표 5-3, 5-4 | 형식 | 주체 표기, 참고 자료 추가 | 중간 | 권장 |
| /context 메모리 파일 항목, Read 도구 호출이 대화에 한 줄로 보임, 하위 에이전트 위임 시 요약만 돌아옴, CLAUDE.example.md 읽는 순서, 부록 실습 2, 결정 기록 대체 칸, CLAUDE.md는 강제 설정이 아닌 컨텍스트 | 표 5-3, 5-4, 본문 | memory, debug, context-window, costs, sub-agents, 예제 파일 | 없음 | 높음 | 일치 |
| 하위 에이전트 위임 뒤 주 컨텍스트는 "늘지 않음"이 아니라 "요약만큼 늘어남" | ch06 본문(범위 밖) | costs, context-window | v1.1 | 중간 | 참고 |

필수 1, 권장 4, 참고 0, 확인한 사실 문장 12개
