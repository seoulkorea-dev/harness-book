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
