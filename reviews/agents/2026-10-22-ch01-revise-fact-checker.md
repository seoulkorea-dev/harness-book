# ch01 1장 수정(PR #82) 기술 감수: fact-checker

- 날짜: 2026-10-22. 범위: src/chapters/ch01.html 인용 링크 12개와 이번에 고친 사실 문장, 표 1-4 기능적 제약 칸
- 결과: 필수 5, 검증 후 확정 1, 권장 7, 참고 2. 확인한 사실 문장 약 45개. OpenAI 두 글은 HTTP 403(열람 실패)

| 발견 | 위치 | 근거 | 제안 | 확신 | 반영 |
|---|---|---|---|---|---|
| (필수) "같은 용어집은 LLM을 … 다음 토큰을 예측 …, 컨텍스트 윈도를 … 토큰의 범위로 설명"이 원문과 다름(용어집 LLM 항목은 방대한 텍스트로 학습한 언어 모델, 다음 단어 예측은 Pretraining 항목, Context window는 되돌아보고 참고할 수 있는 텍스트의 양) | 7행 | platform.claude.com/docs/en/about-claude/glossary | 원문대로 고치거나 용어집 귀속을 뺌 | 높음 | 반영: 정의는 용어표(BOOK_STANDARD 5절, 작가 결정) 그대로 "이 책에서"로 밝히고, 용어집에는 사전 학습의 다음 단어 예측만 귀속. 용어 정의 문구는 Q-106 |
| (필수) "Claude Code의 컨텍스트 엔지니어링 글"의 주체(Anthropic 엔지니어링 글) | 7, 39, 100, 135행 | anthropic.com/engineering/effective-context-engineering-for-ai-agents | "Anthropic의 …"로 | 높음 | 보류: D-108(제품명 표기), Q-101(발표 주체 표기, 작가 확인 대기) |
| (필수) "Claude Code의 장기 실행 글"의 주체 | 25행 | anthropic.com/engineering/effective-harnesses-for-long-running-agents | "Anthropic의 …"로 | 높음 | 보류: 위와 같음(Q-101) |
| (검증 후 확정) Codex 글 귀속 문장(턴 정의, 수백 번 도구 호출, 약 1,500 PR) 1차 원문 미확인 | 62, 98행 | openai.com 두 글 HTTP 403 | 작가 확인 전 삭제나 확인 항목 | 높음 | 보류: 이번 PR에서 바꾸지 않은 기존 문장, Q-040, Q-090 유지 |
| (필수) "모델은 하네스가 넘긴 입력 밖의 정보를 보지 못함"은 단정(학습 지식, 서버 도구) | 표 1-4 화살표 행 | 용어집 Context window, How tool use works | "현재 작업의 정보는 … 입력에 든 것만(학습한 지식은 예외)" | 높음 | 반영 |
| (필수) "기본 도구나 MCP 서버로 연결한 대상에만 작용"은 범위가 좁게 읽힘(Bash 범위, 사용자 정의 도구) | 표 1-4 외부 실행 환경 행 | agent-sdk/agent-loop, How tool use works | 도구가 닿는 대상, 기본 도구는 권한과 격리로 제한 | 중간 | 반영: "도구를 거쳐서만 작용(기본 도구는 범위가 넓어 권한과 격리로 제한)". 그림 1-1 분류는 그대로 |
| (권장) 실행 장치 칸 "팀의 기준 … 담지 않음"과 제품 기본값 | 표 1-4 | code.claude.com/docs/en/glossary | "팀 고유의 기준은 담지 않음(제품 기본값만 있음)" | 중간 | 반영 |
| (권장) 실행 실패 결과 단정형(원문 "돌려줄 수 있다", is_error 선택) | 10행 | handle-tool-calls | 가능형으로 | 높음 | 반영 |
| (권장) 거부 뒤 "typically" 빠짐 | 95행 | agent-sdk/agent-loop | "대개" | 높음 | 반영 |
| (권장) Stop 훅 연속 차단 상한, 종료 코드 2 | 85행 | hooks | 작가 결정 | 중간 | 보류(2장, 7장 몫) |
| (권장) "Claude Code 문서는"이 어느 문서인지 | 40행 | glossary Agentic harness | "Claude Code 용어집은" | 높음 | 반영 |
| (권장) "이 설명에서 한계가 세 가지로 드러남"은 문서가 말한 것처럼 읽힘 | 8행 | How tool use works | "이 설명을 바탕으로 이 책은 … 정리" | 중간 | 반영 |
| (권장) 표 1-9 명령의 근거 자료(Commands, Costs)가 자료 목록에 없음 | 표 1-9 | research S20, S31 | 키 추가와 링크 | 높음 | 보류: 자료 추가는 다음 정비에서(사실은 research 기록과 일치) |
| (참고) 턴, 상한, 종료 사유, Turn 용어집 문장 일치 | 84, 97, 98행 | agent-loop, glossary | 변경 없음 | 높음 | - |
