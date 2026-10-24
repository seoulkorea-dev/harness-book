# 7장 사실 점검(fact-checker)

# Chapter 7 기술 감수 보고 (src/chapters/ch07.html 전체, 확인일 2026-10-24)

## 요약
**필수 1, 권고 8, 참고 2, 확인한 사실 문장 31개.**

- 불일치나 낡음으로 판정한 문장은 없습니다. 필수 1건은 Stop 훅을 "통과할 때까지"로 단정한 문장입니다(R1, 연속 차단 상한이 빠짐).
- 예제 사실은 모두 맞습니다.
  - 기준 상태 두 줄은 실제 `python check.py`의 표준 출력과 글자까지 같습니다. 임시 복사본에서 실행했고 종료 코드는 1입니다(Linux, Python 3.13.16).
  - app.py의 포트는 8000이고 경로는 /new입니다.
  - settings.example.json의 deny는 Edit(./acceptance/**)와 Edit(./check.py)입니다.
  - 부록 lab-1, lab-4와 장 간 앵커(ch01 #loop, ch02 #instruct-enforce, ch03 #example와 #files, ch06 #split, #selection, #example)가 모두 있습니다.
- 하네스 엔지니어링 글(OpenAI)은 이번에도 원문을 열지 못했습니다. openai.com과 www.openai.com 모두 ENOTFOUND였고, 검색 요약에도 lint와 CI 내용이 없습니다. 이 부분은 미확인(참고)입니다.
- 인용 위첨자 키 6개는 문장의 출처와 맞습니다. 다만 52행 문단에는 위첨자가 없습니다(번호 7).

## 판정표

| 번호 | 위치(절, 문장 첫머리) | 원문 | 확인 결과와 출처(확인일 2026-10-24) | 고친 문안 | 등급 |
|---|---|---|---|---|---|
| 1 | example, 93행 "검사가 통과할 때까지 에이전트가 응답을 끝내지 못하게 하는 Stop 훅" | "…Stop 훅(…)도 있으며, Claude Code 문서는 이를 결정적인 관문으로 설명합니다" | 부분 불일치(단정). Best practices "Give Claude a way to verify its work"에 "As a deterministic gate: a Stop hook … blocks the turn from ending until it passes"가 있어 "결정적 관문" 설명 자체는 맞습니다. 그러나 Hooks reference "Stop input" 절에 연속 차단 상한이 있습니다: "after stop hooks have continued the turn eight times in a row, Claude Code overrides the next block and ends the turn". 도구를 호출하면 횟수가 초기화되고, 환경 변수 CLAUDE_CODE_STOP_HOOK_BLOCK_CAP으로 올릴 수 있습니다. 근거: https://code.claude.com/docs/en/best-practices, https://code.claude.com/docs/en/hooks | "…검사가 통과할 때까지 응답을 끝내지 못하게 하는 Stop 훅도 있으며, Claude Code 문서는 이를 결정적인 관문으로 설명합니다. 다만 연속으로 막을 수 있는 횟수에 상한이 있어(기본 8회, 도구를 호출하면 초기화) 상한에 닿으면 검사가 통과하지 않아도 턴이 끝날 수 있습니다." 상한 문장에는 hooks 키 각주 추가(R11, 각주 하나에 근거 문서 하나). | 필수 |
| 2 | example, 74~85행 check.py 발췌 | "핵심 부분을 봅니다" 뒤에 단순화한 코드 | 발췌가 실제 examples/expense-app/check.py(37행)와 다릅니다. 생략하거나 바꾼 곳: (a) ACCEPTANCE_COUNT = 5와 UNIT_KEYWORD = "project_code", (b) test_ids() 함수와 project_code 시험 건수 계산, (c) 건너뜀 건수 집계와 출력, (d) 합격 조건의 skipped == 0, project_code 시험 1건 이상, 수용 시험 정확히 5건. 발췌가 출력하는 형식(폴더: 실행 N건, 실패 M건)도 바로 아래 출력 원문 두 줄(건너뜀, project_code 시험 0건, (정한 수 5건) 포함)과 다릅니다. 독자가 발췌를 실행하면 아래 출력과 달라집니다. 근거: examples/expense-app/check.py와 실제 실행 출력 | 74행에 "아래는 줄인 코드이고, 실제 check.py는 건너뜀 건수, project_code 시험 유무, 수용 시험 수(5건)도 확인합니다"를 한 문장 추가. | 권고 |
| 3 | example, 93행 훅 문단 | Stop 훅과 check.py를 이어 읽을 수 있는 서술 | Hooks reference 종료 코드 표에서 Stop은 exit 2일 때만 중단을 막습니다. exit 1은 non-blocking error이고 문서는 "If your hook is meant to enforce a policy, use exit 2"라고 합니다. 본문의 check.py는 실패 시 종료 코드 1이므로 Stop 훅에 그대로 쓰면 강제되지 않습니다. S-C7-5에 이미 기록된 주의점인데 본문에 없습니다. 근거: https://code.claude.com/docs/en/hooks | "check.py는 실패하면 종료 코드 1로 끝나는데, 훅에서는 종료 코드 2여야 막으므로 훅 명령에서 `|| exit 2`로 바꿔 실행합니다." | 권고 |
| 4 | report, 10행 "이 사례는 두 가지를 보여 줍니다" | "결과를 만든 에이전트의 판단은 완료의 근거가 되지 않습니다." | 원문이 아니라 이 책의 해석입니다(R13). Young 글이 확인한 것은 충분한 시험 없이 기능을 완료로 표시하는 경향과, 브라우저 자동화를 명시하면 잘 확인했다는 것까지입니다. "완료 보고는 근거가 아니다"라는 결론은 글에 없습니다. 근거: https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents | "이 책은 이 사례를 두 가지로 읽습니다. …" | 권고 |
| 5 | report, 9행 "Claude Code의 장기 실행 글" | "Claude Code의 장기 실행 글이 있습니다. 글의 실험에서…" | 1장 101행, 표 1-5(105행)와 같은 꼴이라 일관성은 맞습니다(요청 항목 4). 사실 면에서는 원문이 실험 주체를 "Opus 4.5 running on the Claude Agent SDK in a loop across multiple context windows"라고 쓰고 Claude Code를 언급하지 않습니다. 글은 Anthropic Engineering 게시물(Justin Young, 2025-11-26)입니다. 표기는 D-108/Q-039 작가 결정 사항입니다. | 작가 확정 전 유지. 바꾼다면 1장과 함께 "Anthropic의 장기 실행 글"로(ch01 101행, 105행, ch07 9행). Q-039에 7장 9행 포함 확인. | 권고 |
| 6 | rubric, 53행 "문서의 예제는 기준이 되는 정답을 예시 답안으로 두고…" | "예제 코드의 주석에는 결과를 만든 모델과 다른 모델로 평가하는 편이 일반적으로 좋다는 안내도 있습니다" | 문구는 맞습니다(주석 원문: "Generally best practice to evaluate with a different model from the one used to generate the evaluated output"). 그러나 이 주석은 "Grade your evaluations" 절의 golden answer 예제에 없고, 앞쪽 절의 Likert(1~5점)와 이진 분류 LLM 예제에 있습니다. golden answer 예제는 생성과 채점에 같은 모델 claude-opus-5-5를 씁니다. 같은 문단에서 이어 쓰면 한 예제의 내용으로 읽힙니다. 근거: https://platform.claude.com/docs/en/test-and-evaluate/develop-tests | "문서의 LLM 기반 채점 예제는 golden answer를 채점 모델에 넘겨 비교하게 합니다. 이와 별도로 문서의 다른 LLM 채점 예제 코드 주석에는 …" | 권고 |
| 7 | rubric, 52행 "평가 문서는 상세하고 명확한 기준표를 작성하라고 안내하고" | 52행 문단(위첨자 없음) | 내용은 일치합니다("Have detailed, clear rubrics", Acme Inc. 예, "Be empirical or specific", "Purely qualitative evaluations are hard to assess quickly and at scale"). 다만 이 문단에 develop-tests 위첨자가 없습니다(R11). 46행도 첫 문장에만 위첨자가 있습니다. | 52행 마지막 문장 뒤에 `<sup class="cite" data-ref="develop-tests"></sup>` 추가. | 권고 |
| 8 | example, 92행 금지 규칙 문단 | "…간접으로 수정하는 경우에는 적용되지 않습니다" | 내용은 일치합니다. 다만 같은 permissions 문서 경고문은 "For OS-level enforcement that blocks all processes from accessing a path, enable the sandbox"까지 안내합니다. 본문에는 문서가 제시한 전면 차단 수단(샌드박스)이 없습니다. 근거: https://code.claude.com/docs/en/permissions "Read and Edit" 절 | "…적용되지 않습니다. 모든 프로세스의 접근을 막으려면 문서는 샌드박스를 켜라고 안내하며, 이 예제는 git status 확인으로 보완합니다." | 권고 |
| 9 | report, 9행 "…에이전트의 결과가 개선되었습니다" | "사람이 사용하는 방식 그대로 시험하라고 명시하자, 에이전트의 결과가 개선되었습니다" | 원문은 "Claude did well at verifying features end-to-end once explicitly prompted to use browser automation tools and do all testing as a human user would"입니다. 평가 대상이 "결과"가 아니라 "기능을 끝에서 끝까지 확인하는 일"입니다. ch07 spec의 "더 잘 동작했다" 수준 기준과도 어긋납니다. | "…시험하라고 명시하자, 에이전트가 기능을 처음부터 끝까지 잘 확인했습니다." | 권고 |
| 10 | methods, 42행 "Codex의 하네스 엔지니어링 글에 따르면…" | "문서 구조를 전용 lint와 CI로 기계적으로 검사했습니다. 사람은 우선순위를 정하고 결과를 검증하는 역할을 맡았습니다" | 미확인. https://openai.com/index/harness-engineering/ 와 https://www.openai.com/index/harness-engineering 모두 ENOTFOUND. 검색 요약으로 확인된 것은 게시일(2026-02-11), 저자(Ryan Lopopolo), 5개월 실험, 직접 작성한 코드 0줄, Codex가 앱 로직과 테스트와 CI 설정과 문서를 작성했다는 것까지입니다. lint와 CI, 사람 역할 문장은 research/ch01-sources.md S2(2026-10-04 열람)에만 의존합니다. 2차 출처는 판정에 쓰지 않았습니다. 주체 표기는 1장 113행과 같은 꼴입니다. | 본문 유지. Q-030 유지(작가 직접 열람). | 참고 |
| 11 | check, 표 7-8 | "tests와 acceptance의 실행 건수가 0보다 크고, 두 줄 모두 실패 0건" 및 명령 | 명령은 모두 맞습니다(echo $?는 Git Bash 등 셸, $LASTEXITCODE는 PowerShell, python app.py, http://localhost:8000/new는 app.py 21, 40~41행). 참고 두 가지: (a) 실제 합격 조건은 실패 0건 외에 건너뜀 0건, project_code 시험 1건 이상, 수용 시험 정확히 5건이 더 있습니다(check.py 28, 32, 35행). 확인 기준 칸의 줄임이 의도인지 확인 필요. (b) 부록 16행은 macOS와 Linux에서 python이 없으면 python3으로 바꾸라고 하는데 7장 표 7-8에는 안내가 없습니다(작가 판단). | 변경 불필요. 원하면 확인 기준 칸 끝에 "(건너뜀 0건, 수용 시험 5건 포함)". | 참고 |

### 일치로 확인한 문장(표에 올리지 않음)

| 위치 | 문장 | 근거 |
|---|---|---|
| 9행 | 충분한 시험 없이 완료로 표시하는 경향 | Young 글 "tendency to mark a feature as complete without proper testing" |
| 9행 | 단위 테스트나 개발 서버에 보내는 curl, 끝까지 동작하지 않음을 알아차리지 못함 | 같은 글 "unit tests or curl commands against a development server", "didn't work end-to-end" |
| 9행 | 브라우저 자동화로 사람처럼 시험하라고 명시 | 같은 글 "explicitly prompted to use browser automation tools and do all testing as a human user would" |
| 12행 | 시험을 실행하고도 알아차리지 못함 | 위와 같음 |
| 26행 | 테스트, 빌드, 화면 캡처 비교 제공, "looks done"이 유일한 신호이고 사용자가 검증 루프가 됨 | Best practices "Give Claude a way to verify its work" |
| 26행 | 새 컨텍스트에서 검토 | Best practices "the agent doing the work isn't the one grading it", "Add an adversarial review step"의 fresh context |
| 46행 | 채점 방법 세 가지, 가장 빠르고 신뢰할 수 있고 확장하기 쉬운 방법, 코드 기반 예, LLM 신뢰도 시험 후 확대, 사람은 가능하면 피하라 | develop-tests "Grade your evaluations": "choose the fastest, most reliable, most scalable method", "Test to ensure reliability first, then scale", "Avoid if possible" |
| 46행, 표 7-4 | 입력 열, 코드 기반과 사람의 판정 형식, 사람 채점 용도는 이 책의 정리 | 문서에 없음. 본문이 이를 밝혀 둠(R13 충족) |
| 52행 | 첫 문장 회사 이름 기준, 정답/오답 또는 1~5점, 정성 평가의 한계 | Acme Inc. 예와 "Be empirical or specific" |
| 53행 | 정답을 예시 답안으로 두고 채점 모델이 비교 | LLM 예제 grade_completion(output, golden_answer). golden answer가 rubric 자리로 들어가며 비교한다는 서술은 맞음 |
| 92행 | 금지 규칙은 편집 도구, 인식되는 셸 파일 명령(sed, tee 등), 출력 저장 대상에 적용되고 Python 스크립트의 간접 쓰기에는 미적용 | permissions "Read and Edit": "`Edit` rules apply to all built-in tools that edit files", 경고문의 cat, head, tail, sed, tee와 리다이렉션, "a Python or Node script that opens files itself" 미적용 |
| 93행 | PostToolUse 훅 실패 시 종료 코드 2로 실패 출력을 모델에 전달, 편집은 이미 실행 | Hooks reference 종료 코드 표: PostToolUse는 "Shows stderr to Claude; the tool already ran" |
| 93행 | Stop 훅을 "결정적 관문"으로 설명(키 cc-best-practices) | Best practices "As a deterministic gate". 단정 문제는 필수 1 |
| 92행, 표 7-7 | Edit(./acceptance/**), Edit(./check.py) 금지 | reference/settings.example.json deny와 일치 |
| 88~90행 | 기준 상태 출력 두 줄, 수용 시험 1~3 실패, 종료 코드 1 | 실제 실행 일치(실패: test_1, test_2, test_3) |
| 87행 | 시험 파일이 없으면 0건 실행, 실패 0건 | 빈 폴더 discover 결과 Ran 0 tests, 실패 0건 확인 |
| 인용 키 | 9행 long-running-harness, 26행과 93행 둘째 cc-best-practices, 42행 harness-engineering, 46행과 53행 develop-tests, 92행 permissions, 93행 hooks | bibliography.json의 URL과 저자가 각 출처와 일치. harness-engineering은 내용 미확인 |

## research/ch07-sources.md에 덧붙일 기록 블록

```
## 2026-10-24 fact-checker 재확인(플레이북 정리, 이슈 #115)

- S-C7-1 재확인(https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents, Justin Young, 2025-11-26, 확인 2026-10-24). 원문 일치: "Claude's tendency to mark a feature as complete without proper testing", "unit tests or curl commands against a development server", "didn't work end-to-end", "once explicitly prompted to use browser automation tools and do all testing as a human user would". 실험 주체는 "Opus 4.5 running on the Claude Agent SDK in a loop across multiple context windows"이며 Claude Code 표기 없음. 본문 9행 "개선되었습니다"는 원문 "did well at verifying features end-to-end"보다 넓은 표현(권고).
- S-C7-2 재확인(https://platform.claude.com/docs/en/test-and-evaluate/develop-tests, Anthropic, 게시일 표기 없음, 확인 2026-10-24). "Grade your evaluations" 절: "choose the fastest, most reliable, most scalable method", 코드 기반 "Fastest and most reliable, extremely scalable…", 사람 "Most flexible and high quality, but slow and expensive. Avoid if possible.", LLM "Fast and flexible, scalable and suitable for complex judgment. Test to ensure reliability first, then scale.", Acme Inc. 기준표 예, "Be empirical or specific"(correct/incorrect 또는 1-5). "다른 모델" 주석("Generally best practice to evaluate with a different model from the one used to generate the evaluated output")은 앞쪽 절의 Likert와 이진 분류 LLM 예제에 있고, "Grade your evaluations" 절의 golden answer 예제(claude-opus-5-5로 생성과 채점)에는 없음.
- S-C7-4 재확인(https://code.claude.com/docs/en/permissions, Anthropic, 확인 2026-10-24). "Read and Edit" 절: "`Edit` rules apply to all built-in tools that edit files". 경고문: Read와 Edit deny는 내장 파일 도구, Bash에서 인식되는 cat, head, tail, sed, tee, 리다이렉션 대상에 적용. 파일명을 쓰지 않는 명령과 "a Python or Node script that opens files itself"에는 미적용. 모든 프로세스 차단은 샌드박스("enable the sandbox").
- S-C7-5 재확인(https://code.claude.com/docs/en/hooks, Anthropic, 확인 2026-10-24, 앞 약 20만 자와 Stop input 절 열람). 종료 코드 2: PostToolUse "Shows stderr to Claude; the tool already ran"(차단 불가), Stop "Prevents Claude from stopping, continues the conversation". exit 1은 비차단 오류, "If your hook is meant to enforce a policy, use exit 2". 새로 확인: Stop input 절의 "8-consecutive-continuation cap"(연속 8회 계속 뒤 다음 차단을 무시하고 턴 종료, 도구 호출 시 횟수 초기화, CLAUDE_CODE_STOP_HOOK_BLOCK_CAP으로 상향). Stop 훅은 onFailure: "block" 대상에서 제외.
- S-C7-6 재확인(https://code.claude.com/docs/en/best-practices, Anthropic, 확인 2026-10-24). "Give Claude a way to verify its work": 검사 제공 문장, "looks done" 유일한 신호, "As a deterministic gate: a Stop hook runs your check as a script and blocks the turn from ending until it passes", "so the agent doing the work isn't the one grading it", "Have Claude show evidence rather than asserting success". "Add an adversarial review step"의 fresh context 검토. 같은 문서의 /goal은 Stop 훅과 별도의 강제 수준.
- S-C7-3(Lopopolo, OpenAI, 2026-02-11) 미확인 유지. 2026-10-24 재시도: https://openai.com/index/harness-engineering/ 와 https://www.openai.com/index/harness-engineering 모두 ENOTFOUND. 검색 요약으로 확인된 것은 게시일, 저자, 5개월, 직접 작성한 코드 0줄, Codex가 앱 로직과 테스트와 CI 설정과 문서를 작성했다는 것까지. lint와 CI 문장, 사람 역할 문장은 research/ch01-sources.md S2 기록에만 의존(Q-030).
- 예제 실행 확인(2026-10-24, Linux, Python 3.13.16, examples/expense-app 임시 복사본): python check.py 2>/dev/null 표준 출력
    tests: 실행 3건, 실패 0건, 건너뜀 0건, project_code 시험 0건
    acceptance: 실행 5건, 실패 3건, 건너뜀 0건(정한 수 5건)
  종료 코드 1(실패: test_1_form_offers_project_codes, test_2_unknown_code_rejected_with_reason, test_3_list_shows_project_code). 본문 88~90행과 일치. app.py: 포트 8000, 경로 /new. settings.example.json deny: Edit(./acceptance/**), Edit(./check.py). 7장 발췌 코드는 check.py의 단순화 판(ACCEPTANCE_COUNT, project_code 검사, 건너뜀 집계 생략).
- 본문 조정 제안(2026-10-24): Stop 훅 "통과할 때까지" 단정에 연속 차단 상한 추가(필수), check.py를 훅에서 쓸 때 exit 2 변환 안내, 발췌 단순화 표시, 샌드박스 안내, 다른 모델 주석의 출처 예제 구분, 52행 위첨자 추가, 10행 해석 주체 표시.
```

필수 1, 권고 8, 참고 2, 확인한 사실 문장 31개

관련 파일(절대 경로)
- /home/user/harness-book/src/chapters/ch07.html
- /home/user/harness-book/research/ch07-sources.md
- /home/user/harness-book/examples/expense-app/check.py
- /home/user/harness-book/examples/expense-app/reference/settings.example.json
- /home/user/harness-book/examples/expense-app/app.py
- /home/user/harness-book/src/chapters/ch01.html (101, 105, 113행)
