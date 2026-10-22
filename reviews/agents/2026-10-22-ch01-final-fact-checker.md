# 1장 완성본 fact-checker(2026-10-22, PR #81, 기술 감수)
결과: 필수 4, 권장 8, 참고 6, 확인한 사실 문장 62개. OpenAI 두 글은 다시 HTTP 403.

| # | 등급 | 위치 | 발견 | 처리 |
|---|---|---|---|---|
| 1 | 필수 | "Claude Code의 컨텍스트 엔지니어링 글"(3곳) | 발표 주체는 Anthropic Applied AI 팀 | 보류: BOOK_STANDARD 7절과 R3이 "Claude Code의 … 글은"을 정함(D-131, D-132), 발표 주체 논점은 작가 확인 Q-039 |
| 2 | 필수 | "Claude Code의 장기 실행 글" | 발표 주체는 Anthropic Engineering, Justin Young | 보류(같은 이유, Q-039) |
| 3 | 필수 | 종료 사유는 SDK에서만 | claude -p도 상한 옵션과 JSON 결과 | 반영: "Agent SDK(Python, TypeScript 라이브러리)로 루프를 실행한 경우의 결과 메시지". CLI subtype은 미확인이라 쓰지 않음 |
| 4 | 필수 | 표 1-9 /usage | API와 구독 차이, 추정 금액 | 반영 |
| 5 | 참고 | 하네스 엔지니어링 수치 | 1,500 PR 미확인 | 검증 후 확정(Q-090) |
| 6 | 참고 | Codex 턴 정의, 수백 번 | 미확인 | 검증 후 확정(Q-040, Q-090) |
| 7 | 권장 | "Codex의 … 글" | 발표 주체 OpenAI | 보류(R3 표기, Q-039) |
| 8 | 권장 | 비용 상한 | 추정 지출, 응답 하나 초과 가능 | 반영(버전 조건은 쓰지 않음) |
| 9 | 권장 | Stop 훅 | 사용자 중단 미실행, 연속 8회 상한 | 보류(Chapter 2, 7 몫) |
| 10 | 권장 | /context | 전체 화면 /context all | 반영 |
| 11 | 권장 | LLM, 컨텍스트, 컨텍스트 윈도 정의 | 근거 키 없음 | 반영(platform-glossary, context-engineering) |
| 12 | 권장 | 턴 문장 | 키 하나가 두 문서 | 반영(agent-loop 키 추가, 문장 분리) |
| 13 | 권장 | bibliography agent-loop venue | Agent SDK 표기 | 보류(《Claude Code Docs》 사이트 이름 형식 유지) |
| 14 | 권장 | 마구, 테스트 하네스 | 출처 없음 | 반영("일반적으로 … 뜻하고") |
| 15 | 참고 | Schluntz 저자 표기 | 2차 확인 | 유지(Q-090) |
| 16~18 | 참고 | ReAct 원형, context rot 정도, 워크플로 한계 | 해석, 생략 | 유지 |

키 20곳 대조: 모두 문장과 맞거나(검증 후 확정 포함) 반영. 장별 점검 질문 10개 답은 editor 검토서와 PR 설명.
