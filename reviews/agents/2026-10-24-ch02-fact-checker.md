# 2장 사실 점검(fact-checker, 2026-10-24, 커밋 74dba5a)

## 결론: 필수 2, 권고 14, 참고 6 (확인한 사실 문장 약 62개)

기준일 2026-10-24. 로컬 Claude Code 2.1.310(`claude --version`)에서 `claude -p`로 직접 실행해 확인했습니다. 대화형 화면(TUI)은 열 수 없어 TUI에서 보이는 모습은 확인하지 못했습니다. 원고와 파일은 고치지 않았고, 임시 파일은 scratchpad 아래에만 만들었습니다.

### 일치로 판정한 문장 (표에는 올리지 않음)
- 대조 순서 deny→ask→allow, 처음 일치가 결정, allow는 deny의 예외를 만들지 못함. 근거는 permissions 문서 "Manage permissions" 절이다.
- 이름만 적은 WebFetch 금지는 도구를 컨텍스트에서 제거하고, `Bash(...)`처럼 범위를 적은 규칙은 도구를 남긴다. 근거는 permissions 문서와 Agent SDK permissions 문서의 표다. 로컬 `claude -p`에서도 WebFetch와 WebSearch가 직접 호출 도구 목록에 없었다.
- Bash 규칙은 명령 문자열이 일치할 때만 적용된다. permissions 문서 "What a Bash rule doesn't match" 표에 `Bash(git push *)`가 `git -C . push origin main`을 막지 못한다고 나온다. 로컬에서 같은 원리를 확인했다(아래 실행 기록).
- Edit 금지 규칙은 내장 수정 도구와 Bash가 인식하는 파일 명령, 리다이렉션에는 적용되고, 파일을 스스로 여는 Python 스크립트에는 적용되지 않는다. permissions 문서 Read and Edit 절에 있고, 로컬에서도 재현했다.
- PostToolUse 종료 코드 2는 도구가 이미 실행된 뒤 stderr를 모델에 보여 준다. hooks 문서 표에 있고, 로컬에서도 재현했다.
- Edit|Write matcher는 정확 일치로 작동한다(hooks 문서).
- 훅은 `.claude/settings.json`의 `"hooks"` 아래에 둔다(debug-your-config 문서).
- MCP 도구 검색(tool search)은 기본 켜짐이고 시작 때는 도구 이름과 서버 지시만 컨텍스트에 둔다. mcp 문서 "Scale with MCP tool search" 절, costs 문서 "Reduce MCP server overhead" 절, how-claude-code-works 문서가 같은 내용이다.
- 새 세션은 새 컨텍스트로 시작한다(memory 문서, how-claude-code-works 문서). 긴 대화는 자동 압축되고 초반의 상세 지시는 사라질 수 있다(how-claude-code-works 문서 "When context fills up" 절).
- CLAUDE.md와 자동 메모리는 "context, not enforced configuration"이다(memory 문서). 권한과 훅은 Claude의 결정과 무관하게 한계를 강제한다(debug-your-config 문서 NOTE).
- 자동 메모리는 로컬 세션에서 기본 켜짐이다(memory 문서 "Auto memory is on by default in local sessions").
- `/context`의 "Memory files" 항목에 CLAUDE.md가 표시된다. memory 문서에 문구가 있고, 로컬 2.1.310 출력에도 `Memory files` 행과 경로 표가 나왔다.
- `claude --debug`는 로컬 `claude --help`에 `-d, --debug [filter]`로 있다.
- 설정은 managed, user, project, local 범위에서 합쳐지고 가까운 범위가 덮어쓴다(debug-your-config 문서 "Check resolved settings" 절).
- 하위 에이전트 정의는 `.claude/agents/`의 Markdown과 YAML frontmatter이고 `tools`는 허용 목록이다. 문서의 읽기 전용 검토 예(Read, Grep, Glob)와 `reviewer.example.md`가 같은 구조다(sub-agents 문서).
- 컨텍스트 엔지니어링 글(Rajasekaran 외, 2025-09-29)은 "bloated tool sets", "ambiguous decision points", "minimal viable set of tools"를 말한다. 원고의 요약과 일치하고 주체 표기도 맞다.
- 예제 사실(표 2-4, 2-5, 2-6, 2-7과 본문)은 `docs/example-facts.md`와 `reference/settings.example.json`, `CLAUDE.example.md`, `reviewer.example.md`, `tasks.example.json`, `check.py`와 글자 단위로 맞는지 대조했다. 불일치는 아래 표 번호 2뿐이다.
  - 허용 목록, 확인 요청 `Bash(git commit *)`, 금지 6경로와 `Bash(git push *)`, WebFetch, WebSearch, 훅(PostToolUse, `Edit|Write`, `|| exit 2`)이 맞다.
  - 작업 1~5의 내용과 통과 값, 통과 값이 false인 첫 작업 단위만 수행하는 규칙, 같은 시험이 세 번 연속 실패하면 중단하는 규칙이 맞다.
  - `check.py`의 폴더별 "실행 N건, 실패 N건" 출력이 맞다.

### 지적 표

| 번호 | 등급 | 위치 | 원고 문장 | 확인 결과와 1차 출처 | 고칠 문안 |
|---|---|---|---|---|---|
| 1 | 필수 | 도구 사용 범위와 제약, 첫 문단 (ch02.html 35행) | "연결한 도구의 이름과 설명은 컨텍스트에 들어가 공간을 차지하며[costs]" | 인용이 주장을 받치지 못한다. costs 문서 "Reduce MCP server overhead"는 MCP 도구 정의가 기본 지연 로드라서 "only tool names and server instructions enter context"라고 한다. "설명이 공간을 차지한다"는 기본 설정과 반대로 읽힌다. "Every tool definition takes context space"는 agent-loop 문서(How the agent loop works) "Keep context efficient"에 있다. 같은 문서의 표는 Bash, Read, Edit 같은 핵심 내장 도구는 매 요청에 정의가 들어가고 MCP와 그 밖의 내장 도구는 지연 로드라고 한다. research S29와 S32도 이 직접 문장이 costs와 context-window에 없다고 기록했다. | "도구 정의는 컨텍스트에 들어가 공간을 차지하며(핵심 내장 도구는 매 요청에, MCP 도구는 기본 설정에서 이름과 서버 안내만)" 식으로 고치고 인용을 `agent-loop`(필요하면 `costs` 병기)로 바꾼다. 전제는 R11처럼 인용 하나에 문서 하나다. |
| 2 | 필수 | 표 2-4 역할 행, 운영 기준 칸 | "사람의 몫(규칙 문서 밖): 수용 기준 확정, 작업 1 합의, 작업 5 승인, commit 확인, push" | R7 불일치. `CLAUDE.example.md` 작업 순서에 "대조 보고 뒤 그 단위의 변경을 commit한다(commit은 사람 확인 후)"가 있다. 표 2-5 넷째 행도 "규칙 문서의 작업 순서(사람 확인 뒤 commit)"라고 쓴다. `docs/example-facts.md`의 "사람의 몫" 목록에는 "규칙 문서 밖"이라는 한정이 없다. 수용 기준 확정, 작업 1 합의, 작업 5 승인, push만 규칙 문서에 없다. | "commit 확인"을 괄호 밖으로 빼거나 "사람의 몫(수용 기준 확정, 작업 1 합의, 작업 5 승인, push는 규칙 문서 밖. commit은 규칙 문서가 사람 확인 뒤로 정함)"으로 쓴다. 참고로 "작업 5 승인"도 규칙 문서에는 "통과 값 변경 금지"로만 있다. |
| 3 | 권고 | 같은 문단, /context 인용 (35행) | "/context를 입력하면 나오는 화면에서, 도구 항목으로 그 크기를 확인할 수 있습니다[context-window]" | context-window 문서는 `/context`가 범주별 실시간 분해를 보여 준다고만 하고 "도구" 범주 이름은 없다. 범주 이름은 debug-your-config 문서 "See what loaded into context" 절에 있다(system prompt, system tools, MCP tools, custom subagents, memory files, skills, conversation messages). 로컬 2.1.310 출력은 `System tools`, `System tools (deferred)`, `Memory files`, `Skills`였다. `MCP tools` 행은 MCP를 연결했을 때 나타나는 것으로 보이며 이번 실행에서는 확인하지 못했다. | 인용을 `debug-config`로 바꾸고 "도구 항목(System tools, MCP tools)"으로 쓴다. 표 2-7 도구 확인과 맞추려면 "System tools (deferred)" 행도 한 번 알려 준다. |
| 4 | 권고 | 같은 절 둘째 문단 (36행) | "MCP는 외부 시스템의 기능을 에이전트의 도구로 연결하는 규약이고, 이를 구현한 프로그램을 MCP 서버라고 합니다." | 인용이 없다(R8 기술 용어 정의). mcp 문서 첫 문단은 "an open source standard for AI-tool integrations"라고 한다. MCP 공식 사이트(modelcontextprotocol.io)는 접속 실패(ENOTFOUND)로 열지 못했다. "서버 = 구현 프로그램"은 위 문단에서 확인하지 못했고 mcp 문서의 다른 절에서 찾아야 한다(미확인). | 정의 문장 끝에 `<sup class="cite" data-ref="mcp">` 추가. "규약"을 "개방형 표준(open source standard)"으로 맞추는 것을 권한다. |
| 5 | 권고 | 같은 문단 (36행) | "사용하지 않는 MCP 서버는 연결을 해제하라고 안내합니다[costs]" | costs 문서는 "Disable unused servers: Run /mcp to see configured servers and disable any you're not actively using"라고 한다. 안내는 "연결 해제"가 아니라 `/mcp`에서 끄기(disable)다. `/mcp`에는 `enable`, `disable`, `reconnect` 인자가 있다(commands 문서). | "사용하지 않는 MCP 서버는 `/mcp`에서 끄라고(비활성화) 안내합니다." 52행의 "연결 해제"와 그림 2-2도 같은 표현이면 함께 맞춘다. |
| 6 | 권고 | 같은 문단 (36행) | "Claude Code는 기본 설정에서 MCP 서버의 도구 설명을 처음부터 불러오지 않고 …[mcp]" | "기본 설정" 한정이 있어 맞다. 다만 mcp 문서 "Configure tool search"에는 예외가 있다. `ENABLE_TOOL_SEARCH=false`, Opus 4/Sonnet 4/Haiku 4.5 이전 모델, Azure Foundry 배포, `CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS`가 그렇다. 게이트웨이(`ANTHROPIC_BASE_URL`)는 mcp 문서에 따로 설명이 있다. | 문장은 유지하고, 버전 주석 또는 각주로 "환경 변수나 모델에 따라 처음부터 모두 불러오는 경우가 있음"을 한 줄 덧붙이는 것을 권한다. 사내 게이트웨이를 쓰는 독자에게 중요하다. |
| 7 | 권고 | 같은 절 넷째 문단 (38행) | "어느 규칙에도 일치하지 않는 호출은 권한 모드가 처리하며, 모드에 따라 사람에게 묻거나 자동으로 승인하거나 거부합니다[permission-modes]" | 큰 틀은 맞다. 단순화된 부분이 둘 있다. (a) Agent SDK permissions 문서 "How permissions are evaluated"의 순서는 훅 → deny → ask → 권한 모드 → allow → canUseTool이다. acceptEdits나 bypassPermissions는 allow 규칙 확인 전에 승인한다. 문서도 bypassPermissions에서 allow 규칙은 효과가 없다고 한다(permission-modes 문서). (b) 시작 모드가 환경마다 다르다. permission-modes 문서 "Which mode a session starts in"은 v2.1.283 이상의 대화형 터미널과 VS Code가 `auto`(분류기가 검토)이고, `claude -p`와 Agent SDK는 `default`라고 한다. 저장소 재발 주의("권한 모드 기본값은 버전에 따라 다름")에 해당한다. | 본문은 Chapter 10으로 미루고 있어 틀리지는 않는다. 87행 "권한 모드가 사람에게 묻는 모드라면" 근처에 "자동 판정 모드에서는 사람이 아니라 분류기가 판단하고, `-p`나 SDK 실행에서는 묻지 못하고 거부됨"을 버전 주석(2026년 10월)으로 덧붙이는 것을 권한다. |
| 8 | 권고 | 같은 절 다섯째 문단 (39행) | "확인 요청 규칙에 일치한 호출은 실행 전에 사람에게 확인을 요청합니다[permissions]" | permissions 문서 "Ask rules prompt for confirmation"이라 대화형에서는 맞다. 한계가 빠져 있다. dontAsk 모드는 프롬프트가 필요한 호출을 거부로 바꾼다. SDK는 ask 규칙에 일치하면 `canUseTool` 콜백으로 넘기고, 콜백이 없으면 거부다(Agent SDK permissions 문서 "Ask rules" 절, "How the agent loop works"의 Permission mode 표). `git commit` 확인 요청에 기대는 자동 실행(CI, `-p`)은 사람이 없으면 막힌다. | "대화형 세션에서는" 한정을 달고 "사람이 없는 실행(`-p`, SDK, dontAsk)에서는 확인 요청 규칙이 거부로 처리됨"을 한 줄 덧붙인다. |
| 9 | 권고 | 같은 절 (39행), 표 2-2 "거부 결과 기록" 행, 그림 2-2 | "Claude Agent SDK의 문서는 사람이 거절한 호출도 실행되지 않고, 거부 메시지가 도구 결과로 모델에 전달된다고 설명합니다[sdk-user-input]" | user-input 문서는 "Deny: tool doesn't execute, Claude sees the message"라고 한다. "도구 결과로"라는 표현은 인용된 문서에 없고 agent-loop 문서 "Tool permissions"의 "When a tool is denied, Claude receives a rejection message as the tool result"에 있다. 또 "사람이 거절"이 아니라 앱의 `canUseTool` 콜백이 deny를 돌려주는 경우다. 표 2-2와 그림 2-2는 "금지되거나 거절된 호출은 … 도구 결과로 이력에 추가"라고 SDK 한정 없이 쓴다. 금지 규칙 쪽은 로컬 `claude -p`에서 확인했다(모델이 오류문 "Permission to use Bash with command … has been denied."를 그대로 인용). 대화형 CLI에서 사람이 거절한 경우는 미확인이다(S41과 같음). | 39행에 `agent-loop` 인용을 더하고 "앱이 deny를 돌려주면"으로 고친다. 표 2-2와 그림 2-2의 거부 행은 "금지 규칙 일치: 거부 메시지가 도구 결과로 전달됨(확인). 사람 거절: SDK 문서 기준"으로 근거를 구분한다. |
| 10 | 권고 | 훅 문단 (56행) | "종료 코드 2(Claude Code가 차단 신호로 정한 값)로 끝나면 오류 출력을 모델에 전달해" | 같은 문단이 PostToolUse는 되돌리지 못한다고 말하는데 괄호가 "차단 신호"라서 헷갈린다. hooks 문서 표는 PreToolUse 종료 코드 2를 "Blocks the tool call", PostToolUse를 "Shows stderr to Claude; the tool already ran"으로 구분한다. 로컬 재현: 파일은 만들어졌고 훅 메시지는 `PostToolUse:Write hook blocking error from command ...`로 모델에 전달됐다. | "(PreToolUse에서는 호출을 막고, PostToolUse에서는 이미 실행된 뒤 오류 출력만 전달하는 값)"으로 고친다. |
| 11 | 권고 | 같은 문단 (56행) | "PreToolUse 훅은 도구 실행 전, 권한 규칙 대조보다 먼저 실행되어 호출을 막을 수 있습니다.[hooks]" | 내용은 맞지만 인용한 hooks 참조에는 이 순서를 직접 말하는 문장이 없다. permissions 문서 "Extend permissions with hooks"에 "PreToolUse hooks run before the permission prompt", "A hook that exits with code 2 stops the tool call before permission rules are evaluated"가 있다. SDK 문서도 훅이 맨 먼저라고 한다. 같은 곳에 빠진 한계가 있다. 훅이 allow를 돌려줘도 deny와 ask 규칙은 그대로 평가된다("PreToolUse hook decisions don't bypass permission rules"). | 인용을 `permissions`로 바꾼다(또는 병기). 필요하면 "훅이 allow를 돌려줘도 금지 규칙은 우회되지 않음"을 덧붙인다. 이것은 "훅이 규칙보다 앞서 허용한다"는 오해를 막는다. |
| 12 | 권고 | 지시 기반 규칙과 강제 적용, 마지막 문단 (64행) | "파일 수정 금지 규칙은 수정 도구와 Bash의 일반적인 파일 명령에는 적용되지만, … Python 스크립트를 실행해 수정하는 경우까지 막지는 못합니다. Bash 규칙은 … [permissions]" | 내용은 맞고 로컬에서 재현했다. 인용이 둘째 문장 뒤에만 있어 첫 문장에는 근거 표시가 없다(R11). "일반적인 파일 명령"은 모호하다. 문서는 "file commands Claude Code recognizes in Bash, such as cat, head, tail, sed, and tee"와 `> file` 리다이렉션이라고 한다. `grep -r pattern .`처럼 파일 이름을 적지 않는 읽기와 임의 하위 프로세스도 해당하지 않는다. | 첫 문장 뒤에 `permissions` 인용을 붙이고 "Bash가 인식하는 파일 명령(cat, sed, tee 등)과 리다이렉션"으로 구체화한다. |
| 13 | 권고 | 설정과 결과의 확인 방법, 첫 문단 (98행)과 표 2-5 설명 (77행) | "설정은 사용자, 프로젝트, 로컬 등 여러 파일에서 합쳐지고[debug-config] … 표의 Edit(./data/**)는 data 폴더 아래 모든 파일" | 합쳐진다는 설명은 맞다. 세션 시작 위치에 관한 한계가 빠졌다. permissions 문서 Read and Edit 절의 표에서 `path` 또는 `./path`는 cwd 기준이다(`<cwd>/...`). permissions 문서 "Working directories"는 "Hooks and other `.claude/settings.json` keys load from the current working directory's `.claude/` folder with no parent-directory fallback"이라고 한다. 따라서 예제 폴더 안이 아니라 저장소 루트나 상위 폴더에서 `claude`를 시작하면 프로젝트 권한과 훅이 적용되지 않는다. 처음 실행하는 작업 폴더에서 신뢰를 확인하기 전에는 프로젝트의 허용 규칙이 보류된다(로컬 `-p` 실행에서 `Ignoring 6 permissions.allow entries from .claude/settings.json: this workspace has not been trusted.` 출력). | 98행에 "권한과 훅을 정한 `.claude/settings.json`은 `claude`를 시작한 폴더 기준으로 읽히므로 예제 폴더에서 시작한다. 처음 실행하면 폴더 신뢰 확인 뒤에 허용 규칙이 적용된다"를 한 줄 덧붙인다(2026년 10월 확인, 버전 주석). |
| 14 | 권고 | 표 2-7 검증 행, 훅 문단 (104, 106행) | "테스트가 실패하는 편집 뒤 대화 화면에 훅 오류가 보이며", "대화 화면의 훅 오류로 확인합니다" | hooks-guide 문서 "Hook error in output"에 따르면 훅 결과는 `Ctrl+O` 대화 기록 보기에서 확인한다. Blocking error는 "on most events you see the message that came with the block"(차단 메시지)이고, "`<hook name> hook error` 알림"은 non-blocking 오류의 설명이다. PostToolUse 종료 코드 2가 TUI에서 어떻게 보이는지는 문서에 직접 없다. 비대화형 `claude -p --output-format stream-json`에서는 `hook_response`의 `exit_code: 2`, `outcome: "error"`, stderr 원문이 확인됐다. TUI 화면은 확인하지 못했다(미확인). | 확인 기준을 "대화 기록 보기(Ctrl+O)에서 훅이 낸 오류 메시지(stderr)가 보이고, 모델이 그 메시지를 이어서 수정함"으로 바꾸거나, 부록 실습 4 실행 때 TUI 문구를 RUNLOG에 기록한다. |
| 15 | 권고 | 같은 문단 (106행) | "/hooks는 등록된 훅을 보여 주는 읽기 전용 목록이므로 …" 끝 인용 [hooks-guide] | "읽기 전용"은 hooks 참조 "The /hooks menu"에 있다("open a read-only browser for your configured hooks"). 인용된 hooks-guide는 `/hooks`를 "hooks browser"라고만 한다. commands 문서는 "View hook configurations"만 쓴다. 인용이 마지막 문장(`claude --debug`)에만 붙어 있다. `claude --debug`는 hooks-guide 문서에 있고 debug-your-config 문서 "Check hooks"에도 있다. hooks-guide의 주된 안내는 `claude --debug-file <경로>`와 세션 중 `/debug`다. | `/hooks` 문장 뒤에 `hooks` 인용을 붙이고, 필요하면 `--debug-file`과 `/debug`도 알려 준다. |
| 16 | 권고 | 도구에 대해 정할 것 세 가지, 셋째 항목 (52행) | "하위 에이전트의 정의 파일에 맡긴 작업에 필요한 도구만 적습니다[sub-agents]" | 맞다. 빠진 주의점은 sub-agents 문서 frontmatter 표의 `tools`에 "Inherits every tool available to subagents if omitted"가 있다는 점이다. 적지 않으면 모든 도구를 상속한다. `disallowedTools`는 상속 목록에서 제외한다. 이 책의 `reviewer.example.md`는 `tools: Read, Grep, Glob`이라 허용 목록이다. 이 파일의 도구 지정이 의도대로 작동하는지는 하위 에이전트를 실제로 호출해 보지 않았다. | "(`tools`를 생략하면 모든 도구를 상속하므로 반드시 적는다)"를 덧붙인다. |
| 17 | 권고 | 예제 마지막 문단 (87행) | "금지 규칙을 더하면 수용 시험과 원본 자료의 수정 시도가 모두 거부됩니다(부록 실습 3)", "규칙 문서만 있을 때는 … 막지 못할 수 있고(부록 실습 2)" | R8 실행 기록이 없다. `examples/expense-app/RUNLOG.md`의 실습 2~6은 "실행 전"이다. 이 장의 근거는 문서 설명뿐이다. 2.1.310에서 쓴 `Edit(./data/**)` 금지는 Edit 도구와 `echo > data/...` 리다이렉션을 거부했고, `python3 -c` 스크립트는 막지 못했다. 결과는 아래 실행 기록에 있다. 단, 내가 쓴 규칙은 `data/**`이고 `acceptance/**`, `check.py` 규칙은 실행하지 않았다. 규칙 문서만 있을 때 수정 시도를 막지 못한다는 부분(실습 2)도 실행하지 않았다. | 본문의 단정은 유지하되, 실습 2와 3 실행 후 RUNLOG에 모델·제품 버전과 출력 원문을 남긴 뒤 확정한다(20.3). 아래 research 문안의 S47 기록을 쓸 수 있다. |
| 18 | 참고 | 훅 예제 (표 2-4 검증 행, 설정 예제) | `python -m unittest discover tests -q \|\| exit 2` | macOS와 Linux에서 `python` 명령이 없으면 훅이 매번 "command not found"로 종료 코드 2를 낸다. 모델에는 그 오류가 전달된다. 부록 79행에 python3 대체 안내가 이미 있다. ch02 본문에는 없다. 훅은 시작한 폴더에서 실행되므로(S23) 예제 폴더에서 시작하지 않으면 `tests`를 찾지 못한다. Windows PowerShell에서의 동작은 미시험이다(S23 기록과 같음). | 본문은 그대로 두고 부록 안내만 유지해도 된다. |
| 19 | 참고 | 표 2-6 첫 행, 표 2-1 역할 행 | "작업 5의 통과 값은 사람만 변경" | 작업 5의 통과 값 보호는 `CLAUDE.md` 지시와 commit 확인 때 사람의 확인뿐이다. `tasks.json`의 `Edit` 금지 규칙은 없다(에이전트가 다른 작업 단위의 통과 값을 고쳐야 하므로 둘 수 없다). 본문 63행의 "지시 + 사람 검토" 설명과는 맞다. 표 2-6의 "사람만 변경"은 강제처럼 읽힐 수 있다. | "사람만 변경하도록 규칙 문서에 명시"로 쓰면 R16(장치의 역할)에 맞다. |
| 20 | 참고 | 표 2-4 권한 행 허용 목록 | "허용: 단위 테스트, 검사 스크립트, git status, git diff" | `settings.example.json`의 `Bash(git status)`와 `Bash(python check.py)`는 인수 없는 정확 일치다. `git status -s`나 `python check.py 2>&1`처럼 꼬리가 붙으면 허용 규칙에 일치하지 않아 모드에 따라 묻거나 거부된다(permissions 문서 wildcard 표: 공백 뒤 `*` 없는 규칙은 정확 일치). 본문은 틀리지 않았다. | 필요하면 실습 설명에 "다른 형태로 실행하면 확인을 요청할 수 있음"을 쓴다. |
| 21 | 참고 | 표 2-1, 지시 기반 규칙 절 (55행) | "메모리 문서와 설정 점검 문서는 … 권한 규칙이나 훅을 쓰라고 안내합니다[memory][debug-config]" | 문서마다 말하는 범위가 다르다. memory 문서 첫 절은 `PreToolUse` 훅만 든다. 권한 규칙은 debug-your-config 문서 NOTE("Use permissions or hooks")에 있다. memory 문서에도 관리자 설정의 `permissions.deny`를 기술적 강제로 들고 있는 절이 있다. 인용 둘이 나란해 문장 일부씩 받치는 구조다. | 문장을 둘로 나눠 각각 한 문서씩 인용하면 R11 형식이 더 분명해진다. |
| 22 | 참고(미확인) | 도구 사용 범위와 제약 (37행) | "모델은 도구 호출을 요청만 하고 실행은 하네스가 맡으므로[agent-loop]" | agent-loop 문서는 "Evaluate and respond"에서 모델이 도구 호출을 요청하고 "Execute tools"에서 SDK가 실행한다고 한다. 이 문서는 "harness"라는 말을 쓰지 않는다(S37). how-claude-code-works 문서는 "agentic harness"를 "모델 둘레의 층"이라 부른다. 문장은 책의 정의에 따른 풀이로는 문제 없다. | 필요하면 인용을 `how-cc-works`와 `agent-loop` 중 하나로 정해 R3(주어)를 분명히 한다. |
| 23 | 참고 | bibliography.json | (인용 키) | 새 키는 필요 없다. 이 장이 쓰는 모든 `data-ref`(memory, permissions, how-cc-works, costs, context-window, context-engineering, mcp, agent-loop, permission-modes, sdk-user-input, hooks, debug-config, sub-agents, commands, hooks-guide)가 존재한다. 다만 `memory`, `commands`, `sub-agents`, `context-window`, `costs`가 파일 안에 두 번씩 정의되어 있다(JSON 중복 키, 값은 동일). 파서에 따라 경고가 날 수 있다. | 아래쪽 중복 줄(33~37행)을 삭제하면 된다. |

### 실행 기록 (Claude Code 2.1.310, Linux, Python 3.13.16, 2026-10-24)

1. 버전과 옵션
```
$ claude --version
2.1.310 (Claude Code)
$ claude --help | grep -i debug
  -d, --debug [filter]    Enable debug mode with optional category filtering
  --debug-file <path>     Write debug logs to a specific file path
```

2. `reference/settings.example.json`을 scratchpad의 `proj/.claude/settings.json`으로 복사해 JSON을 읽었다. 결과는 "json ok". `claude -p`가 허용 규칙 6개를 무시했다.
```
Ignoring 6 permissions.allow entries from .claude/settings.json: this workspace has not been trusted. ...
```

3. 금지 규칙 문자열 일치, Edit 금지, Python 우회, 리다이렉션, 이름만 적은 금지. scratchpad의 임시 git 저장소 `t1`에서 설정은 `--settings`로 넘겼다.
   - 설정: `allow ["Bash(git *)","Bash(python3 *)","Bash(echo *)"]`, `deny ["Edit(./data/**)","Bash(git tag *)","WebFetch","WebSearch"]`
   - 이 저장소의 `tools/hooks/pre_bash.py`가 `git push` 문자열이 든 Bash 호출을 막아 첫 시도는 실행되지 않았다. 그 훅을 우회하지 않고, 같은 원리를 보이는 `git tag`(push 대신)로 바꿔 실행했다. 따라서 `git -C . push`라는 원고의 예 자체는 로컬에서 실행하지 않았고 permissions 문서 표로만 확인했다.
```
1. git tag v1                      -> DENIED  "Permission to use Bash with command git tag v1 has been denied."
2. git -C . tag v2                 -> EXECUTED (출력 없음)   # 같은 동작, 다른 표기는 일치하지 않음
3. python3 -c "open('data/projects.csv','w').write('changed')" -> EXECUTED (data/projects.csv가 'changed'로 바뀜)
4. Edit 도구로 data/projects.csv 수정  -> DENIED  "File is in a directory that is denied by your permission settings."
5. echo hacked > data/projects.csv -> DENIED  (리다이렉션 대상 경로가 인식됨)
직접 호출 도구 목록: Agent, Artifact, Bash, Edit, ListAgents, Read, ..., Skill, ToolSearch, Workflow, Write
-> WebFetch와 WebSearch 없음 (이름만 적은 금지 규칙으로 목록에서 제거됨)
최종 상태: data/projects.csv = changed, git tag = v2
```

4. PostToolUse 종료 코드 2 (scratchpad `t2`). 훅은 `echo HOOKMARKER-FAILED-TEST >&2; exit 2`, matcher는 `Edit|Write`다. `--output-format stream-json --verbose`로 실행했다.
```
SYS hook_response {"hook_name":"PostToolUse:Write","exit_code":2,"stderr":"HOOKMARKER-FAILED-TEST\n","outcome":"error"}
모델 응답: Write는 성공했고 훅이 blocking error를 돌려줌 ... "PostToolUse:Write hook blocking error from command: ...: HOOKMARKER-FAILED-TEST"
a.txt 존재(5바이트, hello) -> 도구는 이미 실행된 뒤라 훅이 막지 못함
```

5. `/context` (scratchpad `t3`, 프로젝트에 CLAUDE.md 한 줄)
```
| System prompt | 2k | System tools | 19.8k | System tools (deferred) | 20.3k | Memory files | 10 | Skills | 4.5k | ...
### Memory Files | Project | .../t3/CLAUDE.md | 10 |
```

6. `check.py` (scratchpad 복사본)
   - 기준 상태(원본 폴더): `tests: 실행 3건, 실패 0건` / `acceptance: 실행 5건, 실패 3건` (종료 1).
   - `acceptance/test_*.py` 삭제: `Ran 0 tests ... NO TESTS RAN` / `acceptance: 실행 0건, 실패 0건` → 종료 코드 1.
   - `acceptance/` 폴더 삭제: 종료 코드 1. 빈 폴더: 종료 코드 1.
   - 원고의 "수용 시험이 한 건도 실행되지 않으면 실패"가 맞다.

### research/ch02-sources.md에 덧붙일 기록 문안

```
# 2026-10-24 ch02-playbook 사실 확인(fact-checker). 확인일은 모두 2026-10-24.
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
```

### bibliography.json
새 키는 필요 없습니다. 위 권고 4번(MCP 정의 인용)은 기존 `mcp` 키를 쓰고, 권고 1번과 9번은 기존 `agent-loop`를 쓰며, 권고 3번은 기존 `debug-config`를 씁니다. 중복 키 정리는 표의 23번에 있습니다.

### 장별 점검 질문 10개에 대한 답

| 질문 | 답 |
|---|---|
| 개념 | 모두 일치. 이름만 적은 금지, 범위 금지, 훅의 종료 코드 2, 시점별 의미는 맞다. 단 "차단 신호" 괄호는 PostToolUse에서 혼동을 준다(10). |
| 분류 | 다섯 구성 요소는 이 책의 정리이며 제품 문서의 분류가 아니다. 본문이 이 점을 밝힌 것은 맞다(S36 기록). |
| 논리 | 규칙 문서는 컨텍스트, 권한과 훅은 강제라는 구분은 문서(memory, debug-your-config)와 실행으로 모두 뒷받침된다. |
| 범위 | 권한 모드 시작값, 훅 앞선 평가 순서, ask 규칙의 비대화형 처리는 범위를 줄여 쓴 곳이 있다(7, 8, 11). |
| 절차 | 시작 폴더, 신뢰 확인, `python` 대 `python3` 한계가 빠져 있다(13, 18). |
| 책임 | 승인과 push는 사람에게 있다. 표 2-4의 "규칙 문서 밖" 한정은 원본과 다르다(2). |
| 검증 | `check.py`와 금지 규칙은 로컬에서 재현했다. 실습 2~6의 RUNLOG는 아직 비어 있다(17). |
| 일관성 | 표 2-4와 표 2-5의 commit 확인 설명이 서로 어긋난다(2). 그 밖의 예제 사실은 일치한다. |
| 출처 | 인용 15개 중 정확히 맞는 것은 11개다. 어긋나거나 바꿀 인용은 1, 3, 9, 11, 15번이다. 정의 문장 하나에는 인용이 없다(4). |
| 편집 한계 | 대화형 TUI 표시, 대화형 CLI 사람 거절의 기록 방식, MCP 공식 사이트 정의는 확인하지 못했다. |

필수 2, 권고 14, 참고 6(참고 표에 올린 것은 18~22번의 5개와 23번 정리 1개를 합해 6), 확인한 사실 문장 약 62개

관련 경로
- /home/user/harness-book/src/chapters/ch02.html
- /home/user/harness-book/research/ch02-sources.md
- /home/user/harness-book/research/bibliography.json
- /home/user/harness-book/docs/example-facts.md
- /home/user/harness-book/examples/expense-app/reference/ (settings.example.json, CLAUDE.example.md, reviewer.example.md, tasks.example.json)
- /home/user/harness-book/examples/expense-app/RUNLOG.md
- 임시 실행 파일: /tmp/claude-0/-home-user-harness-book/4fa31d71-64a2-5605-bad4-d31a3ffd2331/scratchpad/ (t1, t2, t3, app, proj)
