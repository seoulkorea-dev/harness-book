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


## C5-9. 5장 사실 점검(fact-checker, 2026-10-24, HEAD 127065a)
확인일 2026-10-24. 원문은 영어, 인용은 짧게. 로컬 Claude Code 2.1.310.
- Anthropic, How Claude remembers your project (https://code.claude.com/docs/en/memory): "target under 200 lines per CLAUDE.md file", 추가 시점 네 가지, "may pick one arbitrarily", "context, not enforced configuration ... PreToolUse hook", @path 가져온 파일은 가져오는 CLAUDE.md와 함께 로드. AGENTS.md는 "no CLAUDE.md in your working directory or above it"일 때 읽음, v2.1.277 이상, Bedrock과 텔레메트리 끈 세션은 v2.1.281 미만에서 불가, v2.1.280 미만은 /memory와 /context 목록에 직접 읽은 AGENTS.md가 보이지 않음. 압축 뒤 루트 CLAUDE.md는 다시 주입, 하위 폴더 CLAUDE.md와 paths 규칙은 on demand. 하위 에이전트의 자동 메모리는 전달되지 않고 포크는 예외.
- Anthropic, Explore the context window (https://code.claude.com/docs/en/context-window), "What survives compaction": 루트 CLAUDE.md와 paths 없는 규칙은 디스크에서 재주입, paths 규칙과 하위 폴더 CLAUDE.md는 on demand 재로드이며 메시지 이력에 있다가 요약에 묻힘. Skill 설명 재주입은 v2.1.304 이상.
- Anthropic, How Claude Code works (https://code.claude.com/docs/en/how-claude-code-works): "When context fills up"(오래된 도구 출력 먼저 삭제, 이어서 요약), "The context window", "Context Claude Code adds on its own"(제품이 직접 더하는 컨텍스트가 네 출처 밖에 있음), 하위 에이전트는 포크가 아니면 새로 시작, `claude --continue`와 `--resume`은 같은 세션 ID로 다시 열기.
- Anthropic, Create custom subagents (https://code.claude.com/docs/en/sub-agents), "What loads at startup": 비포크는 대화 기록 불가, 시스템 프롬프트, 위임 메시지, CLAUDE.md 계층, git 상태를 받음. Explore와 Plan은 CLAUDE.md와 git 상태를 받지 않음. `omitClaudeMd`로 제외 가능. 포크는 부모 대화를 상속하며 인터랙티브 세션에서 기본 켜짐(CLAUDE_CODE_FORK_SUBAGENT=0으로 끔).
- Anthropic, Tools reference (https://code.claude.com/docs/en/tools-reference), "Glob tool behavior": macOS, Linux, WSL에서는 Glob과 Grep이 기본 도구 집합에 없고 Bash의 find와 grep(내장 bfs, ugrep)으로 검색. Windows는 기본 도구. (원고 39행 "glob, grep 같은 도구"의 현재 동작 조건)
- Anthropic, Extend Claude with skills (https://code.claude.com/docs/en/skills): 설명(description)이 상시 컨텍스트, 목록에는 이름도 표시, 본문은 호출될 때 로드, disable-model-invocation: true이면 설명도 컨텍스트에 없음. 설명과 when_to_use는 목록에서 1,536자에서 잘림.
- Anthropic, Commands (https://code.claude.com/docs/en/commands): /context [all], /clear, /compact 설명이 원고와 일치. 사용 시점("관련 없는 작업으로 넘어갈 때")은 context-window의 "Clear between tasks"에 있고 commands에는 없음.
- Anthropic, Embeddings (https://platform.claude.com/docs/en/build-with-claude/embeddings): "Text embeddings are numerical representations of text that let you measure semantic similarity". 원고 임베딩 풀이와 일치.
- Rajasekaran 외(Anthropic, 2025-09-29) 재열람: "context ... must be treated as a finite resource", "embedding-based pre-inference time retrieval"("many AI-native applications employ some form of"), "runtime exploration is slower than retrieving pre-computed data", "smallest possible set of high-signal tokens", "often 1,000-2,000 tokens", "overly aggressive compaction", "Like Claude Code creating a to-do list", 화자 "At Anthropic, we", 저자 Applied AI 팀(Rajasekaran, Dixon, Ryan, Hadfield).
- 예제 대조: CLAUDE.example.md wc -l 32, 여섯 절, 끝 줄바꿈 있음. 발췌 코드 상자 9줄이 원본과 글자까지 같음. settings.example.json deny 6경로 일치. 표 5-7의 git show --stat HEAD는 파일 단위 통계만 보여 통과 값 한 개만 바뀌었는지는 git show HEAD -- tasks.json으로 확인해야 함(임시 저장소에서 재현, 127065a에서 이미 반영).
- 발표 주체 판정: 컨텍스트 엔지니어링 글은 Anthropic Applied AI 팀의 에이전트 일반 글이므로 5장 "Anthropic의"가 글의 화자와 맞음. 1장 "Claude Code의 …"는 Q-039, Q-101 대기.
- 미확인: OpenAI Harness engineering(openai.com DNS 실패, 2차 요약은 방향만 같음, "기대만큼 작동하지 않았다"는 S2의 "실패"를 완화한 옮김), Codex가 AGENTS.md를 읽는다는 문장(developers.openai.com DNS 실패), PowerShell 실행(이 환경에 pwsh 없음, 2026-10-23 기록 의존).
- 원고 대조 불일치(권고 4~16과 필수 1~3 참조): 루트 CLAUDE.md 읽는 순서와 AUTHOR_PREFS.md, "정보가 오는 곳" 단정, 컨텍스트 엔지니어링 정의의 "최신 상태로".
