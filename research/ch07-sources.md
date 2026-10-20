# Chapter 7 출처 기록

2026-10-20 researcher 조사(7장 개정, PR #40). 이전 7장 출처는 research/ch03-10-sources.md에 있음.
## 기록

### S-C7-1. Anthropic(Justin Young), Effective harnesses for long-running agents
- URL: https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
- 게시일: Nov 26, 2025(페이지 표기), 확인일: 2026-10-20
- 작성: Justin Young
- 이 장에서 사용할 내용
  - 실패: "Claude's tendency to mark a feature as complete without proper testing"
  - 시험 방식: 단위 테스트나 개발 서버에 대한 `curl` 명령으로 시험했고, 기능이 "didn't work end-to-end"인 것을 알아차리지 못함(원문은 unit tests 또는 curl)
  - 해결: "explicitly prompted to use browser automation tools and do all testing as a human user would"일 때 잘 동작. 스크린샷은 Puppeteer MCP server로 claude.ai 복제본을 시험하며 촬영
  - 실험 주체: "Opus 4.5 running on the Claude Agent SDK in a loop across multiple context windows". 원문에 Claude Code라는 표기는 확인되지 않음(Claude, Claude Agent SDK로 표기)
  - 한계: 확인한 것은 요약 응답이며, 오류를 "발견하고 수정했다"는 문장의 원문 표현은 이번에 직접 대조하지 못함(미확인)
- 확신: 높음(실패 문장, 주체), 중간(발견 후 수정 표현)

### S-C7-2. Anthropic, Define success criteria and build evaluations(Claude Platform Docs)
- URL: https://platform.claude.com/docs/en/test-and-evaluate/develop-tests (페이지 제목 동일, 이전 위치 표기나 이동 안내는 보이지 않음)
- 게시일: 표기 없음, 확인일: 2026-10-20
- 작성: Anthropic
- 절 제목 "Grade your evaluations"
- 이 장에서 사용할 내용
  - "choose the fastest, most reliable, most scalable method"
  - 코드 기반: "Fastest and most reliable, extremely scalable, but also lacks nuance for more complex judgments". 예: exact match(`output == golden_answer`), string match(`key_phrase in output`)
  - 사람: "Most flexible and high quality, but slow and expensive. Avoid if possible."
  - LLM 기반: "Fast and flexible, scalable and suitable for complex judgment. Test to ensure reliability first then scale."
  - 기준표: "Have detailed, clear rubrics"의 예는 첫 문장에 "Acme Inc."를 언급해야 하며, 없으면 "incorrect"로 자동 채점
  - 판정 형식: "Empirical or specific": "correct" 또는 "incorrect" 출력, 또는 1~5점. "Purely qualitative evaluations are hard to assess quickly and at scale."
  - 다른 모델: 예제 코드 주석 "Generally best practice to use a different model to evaluate than the model used to generate the evaluated output." 단 같은 예제 코드가 생성과 채점에 같은 모델(claude-opus-5-5)을 씀
  - 예시 답안: 문서에 golden answer 비교 예 있음(본문 대조는 코드 기반 위주로 확인)
- 확신: 높음(문서 끝 약 3천 자는 읽지 못함)

### S-C7-3. OpenAI(Ryan Lopopolo), Harness engineering: leveraging Codex in an agent-first world
- URL: https://openai.com/index/harness-engineering/
- 게시일: 2026-02-11(검색 결과 표기), 확인일: 2026-10-20 (원문 열람 실패)
- 이 장에서 사용할 내용
  - 이번에 openai.com 접속이 이름 해석 실패(ENOTFOUND)로 막힘. 검색 요약으로만 게시일, 저자, 5개월 실험, "구조 검증은 custom linter와 구조 테스트"류의 2차 요약 확인
  - "문서 구조를 전용 lint와 CI로 검사", "사람은 우선순위, 결과 검증"은 research/ch01-sources.md S2(2026-10-04 열람)의 기록에만 의존
- 확신: 낮음에서 중간. 2차 출처(ZenML, GitLab 이슈 등)는 근거로 쓰지 않음. Q-030(작가 직접 확인) 유지

### S-C7-4. Anthropic, Configure permissions(Claude Code Docs), "Read and Edit"
- URL: https://code.claude.com/docs/en/permissions, 확인일: 2026-10-20
- 이 장에서 사용할 내용
  - "`Edit` rules apply to all built-in tools that edit files."
  - 경고문: Read와 Edit deny 규칙은 내장 파일 도구, Bash에서 인식되는 파일 명령(`sed`, `tee` 등), `> file` 같은 리다이렉션 대상에 적용됨. 파일명을 쓰지 않는 명령이나, "a Python or Node script that opens files itself" 같은 임의 하위 프로세스의 간접 쓰기에는 적용되지 않음. 모든 프로세스를 막으려면 샌드박스를 켜라고 안내
  - 경로 규칙은 `Edit(path)`와 `Read(path)`만 확인됨. `Write(path)`, `NotebookEdit(path)` 규칙은 받아들이지만 참조하지 않음(시작 시 경고). "Use `Edit(docs/**)` in place of `Write(docs/**)`"
  - `Read` deny는 Edit, Write 도구도 같은 경로에서 막음. NotebookEdit은 제외라 Edit deny를 따로 둠
  - 예제 저장소 reference/settings.example.json은 `Edit(./acceptance/**)`, `Edit(./check.py)`를 deny로 둠(문서 권고와 일치)
- 확신: 높음

### S-C7-5. Anthropic, Hooks reference(Claude Code Docs)
- URL: https://code.claude.com/docs/en/hooks, 확인일: 2026-10-20 (페이지 앞 10만 자까지만 읽음)
- 이 장에서 사용할 내용
  - Stop: exit 2는 "Prevents Claude from stopping, continues the conversation". Stop, SubagentStop 등에서 exit 2는 Claude를 계속 작업하게 함
  - PostToolUse: exit 2는 "Shows stderr to Claude; the tool already ran"(도구를 막지는 못함). exit 0의 stderr은 Claude에 보이지 않음
  - exit 1 등 그 밖의 코드는 비차단 오류. "If your hook is meant to enforce a policy, use `exit 2`."
  - 예외: Stop 훅이 exit 2이면서 stdout이 비고 stderr이 파일 없음이면 비차단 오류로 처리
  - 주의: check.py 같은 스크립트를 훅에 쓸 때 실패 종료 코드가 1이면 강제되지 않음. 훅 래퍼에서 2로 바꿔야 함
- 확신: 높음

### S-C7-6. Anthropic, Best practices for Claude Code, "Give Claude a way to verify its work"
- URL: https://code.claude.com/docs/en/best-practices, 확인일: 2026-10-20
- 이 장에서 사용할 내용
  - "Give Claude a check it can run: tests, a build, a screenshot to compare."
  - "Claude stops when the work looks done. Without a check it can run, 'looks done' is the only signal available, and you become the verification loop"
  - 검사의 예: 테스트 모음, 빌드 종료 코드, 린터, 출력을 fixture와 비교하는 스크립트, 브라우저 스크린샷
  - 강제 수준: 한 프롬프트, `/goal`, "As a deterministic gate: a Stop hook runs your check as a script and blocks the turn from ending until it passes", 하위 에이전트의 두 번째 의견
  - "Have Claude show evidence rather than asserting success: the test output, the command it ran and what it returned, or a screenshot of the result."
  - 독립 검수: "so the agent doing the work isn't the one grading it", fresh context 검토
  - 실패 패턴 "trust-then-verify gap": "Always provide verification (tests, scripts, screenshots). If you can't verify it, don't ship it."
  - 훅: "Unlike CLAUDE.md instructions which are advisory, hooks are deterministic"
- 확신: 높음

### ch07 본문 불일치와 주체 표기 점검
| 발견 | 위치 | 근거 | 제안 | 확신 |
|---|---|---|---|---|
| 주체 "Claude Code는 장시간 실행 에이전트 실험에서" | 6행 | Young 원문의 주체는 Claude, 실험은 Opus 4.5 on Claude Agent SDK. Claude Code 표기는 원문에서 확인 안 됨 | D-108(Anthropic 글을 제품명으로 표기)에 따라 유지할지 작가 확인. 유지하면 "Anthropic의 장시간 실행 에이전트 실험" 같은 중립 표기도 가능 | 중간 |
| "단위 테스트까지 실행"이 원문의 일부만 반영 | 6행 | 원문은 단위 테스트 또는 `curl` 명령을 개발 서버에 실행 | 사실 오류는 아님. 정확히 하려면 "단위 테스트나 curl 명령" | 높음 |
| "~발견하고 수정했습니다" 원문 대조 미완 | 6행 | 원문은 브라우저 자동화를 명시하자 잘 동작했다는 취지만 직접 확인 | fact-checker가 해당 문단 재확인 | 중간 |
| "수정을 금지"가 포괄적으로 읽힘 | 55행, 표 7-4(63행) | Edit deny는 내장 편집 도구, 인식되는 Bash 파일 명령, 리다이렉션에 적용. Python 스크립트의 간접 쓰기는 미적용, OS 수준 차단은 샌드박스 | 원고 문장이 "에이전트가 판정 기준을 변경하지 못하게 한다"로 단정함. 한계 한 문장(간접 쓰기 미적용, 샌드박스) 추가나 표현 완화 검토. 표 7-5의 git status 확인이 보완 수단임을 연결 | 높음 |
| 훅으로 강제하는 근거 없음 | 56행(부록 안내만) | Best practices의 Stop 훅 "deterministic gate", hooks 문서의 exit 2 | 검증을 하네스가 강제하는 문장이 필요하면 S-C7-5, S-C7-6 인용. exit 1은 비차단이므로 "실패 시 2로 종료"를 명시 | 높음 |
| 참고 자료 확인일 "2026년 10월 15일" | 80행 | 이번 확인일 2026-10-20 | 2026년 10월 20일로 갱신(문서 게시일 표기 없음은 유지) | 높음 |
| Claude Code 문서(권한, 훅, Best practices) 참고 자료 누락 | 80행 | 55행 권한, 56행 훅 내용의 출처가 참고 자료에 없음 | 새 근거 문장을 넣는 경우 참고 자료 추가 | 높음 |
| 채점 방법 세 가지와 장단점 | 27~28행 | 문서와 일치. "확장하기 쉬운"은 "most scalable"의 풀이로 무리 없음 | 변경 불필요 | 높음 |
| LLM 기반 채점 "문서는 먼저 신뢰도를 시험한 뒤 확대" | 28행 | "Test to ensure reliability first then scale" 일치 | 변경 불필요 | 높음 |
| 사람 채점 "가능하면 피하라" | 28행 | "Avoid if possible" 일치 | 변경 불필요 | 높음 |
| 기준표 예: 첫 문장에 회사 이름 | 29행 | 원문은 "Acme Inc."를 언급해야 하는 예 | 일치. 이름 특정이 필요하면 "예시 회사 이름" | 높음 |
| 판정 형식 "정답/오답 또는 1~5점" | 29행 | 일치("correct/incorrect" 또는 1–5) | 변경 불필요 | 높음 |
| 다른 모델로 평가 | 30행 | 예제 코드 주석의 문구이며, 같은 예제가 같은 모델을 사용 | 원고가 "예제의 설명"이라 정확함. 문서 본문의 규범이 아니라는 점이 유지되는지 확인 | 높음 |
| 그림 7-2 "승인, 반려", "되돌리기 어려운 결정에만" | 31행 SVG, 41행 | Anthropic 문서에 없음. 문서는 사람 채점을 "Avoid if possible"로만 안내 | 이 책의 설계 판단임을 구분. 출처 인용 문장과 섞이지 않게 | 높음 |
| Lopopolo 문장 근거 약함 | 17행 | 원문 열람 실패, 2026-10-04 기록에만 의존 | 문장 유지, "미확인" 표시, 작가 확인 Q-030 | 중간 |

### 미확인
- Lopopolo(OpenAI) 원문: 이번 환경에서 openai.com과 www.openai.com 이름 해석 실패, 검색 요약만 확인. 찾아본 곳: openai.com 세 경로, InfoQ(접속 불가), 검색 결과
- Young 원문의 "오류 발견 후 수정" 정확한 문장
- Claude Platform Docs 문서 마지막 약 3천 자, Hooks 문서 뒤 17만 자(Stop 입력 상세, 연속 차단 상한 등)

### 장의 주장을 뒷받침하기에 근거가 부족한 곳
- "사람은 우선순위와 결과 검증"(Lopopolo)의 1차 근거
- "독립 검수는 결과를 만들지 않은 쪽이 해야 한다"는 Anthropic 근거는 Best practices의 adversarial review와 "the agent doing the work isn't the one grading it"이 있어 보강 가능(표 7-1 독립 검수 행에 사용 가능)
- 수용 시험을 에이전트가 고칠 수 없게 하는 것의 근거는 permissions 문서(S-C7-4)로 충분하나, 한계(간접 쓰기)를 함께 기록해야 정확함

## 2026-10-20 fact-checker 재확인(PR #40)
- S-C7-1 재확인(https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents, Nov 26, 2025, Justin Young, 확인 2026-10-20). 해소: "identify and fix bugs that weren't obvious from the code alone"(브라우저 테스트 도구 사용 시). 실패 문장, curl, end-to-end, 브라우저 자동화 문장 원문 확인. 실험은 "Opus 4.5 running on the Claude Agent SDK"이고 Claude Code 표기 없음. 본문 7행의 주체 "Claude Code"는 불일치(필수).
- S-C7-2 재확인(https://platform.claude.com/docs/en/test-and-evaluate/develop-tests, Anthropic, 게시일 표기 없음, 확인 2026-10-20). "Grade your evaluations" 절 전체 원문 확인(문서 100000자 이후 구간). 세 방법 문구, Acme Inc. 예, "Empirical or specific"이 본문과 일치. 표 7-4의 "입력" 열과 코드 기반 "일치, 불일치"는 문서에 없는 이 책의 정리. "다른 모델" 문구는 LLM 예제 코드의 주석.
- S-C7-4 재확인(https://code.claude.com/docs/en/permissions, Anthropic, 확인 2026-10-20). "Read and Edit" 절. "Edit rules apply to all built-in tools that edit files". 경고문은 인식되는 Bash 파일 명령(cat, head, tail, sed, tee)과 리다이렉션 대상에 적용, 파일을 스스로 여는 스크립트나 파일명을 쓰지 않는 명령에는 미적용, 전면 차단은 샌드박스. Read deny는 Edit, Write도 막고 NotebookEdit은 제외라서 Edit deny를 따로 둠(Write 검사는 v2.1.228 이상).
- S-C7-5 재확인(https://code.claude.com/docs/en/hooks, Anthropic, 확인 2026-10-20, 앞 100000자 열람). 종료 코드 2 표: PostToolUse는 차단 불가(stderr을 Claude에 표시), Stop은 중단 방지. exit 1은 비차단 오류이고, "If your hook is meant to enforce a policy, use exit 2". 새로 확인: `"onFailure": "block"`(v2.1.295 이상)으로 훅 실패를 차단으로 바꿀 수 있음.
- S-C7-6 재확인(https://code.claude.com/docs/en/best-practices, Anthropic, 확인 2026-10-20). "Give Claude a way to verify its work"의 검사 제공 문장, "looks done"이 유일한 신호, Stop 훅 "deterministic gate", "the agent doing the work isn't the one grading it", 증거 제시 문장 일치. "trust-then-verify gap" 실패 패턴과 "hooks are deterministic" 문장도 일치. Stop 훅 연속 차단 상한은 Stop input 절(hooks 문서 후반)에 있고 이번에 미열람.
- S-C7-3(Lopopolo, OpenAI, 2026-02-11) 미확인 유지. openai.com ENOTFOUND(2026-10-20 재시도). 2차 요약은 판정에 쓰지 않음. 7장 38행은 research/ch01-sources.md S2에만 의존.
- 예제 파일 일치 확인(2026-10-20): docs/CR.md, acceptance/test_cr07.py, check.py, RUNLOG.md(2026-10-16 기준 상태), reference/reviewer.example.md, settings.example.json, tasks.example.json 작업 5, app.py(포트 8000, /new)가 7장 본문, 표 7-6, 7-8과 일치.
