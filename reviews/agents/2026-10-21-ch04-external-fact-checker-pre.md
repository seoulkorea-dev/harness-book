# 4장 예시 개수 출처 확인(fact-checker, 이슈 #48)

fact-checker 보고: ch04 "요청을 명확하게 만드는 방법" 절, 예시 제공(30행), 할 일로 지시(32행), 행동 동사(33행). 확인일 2026-10-21. 파일은 고치지 않았습니다.

확인한 원문은 현행 주소 https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices 입니다. 옛 multishot-prompting 주소(docs.claude.com)는 302로 이 페이지에 넘어갑니다. 페이지에 게시일은 없습니다.

| # | 심각도 | 발견 | 위치 | 근거(원문 인용, URL, 확인일) | 제안 | 확신 |
|---|---|---|---|---|---|---|
| 1 | 권장 | "3~5개 권장"은 문서 표현과 일치합니다. 다만 본문이 조건을 빼고 있습니다. 원문은 예시를 쓸 때의 팁이고 모든 요청에 필수라는 말이 아닙니다. 원문 조건은 "for best results"(최선의 결과를 위해)입니다. 본문의 "권장"은 이 조건을 담고 있지만 "언제 예시를 쓰는가"가 빠져 있어, 모든 요청에 필요한 것처럼 읽힐 수 있습니다. | ch04 30행 | "Include 3–5 examples for best results." (Tip 블록, "Use examples effectively" 절). 같은 절 도입부: "A few well-crafted examples (known as few-shot or multishot prompting) improve accuracy and consistency." "When adding examples, make them: Relevant / Diverse / Structured." 위 URL, 2026-10-21 | 이슈 #48 항목 6에 따라 범위를 밝힙니다. 원문과 다른 내용은 없어 의미는 바꾸지 않습니다. 제안 문구는 아래 (가)를 참고하세요. | 높음 |
| 2 | 참고 | "가장 신뢰할 수 있는 방법의 하나"는 원문과 일치합니다. "one of the most reliable ways"를 옮긴 표현입니다. 원문은 "steer Claude's output format, tone, and structure"(출력의 형식, 어조, 구조를 이끄는 것)입니다. 본문의 "조정"은 이 뜻으로 읽을 수 있습니다. | ch04 30행 | "Examples are one of the most reliable ways to steer Claude's output format, tone, and structure." 같은 URL, 2026-10-21 | 변경 불필요합니다. 선택 사항으로 "조정" 대신 "유도"를 쓸 수 있으나 필수는 아닙니다. | 높음 |
| 3 | 참고 | 본문의 "서로 다른 경우를 포함해"와 "실제 업무와 가깝게"는 원문의 Diverse("Cover edge cases and vary enough that Claude doesn't pick up unintended patterns")와 Relevant("Mirror your actual use case closely")에 해당합니다. 일치합니다. "서로 다른 경우"에는 원문의 edge cases(경계 사례)와 의도하지 않은 패턴을 피한다는 이유가 빠져 있으나 오류는 아닙니다. | ch04 30행 | 같은 절, 같은 URL, 2026-10-21 | 변경 불필요합니다. | 높음 |
| 4 | 참고 | 할 일로 지시(32행)는 일치합니다. 원문은 "Tell Claude what to do instead of what not to do"이고, "Control the format of responses" 절의 첫 항목입니다. 예도 "Do not use markdown" 대신 "smoothly flowing prose paragraphs"로 본문 표의 52행(목록 기호 대신 완결된 문단)과 같은 취지입니다. 다만 원문은 이것을 응답 형식 제어 방법으로 소개합니다. 본문은 일반 원칙처럼 쓰고 발표 주체를 밝히지 않았습니다(아래 5번). | ch04 32행, 52행 | 같은 URL, "Control the format of responses" 절, 2026-10-21 | 사실 오류는 없습니다. 5번을 참고하세요. | 높음 |
| 5 | 권장 | 32행 "할 일로 지시" 문장은 발표 주체가 없습니다(STYLE.md 1절, 4절). 같은 절의 다른 항목은 "Anthropic은 … 설명합니다"로 밝히고 있습니다. | ch04 32행 | STYLE.md 4절. 원문은 위 URL | "하지 말아야 할 일보다 해야 할 일을 적습니다"를 "Anthropic은 응답 형식을 조정할 때 하지 말아야 할 일보다 해야 할 일을 적으라고 안내합니다"처럼 주체와 맥락을 밝히는 방향으로 고칠 수 있습니다. 참고 자료 링크(ref-첫저자성-연도 형식의 Anthropic 2026 항목)는 장 안 다른 항목과 같은 방식으로 붙였는지 확인이 필요합니다. 저는 ref id를 확인하지 못했습니다. | 중간 |
| 6 | 참고 | 행동 동사(33행)는 일치합니다. 원문은 도구 사용 안내("Tool use > Tool usage" 절)에 있습니다. 근거: "If you say 'can you suggest some changes,' Claude will sometimes provide suggestions rather than implementing them, even if making changes might be what you intended." 본문의 "도구를 사용하는 작업에서", "수정 대신 제안만 할 때가 있다"는 "sometimes"를 "~할 때가 있다"로 옮긴 것으로 정확합니다. 원문 비교 예: 덜 효과적 "Can you suggest some changes to improve this function?", 더 효과적 "Change this function to improve its performance." 본문 표 53행(계획서 예)은 이 책의 예이고 원문 예와 같은 구조입니다. | ch04 33행, 53행 | 같은 URL, "Tool use > Tool usage" 절, 2026-10-21 | 변경 불필요합니다. 선택 사항으로, 원문이 "최신 모델은 정밀한 지시 따르기로 훈련되어 명시적 지시가 유리하다"는 맥락에서 이 말을 한 점이 기록 C4-2에 이미 있으므로 본문 맥락 문장이 있는지만 확인하세요. | 높음 |
| 7 | 참고 | 기존 기록 C4-2와 비교하면, 예시 제공의 원문 인용("one of the most reliable ways", "3–5 examples for best results"), 할 일로 지시, 행동 동사의 인용이 모두 지금도 같습니다. 낡음이나 불일치는 없습니다. 게시일과 개정일은 이번에도 확인하지 못했습니다(페이지에 표기가 없음). 다만 페이지 도입부의 대상 모델 목록이 바뀌어 있으므로(Claude Sonnet 5.5 등 포함), 기록의 "최신 모델" 표현을 쓰는 곳에는 확인 연월을 남기는 편이 좋습니다. | research/ch04-sources.md C4-2 | 같은 URL 첫머리, 2026-10-21 | 아래 기록 문안을 추가하세요. | 높음 |

### 항목 3(이슈 #48 항목 6)에 대한 판단과 제안 문구
본문이 원문과 다르지는 않으므로 "출처와 다르면 바꾸지 않음" 조건에 걸리지 않습니다. 사실 오류가 없어 필수 수정은 아닙니다. 다만 현재 문장은 예시가 언제 필요한지를 말하지 않아 모든 요청에 필수로 읽힐 수 있고, 원문의 3~5개는 예시를 쓸 때의 팁("Tip")입니다. 범위를 밝히는 쪽이 원문에 더 가깝습니다.

(가) 권장 문구: "Anthropic은 예시를 출력의 형식, 어조, 구조를 조정하는 가장 신뢰할 수 있는 방법의 하나로 봅니다. 형식과 어조를 맞춰야 할 때 예시를 넣습니다. Anthropic은 예시를 넣을 때 실제 업무와 가깝고 서로 다른 경우를 포함하도록 하고, 최선의 결과를 위해 3~5개를 권장합니다."

(나) 더 짧은 대안: 기존 문장 끝만 "…서로 다른 경우를 포함해 예시를 쓸 때는 3~5개를 권장합니다."로 바꿉니다.

두 문구 모두 의미는 원문과 같습니다. 이 문구의 "권장"의 주체는 Anthropic입니다. 현재 본문 두 번째 문장은 주어가 생략되어 책의 권장처럼 읽히므로, (가)는 이 점도 함께 바로잡습니다. 원문 표현에 맞춰 "모든 요청에 필요하다"는 뜻의 문장은 넣지 않았습니다. 이 책의 판단인 "형식과 어조를 맞춰야 할 때"는 원문 Tip의 문장이 아니라 "output format, tone, and structure" 조정이라는 원문 설명에서 가져온 범위입니다.

### research/ch04-sources.md에 추가할 기록 문안
```
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
```

필수 0, 권장 2, 참고 5, 확인한 사실 문장 4개(예시 제공의 두 문장, 할 일로 지시, 행동 동사 각 1문장 기준으로 세면 예시 제공 2 + 할 일로 지시 1 + 행동 동사 1)
