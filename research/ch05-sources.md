# Chapter 5 개정 출처(2026-10-20, researcher 확인, 메인 세션 저장)

게시일 표기가 없는 문서는 확인일만 적습니다. 원문은 영어, 인용은 짧게. 기존 기록: research/ch03-10-sources.md "보강 6", S-0520a, S-0520b, research/ch01-sources.md S2(Lopopolo).

## C5-1. Anthropic, How Claude remembers your project(Claude Code Docs)
- URL: https://code.claude.com/docs/en/memory, 확인 2026-10-20
- 길이: "Size: target under 200 lines per CLAUDE.md file. Longer files consume more context and reduce adherence." 200줄 미만이 목표(원고 표현 "200줄 미만을 목표로")
- 추가 시점("When to add to CLAUDE.md") 네 가지: 같은 실수 두 번째, 코드 리뷰 지적, 지난 세션과 같은 정정 재입력, 새 팀원에게 같은 맥락 필요. 원고와 일치
- 작성 기준("Write effective instructions"): "concrete enough to verify", "Keep your files short, organized, and consistent"(Size, Structure, Consistency), 모순되는 지시는 "Claude may pick one arbitrarily". 여러 단계 절차와 일부에만 해당하는 지시는 skill이나 경로별 규칙으로. 원고의 네 항목(구체적, 짧게, 일관되게, 분리)은 이 책의 정리로 밝힘
- 강제 여부: "Claude treats them as context, not enforced configuration. To block an action regardless of what Claude decides, use a PreToolUse hook instead."
- AGENTS.md: CLAUDE.md(또는 .claude/CLAUDE.md, CLAUDE.local.md)가 없고 AGENTS.md만 있으면 AGENTS.md를 읽음. "Reading AGENTS.md directly requires Claude Code v2.1.277 or later."
- /context: "run `/context` in a session and check the list under Memory files"
- 확신: 높음

## C5-2. Anthropic, Commands(Claude Code Docs)
- URL: https://code.claude.com/docs/en/commands, 확인 2026-10-20
- `/context [all]`: 컨텍스트 사용량을 색 격자로 보여 줌. "In fullscreen mode, `/context` collapses the per-item breakdown to keep the grid visible. Pass `all` to expand it."
- `/clear`: "Start a new conversation with empty context." `/compact`: "Free up context by summarizing the conversation so far."
- 확신: 높음

## C5-3. Anthropic, Manage costs effectively, Create custom subagents, Explore the context window(Claude Code Docs)
- URL: https://code.claude.com/docs/en/costs , https://code.claude.com/docs/en/sub-agents , https://code.claude.com/docs/en/context-window, 확인 2026-10-20
- /clear: "Use `/clear` to start fresh when switching to unrelated work." "Aim to keep CLAUDE.md under 200 lines"
- 하위 에이전트: "Delegate these to subagents so the verbose output stays in the subagent's context while only a summary returns to your main conversation."(테스트 실행, 문서 가져오기, 로그 처리)
- 압축 뒤: 프로젝트 루트 CLAUDE.md와 경로 지정 없는 규칙은 다시 주입되고, 대화로만 준 지시는 요약에 포함됨(계속 지킬 지시는 규칙 문서에 두는 근거)
- 확신: 높음

## C5-4. Rajasekaran 외, Effective context engineering for AI agents(Anthropic, 2025-09-29)
- URL: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents, 확인 2026-10-20
- 사전 검색("embedding-based pre-inference time retrieval")과 필요할 때 찾기("lightweight identifiers (file paths, stored queries, web links, etc.)")
- "runtime exploration is slower than retrieving pre-computed data", 지침이 없으면 "an agent can waste context by misusing tools, chasing dead-ends"
- 혼합: CLAUDE.md는 먼저 컨텍스트에, glob과 grep으로 필요할 때
- 세 기법: 압축(대화 흐름 유지), 구조화된 노트("iterative development with clear milestones"), 하위 에이전트("returns only a condensed, distilled summary", 흔히 1,000~2,000 토큰, 병렬 탐색이 효과적인 조사와 분석)
- 컨텍스트가 늘면 "the model's ability to accurately recall information from that context decreases"
- 확신: 높음

## 원고 처리
- "200줄 이내" → "200줄 미만을 목표로"(본문, 실패 표, 확인 표)
- 실패 표 4행 "앞에서 받은 지시를 놓침": 직접 근거 없음 → "컨텍스트가 길어져 앞의 정보를 정확히 떠올리기 어려워질 수 있음"으로 한정하고 Rajasekaran 외 링크
- 그림 5-2의 "색인이 오래될 수 있음": 원문은 필요할 때 찾기의 장점으로 서술 → 그림에서 뺌. "미리 계산된 자료라 빠름"은 원문과 일치
- 확인 표 1행: 전체화면 모드에서는 /context all로 항목별 분류를 펼침
- 참고 자료: Commands 문서 추가, 확인 날짜 2026-10-20
- 사전 검색 문장의 주체 "Claude Code는"은 D-108(Anthropic 엔지니어링 글을 제품명으로 표기)에 따라 유지

## 확인하지 못한 것
- Lopopolo(OpenAI) 원문: 이번에도 403. 1차 근거는 research/ch01-sources.md S2(2026-10-04 열람)뿐. 원고 문장은 그대로 두고 다른 환경에서 다시 확인(작가 확인 Q-030)
- 압축 때 세부 정보 손실 문장(Rajasekaran 외)은 이번에 다시 열지 않음(기존 기록 보강 6 의존)

## C5-5. Anthropic, How Claude remembers your project, "Instructions seem lost after /compact"(Claude Code Docs)
- URL: https://code.claude.com/docs/en/memory, 확인 2026-10-20(fact-checker, 흐름 재검수 PR #39)
- 프로젝트 루트 CLAUDE.md는 압축 뒤 디스크에서 다시 읽혀 주입됨. 하위 폴더 CLAUDE.md와 paths: 경로별 규칙은 해당 파일을 다시 열 때 다시 읽힘. 대화로만 준 지시는 사라질 수 있어 CLAUDE.md에 추가하라고 안내(5장 압축 문단)
- rules는 매 세션 또는 일치하는 파일을 열 때 로드, skill은 호출되거나 관련 있을 때 본문 로드. /context의 Memory files 목록은 시작 때 읽힌 파일

## C5-6. Anthropic, Extend Claude with skills; Create custom subagents; Explore the context window(Claude Code Docs)
- URL: https://code.claude.com/docs/en/skills , /sub-agents , /context-window, 확인 2026-10-20
- skills: 설명만 상시 컨텍스트, 본문은 호출될 때 로드(5장 Skill 풀이)
- sub-agents: 새 컨텍스트에서 시작, 테스트 실행 등 장황한 출력은 위임하고 요약만 받도록 안내(표 5-6 막는 장치). tools에 Bash를 넣으면 읽기 전용이 아님
- context-window: 압축 시뮬레이션에서 경로별 규칙은 복원 대상이 아님(memory 문서를 우선 근거로)

## C5-7. Rajasekaran 외(2025) 재확인, 2026-10-20
- "many AI-native applications employ some form of embedding-based pre-inference time retrieval"(본문 "AI 네이티브 애플리케이션이 어떤 형태로든"으로 맞춤)
- "file paths, stored queries, web links, etc." 일치
- "runtime exploration is slower than retrieving pre-computed data"(본문 "미리 계산해 둔 자료"로 맞춤)
- "Like Claude Code creating a to-do list, or your custom agent maintaining a NOTES.md file" 일치(주체 Rajasekaran 외로 밝힘)
- "overly aggressive compaction can result in the loss of subtle but critical context"(본문 "미묘하지만 중요한 맥락"으로 맞춤)
- 말하는 주체는 "At Anthropic, we"(본문 "Claude Code는 … 설명합니다" 두 곳은 Q-039)

## C5-8. 5장 PR #94 기술 감수(fact-checker, 2026-10-23)
확인일 2026-10-23. 원문은 영어, 인용은 짧게.
- Anthropic, Commands (https://code.claude.com/docs/en/commands): "/clear: Start a new conversation with empty context"; "/compact: Free up context by summarizing the conversation so far"; "/context [all]: ... In fullscreen mode, /context collapses the per-item breakdown ... Pass all to expand it". 본문 일치
- Anthropic, How Claude Code works, "When context fills up" (https://code.claude.com/docs/en/how-claude-code-works): "Claude Code manages context automatically as you approach the limit. It clears older tool outputs first, then summarizes the conversation if needed." 자동 요약 문장의 근거(agent-loop의 "the SDK automatically compacts"는 SDK 주체). "The context window": 대화, 파일 내용, 명령 출력, CLAUDE.md, 자동 메모리, 불러온 Skill, 시스템 지침이 윈도에 들어감. MCP 도구 정의는 지연 로드. 하위 에이전트는 "starts fresh unless it's a fork"
- Anthropic, Explore the context window (https://code.claude.com/docs/en/context-window): 시작 때 CLAUDE.md, 자동 메모리, MCP 도구 이름, Skill 설명 로드. 압축 뒤 루트 CLAUDE.md와 paths 없는 규칙은 다시 주입, paths 규칙과 하위 폴더 CLAUDE.md는 필요할 때 다시 로드. 도구 정의가 윈도를 차지한다는 명시 문장은 없음
- Anthropic, Extend Claude with skills (https://code.claude.com/docs/en/skills): 기본은 설명이 항상 컨텍스트에 있고 본문은 호출 때 로드. disable-model-invocation: true이면 설명이 컨텍스트에 없음
- Anthropic, Create custom subagents (https://code.claude.com/docs/en/sub-agents): 비포크 하위 에이전트는 새 컨텍스트에서 시작하고 대화 기록을 보지 못함. 시작 컨텍스트는 자기 시스템 프롬프트, 위임 메시지, CLAUDE.md 계층(Explore와 Plan은 제외), git 상태, skills 필드의 Skill. 포크는 대화 전체를 상속
- Anthropic, How Claude remembers your project (https://code.claude.com/docs/en/memory): 200줄 미만 목표("reduce adherence", 문제 해결 절 "may reduce adherence"), 모순 지침 "may pick one arbitrarily", @path 가져온 파일은 가져오는 CLAUDE.md와 함께 로드(컨텍스트 비용은 줄지 않음), 추가 시점 네 가지("same mistake a second time"), "context, not enforced configuration ... PreToolUse hook", "Reading AGENTS.md directly requires Claude Code v2.1.277 or later"(Bedrock이나 텔레메트리 끈 세션은 v2.1.281 이전에는 읽지 못함), 압축 뒤 루트 CLAUDE.md 다시 주입, "/context ... Memory files", 200줄 초과 시 시작과 /status에서 경고
- Rajasekaran 외 재열람: "smallest set of high-signal tokens", "often 1,000-2,000 tokens", "overly aggressive compaction", "Claude Code creating a to-do list", "runtime exploration is slower than retrieving pre-computed data", "At Anthropic, we". 사전 검색의 단점으로 "작업 중 새로 필요해진 자료가 빠짐"은 원문에 없음(본문은 이 책의 정리로 밝힘)
- OpenAI, Harness engineering: 2026-10-23 403. 판정은 research/ch01-sources.md S2(2026-10-04)에 의존. Q-030 유지
- 예제 대조: CLAUDE.example.md 32줄 6절(wc -l 32, PowerShell Count 32), settings.example.json deny 6개 경로 일치, reviewer.example.md tools Read, Grep, Glob, 실습 5 요청 문장 일치
- 미확인: Codex가 AGENTS.md를 읽는다는 문장은 Codex 문서 열람 불가로 ch10 기록에 의존. 권한 설정 Edit 금지 규칙의 한계(셸이 실행한 프로그램의 파일 쓰기)는 9장 감수에서 확정

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
