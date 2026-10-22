# 1장 정비 fact-checker(2026-10-22, PR #69)

범위: src/chapters/ch01.html의 각주 15개(정비 1차)와 사실 문장 약 45개. OpenAI 두 글은 HTTP 403으로 열람 실패.
결과: 필수 0, 편집 권고 11, 검증 후 확정 4. (각주 번호는 정비 1차 기준. 2차 뒤 번호는 +1~+5)

| # | 발견 | 위치 | 근거 | 제안 | 확신 | 등급 | 처리 |
|---|---|---|---|---|---|---|---|
| 1 | 각주 1 일치 | 첫 절 | how-tool-use-works "The model never runs anything on its own … your code (or Anthropic's servers) runs the operation" | 유지 | 높음 | 확정 | 유지 |
| 2 | "기억" 앞 문장은 문서에 없는 추론 | 첫 절 기억 항목 | 같은 문서, stateless 문장 없음 | 도구 사용 절차로 한정 | 높음 | 편집 권고 | 반영(첫 문장 삭제) |
| 3 | 각주 2 일치(is_error) | 도구 문단 | handle-tool-calls "Handling errors with is_error" | 유지 | 높음 | 확정 | 유지 |
| 4 | 각주 3 ReAct 일치, "원형"은 해석 | ReAct 문단, 표 1-2 | arXiv 2210.03629, ICLR 2023 | 조건 표현 | 높음/중간 | 확정/편집 권고 | 반영 |
| 5 | 각주 4 내용, 날짜 일치, 저자 성 표기 미확인 | 각주 4 | building-effective-agents | 작가 byline 확인 | 중간 | 검증 후 확정 | 유지, Q-090 |
| 6 | Codex 루프 글 본문 수치와 정의 원문 미열람 | Codex 문단, 각주 5, 13 | 403 | 작가 확인 | 낮음 | 검증 후 확정 | 유지, Q-040, Q-090 |
| 7 | Codex 문단 앞 문장들에 각주 없음 | Codex 문단 | STYLE 4절 | 각주 위치 | 높음 | 편집 권고 | 반영(문장마다 각주) |
| 8 | Young 글은 하네스를 정의하지 않고 "주변 체계" 뜻으로 사용 | 하네스 명칭 문단, 표 1-3 | effective-harnesses-for-long-running-agents | 쓰임으로 서술 | 높음 | 편집 권고 | 반영. 주어 표기는 R3대로 유지 |
| 9 | 각주 7, 14, 15 일치 | 여러 곳 | effective-context-engineering | 유지 | 높음 | 확정 | 유지 |
| 10 | 각주 8 Glossary 일치 | 둘째 문단 | Claude Code Glossary Agentic harness | 유지 | 높음 | 확정 | 유지 |
| 11 | 각주 10, 12 일치(Agent SDK, 기본 No limit, 종료 사유 4종) | 루프 절 | agent-sdk/agent-loop | 유지 | 높음 | 확정 | 유지 |
| 12 | 거부 문장, 종료 사유 문장에 각주 없음, 단계 3 허용/확인/거부 근거 | 루프 절 | 같은 문서, Glossary | 앞의 주 10 | 높음 | 편집 권고 | 거부, 종료 사유에 각주 반영. 단계 3은 보류 |
| 13 | 각주 11 Hooks 일치(Stop exit 2 차단), Stop 절 본문 미열람 | 그림 1-2 설명 | hooks | 유지 | 중간 | 확정 | 유지 |
| 14 | 각주 9 저자, 날짜 일치, "약 1,500개 풀 리퀘스트" 미확인 | 하네스 엔지니어링 절 | 403, 2026-10-04 직접 열람 기록 | 유지, 미확인 표시 | 중간 | 검증 후 확정 | 유지, Q-090 |
| 15 | "Claude Code의 … 글" 표기가 발표 주체와 다름 | 여러 곳 | STYLE 4절 | "Anthropic의 … 글" | 높음 | 편집 권고 | 보류: R3과 STYLE 4절 예가 "Claude Code의 장기 실행 글은"을 정함(D-127, Q-039) |
| 16 | 토큰 정의는 Platform Glossary와 뜻이 맞음, 각주 없음 | 첫 절 | platform glossary Tokens | 각주 | 높음 | 편집 권고 | 반영(각주 1) |
| 17 | 컨텍스트 윈도, LLM 정의 각주 없음 | 첫 절 | 같은 용어집 | 확인 필요 | 중간 | 편집 권고 | 보류(v1.1-backlog) |
| 18 | 턴 비교에서 Claude Code 용어집 턴 누락 | Codex 문단 | Glossary Turn | 문서마다 다름 | 높음 | 편집 권고 | 반영 |
| 19 | 표 1-9 명령 확인 | 표 1-9 | commands | 유지 | 높음 | 확정 | 유지 |
| 20 | research 인용 "executes" → "runs" | research S8, S24 | 위 1번 | 정정 | 높음 | 편집 권고 | 반영 |
| 21 | 열람일 갱신 여부 | 각주 | 2026-10-22 재확인 일치 | 작가 판단 | 높음 | 편집 권고 | 유지 |

research/ch01-sources.md에 덧붙일 확인 기록 문안은 같은 날짜 절로 반영했다.
