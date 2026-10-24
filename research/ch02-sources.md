# Chapter 2 사실 확인 기록

확인일: 2026-10-04. 원문을 직접 열어 확인한 내용만 적습니다.

## S1. Anthropic, Prompting best practices (Claude Platform Docs)

- URL: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
- 페이지에 게시일 표기 없음(검색 메타데이터 2026-08-21). 확인일로 표기
- 2장에서 사용한 내용
  - 명확하고 명시적인 지시에 잘 반응함. 원하는 출력 형식과 제약 조건을 구체적으로 지정
  - 단계의 순서나 완결성이 중요하면 번호 목록이나 글머리 기호로 순차 지시
  - 지시의 이유(맥락, 동기)를 함께 주면 목표를 이해해 더 맞는 응답을 함
  - 예시는 출력 형식, 어조, 구조를 조정하는 가장 신뢰할 수 있는 방법 중 하나. 실제 사례와 가깝게, 다양하게, 태그로 구분. 3~5개 권장
  - XML 태그로 지시, 맥락, 예시, 입력을 구분하면 해석 오류가 줄어듦
  - 하지 말 것 대신 할 것을 지시(예: 마크다운 금지 대신 문단으로 작성)
  - 최신 모델은 정확한 지시 이행에 맞춰 훈련됨. "변경을 제안해 줄 수 있어?"는 제안만, "이 함수를 변경해 줘"는 실행
  - 시스템 프롬프트의 역할 지정

## S2. Anthropic, Prompt engineering overview (Claude Platform Docs)

- URL: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview
- 2장에서 사용한 내용
  - 프롬프트 엔지니어링 전에 성공 기준의 명확한 정의, 그 기준으로 시험하는 방법, 첫 초안이 있어야 함
  - 모든 성공 기준이나 실패한 평가가 프롬프트 엔지니어링으로 가장 잘 해결되는 것은 아님. 지연 시간과 비용은 다른 모델 선택으로 더 쉽게 개선되기도 함

# 2026-10-20 ch02 v1.0 보강 확인(fact-checker)

## S23. Anthropic, Hooks reference / Automate actions with hooks(Claude Code Docs)
- URL: https://code.claude.com/docs/en/hooks , https://code.claude.com/docs/en/hooks-guide
- 게시일: 표기 없음, 확인일: 2026-10-20
- 작성: Anthropic
- 2장 확인 방법 절(표 2-5 검증 행)에서 사용한 내용
  - PostToolUse 훅이 종료 코드 2로 끝나면 도구는 이미 실행된 뒤이므로 차단하지 못하고 오류 출력을 모델에 전달
  - 성공한 훅의 출력은 디버그 로그로 가며 대화 기록에 나타나지 않음. 대화 기록에는 차단이나 실패 때 hook error 알림이 보임
  - 훅 확인: /hooks는 읽기 전용 목록, 실행 기록은 claude --debug
  - 훅 명령은 현재 디렉터리에서 실행, CLAUDE_PROJECT_DIR은 프로젝트 루트

## S24. Anthropic, Configure permissions(Claude Code Docs)
- URL: https://code.claude.com/docs/en/permissions
- 게시일: 표기 없음, 확인일: 2026-10-20
- 작성: Anthropic
- 사용한 내용
  - Edit 규칙은 파일을 수정하는 내장 도구 전체에 적용
  - Read, Edit deny는 Bash의 인식되는 파일 명령과 리다이렉션에도 적용되나, Python 스크립트 같은 간접 접근은 막지 못함. 운영 체제 수준 강제는 샌드박스
  - 이름만 쓴 WebFetch deny는 도구를 제거함
  - ./path는 현재 디렉터리 기준
  - /permissions는 규칙과 규칙이 나온 설정 파일을 보여 줌


# 2026-10-20 ch02 개정(구성 요소 깊이 보강) 확인(researcher)

Claude Code 문서는 게시일 표기가 없어 확인일만 적는다. 설정 키와 기본값은 확인일 기준이다.

## S25. Anthropic, Configure permissions(Claude Code Docs). S24 보강
- URL: https://code.claude.com/docs/en/permissions
- 확인일: 2026-10-20, 작성: Anthropic
- 평가 순서는 deny, ask, allow이고 처음 일치하는 규칙이 결과를 정함. 구체성은 순서를 바꾸지 않아 allow로 deny의 예외를 만들 수 없음
- 이름만 쓴 deny(Bash, WebFetch 등)는 도구를 컨텍스트에서 제거함. 범위를 쓴 규칙(Bash(rm *))은 도구를 남기고 일치하는 호출만 막음
- Edit 규칙은 파일을 수정하는 모든 내장 도구에 적용. Write 같은 도구 이름으로 쓴 경로 규칙은 참조되지 않으므로 Edit(경로)로 씀
- Read, Edit deny는 내장 파일 도구, Bash가 인식하는 파일 명령(cat, sed, tee 등), 리다이렉션에 적용. 파일을 스스로 여는 Python, Node 스크립트는 막지 못함(샌드박스 필요)
- Bash 규칙은 명령 문자열 일치. Bash(git push *)는 git -C . push 같은 변형과 일치하지 않음. 확실한 보장은 샌드박스나 PreToolUse 훅
- 경로 표기: //path 절대 경로, ~/path 홈, /path 설정 파일 출처 기준, path 또는 ./path 현재 디렉터리 기준
- PreToolUse 훅이 allow를 돌려줘도 일치하는 deny는 막고 ask는 물음
- /permissions는 모든 규칙과 출처 설정 파일을 보여 주고, 바꾼 규칙은 같은 턴의 다음 도구 호출부터 적용

## S26. Anthropic, How Claude remembers your project(Claude Code Docs)
- URL: https://code.claude.com/docs/en/memory
- 확인일: 2026-10-20, 작성: Anthropic
- 세션은 새 컨텍스트로 시작하고, 지식을 이어 주는 장치는 CLAUDE.md와 자동 메모리
- 둘 다 "context, not enforced configuration". 동작을 막으려면 PreToolUse 훅. 기술적 강제는 permissions.deny, 행동 안내는 CLAUDE.md
- 반드시 특정 시점에 실행할 것은 훅으로 씀
- CLAUDE.md는 파일당 200줄 미만 권장, 모순되는 지시는 임의로 하나를 따를 수 있음, @가져오기는 컨텍스트 비용을 줄이지 않음
- 자동 메모리: 로컬 세션에서 기본 켜짐, 기기 로컬, MEMORY.md 첫 200줄 또는 25KB 로드
- git 커밋이 세션 사이에 지식을 전달한다는 직접 설명은 이 문서에 없음(미확인)

## S27. Anthropic, Debug your configuration(Claude Code Docs). S21 보강
- URL: https://code.claude.com/docs/en/debug-your-config
- 확인일: 2026-10-20, 작성: Anthropic
- CLAUDE.md는 좋은 결정을 돕는 안내, 권한과 훅은 Claude의 결정과 무관하게 한계를 강제. 보안 경계와 절대 일어나면 안 되는 일에는 권한이나 훅
- 확인 명령: /context, /memory, /hooks, /mcp, /permissions, /doctor, /status
- 설정 병합: managed 먼저, 나머지는 local, project, user 순으로 가까운 범위가 덮어씀
- 훅은 settings.json의 "hooks" 아래에만 둠. matcher는 한 문자열("Edit|Write"), 대소문자 구분, 철자 오류는 조용히 실패
- Bash(rm *) deny는 /bin/rm이나 find -delete를 막지 못함
- 사용자 정의 하위 에이전트는 CLAUDE.md를 로드함(Explore, Plan 제외)

## S28. Anthropic, Hooks reference / Automate actions with hooks(Claude Code Docs). S23 보강
- URL: https://code.claude.com/docs/en/hooks , https://code.claude.com/docs/en/hooks-guide
- 확인일: 2026-10-20, 작성: Anthropic
- 훅은 수명 주기의 정해진 지점에서 실행되는 셸 명령. 모델의 선택에 기대지 않고 정해진 동작이 항상 일어나게 함
- 종료 코드 2: PreToolUse는 도구 호출을 차단(stderr가 이유), PostToolUse는 차단하지 않고 stderr를 모델에 보여 줌(도구는 이미 실행됨)
- 성공한 훅의 stdout은 대부분 디버그 로그로 가고 대화 기록에 나타나지 않음. 차단이나 실패 때 hook error 알림. Ctrl+O 대화 기록 보기
- 구조: settings.json "hooks" → 이벤트 → matcher 그룹 → 처리기(type: command)
- /hooks는 읽기 전용 목록, 실행 기록은 claude --debug
- 판단이 필요한 결정에는 prompt 훅이나 agent 훅을 쓸 수 있음

## S29. Anthropic, Manage costs effectively(Claude Code Docs). S22 보강
- URL: https://code.claude.com/docs/en/costs
- 확인일: 2026-10-20, 작성: Anthropic
- MCP 도구 정의는 기본 지연 로드(이름과 서버 지시만 컨텍스트에). /context로 점유 확인
- 명령줄 도구(gh, aws 등)가 MCP 서버보다 컨텍스트 효율이 좋음. 쓰지 않는 서버는 /mcp에서 끔
- 특정 작업 절차는 skills로 옮기고 CLAUDE.md는 200줄 미만
- 출력이 많은 작업은 하위 에이전트에 맡기면 요약만 돌아옴(하위 에이전트 요청도 사용량에 포함)

## S30. Anthropic, Connect Claude Code to tools via MCP(Claude Code Docs)
- URL: https://code.claude.com/docs/en/mcp
- 확인일: 2026-10-20, 작성: Anthropic
- 도구 검색은 기본 켜짐, 시작 때 도구 이름과 서버 지시만 로드. 서버당 도구 상한 없음, 실질 한계는 컨텍스트 예산
- alwaysLoad: true인 서버의 도구는 매 턴 컨텍스트를 차지
- MCP 출력 10,000 토큰 넘으면 경고, 기본 25,000 토큰 제한
- MCP 도구 권한 규칙은 mcp__서버__도구

## S31. Anthropic, Create custom subagents(Claude Code Docs)
- URL: https://code.claude.com/docs/en/sub-agents
- 확인일: 2026-10-20(끝 약 9,500자 미열람), 작성: Anthropic
- 정의 파일은 YAML frontmatter가 있는 Markdown, 필수 name, description. 위치 .claude/agents/, ~/.claude/agents/
- tools는 허용 목록, 생략하면 모든 도구 상속. disallowedTools는 거부 목록
- 문서의 읽기 전용 검토 에이전트 예(tools: Read, Grep, Glob)가 reviewer.example.md와 같은 구조
- 하위 에이전트는 대화 기록을 보지 못하고 CLAUDE.md는 로드, 주 세션의 자동 메모리는 받지 않음. 부모의 permissions.deny는 하위 에이전트에도 적용
- /agents는 현재 안내 문구를 출력(v2.1.197 이하에서 대화형 화면)

## S32. Anthropic, Explore the context window(Claude Code Docs)
- URL: https://code.claude.com/docs/en/context-window
- 확인일: 2026-10-20, 작성: Anthropic
- 시작 때 로드: 시스템 프롬프트, 자동 메모리, 환경 정보, MCP 도구 이름, 스킬 한 줄 설명, CLAUDE.md. 페이지의 토큰 수는 시뮬레이션 값이라 인용하지 않음
- "내장 도구 정의가 컨텍스트를 차지"한다는 직접 문장은 이 페이지에 없음(/context의 system tools 범주는 S21)

## S33. Anthropic, Commands(Claude Code Docs). S20 보강
- URL: https://code.claude.com/docs/en/commands
- 확인일: 2026-10-20, 작성: Anthropic
- /agents(현재 안내 문구), /hooks(읽기 전용), /memory, /doctor, /permissions, /context

## S34. Anthropic, Effective context engineering for AI agents
- URL: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- 게시일: 2025-09-29, 확인일: 2026-10-20, 작성: Rajasekaran 외
- 흔한 실패는 도구 집합이 비대해져 어느 도구를 쓸지 모호한 결정 지점이 생기는 것. 최소한의 실행 가능한 도구 집합
- 구조화된 노트 작성(컨텍스트 밖 파일에 쓰고 나중에 읽음)

## S35. Anthropic, Writing effective tools for agents with agents
- URL: https://www.anthropic.com/engineering/writing-tools-for-agents
- 게시일: 2025-09-11, 확인일: 2026-10-20, 작성: Ken Aizawa 외
- "More tools don't always lead to better outcomes." 소수의 잘 설계한 도구, 겹치는 도구는 혼란을 만듦

## S36. OpenAI, Harness engineering(Lopopolo). S2 재확인 시도
- URL: https://openai.com/index/harness-engineering/
- 게시일: 2026-02-11, 확인일: 2026-10-20
- 403으로 원문 열람 실패. "강제되는 형태로 저장소에 추가"는 ch01-sources.md S2(2026-10-04 열람) 기록에만 근거. 작가가 원문 확인 필요

## 확인하지 못한 것과 근거가 부족한 곳(2026-10-20)
- git 커밋이 세션 사이 지식을 전달한다는 Anthropic 문서의 직접 설명 없음(이 책의 정리로 밝히거나 Young 2025로 한정)
- "내장 도구 정의가 컨텍스트를 차지"한다는 직접 문장 없음(/context system tools 범주까지 확인). 지금 2장 본문 "Agent SDK 문서에 따르면 내장 도구의 정의는 요청마다 컨텍스트에 들어가고"의 출처 재확인 필요
- 다섯 구성 요소 분류는 이 책의 정리(1차 출처에 같은 분류 없음)
- 예제 훅 `|| exit 2`가 Windows PowerShell에서 그대로 동작하는지 미시험
- reviewer 호출은 CLAUDE.md 지시뿐이며 강제 장치 없음

# 2026-10-20 그림 2-2, 표 2-2 fact-checker 확인(그림 체계 통일)

## S37. Anthropic, How the agent loop works(Agent SDK, Claude Code Docs). S5 보강
- URL: https://code.claude.com/docs/en/agent-sdk/agent-loop, 확인일: 2026-10-20
- 루프: Receive prompt(시스템 프롬프트, 도구 정의, 대화 이력) → Evaluate and respond(텍스트 응답 또는 도구 호출 요청) → Execute tools(SDK가 실행) → Repeat → Return result. 권한 확인은 별도 단계가 아님(그림 1-2의 단계 번호는 이 책의 정리)
- 도구 거부: "When a tool is denied, Claude receives a rejection message as the tool result"
- 병렬 실행: Read, Glob, Grep 같은 읽기 전용 도구는 동시 실행 가능, Edit, Write, Bash는 순차 실행
- 컨텍스트: 핵심 내장 도구(Bash, Read, Edit 등)의 정의는 매 요청에 들어가고, MCP 도구와 그 밖의 내장 도구는 도구 검색이 기본 지연 로드. "Every tool definition takes context space"

## S25 재확인(permissions 문서, 2026-10-20)
- "Rules are evaluated in order: deny, then ask, then allow." 이름만 쓴 deny는 도구를 컨텍스트에서 제거. "Ask rules prompt for confirmation"
- 미확인: dontAsk, auto 모드에서 ask 규칙이 사람 승인으로 이어지는지

## S38. Anthropic, How Claude Code works
- URL: https://code.claude.com/docs/en/how-claude-code-works, 확인일: 2026-10-20
- 루프는 gather context, take action, verify results. MCP 도구 정의는 기본 지연 로드, 이름과 서버 지시만 컨텍스트에 둠

# 2026-10-20 ch02-accuracy 사실 확인(fact-checker, 이슈 #10)

## S39. Model Context Protocol, Specification: Tools (revision 2026-07-28)
- URL: https://modelcontextprotocol.io/specification/latest/server/tools, 확인일: 2026-10-20
- tools/list는 도구 정의 전체를 페이지 단위로 돌려줌. 정의를 미루거나 도구를 검색하는 규정은 없음(S30의 "규약이 아니라 Claude Code의 기능" 판정의 보조 근거, 부재 확인)

## S30 보강(mcp 문서 "Scale with MCP tool search", 확인일 2026-10-20)
- 도구 검색 기본 켜짐: 시작 때 도구 이름과 서버 지시만 로드, 정의는 필요할 때. ENABLE_TOOL_SEARCH, 서버별 alwaysLoad로 조절
- 예외: 이전 세대 모델, 비공식 ANTHROPIC_BASE_URL, Azure의 Foundry 배포는 처음부터 로드

## S37 보강(agent-loop, 확인일 2026-10-20)
- "Evaluate and respond"에서 모델이 도구 호출을 요청, "Execute tools"에서 SDK가 실행. 문서는 harness라는 말을 쓰지 않음
- 세션 ID로 재개하면 이전 컨텍스트가 복원됨

## S25 보강(permissions, 확인일 2026-10-20)
- 이름만 쓴 deny는 도구를 컨텍스트에서 제거, Bash(*)도 같음, EndConversation은 제외. 범위 규칙은 도구를 남기고 호출 시 차단

## S26 보강(memory, 확인일 2026-10-20)
- 세션은 새 컨텍스트로 시작. 재개는 claude --resume, /resume 등 사용자 동작

# 2026-10-20 표 2-2 새 행과 그림 2-2 사실 확인(fact-checker, 이슈 #21)

## S25 보강(permissions, 확인일 2026-10-20)
- "Ask rules prompt for confirmation whenever Claude Code tries to use the specified tool." ask 규칙은 auto 모드에서도 프롬프트로 남음(Bash 절의 git clean 예). 이름만 쓴 deny는 도구를 컨텍스트에서 제거, Bash(*)도 같음, EndConversation은 예외

## S40. Anthropic, Configure permissions(Agent SDK, Claude Code Docs)
- URL: https://code.claude.com/docs/en/agent-sdk/permissions, 확인일 2026-10-20
- 평가 흐름: 훅 → deny 규칙 → ask 규칙 → 권한 모드 → allow 규칙 → canUseTool 콜백. dontAsk 모드는 프롬프트가 필요한 호출을 거부로 바꿈(S25 재확인의 미확인 해소)

## S41. Anthropic, Handle approvals and user input(Agent SDK, Claude Code Docs)
- URL: https://code.claude.com/docs/en/agent-sdk/user-input, 확인일 2026-10-20
- 승인이 필요한 호출에서 사용자 확인을 받음. deny 응답이면 "tool doesn't execute, Claude sees the message"
- 한계: 대화형 CLI 대화상자의 거절이 기록되는 방식은 이 문서 대상이 아님(미확인)

## S37 보강(agent-loop)
- "When a tool is denied, Claude receives a rejection message as the tool result". 핵심 내장 도구의 정의는 매 요청, MCP 도구와 그 밖의 내장 도구는 도구 검색이 기본 지연 로드

# 2026-10-20 ch02-flow 사실 확인(fact-checker)

## S42. Anthropic, Configure permissions(Claude Code Docs). S25 재확인
- URL: https://code.claude.com/docs/en/permissions, 확인일: 2026-10-20, 작성: Anthropic
- "Permission rules are enforced by Claude Code, not by the model." 프롬프트와 CLAUDE.md의 지시는 시도에 영향을 주지만 허용 범위를 바꾸지 않음
- 평가 순서 deny, ask, allow, 처음 일치가 결정. 도구 이름만 지정한 deny는 도구를 컨텍스트에서 제거
- /permissions는 모든 규칙과 규칙이 나온 settings.json을 보여 줌

## S43. Anthropic, How Claude remembers your project(Claude Code Docs). S26 재확인
- URL: https://code.claude.com/docs/en/memory, 확인일: 2026-10-20
- "Claude reads them at the start of every session." CLAUDE.md와 자동 메모리는 "context, not enforced configuration"
- CLAUDE.md 계열이 없을 때만 AGENTS.md를 읽음(v2.1.277 이상, 10장에서 필요하면 근거), 하위 폴더의 CLAUDE.md는 필요할 때 읽음

## S44. Anthropic, Hooks reference(Claude Code Docs). S28 재확인
- URL: https://code.claude.com/docs/en/hooks, 확인일: 2026-10-20(앞 100,000자)
- 훅 핸들러는 command, http, mcp_tool, prompt, agent. command와 http는 모델을 호출하지 않음(2장은 셸 명령 훅만 다룬다고 밝힘)
- PostToolUse 종료 코드 2: stderr를 Claude에 보여 줌, 도구는 이미 실행됨

## S45. Anthropic, Debug your configuration(Claude Code Docs). S27 재확인
- URL: https://code.claude.com/docs/en/debug-your-config, 확인일: 2026-10-20
- Permissions와 hooks는 "enforce limits regardless of what Claude decides"(2장 "판단과 관계없이"의 근거)
- /context 범주: system prompt, system tools, MCP tools, custom subagents, memory files, skills, conversation messages

## 확인하지 못한 것
- 대화형 CLI의 사람 거절이 거부 결과로 기록되는 방식(Agent SDK 문서만 확인, 본문은 "Agent SDK 문서에 따르면"으로 한정)


## 2026-10-24 ch02-playbook 사실 확인(fact-checker). 확인일은 모두 2026-10-24.
Claude Code 문서는 게시일 표기가 없어 확인일만 적는다. 로컬 실행은 Claude Code 2.1.310(Linux).

## S46. Anthropic, Configure permissions(Claude Code Docs). S25, S42 재확인
- URL: https://code.claude.com/docs/en/permissions, 작성: Anthropic
- "Rules are evaluated in order: deny, then ask, then allow." 처음 일치가 결정, allow는 deny의 예외를 만들 수 없음
- 이름만 쓴 deny는 도구를 컨텍스트에서 제거, 범위 규칙(Bash(rm *))은 도구를 남기고 호출 시 차단
- "What a Bash rule doesn't match" 표: Bash(git push *)는 git -C . push origin main, git -c push.default=current push, git 'push' origin main과 일치하지 않음
- Read, Edit deny는 내장 파일 도구, Bash가 인식하는 파일 명령(cat, head, tail, sed, tee), 리다이렉션에 적용. 파일을 스스로 여는 Python, Node 스크립트는 적용되지 않음(샌드박스 필요)
- Edit 규칙은 파일을 수정하는 모든 내장 도구에 적용. Write(path)는 일치하지 않음
- path 또는 ./path는 현재 디렉터리 기준. 프로젝트 .claude/settings.json은 현재 작업 디렉터리의 .claude에서만 읽음(상위 폴더 대체 없음). settings.local.json은 git 저장소 루트에서 읽음
- "Permission rules are enforced by Claude Code, not by the model."
- PreToolUse 훅은 권한 프롬프트 전에 실행되고, 종료 코드 2는 권한 규칙 평가 전에 호출을 막음. 훅이 allow를 돌려줘도 deny, ask 규칙은 그대로 평가됨
- 시작 모드: 모드 기본값은 permission-modes 문서의 "Which mode a session starts in"을 따름

## S47. 로컬 실행 확인(Claude Code 2.1.310, claude -p, 2026-10-24)
- 실행 환경: Linux, Python 3.13.16, scratchpad의 임시 git 저장소. 설정은 --settings 파일로 전달
- allow [Bash(git *), Bash(python3 *), Bash(echo *)], deny [Edit(./data/**), Bash(git tag *), WebFetch, WebSearch]
- git tag v1은 거부됨, git -C . tag v2는 실행됨. 같은 원리의 push 예는 이 저장소의 pre_bash 훅 때문에 실행하지 않았고 permissions 문서 표로 확인
- Edit 도구로 data/ 수정은 거부(오류문 "File is in a directory that is denied by your permission settings."), echo > data/... 는 거부, python3 -c 로 data/ 수정은 실행됨
- 모델의 직접 호출 도구 목록에 WebFetch, WebSearch 없음
- PostToolUse 훅(Edit|Write, exit 2): Write 성공 뒤 훅의 stderr가 "PostToolUse:Write hook blocking error from command ..."로 모델에 전달, 파일은 이미 생성됨. stream-json에서 hook_response exit_code 2, outcome error
- /context 출력(비대화형): System prompt, System tools, System tools (deferred), Memory files, Skills, Messages, Free space, Autocompact buffer
- 작업 폴더 신뢰 전 -p 실행에서 프로젝트 허용 규칙 무시 경고
- 미확인: 대화형 TUI에서의 훅 오류 표시 문구, 대화형 CLI에서 사람이 거절한 호출의 기록 방식

## S48. Anthropic, How the agent loop works(Agent SDK, Claude Code Docs). S37 재확인
- URL: https://code.claude.com/docs/en/agent-sdk/agent-loop
- "When a tool is denied, Claude receives a rejection message as the tool result and typically attempts a different approach"
- "Every tool definition takes context space." 핵심 내장 도구(Bash, Read, Edit 등)의 정의는 매 요청에 들어가고, MCP 도구와 그 밖의 내장 도구는 도구 검색이 기본 지연 로드
- 모델이 도구 호출을 요청하고(Evaluate and respond) SDK가 실행(Execute tools). 문서는 "harness"를 쓰지 않음

## S49. Anthropic, Configure permissions(Agent SDK, Claude Code Docs). S40 재확인
- URL: https://code.claude.com/docs/en/agent-sdk/permissions
- 평가 순서: 훅 → deny → ask → 권한 모드 → allow → canUseTool. dontAsk는 프롬프트가 필요한 호출을 거부로 바꿈. v2.1.302 이상 SDK 앱은 default 모드로 시작
- 콜백이 없으면 승인이 필요한 호출은 거부(How the agent loop works의 Permission mode 표)

## S50. Anthropic, Permission modes(Claude Code Docs)
- URL: https://code.claude.com/docs/en/permission-modes
- 대화형 터미널과 VS Code 세션은 v2.1.283 이상에서 auto가 시작 모드. claude -p와 Agent SDK는 default. dontAsk는 프롬프트가 필요한 호출을 거부
- bypassPermissions에서 allow 규칙은 효과 없음. deny 규칙은 모든 모드에서 차단

## S51. Anthropic, Connect Claude Code to tools via MCP(Claude Code Docs). S30 재확인
- URL: https://code.claude.com/docs/en/mcp
- 첫 문단: MCP를 "an open source standard for AI-tool integrations"로 설명
- "Scale with MCP tool search": 시작 때 도구 이름과 서버 지시만 로드. 도구 검색은 기본 켜짐. 예외: ENABLE_TOOL_SEARCH=false, 이전 세대 모델, Azure Foundry 배포, CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS
- modelcontextprotocol.io는 접속 실패(ENOTFOUND)로 열지 못함

## S52. Anthropic, Manage costs effectively(Claude Code Docs). S29 재확인
- URL: https://code.claude.com/docs/en/costs
- "Reduce MCP server overhead": MCP 도구 정의는 기본 지연 로드, 이름과 서버 지시만 컨텍스트에 들어감. "Disable unused servers: Run /mcp ... disable any you're not actively using"(연결 해제가 아니라 끄기)
- 요금 화면(/usage)의 금액은 정가 기준 추정치

## S53. Anthropic, Hooks reference, Automate actions with hooks(Claude Code Docs). S44 재확인
- URL: https://code.claude.com/docs/en/hooks, https://code.claude.com/docs/en/hooks-guide
- 종료 코드 2: PreToolUse는 호출 차단, PostToolUse는 "Shows stderr to Claude; the tool already ran"
- "/hooks: read-only browser for your configured hooks"(hooks 참조 "The /hooks menu"). commands 문서는 "View hook configurations"만 씀
- 성공한 훅의 stdout은 대화 기록에 나오지 않고 디버그 로그로 감. hooks-guide: Ctrl+O 대화 기록 보기에서 확인, blocking error는 차단 메시지가 보임, non-blocking error는 "<hook name> hook error" 알림. 디버그는 claude --debug-file <경로> 또는 /debug (claude --debug도 언급)
- matcher는 문자, 숫자, _, -, 공백, 쉼표, | 만 있으면 정확 일치. Edit|Write는 두 도구에 정확 일치

## S54. 그 밖의 재확인
- memory 문서: "Claude treats them as context, not enforced configuration." 차단은 PreToolUse 훅. 자동 메모리는 로컬 세션에서 기본 켜짐. /context의 "Memory files" 아래 CLAUDE.md 표시. 세션은 새 컨텍스트로 시작
- debug-your-config 문서: /context 범주(system prompt, system tools, MCP tools, custom subagents, memory files, skills, conversation messages). 설정 병합 managed, local, project, user. 권한과 훅은 "enforce limits regardless of what Claude decides"
- how-claude-code-works 문서: 컨텍스트가 차면 먼저 오래된 도구 출력을 지우고 필요하면 요약, 초반의 상세 지시는 사라질 수 있음
- sub-agents 문서: tools는 허용 목록, 생략하면 상속. 사용자 정의 하위 에이전트는 CLAUDE.md 로드. 정의 위치 .claude/agents/
- commands 문서: /context, /hooks, /mcp(enable, disable, reconnect), /permissions, /memory, /doctor, /agents(안내 문구)
- 컨텍스트 엔지니어링 글(Rajasekaran 외, 2025-09-29): "bloated tool sets", "ambiguous decision points", "curating a minimal viable set of tools"
- example 대조: 표 2-4, 2-5, 2-6, 2-7과 본문은 reference/*.example.* 및 check.py와 일치. 불일치는 표 2-4 역할 행의 "규칙 문서 밖" 한정뿐
- 실습 2, 3 실행 기록(RUNLOG)은 아직 없음: 본문의 실습 결과 문장은 부록 실습 실행 뒤 확정(출간 전 실행 목록)
