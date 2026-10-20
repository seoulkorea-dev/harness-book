# Chapter 6 개정 출처(2026-10-20, researcher 확인, 메인 세션 저장)

기존 기록: research/ch03-10-sources.md(S3 Young, S4 Claude Code Docs, "보강 4"). 원문은 영어, 인용은 짧게.

## C6-1. Young, J., Effective harnesses for long-running agents(Anthropic, 2025-11-26)
- URL: https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents, 확인 2026-10-20
- 실패 1: "tended to try to do too much at once", 다음 세션이 "a feature half-implemented and undocumented"에서 시작
- 실패 2: 뒤의 인스턴스가 진행을 "see that progress had been made, and declare the job done"
- 기능 목록: "over 200 features", 처음에 모두 "failing"
- "This incremental approach turned out to be critical to addressing the agent's tendency to do too much at once"
- JSON: "the model is less likely to inappropriately change or overwrite JSON files"(Markdown 대비), "edit this file only by changing the status of a passes field"
- 확신: 높음

## C6-2. Anthropic, Create custom subagents(Claude Code Docs)
- URL: https://code.claude.com/docs/en/sub-agents, 확인 2026-10-20
- "Each subagent runs in its own context window", "It doesn't see your conversation history"(포크는 예외: 부모 대화를 물려받음), 요약만 돌아옴
- "Running many subagents that each return detailed results can consume significant context, and each subagent spends tokens of its own while it runs."
- 확신: 높음

## C6-3. Anthropic, How the agent loop works(Agent SDK)
- URL: https://code.claude.com/docs/en/agent-sdk/agent-loop, 확인 2026-10-20
- "The budget cap covers subagents: their spend counts toward the total." 상한에 이르면 새 하위 에이전트 생성이 `Budget limit reached`로 실패(Claude Code v2.1.217 이상). 상한은 응답 도착 뒤 비교해 한 응답만큼 넘을 수 있음
- "your main agent's context grows by a summary, not by the subtask's transcript"
- 확신: 높음

## C6-4. Anthropic, Manage costs effectively(Claude Code Docs)
- URL: https://code.claude.com/docs/en/costs, 확인 2026-10-20
- "token usage is roughly proportional to team size", "approximately 7x more tokens than standard sessions when teammates run in plan mode"
- 에이전트 팀은 실험 기능, 기본 비활성("Agent teams are disabled by default")
- "The subagent's own requests still draw on your usage."
- 확신: 높음

## C6-5. Anthropic, Glossary(Claude Code Docs)
- URL: https://code.claude.com/docs/en/glossary, 확인 2026-10-20
- "Unlike subagents, which run within a single session and report only to the parent, teammates each have their own context window and you can interact with any of them directly."
- 확신: 높음

## 원고 처리
- "주 대화의 컨텍스트가 늘지 않습니다" → 하위 작업의 전체 기록이 아니라 요약만큼 늘어남(C6-3), 하위 에이전트의 요청도 사용량에 포함(C6-4)
- 에이전트 팀은 실험 기능이고 기본으로 꺼져 있다는 구절 추가
- 비용 상한에 이르면 새 하위 에이전트를 만들 수 없는 동작은 v2.1.217 이상(버전 구절)
- "Claude Code는 … 보고했습니다"(Young 글)는 D-108(제품에 관한 Anthropic 엔지니어링 글은 제품명 표기)에 따라 유지
- "큰 업무를 한 번에 맡기는 편이 효율적이라는 의견"은 반대 의견과 답(장 틀) 문장으로 유지, 근거 문장이 아님

## 확인하지 못한 것
- sub-agents 문서 끝부분 약 9.5천 자, How Claude Code works 재확인
