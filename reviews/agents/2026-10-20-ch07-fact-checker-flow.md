# ch07 fact-checker 점검(2026-10-20, PR #40)

7장 사실 점검 보고(PR #40, 브랜치 ch07-write, src/chapters/ch07.html). 확인일 2026-10-20. 파일은 쓰지 않았습니다.

| # | 심각도 | 위치 | 사실 문장 | 판정 | 근거(주소, 위치, 확인 날짜 2026-10-20) | 제안 |
|---|---|---|---|---|---|---|
| 1 | 필수 | 7행(완료 보고 절 2문단) | "Claude Code는 이 실험에서 에이전트가 충분한 시험 없이 기능을 완료로 표시하는 경향을 보고했습니다" | 불일치(주체) | https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents. 저자 Justin Young, 게시 Nov 26, 2025. 실험 주체는 "Opus 4.5 running on the Claude Agent SDK"이고 Claude Code 표기는 없음 | 주체를 "Anthropic의 Justin Young은 Claude Agent SDK로 실행한 장시간 에이전트 실험에서 … 보고했습니다"로 바꾸거나, 제품명 표기(D-108)를 유지하려면 작가 확인을 받아 DECISIONS.md에 근거를 적습니다 |
| 2 | 권장 | 7행 | "에이전트는 코드를 수정한 뒤 단위 테스트나 개발 서버에 보내는 명령으로 시험했지만, 기능이 처음부터 끝까지 동작하지 않는다는 사실은 알아차리지 못했습니다" | 일치(일부 추가) | 같은 글, failure mode 문단. 원문은 "unit tests or curl commands against a development server", "didn't work end-to-end". "코드를 수정한 뒤"는 원문에 없음 | "코드를 수정한 뒤"를 빼거나 이 책의 풀이로 구분합니다. 명령이 curl임을 밝히면 더 정확합니다 |
| 3 | - | 7행 | "브라우저 자동화 도구로 사람이 사용하는 방식 그대로 시험하라고 명시하자, 에이전트의 결과가 개선되었습니다" | 일치 | 같은 글. "mostly did well at verifying features end-to-end once explicitly prompted to use browser automation tools and do all testing as a human user would" | 변경 불필요 |
| 4 | - | 8행 | "확인 수단을 제공하면 에이전트도 오류를 발견합니다" | 일치(S-C7-1의 미확인 해소) | 같은 글. 브라우저 테스트 도구로 "identify and fix bugs that weren't obvious from the code alone" | 변경 불필요 |
| 5 | 참고 | 38행 | "Codex로 제품을 개발한 팀은 문서 구조를 전용 lint와 CI로 기계적으로 검사했다고 밝혔습니다. 사람은 우선순위를 정하고 결과를 검증하는 역할" | 미확인 | openai.com 원문이 이번에도 ENOTFOUND로 열리지 않았고, 검색 결과는 도입부와 2차 요약(InfoQ, ZenML 등)뿐입니다(2차는 판정 근거에서 제외). 근거는 research/ch01-sources.md S2(2026-10-04 열람)뿐입니다. 찾은 범위: openai.com/index/harness-engineering, 검색 요약 | 문장 유지, 원문 재확인은 작가 확인(Q-030과 같은 방식)으로 AUTHOR_QUEUE에 올립니다 |
| 6 | 권장 | 38행 | 같은 문장 | 형식 | 발표 주체가 "Codex로 제품을 개발한 팀"으로만 나오고 회사 이름이 없습니다. 참고 자료 id(ref-lopopolo-2026) 링크는 있음 | "OpenAI의 Ryan Lopopolo는 Codex로 제품을 개발한 팀이 … 밝혔습니다"로 주체를 밝힙니다. 사례의 주체는 제품 팀(OpenAI 내부 실험 팀)이라는 점도 유지합니다 |
| 7 | - | 23행 | "Claude Code 문서도 … 검사(테스트, 빌드, 화면 캡처 비교)를 제공하라고 안내합니다. 검사가 없으면 결과가 끝난 것처럼 보이는 것이 유일한 신호가 되고, 사용자가 직접 확인을 반복해야 한다" | 일치 | https://code.claude.com/docs/en/best-practices, "Give Claude a way to verify its work". "a check it can run: tests, a build, a screenshot to compare", "'looks done' is the only signal available, and you become the verification loop" | 변경 불필요 |
| 8 | - | 23행 | "일을 한 에이전트가 자기 결과를 채점하지 않도록, 새 컨텍스트에서 검토하게 하는 방법" | 일치 | 같은 절 "By a second opinion" 항목. "the agent doing the work isn't the one grading it". "Add an adversarial review step" 절에서 fresh subagent context | 변경 불필요 |
| 9 | 권장 | 41행, 표 7-4(42~46행) | 표 7-4 캡션 "평가 문서 기준, 사람 채점의 판정 형식과 사용하는 곳은 이 책의 정리" | 일치(출처 표시 불완전) | https://platform.claude.com/docs/en/test-and-evaluate/develop-tests, "Grade your evaluations". 세 방법의 장단점 문구, "choose the fastest, most reliable, most scalable method", 사람 "Avoid if possible", LLM "Test to ensure reliability first then scale"는 일치. 그러나 "입력" 열 전체(결과와 규칙 등)와 코드 기반의 "일치, 불일치"는 문서에 없는 이 책의 정리입니다. 문서에서 일치, 불일치에 해당하는 표현은 exact match와 string match입니다 | 캡션을 "입력 열과 코드 기반 판정 형식, 사람 채점의 판정 형식과 사용하는 곳은 이 책의 정리"로 넓히거나 해당 칸에 "(이 책의 정리)"를 붙입니다. 표에 참고 자료 링크(ref-anthropic-2026a)도 둡니다 |
| 10 | - | 41, 47행 | 코드 기반의 정확 일치와 문구 포함 확인. 기준표 예(첫 문장에 회사 이름이 없으면 오답). 판정 형식(정답, 오답 또는 1~5점). 정성 평가는 빠르고 대량으로 판정하기 어려움 | 일치 | 같은 절. `output == golden_answer`, `key_phrase in output`, "Acme Inc." 예, "'correct' or 'incorrect'" 또는 1~5, "Purely qualitative evaluations are hard to assess quickly and at scale" | 변경 불필요 |
| 11 | 참고 | 48행 | "문서의 예제는 … 예시 답안을 두고 … 예제의 설명에는 결과를 만든 모델과 다른 모델로 평가하는 편이 일반적으로 좋다는 안내" | 일치 | 같은 문서 LLM 기반 채점 예제. golden_answer 비교 코드가 있고, "Generally best practice to use a different model…"는 예제 코드의 주석입니다(본문 규범이 아님) | "예제의 설명"을 "예제 코드의 주석"으로 바꾸면 더 정확합니다. 필수는 아닙니다 |
| 12 | 권장 | 85행, 표 7-7 2행(91행) | "파일 수정 금지 규칙은 파일 편집 도구와, 셸에서 파일 이름이 드러나는 명령에 적용됩니다. … 파일을 스스로 여는 스크립트를 실행해 간접으로 수정하는 경우에는 적용되지 않습니다" / 표: "(파일 편집 도구와 셸 명령에 적용 …)" | 일치(표현이 넓음) | https://code.claude.com/docs/en/permissions, "Read and Edit". "Edit rules apply to all built-in tools that edit files". 경고문은 Bash에서 인식하는 파일 명령(cat, sed, tee 등)과 `> file` 같은 리다이렉션 대상에 적용되고, "a Python or Node script that opens files itself" 같은 임의 하위 프로세스에는 적용되지 않으며 모든 프로세스를 막으려면 샌드박스를 켜라고 안내 | 본문은 "Claude Code가 인식하는 셸 파일 명령과 리다이렉션 대상"으로 좁히고, 표 7-7은 "셸 명령"을 "셸의 인식되는 파일 명령"으로 좁힙니다. 샌드박스 언급은 선택입니다 |
| 13 | - | 86행 | "훅은 파일을 편집한 뒤마다 단위 테스트를 실행하고, 실패하면 종료 코드 2로 끝나 실패 출력을 모델에 돌려줍니다. 편집은 이미 실행된 뒤이므로 훅이 편집을 막지는 못하고" | 일치 | https://code.claude.com/docs/en/hooks, 종료 코드 2 표. PostToolUse는 "Shows stderr to Claude; the tool already ran", 막을 수 없음. exit 1은 비차단 오류라 `\|\| exit 2`가 필요하다는 설명과도 일치. 예제 settings.example.json의 PostToolUse, matcher `Edit\|Write`, `python -m unittest discover tests -q \|\| exit 2`와 일치 | 변경 불필요 |
| 14 | 참고 | 86행 | "검사가 통과할 때까지 응답을 끝내지 못하게 하는 Stop 훅도 있으며, Claude Code 문서는 이를 결정적인 관문으로 설명합니다" | 일치 | best-practices "As a deterministic gate: a Stop hook runs your check as a script and blocks the turn from ending until it passes". hooks 문서의 Stop exit 2는 "Prevents Claude from stopping". 같은 문서가 연속 차단 상한(cap)이 있음을 따로 안내(Stop input 절, 이번에 상세 미열람) | 필요하면 "연속 차단에는 상한이 있다"를 덧붙입니다. 현행 문장은 문서 문구와 일치합니다 |
| 15 | - | 85행 외 | 훅 문서에 새로 보인 `"onFailure": "block"`(v2.1.295 이상)으로 exit 1도 차단 설정 가능 | 낡음 아님(본문과 충돌 없음) | hooks 문서, exit 1 설명. 본문은 exit 1이 항상 비차단이라고 쓰지 않았음 | 본문 변경 없음. 버전 주석 불필요. 10장 등에서 "exit 1은 비차단"이라고 단정하는 곳이 있으면 따로 점검합니다 |
| 16 | - | 6~9, 60~104행 | 예제 파일과의 일치: 수용 기준 5개(CR.md), 수용 시험 1~5 대응(test_cr07.py), check.py 코드 발췌, 기준 상태 출력, reviewer 도구(Read, Grep, Glob)와 판정값, 작업 5 확인 방법, localhost:8000/new | 일치 | CR.md 수용 기준 1~5 = 본문 60행, test_1~5 = 표 7-6 "수용 시험 1~5". check.py 13행의 종료 조건과 본문 79행 동일(발췌는 docstring 생략, import 한 줄 병합). RUNLOG.md 기준 상태 "tests: 실행 3건, 실패 0건 / acceptance: 실행 5건, 실패 3건 / exit=1(실패 test_1~3)" = 82~83행. reviewer.example.md의 tools와 보고 형식 = 84행. tasks.example.json 작업 5 "사람 승인(통과 값은 사람이 변경)" = 표 7-6 4행, ch06 54행. app.py의 8000 포트와 /new 경로 = 표 7-8. settings.example.json deny의 `Edit(./acceptance/**)`, `Edit(./check.py)` = 85행 | 변경 불필요 |
| 17 | - | 9행 | 작가의 작업 방식: 빌드, lint, 사이트 검증 출력, GitHub Actions | 일치 | CLAUDE.md의 검사 절차, tools/check_all.py(빌드, 금칙어, lint, 그림 점검), .github/workflows/check.yml, verify-site.yml | 변경 불필요 |
| 18 | - | 81, 86행 | 부록 링크 practice.html#lab-1, #lab-4. ch02 #instruct-enforce, ch03 #files, #example, ch06 #split, #selection, #example | 일치 | src/appendix/practice.html 17행(lab-1)과 50행(lab-4), 각 장 id 확인. lab-4는 ch07.html#example로 되돌아 링크 | 변경 불필요 |
| 19 | - | 전체 | 버전 주석 필요 여부 | 해당 없음 | 훅, 권한, Best practices 문구에서 본문과 달라진 사실을 찾지 못해 낡음 판정이 없습니다. 7장에 aside.footnote가 없는 것은 규칙 위반이 아닙니다 | 추가 불필요 |


## 처리(메인 세션)
| 항목 | 처리 | 내용 |
|---|---|---|
| 1 필수(Young 글 주체) | 작가 확인 | D-108(본문 주체는 제품명 기본, Anthropic 엔지니어링 글 포함)에 따라 유지. 같은 유형인 Q-039에 7장 문장을 이미 추가함(권장안 "Anthropic의 장시간 실행 에이전트 실험") |
| 2 | 반영 | "코드를 수정한 뒤" 삭제, "curl 명령" |
| 5 | 작가 확인 | Lopopolo 원문 미확인, Q-030 유지 |
| 6 | 유지 | D-108(제품명 Codex 기본) |
| 9 | 반영 | 표 7-4 캡션에 입력 열, 코드 기반 판정 형식도 이 책의 정리로 |
| 11 | 반영 | "예제 코드의 주석" |
| 12 | 반영 | 본문과 표 7-7의 적용 범위를 인식되는 셸 파일 명령으로 좁힘 |
| 14 | 유지 | 연속 차단 상한은 이 장 범위 밖 |
