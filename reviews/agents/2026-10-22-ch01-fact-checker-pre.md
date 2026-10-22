# 1장 다시 만들기: fact-checker 사전 확인(2026-10-22)

- 범위: 다시 쓰면서 새로 넣을 사실 문장 8건(확인일 2026-10-22). 출처 기록은 research/ch01-sources.md "2026-10-22 1장 다시 만들기 사전 확인"
- 결과: 필수 2, 권장 3, 참고 6

| 발견 | 위치 | 근거 | 제안 | 확신 |
|---|---|---|---|---|
| "OpenAI 글에서 이 이름이 알려졌다"는 1차 근거 부족. Hashimoto 글(2026.2.5)이 먼저 이 말을 씀 | 첫머리, 하네스 엔지니어링 절 | mitchellh.com 원문, OpenAI 글 HTTP 403 | "제목으로 쓰였다"로 좁히고 두 글을 순서대로 밝힘(반영, Q-108) | 높음 |
| 권한 모드 정의가 문서보다 좁음 | 루프 절 | permissions 문서 Permission modes | 승인 방식(물음, 자동 승인, 자동 거부)으로 정의(반영, Q-110) | 높음 |
| 금지 규칙의 적용 범위는 양면 서술 필요 | 루프 절 | permissions 문서 Read and Edit 경고 | cat, sed에는 적용, 스크립트 직접 열기는 막지 못함, 샌드박스(반영) | 높음 |
| Stop 훅 stop_hook_active 문장 맞음 | 루프 절 | hooks 문서 Stop decision control | 주체(훅 작성자) 밝힘(반영) | 높음 |
| 자동 압축 맞음(오래된 도구 출력 먼저 지우고 필요하면 요약) | background, 표 1-1, 표 1-8 | how-claude-code-works | 순서대로 씀(반영) | 높음 |
| 세션 기록은 작업하는 동안 계속 저장 | 루프 절 | how-claude-code-works | 반영 | 높음 |
| 거부 메시지, 상한 기본값, 종료 사유 맞음 | 루프 절 | agent-loop | 유지 | 높음 |
| OpenAI 글 세부(1,500 PR, 100줄 AGENTS.md, 린터 메시지, 화면) 1차 미확인 | 하네스 엔지니어링 절 | HTTP 403 | 1,500 PR은 S2 기록 유지, 나머지는 본문에 넣지 않음 | 중간 |
| Codex 소개 문구는 CLI 한정 1차 | 한 요청 절 | github.com/openai/codex | "OpenAI의 Codex"를 예로만 씀 | 중간 |
