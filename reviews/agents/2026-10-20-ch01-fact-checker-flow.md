# ch01 fact-checker 흐름 재점검 사실 확인(2026-10-20)
결과: 필수 4, 권장 3, 참고 7, 확인한 사실 문장 14. 출처 기록: research/ch01-sources.md "2026-10-20 ch01-flow 사실 확인"

| 발견 | 위치 | 근거 | 제안 | 확신 | 처리 |
|---|---|---|---|---|---|
| 필수 1 "Stop 훅이 없으면 루프는 … 계속" 조건이 원문과 다름(원문은 상한이 없으면) | loop | Agent SDK How the agent loop works | "상한이 없으면" | 높음 | 반영 |
| 필수 2, 3 Rajasekaran 외(2025) 글의 주체가 "Claude Code"로 표기됨(글은 Anthropic Applied AI 팀) | agent-harness, prompt-context, manager | Effective context engineering for AI agents | "Anthropic은" | 높음 | 작가 확인(Q-039). 기존 문장이며 D-108 적용 결과이므로 문구 유지 |
| 필수 6 "API는 요청 사이의 상태를 유지하지 않습니다" 일반 문장 미확인 | background 기억 항목 | How tool use works(새 요청마다 원래 대화, 응답, 도구 결과를 다시 보냄) | 절차에 맞춰 쓰고 출처 추가 | 중간 | 반영(문장 수정, 참고 자료에 How tool use works) |
| 권장 4 allow, ask, deny 근거 링크 | loop | Permissions 문서 | 링크 또는 범위 한정 | 중간 | 보류(표 1-9와 같은 Claude Code 규칙 이름, 1장 참고 자료 S18 범위) |
| 권장 5 Agent SDK 풀이 일치 | loop | Agent SDK overview | 유지 | 높음 | 유지 |
| 권장 9 Stop 훅 일치, 연속 차단 상한 8회와 F-13 시험 결과 | loop | Hooks reference | 7장으로 넘김 | 중간 | 보류(상한 8회는 7장 범위, F-13은 PR 설명의 작가 확인 참고) |
| 참고 13 Codex 턴 정의(OpenAI 2026) 원문 미확인(접근 불가) | loop 끝 문단 | S3 | 작가가 원문 확인 | 낮음 | 기존 문장, PR 설명에 적음 |
| 참고 7, 8, 10, 11, 12, 14 | 여러 곳 | | 유지 | | 유지 |
