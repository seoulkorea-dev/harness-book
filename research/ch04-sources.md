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

## C4-3. Anthropic, Define success criteria and build evaluations
- URL: https://platform.claude.com/docs/en/test-and-evaluate/develop-tests, 확인 2026-10-20(앞 100,000자만 읽음)
- 게시일: 표기 없음, 작성: Anthropic(Claude Platform Docs)
- 사용한 내용: 성공 기준을 먼저 정의하고 평가를 설계하는 것을 시작 단계로 설명. overview의 "Before prompt engineering" 절이 이 문서를 연결함

## C4-1, C4-2 재확인(2026-10-20 fact-checker, 흐름 재점검 PR #38)
- C4-1(overview): "Before prompt engineering"의 세 전제와 "When to prompt engineer"의 "Not every success criteria or failing eval is best solved by prompt engineering" 원문이 기록과 같음. 4장의 "완료 기준을 먼저 정하는 방식"은 이 개요 문서의 내용(본문에 문서명을 밝힘)
- C4-2(best practices): 여섯 방법의 근거 문장이 기록과 같음. "If you want 'above and beyond' behavior, explicitly request it rather than relying on the model to infer this from vague prompts"(Be clear and direct). "trained for precise instruction following"은 도구 사용 절의 문장(본문에 "도구 사용을 안내하는 절에서"로 맥락을 밝힘)
- 예제 D-012(examples/expense-app/DECISIONS.md): CR 조건부 수용, 인사 시스템 일 1회 갱신 자료 사용, 근거는 운영 위원회 결정과 실시간 연동 규격 없음(본문의 결정 주체를 운영 위원회로 맞춤)
- 미확인 유지: 두 페이지의 게시일과 개정일

## C4-2 재확인(2026-10-21 fact-checker, 예시 제공과 행동 동사)
- S: C4-2 Anthropic, Prompting best practices
- URL: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices, 확인 2026-10-21
- 구 주소 https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/multishot-prompting 은 302로 위 페이지에 넘어감(multishot 전용 페이지는 현재 별도로 열리지 않음)
- 게시일: 표기 없음, 작성: Anthropic(Claude Platform Docs)
- 사용한 내용:
  - "Use examples effectively" 절: "Examples are one of the most reliable ways to steer Claude's output format, tone, and structure." Relevant/Diverse/Structured 세 조건. Tip 블록 "Include 3–5 examples for best results."(예시를 쓸 때의 팁이며 모든 요청의 필수가 아님)
  - "Control the format of responses" 절: "Tell Claude what to do instead of what not to do"
  - "Tool use > Tool usage" 절: "Claude's latest models are trained for precise instruction following… If you say 'can you suggest some changes,' Claude will sometimes provide suggestions rather than implementing them, even if making changes might be what you intended."
- 판정: 4장 30, 32, 33행 일치. 30행은 3~5개가 예시를 쓸 때의 팁임을 밝히는 범위 보강을 권장(이슈 #48 항목 6)
- 미확인 유지: 게시일과 개정일. 대상 모델 목록은 페이지 도입부에서 바뀔 수 있음

## C4-2 재확인(2026-10-22 fact-checker, 외부 검수 브랜치 ch04-external-review)
- S: C4-2 Anthropic, Prompting best practices
- URL: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices, 확인 2026-10-22
- 게시일: 표기 없음, 작성: Anthropic(Claude Platform Docs)
- 사용한 내용:
  - "Use examples effectively": 첫 문장 "one of the most reliable ways to steer Claude's output format, tone, and structure". 조건 Relevant("Mirror your actual use case closely"), Diverse("Cover edge cases and vary enough…"), Structured. 3–5개는 Tip 블록("Include 3–5 examples for best results.")
  - "Control the format of responses": 첫 항목 "Tell Claude what to do instead of what not to do"
  - "Tool usage": "…can you suggest some changes… sometimes provide suggestions rather than implementing them"
- 내부 대조: ch02 표 2-3, 2-4(되돌리기 어려운 규칙은 권한 규칙으로 강제), ch02 tool-scope 절(모델은 요청만, 실행은 하네스. Agent SDK 문서 인용), ch02#instruct-enforce와 ch02#tool-scope 앵커 존재 확인
- 판정: 4장 31행은 형식과 어조만 쓰고 구조를 뺐고(표 4-3과 불일치), 조건 목록과 Tip을 한 문장으로 합침(권장). 33, 34행과 확인 방법 절 끝 문장은 일치
- 미확인 유지: 두 페이지의 게시일과 개정일. git diff는 실행하지 못해 지정한 여섯 곳만 대조

## C4-1, C4-2 재확인(2026-10-22 작성 에이전트, 3단계 4장 정비, 이슈 #66)
- 자료 키: prompt-overview(C4-1), prompting-best-practices(C4-2)를 research/bibliography.json에 추가(옛 표기 "Anthropic, 2026"은 두 문서를 한 항목에 묶었으므로 문서 하나에 키 하나로 나눔, 기준서 8절)
- C4-1 overview, 확인 2026-10-22: "This guide assumes that you have: 1. A clear definition of the success criteria for your use case 2. Some ways to empirically test against those criteria 3. A first draft prompt you want to improve". "Not every success criterion or failing eval is best solved by prompt engineering. For example, you can sometimes improve latency and cost more easily by choosing a different model."
  - 원고 처리: 성공 기준은 사용 사례 전체를 평가로 시험하는 기준이므로, 4장은 "이 책은 같은 순서를 요청 한 건에 적용"으로 범위를 밝힘(실무자, 편집자 1차 R13 지적). 세 문제(자료의 양과 선별, 반복 작업의 일관성, 결과 검증)는 이 책의 정리이고 원문 예는 지연 시간과 비용임을 본문에 밝힘
- C4-2 best practices, 확인 2026-10-22(현행 문구)
  - Be clear and direct: "If you want Claude to do more than the task strictly requires, explicitly request it rather than relying on the model to infer this from vague prompts." 이전 기록의 "above and beyond" 문구는 현행 페이지에 없음. 원고는 "과제가 요구하는 것보다 더 많은 일을 원하면"으로 옮김
  - 같은 절 목록: "Be specific about the output format and constraints you want." "Provide instructions as sequential steps using numbered lists or bullet points when the order or completeness of steps matters."
  - Add context to improve performance: "Providing context or motivation behind your instructions … can give Claude more information about your goals and help it deliver more targeted responses."
  - Use examples effectively: "Examples are one of the most reliable ways to steer Claude's output format, tone, and structure." Relevant, Diverse, Structured. Tip "Include 3–5 examples for best results."
  - Structure prompts with XML tags: "XML tags help Claude parse complex prompts unambiguously, especially when your prompt mixes instructions, context, examples, and variable inputs."
  - Control the format of responses: "Tell Claude what to do instead of what not to do", 예 "Do not use markdown in your response" → "Your response should be composed of smoothly flowing prose paragraphs."
  - Tool usage: "Claude's latest models are trained for precise instruction following … If you say "can you suggest some changes," Claude will sometimes provide suggestions rather than implementing them, even if making changes might be what you intended."
  - 원고 처리: "도구 사용 절"과 "명확하고 직접적인 지시 절"을 나누어 씀(1차 실무자, 편집자 지적)
- 예제 사실(R7): 요청문의 EXP-105, EXP-109, "통합 테스트 시작 예정일 2026-10-19"는 docs/example-facts.md와 examples/expense-app/에 없어 뺌. 운영 위원회 날짜는 D-012(2026-10-12, examples/expense-app/DECISIONS.md), 요청 부서, 요청일, 사유는 docs/CR.md와 같음. "정산 요청 화면(등록, 목록)에는 프로젝트 코드 항목이 없음"은 docs/CR.md 수용 기준 1, 3과 example-facts의 구현 전 상태(수용 시험 1, 2, 3 실패)에 따름
- 미확인 유지: 두 페이지의 게시일과 개정일
