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

## 2026-10-20 fact-checker 재확인(PR #30)
### S-C6-6. Anthropic, Create custom subagents, 포크 절(Claude Code Docs)
- URL: https://code.claude.com/docs/en/sub-agents, 확인 2026-10-20(C6-2의 미확인 끝부분 약 9.5천 자 포함해 전부 읽음)
- "A fork is a subagent that inherits the entire conversation so far instead of starting fresh." 비포크 하위 에이전트는 "Fresh context with the prompt you pass". 포크도 자신의 도구 호출은 주 대화에 남기지 않고 최종 결과만 돌려줌. 포크 모드는 v2.1.302부터 기본 켜짐, 대화형 터미널은 v2.1.232부터. Claude가 스스로 포크를 시작할 수 있음. "Non-fork subagent"는 별도 프롬프트 캐시
- 사용: 본문 "일반 하위 에이전트" 한정 근거, 그림 6-2와 표 6-3의 "주 대화를 보지 않음" 한정 필요 여부
- 확신: 높음(문서 내용), 책에 반영할 범위는 작성 쪽 결정

### S-C6-7. Anthropic, How the agent loop works, 예산 여유(Agent SDK)
- URL: https://code.claude.com/docs/en/agent-sdk/agent-loop, "Budget headroom", 확인 2026-10-20
- 상한은 모델 응답 도착 뒤 비교하므로 상한에 이른 응답까지 완료되고, 실행 중이던 하위 에이전트의 지출만큼 더 넘을 수 있음. 상한 도달 시 실행 중인 백그라운드 하위 에이전트도 중단(v2.1.217 이상)
- 사용: 버전 주석 보강 여부 판단(선택)

### S-C6-8. Young(2025) 인용 주체 확인
- URL: https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents, 확인 2026-10-20
- 저자 Justin Young, 2025-11-26. 실험 대상은 Claude Agent SDK 위의 Claude. "Claude Code"는 감사의 말("code RL & Claude Code teams")에만 나옴. 본문 "Claude Code는 … 보고했습니다"의 근거 문장은 글에 없음 → AUTHOR_QUEUE Q-039와 같은 유형(D-108 적용 결과 유지, 작가 결정 대기)
- 원문 일치 확인: 두 실패, over 200 features와 초기 "failing", 한 번에 한 기능, incremental approach critical, JSON이 Markdown보다 덮어쓰기 적음, passes 필드만 수정

### S-C6-9. 예제 파일 대조(내부 기록)
- examples/expense-app/reference/tasks.example.json = 표 6-4와 본문 JSON(작업 2, 3)과 글자 일치, 확인 2026-10-20
- examples/expense-app/RUNLOG.md(2026-10-16): tests 3건 실패 0건, acceptance 5건 실패 3건(test_1, 2, 3). 넷째·다섯째 통과는 이 목록에서 도출. 실행은 이번에 하지 못함
