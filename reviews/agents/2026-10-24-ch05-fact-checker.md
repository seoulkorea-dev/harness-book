# 5장 사실 점검 보고 (fact-checker, 2026-10-24)

범위: src/chapters/ch05.html 전체(HEAD 00e5635), research/ch05-sources.md, research/bibliography.json, docs/specs/ch05-spec.md, docs/example-facts.md, examples/expense-app/(reference/ 포함). 원고와 다른 파일은 고치지 않았습니다.

## 요약
필수 2, 권고 8, 참고 8 (확인한 사실 문장 약 74개)

- 필수 1: 세 곳(8, 35, 55행)의 "Claude Code의 컨텍스트 엔지니어링 글"은 주체 오류입니다. 해당 글은 Anthropic Engineering의 모델 전반 글이므로 "Anthropic의"가 맞습니다(4장 판정과 같은 기준). 직전 판(HEAD~1)에는 "Anthropic의"로 되어 있었습니다.
- 필수 2: 표 5-5 넷째 행 "편집 뒤 훅이 실행한 단위 테스트 결과"는 예제 훅이 실패(종료 코드 2)할 때만 에이전트에게 전달됩니다. 통과 출력은 전달되지 않습니다.
- 예제 값(32줄, 여섯 절, 발췌, 금지 경로 여섯 개, reviewer의 도구, 실습 5 요청 문장)은 원본과 모두 일치합니다.
- Codex 하네스 엔지니어링 글: 주체 표기는 맞고 내용은 이번에도 미확인입니다(openai.com이 이 환경에서 열리지 않음, Q-030 유지).
- 다른 장 링크: 7개 모두 도착 절이 있고 문구가 일치합니다. 단 ch03#example의 현재 제목은 "기능 추가 에이전트: CR 구현"이므로 3장 정리 PR이 먼저 병합되어야 문구가 맞습니다.

## 표
| # | 위치 | 문장 | 확인 결과와 근거 | 등급 | 고친 문안 |
|---|---|---|---|---|---|
| 1 | resource 절 8행, retrieval 절 35행, 55행 | "Claude Code의 컨텍스트 엔지니어링 글은 …" (세 곳) | 불일치(발표 주체). 이 글(Rajasekaran 외, Effective context engineering for AI agents, 2025-09-29)은 Anthropic Engineering(Applied AI 팀)이 에이전트와 LLM 전반을 다룬 글이며 Claude Code는 예로만 나옵니다(원문 열람, 2026-10-24). bibliography.json의 venue도 Anthropic. 기준서 7.1("제품과 무관한 글은 회사 이름", "○○의 … 글은"), BOOK_SPEC 7절 둘째 줄, 4장 판정과 1장 수정, 2장 38행("Anthropic의 컨텍스트 엔지니어링 글")과 같은 기준. HEAD~1 판은 "Anthropic의"였고 이번 정리에서 바뀌었음(git diff HEAD~1 HEAD). research C5-7이 이미 "말하는 주체는 At Anthropic, we"로 기록 | 필수 | 8행: "Anthropic의 컨텍스트 엔지니어링 글은 컨텍스트를 한정된 자원으로 다뤄야 한다고 설명합니다." 35행: "두 방법의 설명은 Anthropic의 컨텍스트 엔지니어링 글을 바탕으로 합니다." 55행: "Anthropic의 컨텍스트 엔지니어링 글은 지나치게 압축하면 … 설명하고, Claude Code가 작업 중에 할 일 목록을 만들어 두고 다시 보는 것을 구조화된 노트의 예로 듭니다"(뒷부분의 Claude Code는 글이 든 예의 주체라 유지). 38행 "같은 글은 Claude Code를 혼합 방식의 예로 듭니다"는 그대로 맞음 |
| 2 | 표 5-5 넷째 행(작업 중 수집, 생성 정보) | "편집 뒤 훅이 실행한 단위 테스트 결과" | 불일치(전달 조건 누락). 예제 훅은 reference/settings.example.json의 PostToolUse(Edit\|Write), 명령 `python -m unittest discover tests -q \|\| exit 2`. Hooks 문서(code.claude.com/docs/en/hooks, 종료 코드 절, 2026-10-24): PostToolUse는 종료 코드 0이면 Claude가 훅의 stderr를 보지 못하고 일반 stdout도 컨텍스트에 들어가지 않으며(JSON additionalContext 제외), 종료 코드 2일 때만 stderr가 Claude에게 보임. unittest의 결과는 stderr로 나가므로 통과하면 에이전트는 아무것도 받지 못하고, 실패하면 오류 출력이 전달됨. 표의 문장은 매번 테스트 결과가 컨텍스트에 쌓이는 것처럼 읽힘 | 필수 | "편집 뒤 훅이 실행한 단위 테스트가 실패했을 때의 오류 출력(통과하면 에이전트에게 전달되지 않음)" |
| 3 | kinds 절 14행 | "기본 설정에서 Skill은 이름과 설명만 늘 컨텍스트에 있고" | 부분 불일치. Skills 문서: "skill descriptions are loaded into context … full skill content only loads when invoked". How Claude Code works: "Claude sees skill descriptions at session start". Explore the context window: "skill descriptions". 이름이 함께 올라간다는 문장은 세 문서 어디에도 없음(Skills 문서 100,000자까지 열람, 나머지 18,000자 미열람). `disable-model-invocation: true`이면 설명도 컨텍스트에 없음(기본 설정 한정은 이미 반영됨) | 권고 | "기본 설정에서 Skill은 설명만 늘 컨텍스트에 있고, 본문은 필요할 때 읽힙니다." |
| 4 | resource 절 10행 | "관련 없는 작업으로 넘어갈 때는 /clear 명령으로 새 대화를 시작하고, 긴 대화는 /compact … 요약해 공간을 확보할 수 있습니다" [commands] | 부분 일치. Commands 문서: /clear = "Start a new conversation with empty context", /compact = "Free up context by summarizing the conversation so far". "관련 없는 작업으로 넘어갈 때"라는 사용 시점은 Commands 문서에 없고(해당 문서에서 unrelated, between tasks 검색 결과 없음) Explore the context window의 "Clear between tasks: run /clear when switching to unrelated work"에 있음. 앞 주장을 뒷받침하지 못하는 부분이 있음 | 권고 | 같은 문장 끝에 context-window 인용을 추가하거나, 문장을 둘로 나눠 "관련 없는 작업으로 넘어갈 때는 /clear로 새 대화를 시작합니다<context-window>. /clear는 새 대화를 시작하고 /compact는 요약해 공간을 확보합니다<commands>." |
| 5 | 표 5-2 첫째 행 | "컨텍스트에는 이 네 출처를 거친 정보만 들어오므로, 출처가 없는 자료는 에이전트가 읽지 못함" | 지나친 단순화. How Claude Code works "Context Claude Code adds on its own"와 The context window 절: 시스템 지침, 출력 스타일, 시스템 알림(system reminder), 자동 메모리, MCP 도구 이름, Skill 설명이 네 출처와 별개로 들어감. 같은 표 셋째 행이 "제품의 시스템 지침"을 따로 적어 표 안에서도 어긋남 | 권고 | "에이전트가 읽는 자료는 이 네 출처로 들어오며(제품이 덧붙이는 시스템 지침 제외), 출처가 없는 자료는 에이전트가 읽지 못함" |
| 6 | retrieval 절 41행 | "하위 에이전트는 … 위임할 때 받은 지시와 규칙 문서(CLAUDE.md)를 근거로 작업합니다. … 포크는 예외입니다" | 일치하나 예외 누락. Create custom subagents 문서(What loads at startup): 시작 컨텍스트는 자기 시스템 프롬프트, 위임 메시지, CLAUDE.md 계층, git 상태, skills 필드의 Skill. 내장 Explore와 Plan은 CLAUDE.md와 git 상태를 받지 않고, `omitClaudeMd: true`면 CLAUDE.md도 받지 않음. 이 장의 reviewer는 사용자 정의 하위 에이전트라 CLAUDE.md를 받음(예제와 모순 없음). 포크는 "inherits the parent conversation" 일치 | 권고 | "기본 설정의 하위 에이전트는 … 위임할 때 받은 지시와 규칙 문서(CLAUDE.md)를 근거로 작업합니다(내장 Explore와 Plan은 규칙 문서를 받지 않습니다)." |
| 7 | retrieval 절 35행 | "글은 많은 AI 네이티브 애플리케이션이 임베딩 기반 검색으로 중요한 자료를 모델이 추론하기 전에 찾아 둔다고 설명합니다" | 부분 일치. 원문: "many AI-native applications employ some form of embedding-based pre-inference time retrieval". research C5-7은 "어떤 형태로든"으로 맞췄다고 기록했으나 지금 원고에는 빠져 있어 단정이 원문보다 강함 | 권고 | "… 많은 AI 네이티브 애플리케이션이 어떤 형태로든 임베딩 기반 검색으로 …" |
| 8 | 표 5-7 다섯째 행 | "git show --stat HEAD(commit 전이면 git status) … tasks.json은 그 단위의 '통과' 값만 바뀜" | 명령 출력이 확인 기준을 다 뒷받침하지 못함(R8). 재현(scratchpad의 임시 저장소에서 tasks.example.json의 작업 2 통과 값을 false→true로 바꿔 commit): `git status --short` → ` M tasks.json`, `git show --stat HEAD` → `tasks.json \| 2 +-` / `1 file changed, 1 insertion(+), 1 deletion(-)`. 바뀐 파일 목록 확인은 되지만 어느 작업의 값이 바뀌었는지는 나오지 않음 | 권고 | 확인 방법에 "tasks.json은 git show HEAD -- tasks.json(commit 전이면 git diff tasks.json)으로 바뀐 줄 확인" 추가 |
| 9 | check 절 103행, 표 5-7 첫째 행 | "메모리 파일은 Claude Code가 /context 화면에서 … 표시하는 항목 이름이고" / "메모리 파일 항목에 규칙 문서가 보임" | 일치하나 화면 표기 누락. Memory 문서(Troubleshoot): "run /context and check the list under Memory files". 화면 이름은 영어 "Memory files"라 한글 "메모리 파일"을 찾으면 보이지 않을 수 있음. 같은 문서: v2.1.280 이전에는 /context와 /memory가 직접 읽은 AGENTS.md를 표시하지 않음(버전 주석의 AGENTS.md 사용자에게 해당) | 권고 | 103행에 "(화면에는 Memory files로 표시됩니다)" 추가. 버전 주석에 한 문장은 선택 |
| 10 | kinds 절 13행, 표 5-1 첫째 행 | "상시 규칙은 규칙 문서(Claude Code의 CLAUDE.md)에서 옵니다" | 누락(실무 주의점). How Claude Code works와 Memory 문서: 자동 메모리(MEMORY.md의 처음 200줄 또는 25KB)도 매 세션 시작에 로드되고 Claude가 스스로 씀. 사용자 범위 ~/.claude/CLAUDE.md와 `.claude/rules/`의 paths 없는 규칙도 시작에 로드. 장에는 자동 메모리 언급이 없어 "상시로 읽히는 것은 사람이 쓴 규칙 문서뿐"으로 읽힐 수 있음 | 권고 | 14행 뒤에 한 문장 추가: "Claude Code는 이 밖에 에이전트가 스스로 적은 자동 메모리도 매 세션 시작에 읽습니다. 이 장은 사람이 작성하고 관리하는 규칙 문서를 다룹니다." 또는 작가 확인 |
| 11 | rule-doc 절 61행(나누어서) | "규칙 문서에 @경로를 적으면 그 파일은 시작할 때 함께 읽혀 상시 규칙이 됩니다" | 일치(조건 보강 가능). Memory 문서(Import additional files): "imported files are expanded and loaded into context alongside the CLAUDE.md that references them", 컨텍스트 비용은 줄지 않음, 최대 4단계. 코드 스팬과 코드 블록 안의 @는 가져오지 않음. 하위 폴더 CLAUDE.md가 가져오면 그 파일이 읽힐 때 함께 읽힘. 이 장의 예제 규칙 문서에는 @가 없음(확인) | 참고 | 선택: "…그 규칙 문서와 함께 읽혀(루트 규칙 문서라면 시작할 때)". 가져오기는 컨텍스트 비용을 줄이지 않는다는 점은 Memory 문서 Size 항목에 있음 |
| 12 | maintenance 절 66행 | "수정하거나 삭제할 항목은 폴더 구조나 명령이 변경되었을 때, 같은 내용이 다른 문서에 생겼을 때, 문서가 권장 길이를 넘었을 때 찾아봅니다" | 인용 없음. 앞 문장(추가 시점 네 가지)은 Memory 문서와 일치. 이 문장의 세 조건은 문서에 그대로 없음(Consistency 항목은 "periodically … remove outdated or conflicting", 길이 초과는 시작 시 경고). 책의 권장으로 읽히므로 오류는 아님 | 참고 | 유지. 제품 문서의 안내로 오해될 우려가 있으면 "이 장은 … 때 찾아보기를 권합니다"로 |
| 13 | kinds 절 31행 | "Codex의 하네스 엔지니어링 글에 따르면, Codex로 제품을 개발한 OpenAI 팀은 … 한 파일에 모두 담는 방식이 기대만큼 작동하지 않았다고 밝혔습니다. … 약 100줄의 AGENTS.md가 세부 문서의 위치를 안내하는 구성" | 주체 표기 일치(글 + 제품을 쓴 팀, BOOK_SPEC 7절, 재발 주의 항목 부합). 내용은 미확인: 2026-10-24 openai.com 연결 실패(getaddrinfo ENOTFOUND), 이전 기록은 403. 웹 검색 결과는 "AGENTS.md를 목차처럼 쓴다"는 취지의 2차 요약만 보이고 "약 100줄"은 확인되지 않음. 판정 근거는 research/ch01-sources.md S2(2026-10-04 열람)뿐. bibliography의 작성자 Ryan Lopopolo, 게시일 2026.2.11은 S2와 일치. "기대만큼 작동하지 않았다"는 S2의 "실패"보다 약한 표현 | 참고 | 문장 유지. Q-030(작가가 다른 환경에서 원문 확인) 유지 |
| 14 | rule-doc 절 58행 | "Claude Code는 CLAUDE.md를, Codex는 AGENTS.md를 읽습니다" | Claude Code 쪽은 Memory 문서와 일치. Codex 쪽은 OpenAI 문서를 직접 열지 못함(developers.openai.com 연결 실패). 웹 검색 결과에 공식 Codex 가이드(Custom instructions with AGENTS.md: 디렉터리마다 AGENTS.override.md, AGENTS.md 순으로 확인, project_doc_max_bytes 기본 32 KiB)와 Best practices("loads into context automatically") 요약이 있어 단서는 일치. 10장 기록(openai-2026a) 의존 | 참고 | 유지. 직접 열람은 다른 환경에서 |
| 15 | 1장 137행, 177행 (이 worktree) | "Claude Code의 컨텍스트 엔지니어링 글" | 이 worktree의 ch01.html에는 1장 수정이 아직 없음(기준 브랜치 차이). 5장 수정과 1장 수정 병합 뒤 두 장이 같은 표기("Anthropic의")인지 확인 필요 | 참고 | 병합 순서 확인 |
| 16 | retrieval 절 38행 | "Claude Code는 CLAUDE.md를 작업 전에 컨텍스트에 포함하고, 파일은 … glob과 grep 같은 도구로 필요할 때 찾습니다" | 글의 서술과 일치("CLAUDE.md files are naively dropped into context up front", "primitives like glob and grep"). 제품 문서와 비교하면 루트 CLAUDE.md는 시작 때, 하위 폴더 CLAUDE.md는 해당 폴더 파일을 읽을 때 로드(Memory 문서). 같은 장 13행이 이미 하위 폴더 규칙을 필요할 때 읽는 문서로 분류하므로 모순은 아님 | 참고 | 유지 |
| 17 | 다른 장 링크 | ch03#example, ch06#split, ch08#kinds, ch10#rule-docs, ch02#instruct-enforce, practice#lab-2/lab-3/lab-5 | 도착 앵커 모두 존재. 제목 대조: ch06 "작업 단위 분할", ch08 "기록의 세 종류", ch10 "규칙 문서 비교", ch02 "지시 기반 규칙과 강제 적용"은 링크 문구와 일치. ch03#example의 현재 제목은 "기능 추가 에이전트: CR 구현"이라 링크 문구("예제: 변경 요청 사항의 에이전트 명세서 작성")와 다르고, 3장 정리 PR이 병합되면 일치. 실습 2의 도착 절은 CLAUDE.md 작성과 수정 범위를 묻는 요청 두 줄을 포함해 71행 설명("수정 범위를 묻는 요청")과 맞음 | 참고 | 3장 정리 PR 병합 뒤 재확인 |
| 18 | example 절 83행 | "수정하지 않음의 경로는 권한 설정 예시의 금지 규칙에도 들어 있습니다. 그래서 … 권한 설정은 도구 호출의 강제를 맡습니다" | 경로 여섯 개 일치(deny: data, acceptance, check.py, CLAUDE.md, DECISIONS.md, .claude). Edit 금지 규칙이 셸이 실행한 프로그램의 파일 쓰기까지 막는지는 C5-8에 따라 9장 감수에서 확정 대기. 이번에 새로 확인하지 못함 | 참고 | 9장 감수 결과에 따름 |

## 일치로 판정한 문장(확인 위치)
| 위치 | 문장 요지 | 근거 |
|---|---|---|
| 4행 | 컨텍스트 엔지니어링 정의 [context-engineering] | 원문 정의("strategies for curating and maintaining the optimal set of tokens"), 1장 정의와 같은 문장 |
| 8행 | 토큰이 늘수록 정보를 정확히 떠올리는 능력이 떨어짐 | 원문 "the model's ability to accurately recall information … decreases"(context rot) |
| 10행 | /context는 공간을 차지하는 것을 보여 줌 | Commands: "Visualize current context usage as a colored grid" |
| 10행 | 한도에 가까워지면 오래된 도구 출력을 먼저 지우고 필요하면 요약 | How Claude Code works, When context fills up, 문장 그대로 |
| 14행 | 시점은 Claude Code 문서의 설명을 정리(시작 때 CLAUDE.md 등, 작업 중 경로별 규칙, 파일 읽기) | Explore the context window, What the timeline shows |
| 15행 | 네 종류와 시스템 지침, 불러온 Skill이 같은 윈도 | How Claude Code works, The context window: 대화, 파일, 명령 출력, CLAUDE.md, 자동 메모리, 불러온 Skill, 시스템 지침 (표 5-2 셋째 행도 같은 근거로 일치, 질문 2) |
| 34, 36, 37행 | 식별자(파일 경로, 저장된 쿼리, 웹 링크), 실행 중 탐색이 느림, 도구와 기준이 없으면 컨텍스트 낭비 | 원문 "lightweight identifiers (file paths, stored queries, web links, etc.)", "runtime exploration is slower than retrieving pre-computed data", "can waste context by misusing tools" (새로 붙인 인용 모두 앞 주장을 뒷받침함, 질문 2) |
| 38행 | 가장 작은 신호 강한 정보 묶음을 목표로 함 | 원문 "smallest set of high-signal tokens that maximize the likelihood of your desired outcome" (원문은 컨텍스트 엔지니어링 전반의 지침 원리로 서술, "어느 방법이든"은 이 책의 요약으로 무리 없음) |
| 39, 40행, 표 5-4 | 압축=대화 흐름이 긴 작업, 구조화된 노트=단계별 목표가 있는 개발, 하위 에이전트=병렬 탐색 조사와 분석 | 원문 "extensive back-and-forth", "iterative development with clear milestones", "complex research and analysis where parallel exploration pays dividends" |
| 53행 | 하위 에이전트 요약은 흔히 1,000~2,000 토큰 | 원문 "often 1,000-2,000 tokens" (Anthropic이 소개한 값, 제품 제한 아님) |
| 55행 | 지나치게 압축하면 미묘하지만 중요한 맥락을 잃을 수 있음, 할 일 목록 예 | 원문 "overly aggressive compaction can result in the loss of subtle but critical context", "Like Claude Code creating a to-do list" |
| 56행 | 대화로 준 지시는 요약에서 누락, 루트 CLAUDE.md는 디스크에서 다시 읽힘, 경로별 규칙과 하위 폴더 규칙 문서는 압축 직후 다시 읽히지 않고 해당 파일을 다룰 때 읽힘 | Memory 문서 "Instructions seem lost after /compact", Explore the context window의 What survives compaction 표(원문은 reads, writes, or edits의 trigger file이라 "다시 열 때"는 읽기 한정으로 읽히지 않게만 주의) |
| 59행 버전 주석 | v2.1.277 이상, AGENTS.md만 있을 때, Bedrock과 텔레메트리를 끈 세션은 v2.1.281 이상 | Memory 문서 AGENTS.md 절 표와 When AGENTS.md support is unavailable 절. 형식 "버전 주석 (2026년 10월)" 준수 |
| 60, 61행 | 네 기준의 근거 | Memory 문서 Write effective instructions: "concrete enough to verify", Size/Structure/Consistency, 예시 "API handlers live in src/api/handlers/". 네 기준은 책의 정리라고 60행에 밝힘 |
| 61행 | 200줄 미만 권장 목표, 제품이 강제하지 않음 | Memory 문서 "target under 200 lines", 초과 시 시작 때와 /status에서 경고만 하고 4 MiB 초과 파일만 건너뜀 |
| 64행 | 추가 시점 네 가지 | Memory 문서 When to add to CLAUDE.md, 네 항목 일치 |
| 67행 | CLAUDE.md는 강제 설정이 아닌 컨텍스트, 막으려면 도구 실행 전 훅 | Memory 문서 "context, not enforced configuration … use a PreToolUse hook" |
| 68행 | 권한 규칙=허용, 확인 요청, 금지, 지시와 강제 | BOOK_SPEC 4절 용어표와 같음. settings.example.json의 allow/ask/deny 구조 |
| 70, 71행 | 변경 요청 사항 설명, check.py=단위 테스트와 수용 시험을 함께 실행, reviewer는 파일을 수정하지 않고 수용 기준과 대조 | example-facts.md, check.py(tests와 acceptance를 discover해 실행), reference/reviewer.example.md(tools Read, Grep, Glob) |
| 71행 | 작업 단위 정의, 통과 값(true 또는 false) | BOOK_SPEC 5절 용어표, tasks.example.json의 "통과" 키(작업 1 true, 나머지 false) |
| 72행 | 여섯 절, 빈 줄 포함 32줄 | `wc -l examples/expense-app/reference/CLAUDE.example.md` → 32, `python3 -c "len(read().splitlines())"` → 32. 절: 목적, 읽는 순서, 작업 순서, 수정 범위, 중단 규칙, 명령 |
| 73~81행 코드 상자 | 읽는 순서 절 전체와 수정 범위 절 앞 두 줄 | 원본 CLAUDE.example.md 6~10행, 19~21행과 글자 단위로 같음. 수정 범위 절의 셋째 줄("수용 시험이 실패하면 시험이 아니라 구현을 고친다.")은 발췌에서 빠졌으며 본문이 "발췌"라고 밝힘 |
| 82~84행 | 읽는 순서 첫째가 docs/CR.md, 수정할 수 있음과 수정하지 않음에 겹침 없음 | CLAUDE.example.md, example-facts.md 규칙 문서 절 |
| 84행, 표 5-5 셋째 행 | 요청 문장 "CLAUDE.md의 규칙대로 tasks.json의 다음 작업 단위를 수행해 줘." | src/appendix/practice.html 96행과 110행(실습 5)과 같음 |
| 표 5-5 | 읽는 순서 네 문서, 검토 하위 에이전트 대조 보고, 완료 보고에 check.py 출력 원문 | CLAUDE.example.md 작업 순서 절. 하위 에이전트 요약만 주 대화로 돌아옴: Create custom subagents "only the relevant summary returns to your main conversation" |
| 91행 | 중단 규칙의 인계 메모 항목 다섯 가지(현재 상태, 읽을 문서, 미결정, 다음 작업, 확인 명령), 새 세션에 지난 대화가 없음 | CLAUDE.example.md 26행, How Claude Code works "Each new session starts with a fresh context window" |
| 101행 | reviewer는 시험을 실행하지 않음 | tools가 Read, Grep, Glob뿐(Bash 없음). sub-agents 문서: tools는 허용 목록 |
| 표 5-7 둘째 행 | `wc -l CLAUDE.md`, PowerShell `(Get-Content CLAUDE.md).Count` | wc -l 실행 확인(32). PowerShell은 이 환경에 없어 실행 못 함, 기록 C5-8의 Count 32와 Get-Content 동작(줄 배열)에 의존 |
| 표 5-7 첫째 행 | `/context all`로 항목별 목록 펼침 | Commands: 전체 화면 모드에서 항목별 분류를 접고 all로 펼침 |

## research/ch05-sources.md에 붙일 기록 문안
```
## C5-9. 5장 정리본(HEAD 00e5635) 기술 감수(fact-checker, 2026-10-24)
확인일 2026-10-24. 원문은 영어, 인용은 짧게.
- Rajasekaran 외, Effective context engineering for AI agents (https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents, 2025-09-29): Anthropic Engineering(Applied AI 팀) 게시, 에이전트와 LLM 전반 글이며 Claude Code는 예로만 등장. 발표 주체 표기는 "Anthropic의 … 글"(BOOK_SPEC 7절, 기준서 7.1). 확인한 문장: "the model's ability to accurately recall information from that context decreases", "many AI-native applications employ some form of embedding-based pre-inference time retrieval"(some form of), "lightweight identifiers (file paths, stored queries, web links, etc.)", "runtime exploration is slower than retrieving pre-computed data", "CLAUDE.md files are naively dropped into context up front" + "primitives like glob and grep", "smallest set of high-signal tokens", 압축 "extensive back-and-forth", 구조화된 노트 "iterative development with clear milestones", 하위 에이전트 "(often 1,000-2,000 tokens)"와 "parallel exploration pays dividends", "overly aggressive compaction"
- Anthropic, Hooks reference (https://code.claude.com/docs/en/hooks, 종료 코드 절): PostToolUse는 종료 코드 0이면 Claude가 stderr를 보지 못하고 일반 stdout도 컨텍스트에 넣지 않음(JSON additionalContext 등만 전달), 종료 코드 2이면 "Shows stderr to Claude; the tool already ran". PreToolUse 종료 코드 2는 도구 호출을 막음. 5장 표 5-5의 "훅이 실행한 단위 테스트 결과"는 실패(종료 코드 2) 때만 전달됨
- Anthropic, How Claude Code works (https://code.claude.com/docs/en/how-claude-code-works): The context window 절은 대화, 파일 내용, 명령 출력, CLAUDE.md, 자동 메모리, 불러온 Skill, 시스템 지침이 윈도에 든다고 설명. "Context Claude Code adds on its own"에 출력 스타일, 시스템 알림 등. "Claude sees skill descriptions at session start"(이름 언급 없음). 하위 에이전트는 "starts fresh unless it's a fork". When context fills up 문장 재확인
- Anthropic, Create custom subagents (https://code.claude.com/docs/en/sub-agents, 앞 100,000자): 하위 에이전트 시작 컨텍스트는 자기 시스템 프롬프트, 위임 메시지, CLAUDE.md 계층(Explore와 Plan 제외, omitClaudeMd: true면 제외), git 상태(Explore와 Plan 제외), skills 필드의 Skill. 대화 기록은 보지 못하고 포크만 상속. tools는 허용 목록이며 "tools: Read, Grep, Glob"은 형식이 맞음. 뒤 16,349자는 미열람
- Anthropic, Extend Claude with skills (https://code.claude.com/docs/en/skills, 앞 100,000자): 목록에는 description이 올라간다고만 서술, 이름이 올라가는지는 문서에 명시 없음. disable-model-invocation: true이면 설명도 컨텍스트 밖. 뒤 18,114자는 미열람
- Anthropic, How Claude remembers your project (https://code.claude.com/docs/en/memory): 200줄 미만 목표와 "reduce adherence"; 가져오기는 "loaded into context alongside the CLAUDE.md that references them"(최대 4단계, 코드 스팬 안의 @는 가져오지 않음); 하위 폴더 CLAUDE.md는 그 폴더 파일을 읽거나 쓰거나 편집할 때 로드; paths 없는 규칙은 시작에 로드; AGENTS.md는 CLAUDE.md와 CLAUDE.local.md가 없을 때만 기본으로 읽음, v2.1.277 이상, v2.1.281 이전 Bedrock과 텔레메트리 끈 세션은 CLAUDE.md만 읽음, v2.1.280 이전에는 /context와 /memory에 직접 읽은 AGENTS.md가 표시되지 않음; /context의 "Memory files"; 자동 메모리는 MEMORY.md 처음 200줄 또는 25KB를 매 세션 로드
- Anthropic, Explore the context window (https://code.claude.com/docs/en/context-window): What survives compaction 표(루트 CLAUDE.md와 paths 없는 규칙은 디스크에서 다시 주입, paths 규칙과 하위 폴더 CLAUDE.md는 필요할 때 다시 로드). "Clear between tasks: run /clear when switching to unrelated work"(5장 10행의 사용 시점 근거는 Commands가 아니라 이 문서)
- Anthropic, Commands (https://code.claude.com/docs/en/commands): /clear, /compact, /context [all] 설명은 원고와 일치. 문서에 "unrelated"나 "between tasks" 표현 없음
- OpenAI, Harness engineering: 2026-10-24 openai.com 연결 실패(ENOTFOUND). 웹 검색에서 원문 접근 불가, 2차 요약에는 "약 100줄" 확인되지 않음. 판정은 research/ch01-sources.md S2(2026-10-04)에 의존, Q-030 유지. Codex의 AGENTS.md 읽기: 공식 가이드(developers.openai.com/codex/guides/agents-md)와 Best practices는 검색 결과 요약으로만 확인(직접 열람 불가)
- 예제 대조: reference/CLAUDE.example.md `wc -l` 32, splitlines 32, 여섯 절, 코드 상자 발췌 일치. reviewer.example.md tools Read, Grep, Glob. settings.example.json deny 6개 경로, hooks는 PostToolUse(Edit|Write) `python -m unittest discover tests -q || exit 2`. practice.html 실습 5 요청 문장 일치. 임시 저장소 재현: tasks.json 통과 값 하나를 바꾸어 commit한 뒤 `git show --stat HEAD` → "tasks.json | 2 +-, 1 file changed, 1 insertion(+), 1 deletion(-)"(어느 작업인지는 출력에 없음)
- 링크 대조: ch06#split "작업 단위 분할", ch08#kinds "기록의 세 종류", ch10#rule-docs "규칙 문서 비교", ch02#instruct-enforce "지시 기반 규칙과 강제 적용" 일치. ch03#example 현재 제목 "기능 추가 에이전트: CR 구현"(3장 정리 PR 병합 시 "예제: 변경 요청 사항의 에이전트 명세서 작성")
```

## 장별 점검 질문 10개
| 질문 | 답 |
|---|---|
| 개념 | 컨텍스트, 토큰, 컨텍스트 윈도, 압축, Skill, 경로별 규칙, 하위 에이전트, 포크의 정의는 BOOK_SPEC 5절과 제품 문서에 맞음. 다만 표 5-2 첫째 행의 "네 출처만"은 과도함(#5) |
| 분류 | 네 종류는 이 책의 정리로 밝혔고(14행), 자동 메모리와 사용자 범위 규칙 문서가 어디에 속하는지는 빠져 있음(#10) |
| 논리 | 한도, 종류, 제공 시점, 규칙 문서 작성, 갱신, 예제, 실패, 확인의 흐름에 사실 모순 없음. 표 5-5 훅 항목은 전달 조건을 바로잡아야 함(#2) |
| 범위 | 하위 에이전트의 시작 컨텍스트 예외(#6)와 Skill의 이름(#3)에서 범위가 문서보다 넓거나 단정적 |
| 절차 | `wc -l`, `/context all`은 확인됨. `git show --stat HEAD`는 파일 목록까지만 확인해 줌(#8) |
| 책임 | 발표 주체: Anthropic 글(#1 수정 필요), Codex 글과 OpenAI 팀(주체 맞음, 내용 미확인), Claude Code 문서(맞음) |
| 검증 | 예제 값과 코드 상자는 원본과 일치. reviewer는 시험을 실행하지 않는다는 서술도 일치 |
| 일관성 | 같은 글을 2장은 "Anthropic의", 5장은 "Claude Code의"로 불러 어긋남(#1). 1장 표기는 병합 뒤 확인(#15) |
| 출처 | 모든 인용이 bibliography.json에 있고 하나의 인용은 하나의 문서. 10행 /clear 문장은 근거 문서가 둘(#4). 66행은 인용 없음(#12) |
| 편집 한계 | OpenAI 원문(Harness engineering, Codex 문서)을 열지 못함. Skills와 Create custom subagents 문서의 마지막 일부를 읽지 못함 |

필수 2, 권고 8, 참고 8, 확인한 사실 문장 74개
