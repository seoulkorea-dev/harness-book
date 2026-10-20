# Chapter 4 개정 출처(2026-10-20, researcher 조사, 메인 세션 저장)

docs.claude.com 주소는 platform.claude.com으로 넘어갑니다(현행 주소는 아래). 게시일 표기가 없어 확인일만 적습니다. 원문은 영어, 인용은 짧게.

## C4-1. Anthropic, Prompt engineering overview
- URL: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview, 확인 2026-10-20
- "Before prompt engineering": 이 안내는 (1) "A clear definition of the success criteria for your use case", (2) "Some ways to empirically test against those criteria", (3) 첫 초안을 갖췄다고 전제하고, 없으면 "spend time establishing that first"
- "When to prompt engineer": "Not every success criteria or failing eval is best solved by prompt engineering. For example, you can sometimes improve latency and cost more easily by selecting a different model."
- 원고 판정: 성공 기준과 시험 방법을 먼저(일치), 속도와 비용은 모델 교체(일치, "sometimes")
- 확신: 높음

## C4-2. Anthropic, Prompting best practices
- URL: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices, 확인 2026-10-20
- 구체적 지시: "Be specific about the desired output format and constraints." "Provide instructions as sequential steps using numbered lists or bullet points when the order or completeness of steps matters."
- 이유 제공: "Providing context or motivation behind your instructions … can help Claude better understand your goals and deliver more targeted responses."
- 예시 제공: "Examples are one of the most reliable ways to steer Claude's output format, tone, and structure." Relevant, Diverse, Structured. "Include 3–5 examples for best results."
- 구획 구분: "XML tags help Claude parse complex prompts unambiguously, especially when your prompt mixes instructions, context, examples, and variable inputs."
- 할 일로 지시: "Tell Claude what to do instead of what not to do"(응답 형식 제어 절)
- 행동 동사: "If you say 'can you suggest some changes,' Claude will sometimes provide suggestions rather than implementing them"(도구 사용 절)
- 최신 모델: "Claude's latest models are trained for precise instruction following"(도구 사용 절)
- "Be clear and direct": 기대 이상의 결과를 원하면 명시적으로 요청하고 모호한 프롬프트에서 추론하게 두지 말라는 취지(원고의 "요청에 없는 조건은 모델이 대신 채워 주기를 기대할 수 없음"의 가까운 근거)
- 확신: 높음

## 근거가 부족한 곳(원고 처리)
- "지시를 정확히 따르는 모델일수록 요청에 없는 조건은 결과에도 반영되지 않는다"는 원문 문장이 아니라 추론. "Be clear and direct"의 취지를 근거로 표현을 고침
- "자료 부족, 반복 작업의 일관성, 결과 검증은 프롬프트만으로 해결되지 않는다"는 이 책의 정리로 밝힘(원문은 속도와 비용 예만)

## 확인하지 못한 것
- 두 페이지의 게시일, 개정일
- "trained for precise instruction following"과 같은 취지의 문장이 모델별 안내 절에도 있는지
