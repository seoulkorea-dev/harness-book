# Chapter 4 사실 점검 보고 (fact-checker, 2026-10-24)

범위: src/chapters/ch04.html 전체. 기준: docs/specs/ch04-spec.md, BOOK_SPEC 4, 5, 7절, research/ch04-sources.md, research/bibliography.json, docs/example-facts.md, examples/expense-app/. 원고는 고치지 않음. 이 장에는 실행할 명령이 없어(요청문은 모델에 보내는 글) R8은 1차 문서 확인으로 대신함. 참고로 tools/check_all.py는 통과(빌드, 금칙어, 번호, 구조, 문체, 그림 안 이름, 검수 규칙)하고, tools/check_tasks.py는 작업 2, 3 "공백 2건"(example-facts의 "정비 예정" 항목과 같음, 4장과 무관)을 출력함.

## 요약
필수 2, 권고 3, 참고 5 (확인한 사실 문장 31개)

## 확인 결과 표
| # | 위치 | 문장 | 확인 결과와 근거 | 등급 | 고친 문안 |
|---|---|---|---|---|---|
| 1 | limits, 자료의 양과 선별 | "Claude Code의 엔지니어링 글은 컨텍스트의 토큰이 늘수록 모델이 그 정보를 정확히 기억해 내는 능력이 떨어진다고 설명합니다[context-engineering]" | 내용은 일치함. 원문 "as the window grows ... the model's ability to accurately recall information from that context decreases"(글 본문 context rot 설명, 2026-10-24 재확인). 발표 주체는 불일치함. 글은 anthropic.com/engineering의 Anthropic Engineering 글(2025-09-29, Anthropic Applied AI 팀의 Prithvi Rajasekaran, Ethan Dixon, Carly Ryan, Jeremy Hadfield)이며 Claude Code 제품의 글이 아님. 글의 주제는 에이전트 일반임. BOOK_SPEC 7절은 제품 출시 전 글과 모델, API 전반의 문서에는 회사 이름을 쓰도록 하며, 같은 글을 ch02(38행), ch05(34, 54행)는 "Anthropic의 컨텍스트 엔지니어링 글"로 씀. R3 위반 | 필수 | "Anthropic의 컨텍스트 엔지니어링 글은 컨텍스트의 토큰이 늘수록 …" |
| 2 | limits, 결과 검증 | 링크 "Chapter 3의 예제: 변경 요청 사항의 에이전트 명세서 작성" (ch03.html#example) | 현재 저장소의 ch03 #example 절 제목은 "기능 추가 에이전트: CR 구현"이며 링크 문구와 다름. ch04 명세(36행)는 "3장 정리 뒤 제목"이라 적었으므로 ch03 정비 PR이 제목을 바꾸기 전까지는 불일치 상태임. 도착 절 내용은 일치함(수용 기준 정의, 검사 스크립트 check.py로 완료 판정, 사람이 정한 완료 조건). 본문 설명 "수용이 정해진 뒤 이 변경을 구현하는 단계"도 ch03 절 내용과 맞음 | 필수 | ch03 제목을 바꾸는 PR과 같은 시점에 반영하거나, 먼저 병합하면 문구를 현재 제목에 맞춤. 3장 정비가 늦어지면 AUTHOR_QUEUE에 기록 |
| 3 | techniques, 할 일로 지시 | "권한 규칙도 같은 동작을 다르게 표기한 명령처럼 규칙과 일치하지 않는 경로는 막지 못합니다[permissions]" | 근거 있음. Configure permissions의 "What a Bash rule doesn't match" 절: Bash 규칙은 명령 문자열을 대조하며, 같은 프로그램을 다른 형태로 부르면 막지 못함. 예: 규칙 Bash(git push *)는 `git -C . push origin main`을 막지 못함. 다만 문서가 보이는 범위는 Bash 규칙이고, 같은 문서는 Edit 규칙은 편집용 내장 도구 전체에 적용되고 Read 규칙은 Grep, Glob 등에 최선을 다해 적용(best-effort)된다고 구분함. "권한 규칙도 … 막지 못합니다"는 범위가 넓어 읽힘(R13). "경로"는 파일 경로로도 읽힘. 같은 절의 앞 문장("원본 자료 수정 … 권한 규칙으로 강제")과 이어 읽으면 data/ 수정 금지 규칙까지 새는 것처럼 읽힐 수 있음 | 권고 | "Claude Code 문서에 따르면 Bash 규칙은 명령 문자열이 일치할 때만 적용되어, git -C . push처럼 같은 동작을 다르게 적은 명령은 막지 못합니다." (ch02 69행과 같은 근거, 범위를 Bash로 한정) |
| 4 | techniques, 할 일로 지시 | "권한 규칙은 도구 사용을 허용, 확인 요청, 금지하는 규칙이며, 모델의 판단과 관계없이 제품이 적용합니다" | 일치. Manage permissions 절: Allow, Ask, Deny 규칙 정의. 같은 절 NOTE "Permission rules are enforced by Claude Code, not by the model" 및 BOOK_SPEC 4절(강제 정의)과 맞음. 다만 이 정의 문장에는 각주가 없고 다음 문장 끝에만 [permissions]가 있음(R11 "각주 하나에 근거 하나") | 참고 | 정의 문장 끝에 [permissions] 추가 또는 현행 유지(다음 문장 각주가 같은 문서) |
| 5 | techniques, 행동 동사 | "권한 모드는 도구 호출을 승인하는 방식을 정하는 설정입니다" | 일치. Permission modes 절 "Claude Code supports several permission modes that control how it approves tool calls". BOOK_SPEC 5절 용어와 같음. 정의 문장에 각주 없음. 링크 "Chapter 2의 도구 사용 범위와 제약"은 ch02 #tool-scope 제목과 같고, 그 절 42행이 권한 모드를 다루므로 도착 내용도 맞음. 모드 값과 기본값은 쓰지 않아 기본값 오류 위험 없음(재발 주의 항목 해당 없음) | 참고 | 현행 유지 |
| 6 | techniques, 할 일로 지시 | 링크 "Chapter 2의 지시 기반 규칙과 강제 적용" 및 "권한 규칙의 적용 범위는 … 다룹니다" | 제목 일치(ch02 #instruct-enforce). 도착 절 69행이 적용 범위(Python 스크립트, Bash 문자열 일치, 훅 한계, 샌드박스)를 다루므로 내용도 맞음 | 일치 | 없음 |
| 7 | intro, 문단 2 | "프롬프트 엔지니어링(Prompt Engineering)은 원하는 결과를 얻도록 지시문을 작성하고 구성하는 방법입니다[context-engineering]" | 일치. 원문 "Prompt engineering refers to methods for writing and organizing LLM instructions for optimal outcomes." 인용이 정의를 뒷받침함. 발표 주체는 문장에 없으나 각주가 Anthropic 글을 가리킴. ch01 137행과 같은 정의 | 일치 | 없음 |
| 8 | limits, 자료의 양과 선별 | "컨텍스트 엔지니어링은 모델이 응답을 생성하는 동안 필요한 정보를 선별하고 유지하는 전략입니다" | 정의는 일치. 원문 "Context engineering refers to the set of strategies for curating and maintaining the optimal set of tokens (information) during LLM inference". 그러나 이 정의 문장과 바로 앞 "어떤 정보를 언제 넘길지 정하는 일은 컨텍스트 엔지니어링의 몫입니다"에 각주가 없음(앞 각주는 context rot 문장에 붙음). "언제 넘길지"는 글의 정의 문장에 없는 이 책의 풀이임(R4, R11) | 권고 | 정의 문장 끝에 [context-engineering] 추가, "어떤 정보를 언제 넘길지 정하는 일" 문장은 이 책의 정리임을 밝히거나 "무엇을 포함할지 정하는 일"로 줄임 |
| 9 | limits, 자료의 양과 선별 | "토큰은 모델이 텍스트를 나누어 처리하는 단위이고, 컨텍스트 윈도는 모델이 한 번에 처리할 수 있는 토큰의 범위입니다" | BOOK_SPEC 5절 용어표와 같은 이 책의 정의. 1차 출처 대조: Anthropic Glossary는 Tokens를 "the smallest individual units of a language model", Context window를 "the amount of text a language model can look back on and reference when generating new text"로 설명함. 취지는 맞으나 문구가 달라 각주가 없는 정의임. 같은 정의가 ch05 6행에도 있음 | 참고 | 필요하면 [platform-glossary] 각주 추가(이미 bibliography에 있음). 작가 확정 용어이므로 정의 문구는 유지 |
| 10 | check | "같은 요청도 보낼 때마다 결과가 달라질 수 있습니다[platform-glossary]" | 근거 일치. Glossary Temperature 절 "Even with temperature set to 0, the results will not be fully deterministic, and identical inputs might produce different outputs across API calls". 단 원문은 API 호출 기준이고, 본문은 생성형 AI 채팅에 요청문을 보내게 함(119행). 채팅 제품에서도 같은 성질이 있다는 문장은 이 문서에 없음. 원고 문장은 "달라질 수 있습니다"로 근거 범위 안이지만 "요청"의 범위를 API 외로 넓혀 읽을 여지 있음(R13) | 권고 | "Anthropic의 용어집은 모델 API에서 같은 입력도 호출마다 다른 출력이 나올 수 있다고 설명합니다[platform-glossary]. 채팅에서도 같은 요청의 결과가 달라질 수 있으므로 …"는 근거가 없으니 쓰지 말고, "모델은 같은 입력에도 호출마다 다른 출력을 낼 수 있습니다[platform-glossary]"로 주어를 모델로 |
| 11 | elements | "Anthropic의 프롬프트 엔지니어링 개요 문서는 프롬프트를 다듬기 전에 사용 사례의 성공 기준과 그 기준으로 결과를 시험하는 방법을 먼저 갖추라고 안내합니다[prompt-overview]" | 일치. Overview "Before prompt engineering": 성공 기준 정의, 경험적 시험 방법, 첫 초안 프롬프트를 갖췄다고 전제하고 "If not, spend time establishing that first". 후속 문장(평가 시험 입력 반복, 하나의 요청에서는 완료 기준에 해당)은 이 책의 범위 한정을 밝힌 것 | 일치 | 없음 |
| 12 | elements | "최신 모델이 지시를 정밀하게 따르도록 훈련되었다고 설명합니다"(도구 사용 절), "과제가 엄밀히 요구하는 범위를 넘는 결과를 원하면 … 명시적으로 요청하라"(명확하고 직접적인 지시 절)[prompting-best-practices] | 일치. Tool usage 절 "Claude's latest models are trained for precise instruction following". Be clear and direct 절 "If you want Claude to do more than the task strictly requires, explicitly request it rather than relying on the model to infer this from vague prompts". 절 이름 구분 정확. "두 안내를 함께 읽으면 … 볼 수 있습니다"는 이 책의 추론으로 표시되어 있음 | 일치 | 없음 |
| 13 | techniques | 구체적 지시(출력 형식과 제약, 번호 목록이나 글머리표) | 일치. Be clear and direct 절 목록 "Be specific about the output format and constraints you want", "sequential steps using numbered lists or bullet points when the order or completeness of steps matters" | 일치 | 없음 |
| 14 | techniques | 이유 제공 | 일치. Add context to improve performance 절 "context or motivation behind your instructions ... can give Claude more information about your goals and help it deliver more targeted responses" | 일치 | 없음 |
| 15 | techniques | 예시 제공(형식, 어조, 구조, 실제 업무와 가까운 것, 서로 다르게, 3~5개) | 일치. Use examples effectively 절 첫 문장, Relevant(Mirror your actual use case), Diverse(Cover edge cases and vary enough that Claude doesn't pick up unintended patterns), Tip "Include 3–5 examples for best results". 본문이 3~5개를 예시를 쓸 때의 기준이라고 한정한 것도 맞음 | 일치 | 없음 |
| 16 | techniques | 구획 구분("XML 태그라고 부르고 … 모호함 없이 읽게 돕는다") | 일치. Structure prompts with XML tags 절 "XML tags help Claude parse complex prompts unambiguously, especially when your prompt mixes instructions, context, examples, and variable inputs". 한글 태그 이름 사용은 이 책의 선택으로 밝힘(문서 예는 영어 태그) | 일치 | 없음 |
| 17 | techniques | 할 일로 지시("마크다운을 사용하지 마" 대신 "부드럽게 이어지는 문단으로 작성해") | 일치. Control the format of responses 절 첫 항목과 예 | 일치 | 없음 |
| 18 | techniques | 행동 동사("변경 사항을 제안해 줄 수 있어?" → 제안만 할 때가 있음) | 일치. Tool usage 절 "If you say 'can you suggest some changes,' Claude will sometimes provide suggestions rather than implementing them, even if making changes might be what you intended" | 일치 | 없음 |
| 19 | limits, 도입 | "개요 문서도 … 다른 방법으로 더 쉽게 개선된다 … 지연 시간과 비용은 다른 모델을 선택하면 더 쉽게 개선될 때가 있다[prompt-overview]" | 일치. When to prompt engineer 절 "Not every success criterion or failing eval is best solved by prompt engineering. For example, you can sometimes improve latency and cost more easily by choosing a different model". 세 문제(자료의 양과 선별 등)는 "같은 관점에서 … 나눕니다"로 이 책의 정리임이 드러남 | 일치 | 없음 |
| 20 | intro, elements | 에이전트 정의(12행) | BOOK_SPEC 4절 정의("인공지능 모델이 루프 안에서 도구를 사용해 …, 모델과 하네스로 이루어짐")에서 "루프 안에서"와 "모델과 하네스로 이루어짐"이 빠진 한 줄 요약. 명세(55행)가 "한 줄로 되살림"을 허용하므로 사실 오류는 아님. 다만 "모델이 … 시스템"으로 읽히면 모델이 시스템 전체인 것처럼 읽힐 수 있음(BOOK_SPEC 4절 "모델이 하네스 안에 있는 것처럼 읽히는 문장" 주의와는 다른 방향의 단순화) | 참고 | 핵심 정의는 작가 확정. 바꾸지 않고 AUTHOR_QUEUE에 "한 줄 되살림에 '루프 안에서' 추가 여부" 질문으로만 기록 가능 |
| 21 | example | 요청문의 변경 요청 사항: 내용, 재무팀, 요청일 2026-10-05, 사유 | 일치. examples/expense-app/docs/CR.md와 docs/example-facts.md의 "변경 요청 사항" 절과 같은 값 | 일치 | 없음 |
| 22 | example | "2026-10-12 운영 위원회", D-012 조건부 수용, "인사 시스템이 하루 한 번 갱신하는 자료(data/projects.csv)" | 일치. examples/expense-app/DECISIONS.md D-012: 2026-10-12, 운영 위원회 결정, 실시간 연동 규격 없음, 인사 시스템 일 1회 갱신 자료. 결정 주체를 운영 위원회로 쓴 것도 맞음 | 일치 | 없음 |
| 23 | example | "정산 요청 화면(등록, 목록)에는 프로젝트 코드 항목이 없음" | 일치. example-facts "구현 전 상태"(수용 시험 1, 2, 3 실패)와 CR.md 수용 기준 1, 3. 단 "프로젝트 코드는 인사 시스템에서 관리"의 "관리"는 원본에 없는 표현임(원본은 "인사 시스템이 일 1회 갱신하는 자료"). 의미 차이는 작음 | 참고 | "인사 시스템이 갱신하는 자료이며"로 맞추면 원본과 같음(선택) |
| 24 | example, fail, check | 요청문의 완료 기준 1~4, 표 4-5, 4-6의 대응 | 내부 일치. 표 4-5의 방지 장치 5개가 요청문 문장과 대응하고, 표 4-6의 다섯 확인 항목이 완료 기준 4개와 출력 형식에 대응. 요청문에 없는 값(EXP-105 등)은 research 기록대로 제거됨 | 일치 | 없음 |
| 25 | limits, 반복 작업의 일관성 | "에이전트가 세션을 시작할 때마다 읽는 규칙 문서" | BOOK_SPEC 5절 용어와 같음. 링크 "Chapter 5의 규칙 문서의 작성"은 ch05 #rule-doc 제목과 같음 | 일치 | 없음 |
| 26 | limits | 링크 "Chapter 5의 미리 제공하는 정보와 필요할 때 찾는 정보" | 제목 일치(ch05 #retrieval). 도착 절이 자료를 미리 포함할지 필요할 때 찾을지를 다루므로 "자료를 나누어 필요할 때 읽게 하는 방법"과 맞음 | 일치 | 없음 |
| 27 | limits | 링크 "Chapter 7의 완료 기준을 검사로 변환" | 제목 일치(ch07 #criteria). 내용 일치 | 일치 | 없음 |
| 28 | limits, 결과 검증 | "완료 기준 가운데 사람이 정한 것을 수용 기준이라고 하고, 그 기준을 확인하는 시험을 수용 시험" | BOOK_SPEC 5절("사람이 정한 완료 조건, 그 조건을 확인하는 시험")과 ch03 22행 정의, ch07 13행과 일치. 제품 문서에서 가져온 정의가 아닌 이 책의 용어라 각주 없음이 맞음 | 일치 | 없음 |
| 29 | intro | "Chapter 1에서는 … 프롬프트, 컨텍스트, 하네스의 세 설계 층" | BOOK_SPEC 4절 "세 설계 층"과 일치 | 일치 | 없음 |
| 30 | limits, 반복 작업의 일관성 | "규칙 문서도 에이전트가 읽고 따르는 지시이므로 지켜졌는지는 따로 확인합니다" | BOOK_SPEC 4절 "지시와 강제"와 ch02 60행(Claude Code 문서: CLAUDE.md는 컨텍스트이며 허용 동작을 바꾸지 않음)과 일치 | 일치 | 없음 |
| 31 | 그림 4-1, 4-2, 표 4-1~4-4 | 접근성 설명과 해설표의 사실 문장 | 본문 및 명세와 일치(방법 이름, 요소 이름, 흐름). 새 제품 사실 없음. 그림 안에 제품명, 회사명 없음(check_all "그림 안 이름" 통과) | 일치 | 없음 |

## 본문 밖에서 발견한 같은 유형의 문제(4장 범위 밖, 참고)
- src/chapters/ch01.html 137행 "2025년 9월 공개된 Claude Code의 컨텍스트 엔지니어링 글" 도 같은 발표 주체 오류(위 1번과 같은 글). 1장 정비 때 "Anthropic의 컨텍스트 엔지니어링 글"로 맞출 것을 권고.

## research/ch04-sources.md에 붙일 기록 문안

## C4-1, C4-2, C4-4, C4-5 재확인과 새 확인(2026-10-24 fact-checker, 4장 플레이북 정리 PR)
- S: C4-4 Anthropic, Effective context engineering for AI agents(자료 키 context-engineering)
- URL: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents, 확인 2026-10-24
- 게시일: 2025-09-29, 작성: Anthropic Engineering(Applied AI 팀: Prithvi Rajasekaran, Ethan Dixon, Carly Ryan, Jeremy Hadfield. 기여: Rafi Ayub, Hannah Moran, Cal Rueb, Connor Jennings). 팀 표기는 Engineering이며 Claude Code 제품 글이 아님(주제는 에이전트 일반). BOOK_SPEC 7절에 따라 4장은 "Anthropic의 컨텍스트 엔지니어링 글"로 씀
- 사용한 내용:
  - 프롬프트 엔지니어링 정의: "Prompt engineering refers to methods for writing and organizing LLM instructions for optimal outcomes."(4장 도입 문단 2)
  - 컨텍스트 엔지니어링 정의: "the set of strategies for curating and maintaining the optimal set of tokens (information) during LLM inference"(4장 limits)
  - context rot: 컨텍스트의 토큰이 늘수록 그 컨텍스트에서 정보를 정확히 기억해 내는 능력이 떨어짐(4장 limits)
- 판정: 내용 일치, 4장 limits의 주어 "Claude Code의 엔지니어링 글"은 불일치(필수, 고칠 문안은 보고서 1번)
- S: C4-5 Anthropic, Glossary(자료 키 platform-glossary)
- URL: https://platform.claude.com/docs/en/about-claude/glossary, 확인 2026-10-24
- 게시일: 표기 없음, 작성: Anthropic(Claude Platform Docs)
- 사용한 내용: Temperature 절 "Even with temperature set to 0, the results will not be fully deterministic, and identical inputs might produce different outputs across API calls"(API 호출 기준). Tokens 절 "the smallest individual units of a language model". Context window 절 "the amount of text a language model can look back on and reference when generating new text". 4장의 토큰과 컨텍스트 윈도 정의는 이 책의 용어(BOOK_SPEC 5절)이며 위 문구와 취지가 같음
- S: Configure permissions(자료 키 permissions)
- URL: https://code.claude.com/docs/en/permissions, 확인 2026-10-24
- 게시일: 표기 없음, 작성: Anthropic(Claude Code Docs)
- 사용한 내용: Manage permissions 절의 Allow, Ask, Deny 정의와 "Permission rules are enforced by Claude Code, not by the model". Permission modes 절 "control how it approves tool calls"(기본값은 4장에서 쓰지 않음). "What a Bash rule doesn't match" 표: Bash(git push *)는 `git -C . push origin main`, `git 'push' origin main`을 막지 못함. "Bash 규칙은 명령 문자열을 대조하며 deny나 ask 규칙은 프로그램 둘레의 보안 경계가 아님". Edit 규칙은 편집용 내장 도구 전체에 적용, Read 규칙은 Grep, Glob 등에 best-effort. 4장은 이 범위를 Bash로 한정해 쓰도록 권고(보고서 3번)
- C4-1 overview, 확인 2026-10-24: "Before prompt engineering" 세 전제와 "When to prompt engineer"의 latency와 cost 문장 원문이 2026-10-23 기록과 같음
- C4-2 best practices, 확인 2026-10-24: Be clear and direct("do more than the task strictly requires ... rather than relying on the model to infer this from vague prompts"), Add context, Use examples effectively(Relevant, Diverse, Tip 3–5), XML tags, Control the format of responses, Tool usage("trained for precise instruction following", "can you suggest some changes")의 원문이 2026-10-22, 23 기록과 같음. 페이지 도입부의 대상 모델 목록은 갱신되어 있으나 4장이 인용한 절의 문구는 바뀌지 않음
- 예제 사실(R7) 확인 2026-10-24: 재무팀, 요청일 2026-10-05, 사유(docs/CR.md), D-012(2026-10-12, 운영 위원회, 실시간 연동 규격 없음, 인사 시스템 일 1회 갱신 자료 data/projects.csv)가 docs/example-facts.md와 examples/expense-app/DECISIONS.md와 일치
- 링크 확인 2026-10-24: ch02 #tool-scope, #instruct-enforce, ch05 #retrieval, #rule-doc, ch07 #criteria는 링크 문구와 도착 절 제목이 같고 내용이 맞음. ch03 #example은 제목이 "기능 추가 에이전트: CR 구현"이라 링크 문구와 다름(ch03 정비 대기)
- 미확인 유지: 각 Claude 문서 페이지의 게시일과 개정일(페이지에 표기 없음). 채팅 제품(API가 아닌)에서 같은 입력의 출력이 달라지는지를 직접 서술한 1차 문서

## 최종 줄
필수 2, 권장 3, 참고 5, 확인한 사실 문장 31개
(권장 3 = 표 3, 8, 10번. 참고 5 = 표 4, 5, 9, 20, 23번. 본문 밖 ch01 동반 수정 권고는 별도 기재)
