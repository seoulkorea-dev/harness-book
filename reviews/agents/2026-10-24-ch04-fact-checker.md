# 4장 사실 점검(fact-checker, 2026-10-24, 커밋 76117dd)

결론: 필수 0, 권고 10, 참고 3 (확인한 사실 문장 28개). 인용 7개 문서(5개 문서)는 모두 원문의 범위와 강도 안에 있습니다. 불일치와 낡음은 없습니다. 고칠 곳은 주체 표기, 범위 표기, 인용 위치, 예제 한 문장입니다. 점검 기준은 2026-10-24 확인한 현행 페이지 원문입니다(브랜치 ch04-playbook, git은 읽기만 하고 원고는 고치지 않았습니다). 실행할 명령은 없습니다.

## 1. 일치 판정 (인용과 절 위치)
| 원고 위치 | 원문 확인 (1차 출처, 절) | 판정 |
|---|---|---|
| 네 요소 절, "Anthropic의 프롬프트 엔지니어링 개요 문서는 …먼저 갖추라고" | Prompt engineering overview(https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview) "Before prompt engineering": 이 안내는 "A clear definition of the success criteria", "Some ways to empirically test against those criteria", 첫 초안을 전제하고 "If not, spend time establishing that first" | 일치 |
| 같은 절, "도구 사용 절은 최신 모델이 지시를 정밀하게 따르도록 훈련" | Prompting best practices(https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) Tool use > "Tool usage": "Claude's latest models are trained for precise instruction following" | 절 위치와 내용 일치 |
| 같은 절, "명확하고 직접적인 지시 절 …명시적으로 요청" | General principles > "Be clear and direct": "If you want Claude to do more than the task strictly requires, explicitly request it rather than relying on the model to infer this from vague prompts" | 일치 |
| 구체적 지시 | 같은 절 목록 "Be specific about the output format and constraints you want", "sequential steps using numbered lists or bullet points when the order or completeness of steps matters" | 일치 |
| 이유 제공 | "Add context to improve performance": "context or motivation behind your instructions … can give Claude more information about your goals and help it deliver more targeted responses" | 일치 |
| 예시 제공 | "Use examples effectively": "one of the most reliable ways to steer Claude's output format, tone, and structure". Relevant("Mirror your actual use case closely"), Diverse("vary enough that Claude doesn't pick up unintended patterns"). Tip "Include 3–5 examples for best results" | 일치. 3~5개가 Tip이라는 범위 문장도 원문과 맞음 |
| 구획 구분 | "Structure prompts with XML tags": "help Claude parse complex prompts unambiguously, especially when … mixes instructions, context, examples, and variable inputs". 같은 절 "Use consistent, descriptive tag names" | 일치 |
| 할 일로 지시 | "Control the format of responses" 첫 항목: "Do not use markdown in your response" 대신 "Your response should be composed of smoothly flowing prose paragraphs." | 일치 |
| 행동 동사 | "Tool usage": "can you suggest some changes" → "sometimes provide suggestions rather than implementing them". 처방 예 "Change this function to improve its performance."(원고의 "수정해 줘"와 같은 방향) | 일치 |
| 한계 절, 속도와 비용 | overview "When to prompt engineer": "Not every success criterion or failing eval is best solved by prompt engineering. For example, you can sometimes improve latency and cost more easily by choosing a different model." | 일치("sometimes"를 "때가 있다"로 옮김) |
| 토큰 증가와 기억력 | Anthropic Engineering, "Effective context engineering for AI agents"(https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents, 2025-09-29, Prithvi Rajasekaran 외). 토큰이 늘수록 정보를 정확히 기억해 내는 능력이 떨어지고(context rot), "this characteristic emerges across all models", 정도는 모델마다 다름 | 방향 일치. 아래 4번에서 보강 |
| 확인 방법 절, 같은 요청도 결과가 달라질 수 있음 | Glossary(https://platform.claude.com/docs/en/about-claude/glossary) Temperature: "Even with temperature set to 0, … identical inputs might produce different outputs across API calls" | 방향 일치. 범위는 API 호출. 아래 6번에서 보강 |
| 서지 키 | bibliography.json에 prompt-overview, prompting-best-practices, context-engineering(date 2025.9.29), platform-glossary 모두 있고 주소가 위 주소와 같음 | 일치 |

## 2. 예제 사실 대조 (R7)
- examples/expense-app/docs/CR.md와 docs/example-facts.md: 재무팀, 요청일 2026-10-05, 사유 "프로젝트별 경비 집계를 월말 결산에 반영하기 위함"이 원고와 같습니다. 원고의 "반영하기 위함"은 CR.md 문구와 같습니다(example-facts는 "반영").
- examples/expense-app/DECISIONS.md D-012: 2026-10-12, "CR 조건부 수용. 프로젝트 코드는 인사 시스템 일 1회 갱신 자료(data/projects.csv) 사용", 이유 "운영 위원회 결정, 실시간 연동 규격 없음". 원고와 일치합니다.
- 요일 검산(python): 2026-10-05는 월요일, 2026-10-12는 월요일입니다(오늘 2026-10-24는 토요일). 7일 간격이라 무리가 없습니다.
- 참고: 요청문의 docs/CR.md는 저장소 루트에 없고 examples/expense-app/docs/CR.md에 있습니다(example-facts도 같은 경로 설명). 앵커 ch08#decisions, ch01#loop, ch01#prompt-context, ch02#components, ch02#tool-scope, ch02#instruct-enforce, ch03#example, ch05#rule-doc, ch07#criteria는 모두 src에 존재합니다.
- 원고만의 서술 중 원본에 없는 것은 "이 영향 검토를 거쳐"(아래 8번)와 "프로젝트 코드는 인사 시스템에서 관리"(D-012가 인사 시스템 자료를 쓰기로 한 결정과 모순되지 않는 설정이라 유지)입니다.

## 3. 보고 표
| 번호 | 등급 | 위치 | 원고 문장 | 확인 결과와 1차 출처 | 고칠 문안 |
|---|---|---|---|---|---|
| 1 | 권고 | 네 요소 절 세 번째 문단 | "이 안내는 모델을 사용하는 응용 프로그램을 여러 시험 입력으로 반복해 평가하는 경우를 다룹니다." | 이 내용은 인용한 overview가 아니라 overview가 연결한 "Define success criteria and build evaluations"(https://platform.claude.com/docs/en/test-and-evaluate/develop-tests)에 있음. 원문: "Building a successful LLM-based application starts with clearly defining your success criteria and then designing evaluations", 예시는 수십~수천 건의 시험 사례. overview에는 "응용 프로그램"과 "여러 시험 입력"이 없음. 인용 키가 문장 근거와 어긋남(R11, R4) | 원문 "이 안내는 모델을 사용하는 응용 프로그램을 여러 시험 입력으로 반복해 평가하는 경우를 다룹니다." → "개요 문서가 연결한 성공 기준 문서는 모델을 사용하는 응용 프로그램을 여러 시험 입력으로 평가하는 경우를 다룹니다<sup class="cite" data-ref="develop-tests"></sup>." (아래 bibliography 키 추가) |
| 2 | 권고 | 같은 절 네 번째 문단 | "두 안내를 함께 놓으면, 모델이 적힌 지시를 정밀하게 따를수록 요청에 적지 않은 목적과 완료 기준은 결과에 반영되기 어렵습니다." | 두 원문 모두 이 결론을 말하지 않음. 도구 사용 절 문장은 도구 호출 맥락, "Be clear and direct"는 요구 이상의 일을 원할 때의 안내. 목적과 완료 기준을 "과제가 요구하는 것 이상"으로 보는 것은 이 책의 해석(research C4-2 "근거가 부족한 곳"에도 추론으로 기록됨). 주장 범위(R13) | 원문 "두 안내를 함께 놓으면, 모델이 적힌 지시를 정밀하게 따를수록 요청에 적지 않은 목적과 완료 기준은 결과에 반영되기 어렵습니다." → "이 책은 두 안내를 함께 놓고 이렇게 해석합니다. 모델이 적힌 지시를 정밀하게 따른다면, 요청에 적지 않은 목적과 완료 기준은 결과에 반영되지 않을 수 있습니다." |
| 3 | 권고 | 한계 절 첫 문단 | "성공 기준에 못 미치는 결과 가운데 일부는 프롬프트 엔지니어링이 아닌 다른 방법으로 더 쉽게 개선된다고 설명합니다." | 원문의 일반 문장은 "Not every success criterion or failing eval is best solved by prompt engineering"(프롬프트가 최선이 아닐 수 있다). "more easily"는 지연 시간과 비용 예에만 붙음. "더 쉽게"를 일반 문장으로 넓힘(R13) | 원문 "성공 기준에 못 미치는 결과 가운데 일부는 프롬프트 엔지니어링이 아닌 다른 방법으로 더 쉽게 개선된다고 설명합니다." → "모든 성공 기준이나 실패한 평가가 프롬프트 엔지니어링으로 풀기에 가장 좋은 것은 아니라고 설명합니다." (뒤 문장 "예를 들어 지연 시간과 비용은 …"은 유지) |
| 4 | 권고 | 한계 절 "자료의 양과 선별" 항목 | "컨텍스트의 토큰이 늘수록 모델이 그 정보를 정확히 기억해 내는 능력은 떨어집니다" | 원문(Anthropic Engineering 글)은 모든 모델에서 나타나고 정도는 모델마다 다르다고 함. 원고는 발표 주체가 없고 정도 차이가 빠져 있음(R3, R1) | 원문 "컨텍스트의 토큰이 늘수록 모델이 그 정보를 정확히 기억해 내는 능력은 떨어집니다" → "Anthropic Engineering의 컨텍스트 엔지니어링 글은 컨텍스트의 토큰이 늘수록 모델이 그 정보를 정확히 기억해 내는 능력이 떨어지고, 이 특성이 모든 모델에서 나타나며 정도는 모델마다 다르다고 설명합니다" |
| 5 | 권고 | 같은 항목, 토큰과 컨텍스트 윈도 정의 | "컨텍스트 윈도(Context Window)는 모델이 한 번에 처리할 수 있는 토큰의 범위입니다." | 정의 문장에 각주 없음(R8은 기술 용어를 1차 출처로 확인). Glossary: Context window는 "the amount of text a language model can look back on and reference when generating new text"(작업 기억), Tokens는 "smallest individual units of a language model"(단어, 하위 단어, 문자, 바이트). "한 번에 처리할 수 있는 토큰의 범위"는 원문과 약간 다름 | 원문 "컨텍스트 윈도(Context Window)는 모델이 한 번에 처리할 수 있는 토큰의 범위입니다." → "컨텍스트 윈도(Context Window)는 모델이 텍스트를 생성할 때 되돌아보고 참조할 수 있는 텍스트의 양으로, 토큰 단위로 셉니다<sup class="cite" data-ref="platform-glossary"></sup>." (키 platform-glossary는 이미 있음) |
| 6 | 권고 | 확인 방법 절 첫 문단 끝 | "같은 요청도 보낼 때마다 결과가 달라질 수 있으므로<sup …platform-glossary>, 한 번의 결과만으로" | 용어집 근거는 API 호출 맥락("identical inputs might produce different outputs across API calls", temperature 0에서도). 채팅까지 넓힌 것은 이 책의 확장이고 주체가 없음. 위첨자가 문장 가운데 있어 플레이북 7.4(문장 끝, 마침표 앞)와 다름 | 원문 `같은 요청도 보낼 때마다 결과가 달라질 수 있으므로<sup class="cite" data-ref="platform-glossary"></sup>, 한 번의 결과만으로` → `Anthropic의 용어집은 같은 입력도 API 호출마다 다른 출력을 낼 수 있다고 설명합니다<sup class="cite" data-ref="platform-glossary"></sup>. 채팅에서도 같은 요청의 결과가 달라질 수 있으므로 한 번의 결과만으로` |
| 7 | 권고 | 표 4-3, 예시 제공 행 기능적 제약 | "예시끼리 비슷하면 의도하지 않은 공통점까지 따라 함" | 원문은 "vary enough that Claude doesn't pick up unintended patterns"(확률적). 본문 37행은 "따라 할 수 있기" 인데 표는 단정. 일관성과 R1, 플레이북 7.2 | 원문 `<td>예시끼리 비슷하면 의도하지 않은 공통점까지 따라 함</td>` → `<td>예시끼리 비슷하면 의도하지 않은 공통점까지 따라 할 수 있음</td>` |
| 8 | 권고 | 예제 절 마지막 문단 | "운영 위원회는 이 영향 검토를 거쳐 변경 요청 사항을 조건부 수용하고," | D-012 이유는 "운영 위원회 결정, 실시간 연동 규격 없음"뿐이고 영향 검토 과정은 원본에 없음(R7). 앞 문단의 영향 검토 요청은 이 책이 만든 가상의 요청 | 원문 "운영 위원회는 이 영향 검토를 거쳐 변경 요청 사항을 조건부 수용하고," → "예제에서 운영 위원회는 2026-10-12에 변경 요청 사항을 조건부 수용하고," |
| 9 | 권고 | 도입 단락 | "요청에 적지 않으면 모델은 그 빈자리를 추측으로 채웁니다." | 현행 모델은 모호하면 되묻기도 함(원고 예제 절 "필요한 자료를 되물어야"와 불일치). 그림 4-1의 "누락된 요소는 추측으로 채움", 표 4-2 해당 행도 같은 단정(R1, 일관성) | 원문 "요청에 적지 않으면 모델은 그 빈자리를 추측으로 채웁니다." → "요청에 적지 않으면 모델은 그 빈자리를 추측으로 채우거나 되묻습니다." 그림과 표 4-2 문구도 "추측으로 채우거나 되물음"으로 맞추거나, 그림은 두고 도입만 고칠지는 작가 판단 |
| 10 | 권고 | 방법 절 끝(또는 아래 6여섯 방법 목록 뒤) | (버전 주석 없음) | best practices 페이지는 현재 모델별 안내 페이지(Sonnet 5.5, Opus 5.5 등 "literal instruction following" 등)가 따로 있고 "Claude's latest models"의 대상이 바뀜. 플레이북 7.1은 바뀌는 정보를 확인 시점과 함께 쓰라고 함. 4장에는 aside.version-note가 없음 | 새 주석 문안(형식은 다른 장의 aside.version-note를 따름): "버전 주석 (2026년 10월) 이 절이 인용한 프롬프트 작성 모범 사례 문서는 2026년 10월에 확인한 내용입니다. 이 문서는 모델별 안내 페이지를 따로 두며, 최신 모델의 범위와 권장이 바뀔 수 있으니 사용하는 모델의 안내를 먼저 확인합니다." |
| 11 | 참고 | 방법 절 구획 구분, 표 4-4, 예제 요청문 | "<변경 요청 사항>" 등 한글, 띄어쓰기 있는 태그 | 문서는 "consistent, descriptive tag names"만 권하고 영어 예(<instructions>)만 듦. 한글이나 띄어쓰기가 있는 태그 이름이 같은 효과라는 근거는 찾지 못함(미확인, 찾은 범위: best practices 전문). 문서가 말한 일관성과 설명적 이름은 지킴 | 본문에 "한글 태그 이름은 이 책의 선택"이라고 한 구를 더하거나, 태그 이름의 띄어쓰기를 없애는 것(<변경요청사항>)을 작가가 정하도록 AUTHOR_QUEUE에 질문. 원고 수정 필수 아님 |
| 12 | 참고 | 확인 방법 절 | "예제 절의 두 번째 요청을 생성형 AI 채팅에 직접 보내고" | 실무 주의 누락: 변경 요청 사항과 사내 시스템 정보를 외부 채팅 서비스에 넣기 전에 조직의 정보 반출과 보관 정책을 확인해야 함. 출처 없는 실무 판단이라 원고에 단정으로 넣지 않고 조건부로만 제안 | 필요하면 "소속 조직이 허용한 도구에서" 한 구 추가(작가 판단). 근거 문서는 찾지 않았음 |
| 13 | 참고 | 서지 | prompt-overview, prompting-best-practices 게시일과 개정일 | 두 페이지에 게시일 표기 없음, 이번에도 확인하지 못함(develop-tests도 초반 100,000자까지만 읽음, 날짜 없음). 미확인 유지 | 조치 없음. 열람일은 서지에 쓰지 않는 규칙(7.4) 때문에 research에만 기록 |

## 4. 실무자 관점 (더 단순하게 쓴 곳)
- 위 9번(추측으로 채움 vs 되물음).
- 위 2번(정밀한 지시 따르기를 목적과 완료 기준 누락의 근거로 쓴 것은 해석).
- 위 10번(모델별 안내 페이지가 따로 있는 점).
- 예제 흐름: 요청이 읽기 전용 영향 검토라는 점, 완료 기준 2와 3 사이의 긴장("모든 공수가 확인 필요가 될 수 있음")은 표 4-6의 "예: 결과의 예상 공수"가 이미 인정해 문제 없음.
- 그 밖의 용어와 서술은 입문 독자에게 적절해 지적하지 않습니다.

## 5. research/ch04-sources.md에 덧붙일 기록 문안
```
## C4-1, C4-2, C4-4, C4-5 재확인과 새 출처 C4-6(2026-10-24 fact-checker, ch04-playbook)
- S: C4-1 Anthropic, Prompt engineering overview(자료 키 prompt-overview)
- URL: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview, 확인 2026-10-24
- 게시일: 표기 없음, 작성: Anthropic(Claude Platform Docs)
- 사용한 내용: "Before prompt engineering"의 세 전제와 "If not, spend time establishing that first". "When to prompt engineer"의 "Not every success criterion or failing eval is best solved by prompt engineering. For example, you can sometimes improve latency and cost more easily by choosing a different model." 2026-10-23 기록과 같음. "more easily"는 지연 시간과 비용 예에만 붙음
- S: C4-2 Anthropic, Prompting best practices(자료 키 prompting-best-practices)
- URL: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices, 확인 2026-10-24
- 사용한 내용: Be clear and direct, Add context to improve performance, Use examples effectively(Relevant/Diverse/Structured, Tip 3–5), Structure prompts with XML tags("Use consistent, descriptive tag names"), Control the format of responses, Tool use > Tool usage의 원문이 2026-10-23 기록과 같음. 현행 페이지는 모델별 안내 페이지(Sonnet 5.5, Opus 5.5 등)를 먼저 읽으라고 안내함(도입부 표). 한글 태그 이름에 대한 안내는 찾지 못함(미확인)
- S: C4-4 Anthropic Engineering, Effective context engineering for AI agents(자료 키 context-engineering)
- URL: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents, 확인 2026-10-24
- 게시일: 2025-09-29, 작성: Prithvi Rajasekaran 외
- 사용한 내용: "as the number of tokens in the context window increases, the model's ability to accurately recall information" 감소(context rot). "While some models exhibit more gentle degradation than others, this characteristic emerges across all models."
- S: C4-5 Anthropic, Glossary(자료 키 platform-glossary)
- URL: https://platform.claude.com/docs/en/about-claude/glossary, 확인 2026-10-24
- 사용한 내용: Context window("the amount of text a language model can look back on and reference when generating new text"), Tokens("smallest individual units of a language model"), Temperature 절 "Even with temperature set to 0, the results will not be fully deterministic, and identical inputs might produce different outputs across API calls"(API 호출 맥락)
- S: C4-6 Anthropic, Define success criteria and build evaluations(자료 키 develop-tests)
- URL: https://platform.claude.com/docs/en/test-and-evaluate/develop-tests, 확인 2026-10-24(앞 100,000자만 읽음, 전체 약 153,000자)
- 게시일: 표기 없음, 작성: Anthropic(Claude Platform Docs)
- 사용한 내용: "Building a successful LLM-based application starts with clearly defining your success criteria and then designing evaluations to measure performance against them." 시험 사례를 많이 두는 예(트윗 1,000건 등). 4장 "성공 기준은 응용 프로그램을 여러 시험 입력으로 평가하는 경우"의 근거(overview가 아니라 이 문서)
- 예제 사실(R7) 확인 2026-10-24: examples/expense-app/docs/CR.md(재무팀, 요청일 2026-10-05, 사유), examples/expense-app/DECISIONS.md D-012(2026-10-12, 조건부 수용, 인사 시스템 일 1회 갱신 data/projects.csv, 이유 "운영 위원회 결정, 실시간 연동 규격 없음"), docs/example-facts.md와 일치. python 요일 검산: 2026-10-05 월요일, 2026-10-12 월요일. D-012 원본에 "영향 검토를 거쳐"는 없음
- 미확인 유지: prompt-overview, prompting-best-practices, develop-tests의 게시일과 개정일. 한글, 띄어쓰기 포함 태그 이름의 효과
```

## 6. bibliography.json 새 키
```
"develop-tests": {"type": "web", "author": "Anthropic", "title": "Define success criteria and build evaluations", "venue": "Claude Platform Docs", "url": "https://platform.claude.com/docs/en/test-and-evaluate/develop-tests"}
```
(키가 추가되지 않으면 1번의 고침은 하지 말고, 대신 "개요 문서는 …"의 범위를 "성공 기준과 시험 방법을 먼저 갖추라" 까지만 두고 해당 문장을 지우십시오.)

## 7. 장별 점검 질문 10개 (20.4, 사실 점검 관점의 답)
| 질문 | 답 |
|---|---|
| 1 개념 | 토큰, 컨텍스트 윈도 정의가 용어집과 약간 다르고 각주 없음(5번) |
| 2 분류 | 여섯 방법과 표 4-3, 4-4, 그림 4-2가 같은 여섯 가지. 표 4-3의 단정 하나만 다름(7번) |
| 3 논리 | 두 안내 결합은 책의 해석(2번), 예시 문서 인용은 근거를 뒷받침함 |
| 4 범위 | 원칙, 예제, 제품 사실은 구분됨. 개요 문서의 일반 문장 범위를 넓힌 곳 1(3번) |
| 5 절차 | 요청 한 건의 절차, 확인 방법 표 4-6이 완료 기준 네 개와 출력 형식에 대응함 |
| 6 책임 | 수행은 모델, 판정은 요청하는 사람, 결정은 운영 위원회로 나뉨. 8번의 서술만 근거 없음 |
| 7 검증 | 예제 사실은 원본과 일치(요일 검산 포함). 모델 결과는 일부러 싣지 않음 |
| 8 일관성 | 본문, 표 4-3, 그림 4-1의 "추측" 단정이 본문 76행 "되물어야"와 어긋남(9번) |
| 9 출처 | 인용 7건 모두 현행 원문과 일치. 발표 주체 누락 2곳(4번, 6번), 서지 키 1건 추가 필요(1번), 버전 주석 없음(10번) |
| 10 편집 한계 | 게시일 미확인(13번), 한글 태그 이름(11번), 정보 정책 문구(12번)는 작가 판단 |

필수 0, 권고 10, 참고 3, 확인한 사실 문장 28개

관련 파일(모두 읽기만 함): /home/user/harness-book/src/chapters/ch04.html, /home/user/harness-book/research/ch04-sources.md, /home/user/harness-book/research/bibliography.json, /home/user/harness-book/docs/example-facts.md, /home/user/harness-book/examples/expense-app/docs/CR.md, /home/user/harness-book/examples/expense-app/DECISIONS.md
