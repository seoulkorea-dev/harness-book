# 4장 사실 확인(fact-checker, 이슈 #48)

# 4장 사실 확인 보고 (src/chapters/ch04.html, 2026-10-22 확인)

범위에 관한 단서: 이 세션에는 셸이 없어 `git diff origin/main...HEAD`를 실행하지 못했습니다. 그래서 요청에서 짚은 여섯 곳(예시 제공, 할 일로 지시, 행동 동사 항목, 확인 방법 절, 표 4-6, 참고 자료)과 이와 연결된 표 4-3, 4-4를 현재 파일에서 직접 대조했습니다. diff에 있지만 이 목록 밖인 문장은 보지 못했습니다. 원문은 요청에 준 주소를 오늘 다시 열어 확인했습니다. 사이트에 게시일과 개정일 표기는 없습니다. 파일은 고치지 않았습니다.

| # | 심각도 | 발견 | 위치 | 근거 | 제안 | 확신 |
|---|---|---|---|---|---|---|
| 1 | 권장 | 예시 제공 항목의 "형식과 어조를 맞춰야 할 때 사용"은 원문보다 좁게 쓴 해석입니다. 원문은 "output format, tone, and structure"를 조정한다고 하고, 이를 "맞춰야 할 때만 쓰라"고 한정하지는 않습니다. 같은 장의 표 4-3 예시 제공 행은 "형식, 어조, 구조"라고 써서 장 안에서도 어긋납니다. | techniques 절, 예시 제공 항목(31행) | Best practices "Use examples effectively" 절 첫 문장 "Examples are one of the most reliable ways to steer Claude's output format, tone, and structure." 확인 2026-10-22 | "형식, 어조, 구조를 조정할 때 사용합니다"로 표 4-3과 맞추고, "그래서"로 잇는 문장은 이 책의 해석임이 드러나게 합니다. | 높음 |
| 2 | 권장 | "Anthropic은 이때 실제 업무와 가깝고 서로 다른 경우를 포함한 예시 3~5개를 권장합니다"는 원문의 두 곳을 한 문장으로 합쳤습니다. 3~5개는 Tip 블록의 "Include 3–5 examples for best results."이고, "실제 업무와 가까움(Relevant)"과 "서로 다름(Diverse)"은 별도 조건 목록입니다. 또 "이때"가 형식과 어조를 맞춰야 하는 상황으로 한정되는데, 3~5개 팁은 그런 한정이 없습니다. Diverse의 원문은 "Cover edge cases and vary enough"라서 "서로 다른 경우"는 약간 느슨한 번역입니다. 3~5개 수치 자체는 일치합니다. | 같은 항목(31행), 표 4-3 예시 제공 행 | 같은 절의 조건 목록(Relevant, Diverse, Structured)과 Tip 블록. research/ch04-sources.md "C4-2 재확인(10-21)"의 3~5개는 팁이라는 범위 보강 권고와도 같은 취지 | "예시를 쓸 때는 실제 업무와 가깝고 예외 상황을 포함해 서로 다르게 고르고, Anthropic은 3~5개를 권장합니다"처럼 조건과 팁을 나눠 씁니다. 수치 오류는 아니므로 필수는 아닙니다. | 높음 |
| 3 | 일치 | "Anthropic은 응답 형식을 조정할 때 하지 말아야 할 일보다 해야 할 일을 적으라고 안내" | techniques 절 할 일로 지시(33행) | "Control the format of responses" 절의 "Tell Claude what to do instead of what not to do". 원문 예시는 "Do not use markdown"을 문단형 산문 요청으로 바꾸는 것이고, 표 4-4의 "목록 기호를 사용하지 마"와 "완결된 문단으로 작성해 줘"가 이와 같은 구도입니다. | 조치 없음 | 높음 |
| 4 | 일치 | "어기면 되돌리기 어려운 금지는 요청 문장이 아니라 권한 규칙으로 강제"는 2장과 같은 말입니다. 링크 대상도 있습니다. | 같은 항목(33행) | ch02 표 2-3 "어기면 되돌리기 어려운 규칙 → 강제(권한 규칙)". 같은 장의 지시와 강제 절은 프롬프트나 CLAUDE.md의 지시는 허용되는 동작 자체를 정하지 않는다고 설명합니다. 표 2-4의 원본 자료 수정 금지(Edit(./data/**))가 예입니다. `ch02.html#instruct-enforce`는 ch02의 `<h2 id="instruct-enforce">지시와 강제</h2>`로 존재합니다. | 조치 없음. 참고로 ch02는 금지 규칙에도 한계가 있다고 밝힙니다(스크립트를 통한 간접 수정은 못 막음. 해결은 Chapter 9). ch04의 "강제"는 이 한계까지 포함한 말이 아니므로, 필요하면 독자가 ch02로 이어서 읽게 하는 정도로 충분합니다. | 높음 |
| 5 | 일치 | "행동 동사로 실행을 요청해도, 실제 실행 여부는 사용할 수 있는 도구와 권한 설정이 정합니다(Chapter 2)"는 ch02 tool-scope 절이 뒷받침합니다. | 같은 목록 행동 동사 항목(34행) | ch02 tool-scope 절: 가용성(모델이 볼 수 있는 도구의 범위)과 권한 평가(금지, 확인, 허용)의 두 단계로 나누고, "모델이 도구 호출을 요청만 하고 실행은 하네스가 하기 때문"이라고 서술합니다(Agent SDK 문서 인용). 그림 2-2의 "요청만으로는 실행 아님"도 같은 뜻입니다. `ch02.html#tool-scope`도 존재합니다. 앞 문장 "제안해 줄 수 있어?"는 Best practices의 Tool usage 절 "If you say 'can you suggest some changes,' Claude will sometimes provide suggestions rather than implementing them"과 일치합니다("수정 대신 제안만 할 때가 있다"는 "sometimes"를 지킴). | 조치 없음 | 높음 |
| 6 | 일치 | 확인 방법 절 끝 문장 "기준에 못 미치는 항목이 있으면 누락된 조건을 요청에 보완해 다시 요청합니다"는 표 4-6과 어긋나지 않습니다. 절 안의 "예상 공수 수치의 근거를 찾고 없으면 '확인 필요' 표시를 본다"는 표 4-6 둘째 행과 같습니다. | check 절(104행), 표 4-6 | 표 4-6의 세 행(출력 형식 다섯 항목, 근거 없는 수치의 "확인 필요", 권고안 세 선택지와 이유 한 문장)은 예제 요청의 출력 형식 줄과 완료 기준 1, 2에 그대로 대응합니다. 그림 4-1의 점선, 표 4-2 결과 확인 행도 같은 재요청 경로를 말합니다. | 조치 없음. 재요청은 표의 열이 아니라 본문에만 있으므로 표에 넣을 필요는 없습니다. | 높음 |
| 7 | 참고 | 참고 자료는 id `ref-anthropic-2026` 하나에 문서 두 개(Prompting best practices, Prompt engineering overview)를 묶었고, 본문 링크도 모두 이 id입니다. 장 안의 형식은 일관됩니다. 같은 방식은 ch06 참고 자료에도 있습니다. 확인일은 "2026년 10월 20일"인데, research에는 10월 21일 재확인이 있고 오늘 10월 22일에 다시 확인했습니다. 이 확인에서 예시 제공, 할 일로 지시, 행동 동사의 근거 문장은 바뀌지 않았습니다. | refs 절(115행) | ch06은 같은 방식(`(확인 2026년 10월 20일)`을 저자 바로 뒤에 둠), ch05는 확인일을 제목 뒤에 둡니다. 장마다 어순이 다르며, ch04는 ch06과 같습니다. 이는 STYLE.md 4절의 해당 규정을 열어 보지 않은 채 장끼리 비교한 결과입니다. | 확인일 갱신 여부는 메인 세션이 정합니다. 항목별 문장(31~34행)에는 개별 링크가 없고 절 첫 문장(27행)의 링크에 기대고 있는데, 이는 기존 방식이라 이번 변경의 문제는 아닙니다. | 중간 |

## research/ch04-sources.md에 추가할 기록 문안

```
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
```

필수 0, 권장 2, 참고 1, 확인한 사실 문장 7개(일치 4, 권장 2, 참고 1)
