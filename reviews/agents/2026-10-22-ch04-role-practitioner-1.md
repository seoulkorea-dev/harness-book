# 4장 역할 검토: 실무자 1차 읽기(2026-10-22, 이슈 #66)

- 대상: src/chapters/ch04.html 전체(브랜치 ch04-rework). 주장 줄, 첫 문단, 요약, 6개 절, 표 4-1~4-6, 그림 4-1, 4-2(aria-label과 SVG 글자), 참고 자료
- 대조한 자료: 기준서를 보기 전에 ch04 통독. 이어서 ch01~ch03, ch05, ch08(D-012), 마지막에 BOOK_STANDARD.md, REVIEW_RULES.md, AUTHOR_PREFS.md, STYLE.md, docs/example-facts.md, research/ch04-sources.md, research/bibliography.json
- 직접 실행한 명령(읽기만): grep으로 다른 장 앵커 확인(ch01#layers, #prompt-context, ch02#instruct-enforce, #tool-scope, #components, ch03#example, ch05#rule-doc, ch07#criteria, ch08#decisions 모두 있음), ch08의 D-012 확인, `python3 lint/check_rules.py`와 `check_rules.check_file('src/chapters/ch04.html')`(세부 위반 23건), `python3 lint/check_style.py`(ch04 출력 없음)
- 공식 문서 확인(모두 2026-10-22, WebFetch): platform.claude.com의 prompt-engineering/overview, claude-prompting-best-practices, test-and-evaluate/strengthen-guardrails/reduce-hallucinations, code.claude.com의 best-practices, memory
- 고칠 문장 비율: 18 ÷ 89 = 20.2%
  - N: 주장 줄 1, 첫 문단 5, 요약 li 3, 절 본문 p와 li 80(elements 14, techniques 22, limits 15, example 16, fail 3, check 5, principle 5). 표, 그림, pre, 참고 자료 제외. R10 링크 문장처럼 규칙만 어긴 문장은 비율에 넣지 않고 맨 끝 절에 따로 적음
- 절별 건수: 머리 4 / elements 3 / techniques 0 / limits 4 / example 6 / fail 0 / check 1 / principle 0. 표, 그림, 제목 지적 12건 따로, 권고 9건

## 총평(가장 큰 문제 먼저)
1. **장 첫머리의 작동 설명이 사실과 다르고 이 책의 정의와 부딪힘.** "모델은 요청에 적힌 조건과 함께 입력된 자료만으로 결과를 생성"은 사실과 다름(학습된 일반 지식, 시스템 프롬프트, 규칙 문서, 도구 결과도 영향). 표 4-1 입력 행("일반 지식에 근거한 결과")과 장 안에서도 모순. 용어표의 컨텍스트 정의("입력되는 정보 전체, 프롬프트는 그 일부")와도 부딪힘. 주장 줄의 "문장의 표현이 아니라"도 techniques 절과 모순이고 R1 배타 형식
2. **예제의 완료 기준과 확인 방법이 형식만 보고 내용은 보지 않음(R14, R17).** 표 4-5 둘째 행의 핵심 실패(연동 규격 부재를 모른 채 공수 추정)를 요청의 완료 기준 두 개와 표 4-6 세 항목이 확인하지 않음
3. **Anthropic 문서 인용의 범위를 넓혔고(R13), 한 문장은 현행 원문과 다름.** 개요 문서의 "success criteria for your use case"는 응용 전체를 평가로 시험하는 기준. limits 끝 문단은 서로 다른 두 절(Tool usage, Be clear and direct)을 "도구 사용을 안내하는 절에서"로 묶음. "above and beyond" 문장은 2026-10-22 현행 페이지에 없고, 지금 문장은 "If you want Claude to do more than the task strictly requires, explicitly request it rather than relying on the model to infer this from vague prompts."(번역 "기대 이상"도 맞지 않음). 같은 문단에 출처 없는 반론(R2)
4. **예제 이름 규칙(R12) 위반 10곳.** 장 첫 등장(limits "경비 정산 예제")에 정해진 이름 없음, example 절은 "변경 요청(Change Request) CR"
5. **"프롬프트로 해결되지 않는 문제" 첫 항목 이름과 설명이 맞지 않음.** "자료 부족"인데 설명은 자료가 많아 한도에 이르는 문제. Claude Code 문서는 "performance degrades as it fills". 반복 작업 항목은 규칙 문서만 처방(규칙 문서는 지시, memory 문서 "Claude treats them as context, not enforced configuration"), 재사용 요청 양식(스킬, 사용자 명령)은 빠짐(권고)

## 문장별 지적
| 발견 | 위치 | 근거 | 제안 | 확신 |
|---|---|---|---|---|
| 배타 형식, 장 안 모순 | claim "결과의 품질을 정하는 것은 문장의 표현이 아니라," | techniques 첫 문장, R1 | "결과의 품질은 문장을 다듬는 것만으로는 충분하지 않고, 요청에 목적, 입력, 출력 형식, 완료 기준이 들어 있는지에 크게 좌우됩니다." | 높음 |
| 모델의 입력 범위를 사실과 다르게 좁힘 | lead "모델은 요청에 적힌 조건과 함께 입력된 자료만으로 결과를 생성합니다." | 일반 지식, 시스템 프롬프트, 규칙 문서, 도구 결과. 표 4-1, 용어표 | "모델은 요청과 함께 입력된 정보와 학습한 일반 지식으로 결과를 생성합니다. 요청하는 사람이 적지 않은 이번 일의 조건은 그 어디에도 없으므로 모델이 추측으로 채웁니다." | 높음 |
| 단정 | lead "그래서 조건이 누락된 요청은 … 결과를 받습니다." | 모델이 되묻기도 함(example-before), R1 | "… 결과를 받기 쉽습니다." | 중간 |
| 항목 이름과 설명 불일치 | 요약 li3 "자료 부족, …" | limits 첫 항목 | "자료의 양과 선별, …"(limits 항목 이름도 같게) | 중간 |
| lead와 같은 과도한 단순화 | elements "모델은 요청과 자료만 보고 결과를 만들며," | 위와 같음 | "모델은 요청에 적히지 않은 이번 일의 조건을 알 수 없어서 추측으로 채웁니다." | 높음 |
| 논거가 약함(출력 형식도 요청하는 사람만 앎) | elements "입력과 출력 형식은 자료와 양식으로 눈에 보이지만," | 빠지기 쉬운 이유는 요청하는 사람 머릿속에서 당연해서 | "입력과 출력 형식은 자료와 양식을 붙이면서 자연히 적게 되지만, 목적과 완료 기준은 요청하는 사람에게 당연해서 빠지기 쉽고, 적지 않으면 모델에게 짐작할 단서가 없습니다." | 중간 |
| 출처의 범위를 넓힘(R13) | elements "완료 기준을 먼저 정하는 방식은 … 개요 문서에도 있습니다." | 개요 문서는 사용 사례의 성공 기준과 평가 | "개요 문서는 프롬프트를 다듬기 전에 사용 사례의 성공 기준과 그 기준으로 결과를 시험하는 방법을 먼저 갖추라고 안내합니다. 이 책은 이 순서를 요청 한 건에 적용해 …" | 높음 |
| 이름과 설명 불일치, 동작 단순화 | limits "자료 부족: … 한도에 이르고," | best practices "performance degrades as it fills" | "자료의 양과 선별: … 컨텍스트 윈도를 채워 결과가 나빠지고 한도에 이르며, …" | 중간 |
| 장 첫 등장인데 예제 이름 규칙 위반 | limits "Chapter 3의 경비 정산 예제는" | R12, D-125 | "경비 정산 시스템 개편 변경 요청 사항(이하 변경 요청 사항) 예제는 …" | 높음 |
| 출처 없는 반론(R2 실패) | limits "… 간단히 작성해도 된다는 의견이 있습니다." | check_rules R2 | 삭제 | 높음 |
| 두 절을 한 절처럼 묶음, 현행 원문과 다름 | limits "Anthropic은 도구 사용을 안내하는 절에서 …, 기대 이상의 결과를 원하면" | Tool usage 절, Be clear and direct 절, 현행 원문 "do more than the task strictly requires" | "최신 모델이 지시를 정밀하게 따르도록 훈련되었다고 설명하고, 과제가 요구하는 것보다 더 많은 일을 원하면 … 명시적으로 요청하라고 안내합니다." | 높음 |
| CR과 영어 병기 | example "… 변경 요청(Change Request) CR의 영향 검토를" | R12 | "재무팀이 보낸 변경 요청 사항의 영향 검토를 …" | 높음 |
| CR | example "CR은 Chapter 3에서 …" | R12 | "이 변경 요청 사항은 Chapter 3에서 구현을 설계한 것과 같으며, …" | 높음 |
| 프롬프트와 본문의 CR 표지 | example-after 해설 "요청문의 "CR:"은 …" | R12(코드나 파일 경로 아님) | 프롬프트 줄을 "제목: …"으로, 해설은 EXP 번호부터 | 높음 |
| 단정 | example-after "이 사실을 모르는 검토는 작업량(공수)을 잘못 추정합니다." | R1 | "… 실시간 연동을 전제로 작업량(공수)을 추정하기 쉽습니다." | 중간 |
| CR | example-after "… CR을 조건부 수용하고," | R12 | "변경 요청 사항을" | 높음 |
| 예제에 쓴 방법을 부정확하게 설명 | example-after "… 구획 구분 … 과 이유 제공(첫 문장의 운영 위원회 결정)을 사용했습니다." | 구체적 지시(다섯 항목, 번호 붙인 완료 기준)도 있음, 첫 문장은 목적 | 실제 쓴 방법을 빠짐없이 | 중간 |
| CR | check "CR 영향 검토 요청은 …" | R12 | "변경 요청 사항의 영향 검토는 …" | 높음 |

권고(비율에 넣지 않음)
| 발견 | 위치 | 근거 | 제안 | 확신 |
|---|---|---|---|---|
| 태그의 원래 이름(XML 태그) 빠짐 | techniques 구획 구분 | 원문 "XML tags" | "XML 태그로 구분, 태그 이름은 정해진 것이 없음" | 중간 |
| 근거 없는 수치 처리의 공식 근거 | example-after 완료 기준 1 | reduce-hallucinations "Allow Claude to say 'I don't know'", "Verify with citations" | 근거로 들고, 수치마다 근거 자료 줄을 적게 요청 | 중간 |
| 상대 날짜 | 프롬프트 "다음 주 운영 위원회에서" | 기준일 필요, D-012는 2026-10-12 | 날짜로 | 중간 |
| 공수 근거 자료가 입력에 없음 | 프롬프트 출력 형식, 완료 기준 1 | 예상 공수가 전부 "확인 필요"가 됨 | 공수 단위 지정, 가정과 함께 "추정" 표시 | 중간 |
| 행동 동사의 실행 조건 | techniques 행동 동사 | 권한 모드와 사용자 승인도 실행을 정함 | "도구, 권한 규칙과 권한 모드, 사람의 승인이 정합니다" | 낮음 |
| 반복 요청 처방이 규칙 문서 하나 | limits 반복 작업 | memory 문서(지시), best practices(스킬) | 재사용할 요청 양식도 | 중간 |
| 보내기 전 점검의 공식 근거 | principle, check | best practices "Show your prompt to a colleague with minimal context" | 점검 질문에 한 줄 | 중간 |
| 에이전트 환경의 입력 형태 | elements 입력 정의 | "Let Claude fetch what it needs" | 읽을 위치를 지정해 줌 | 낮음 |
| 목적 정의에 없는 요소(기한) | example-before | elements 정의 | 정의에 넣거나 뺌 | 낮음 |

## 표, 그림, 제목 지적
| 발견 | 위치 | 근거 | 제안 | 확신 |
|---|---|---|---|---|
| 지나친 단정 | 그림 4-1 제목 "목적과 완료 기준은 요청하는 사람만 줄 수 있습니다", 카드 "요청하는 사람만 아는 정보" | 모델이 질문해 기준 초안을 만들기도 함("Let Claude interview you"), 확정은 사람 | "목적과 완료 기준은 요청하는 사람이 정합니다" | 중간 |
| 실패 표 둘째 행을 확인하는 항목 없음 | 표 4-6 | R14, R17 | "영향 범위와 일정 영향" 행, 프롬프트 완료 기준 3 | 높음 |
| 행 층위(R5) | 표 4-4 구획 구분 행 | 이 행만 설명 | 짧은 실제 요청문 | 중간 |
| 열 이름, 캡션 CR | 표 4-5 | R9, R12 | "실패 유형 / 원인 / 방지 장치" | 높음 |
| 열 이름, 설명 줄, 캡션 CR | 표 4-6 | R9, R12 | "확인 항목 / 확인 방법 / 확인 기준" | 높음 |
| 해설표 세트 A 아님, 칸 지시 표현 | 표 4-2, 4-3 | R9 | "구성 요소 / 주요 역할 / 관련 절", 실제 절 제목 | 높음 |
| 모호한 열 이름 | 표 4-4 "방법" | R9 | "구분" | 높음 |
| 설명 줄이 열 이름 나열 | 표 4-1 | R9 | 결론 한 줄 | 중간 |
| 같은 내용 네 번 | 목록, 그림 4-2, 표 4-3, 표 4-4 | 반복 | 그림 4-2와 표 4-3을 합치는 안은 작가 확인(D-132) | 중간 |
| 캡션 근거 표기 | 그림 4-2 캡션 | 기준서 10절 | "(공개 자료를 바탕으로 이 책이 정리)" | 높음 |
| 예제 절 제목 | h2#example | 기준서 3절 | "예제: 변경 요청 사항의 영향 검토 요청" | 높음 |
| 항목 이름 | limits "자료 부족" | 위와 같음 | "자료의 양과 선별" | 중간 |

그림 4-1, 4-2 SVG 글자의 겹침이나 넘침은 좌표로 확인했고 이상 없음. 제품명과 회사명도 그림 안에 없음.

## 기준서 대조에서 추가로 걸린 것
- check_rules 세부 23건(정비 전이라 경고): R10 같은 장 링크 6곳, R2 1곳, R12 8곳과 영어 병기 1곳(+ 첫 등장 이름 누락), R9 7곳, R11(본문 링크 4곳, 장 끝 참고 자료, 두 문서 한 항목, 열람일. bibliography.json에 prompt-overview, prompting-best-practices 추가 필요), R1 경고 2곳(주장 줄, limits "개인의 프롬프트가 아니라")
- R13 필수: 성공 기준과 완료 기준 동일시
- R14, R17 필수: 표 4-5 둘째 행에 대응하는 확인 기준 없음
- R16: 규칙 문서(지시)를 일관성을 보장하는 장치처럼 씀
- 용어표: 완료 기준 정의 불일치(용어표 "작업이 끝났다고 판정하는 조건"), 프롬프트 정의에 비추어 lead 첫 문장
- research/ch04-sources.md(C4-2): "above and beyond" 원문이 2026-10-22 현행 페이지에서 바뀜. "Be specific about the output format and constraints you want."도 문구가 조금 바뀜
- 장 첫 문단 틀은 순서는 맞으나 기준서가 편집 권고로 든 같은 꼴
- 장 흐름: 3장(구현)에서 4장(구현 전 영향 검토)으로 시간이 거꾸로 감. 예제 첫 문단에 "결정(D-012) 전 시점"을 밝히기를 권고
- docs/example-facts.md: "통합 테스트 시작 예정일 2026-10-19", EXP-105, EXP-109는 example-facts에 없음(R7)
