# 2장 사실 점검 보고(fact-checker, 2026-10-24)

범위: src/chapters/ch02.html 전체(제품 기능, 기본값, 명령과 설정 이름, 수치, 인용, 발표 주체, 다른 장 링크, 예제 값). 원고는 고치지 않음.
기준: NEW_BOOK_PLAYBOOK.md 7장, 8장, 12장, docs/specs/ch02-spec.md, research/ch02-sources.md, research/bibliography.json, docs/example-facts.md, examples/expense-app/.
확인한 Claude Code 문서는 모두 2026-10-24에 직접 열어 확인함(게시일 표기 없음).

## 요약
필수 2, 권고 11, 참고 7. 확인한 사실 문장 56개(지적 표 20행이 가리키는 문장 26개 + 일치 확인 표 30행).

사용자가 짚은 다섯 항목의 결론은 다음과 같습니다.
1. tool-scope: 하위 에이전트 정의 파일의 도구 지정은 일치. "사용하지 않는 서버는 종료하라"는 불일치(문서는 /mcp에서 끄라는 disable). Agent SDK 문장은 내용 일치, 각주 문서가 문장 일부만 뒷받침(행 5).
2. 표 2-1 권한 행은 일치. 표 2-2 권한 확인 행은 기본 흐름으로는 일치하나 모드별 예외가 빠짐(행 7).
3. Stop 훅 문장은 일치. 보완할 참고 사항 있음(행 15).
4. 다른 장 링크 중 ch10#permissions, ch06#multi-agent, ch09#approval, ch09#isolation, ch01#agent-harness는 내용과 제목 일치. ch10#criteria는 내용 불일치, ch03#example은 문구와 제목이 다름(행 11, 12).
5. 예제 값은 표 2-4~2-7 모두 example-facts.md, settings.example.json, reviewer.example.md, check.py 출력과 일치. 예외는 표 2-5 다섯째 행의 "단위 테스트 명령만 있음"(행 2).

## 지적 표

| # | 위치 | 문장 | 확인 결과와 근거(URL 또는 파일:행) | 등급 | 고친 문안 |
|---|---|---|---|---|---|
| 1 | tool-scope 둘째 단락(ch02.html:39) | "사용량과 비용을 줄이는 방법을 다룬 Claude Code 문서는 사용하지 않는 서버는 종료하라고 안내합니다" | 불일치. costs 문서 "Reduce token usage > Reduce MCP server overhead"는 "Disable unused servers: Run /mcp to see configured servers and disable any you're not actively using"라고 씀. mcp 문서는 /mcp 패널에서 서버를 끄면(toggle off) 연결을 중단하되 설정은 남는다고 설명하고, 제거는 별도 명령 claude mcp remove임. "종료"는 프로세스를 끝낸다는 뜻이라 문서의 disable(연결 안 함, 설정 유지)과 다름. https://code.claude.com/docs/en/costs , https://code.claude.com/docs/en/mcp (2026-10-24 확인) | 필수 | "…Claude Code 문서는 /mcp에서 사용하지 않는 서버를 비활성화하라고 안내합니다" (또는 "끄라고") |
| 2 | 표 2-5 다섯째 행(ch02.html:88) | "없음(규칙 문서의 명령 절에는 단위 테스트 명령만 있음)" | 불일치(R7). examples/expense-app/reference/CLAUDE.example.md 명령 절(31~35행)에는 단위 테스트(python -m unittest discover tests -q) 외에 전체 검사(python check.py), 앱 실행(python app.py), python3 안내가 있음. docs/example-facts.md 23~28행도 같음. 의도는 "수정할 때마다 실행하라는 지시가 없음"으로 보임 | 필수 | "없음(규칙 문서의 명령 절에 단위 테스트 명령은 있으나 수정할 때마다 실행하라는 지시는 없음)" |
| 3 | tool-scope 둘째 단락(ch02.html:39) | "이렇게 해도 도구 이름과 안내는 컨텍스트에 남고 선택할 대상도 늘어나므로, …문서는 …안내합니다" | 이유 귀속 문제(R3, R13). costs 문서는 서버를 끄라고만 쓰고 "선택할 대상이 늘어나므로"라는 이유는 쓰지 않음. 앞 절반(이름과 안내가 컨텍스트에 남음)은 costs와 how-claude-code-works가 뒷받침. 뒤 절반은 이 책의 설명이고 context-engineering 글(도구 모호성)과 연결한 것 | 권고 | 이유를 문서의 말로 쓰지 않도록 분리: "도구 이름과 안내는 컨텍스트에 남고 선택할 대상도 늘어납니다. 사용량과 비용을 줄이는 방법을 다룬 Claude Code 문서는 사용하지 않는 서버를 /mcp에서 끄라고 안내합니다." |
| 4 | tool-scope 둘째 문단(ch02.html:38) | "연결한 도구의 이름과 설명은 컨텍스트에 들어가 공간을 차지하며[costs], …/context를…도구 항목으로 그 크기를 확인할 수 있습니다[context-window]" | 각주 문서와 문장이 어긋남(R4, R11). (a) costs는 MCP 도구 정의가 기본 지연 로드라 "tool names and server instructions"만 컨텍스트에 들어간다고 쓰며, 모든 도구의 "설명"이 들어간다는 문장은 없음. 도구 정의가 요청마다 컨텍스트를 차지한다는 문장은 agent-loop 문서("Every tool definition takes context space"; 핵심 내장 도구는 매 요청, MCP와 그 밖의 내장 도구는 도구 검색이 기본 지연 로드)에 있음. (b) context-window 문서는 "run /context for a live breakdown by category"만 쓰고 system tools, MCP tools 범주 이름은 쓰지 않음. 범주 이름은 debug-your-config 문서("system prompt, system tools, MCP tools, custom subagents, memory files, skills, conversation messages")에 있음. (c) 위첨자 두 개가 문장 가운데(쉼표 앞)에 있음(플레이북 7.4). 같은 문제가 ch02.html:17 "시작하고[memory], 긴 대화는…"에도 있음 | 권고 | (a) 첫 각주를 agent-loop로 바꾸고 문장을 "연결한 도구의 정의가 컨텍스트에서 공간을 차지하며"로 쓰거나 costs 근거에 맞게 "MCP 도구의 이름과 서버 안내"로 한정. (b) 둘째 각주를 debug-config로. (c) 문장을 나눠 각주를 문장 끝으로 |
| 5 | tool-scope 확인 요청 단락(ch02.html:43) | "Claude Code의 에이전트 루프를 프로그램에서 실행하게 하는 Claude Agent SDK의 문서는 사람이 거절한 호출도 실행되지 않고, 거부 메시지가 도구 결과로 모델에 전달된다고 설명합니다[sdk-user-input]" | 내용은 일치하나 각주 하나가 두 문서의 내용을 받침(R11). user-input 문서는 deny 응답 코드 주석 "tool doesn't execute, Claude sees the message"와 "Claude sees this message and may adjust its approach"까지만 말함. "도구 결과(tool result)로 전달"은 agent-loop 문서("When a tool is denied, Claude receives a rejection message as the tool result")에 있고, SDK가 "Claude Code의 에이전트 루프를 실행"한다는 설명도 agent-loop 문서("embed Claude Code's autonomous agent loop", "runs the same execution loop that powers Claude Code")에 있음. https://code.claude.com/docs/en/agent-sdk/user-input , https://code.claude.com/docs/en/agent-sdk/agent-loop | 권고 | 각주를 agent-loop로 바꾸거나, "…SDK의 문서는 사람이 거절한 호출은 실행되지 않고 Claude가 그 메시지를 본다고 설명합니다[sdk-user-input]"로 줄이고 "도구 결과로"는 agent-loop 각주를 따로 둠 |
| 6 | tool-scope 43행, 표 2-2 "사람 확인" 행(51행), 그림 2-2 | "확인 요청 규칙에 일치한 호출은 실행 전에 사람에게 확인을 요청합니다" / "확인 요청 규칙에 일치한 호출을 실행 전에 사람이 승인하거나 거절" | 조건이 빠짐(플레이북 7.1 "규칙에 없는 동작의 처리", R1). permission-modes 문서: dontAsk 모드는 "denies calls matching your explicit ask rules rather than prompting"(사람에게 묻지 않고 거부). Agent SDK permissions 문서: dontAsk에서 ask 규칙에 걸린 호출은 거부. 같은 문서: v2.1.302 이상에서 claude -p와 Agent SDK는 모드를 지정하지 않으면 Manual로 시작하고 승인이 필요한 호출은 allow 규칙, 훅, canUseTool 콜백, --permission-prompt-tool로 승인하지 않으면 거부. 예제의 git commit 확인 요청도 사람이 없는 실행에서는 거부로 바뀜. 대화형 CLI 대화상자의 사람 거절이 기록되는 방식은 1차 문서에서 확인하지 못함(research S41 기록과 같음). https://code.claude.com/docs/en/permission-modes , https://code.claude.com/docs/en/agent-sdk/permissions | 권고 | 43행에 "대화형 세션에서는" 추가하고 한 문장 보태기: "dontAsk 모드나 사람이 응답하지 않는 실행(claude -p 등)에서는 확인 요청에 일치한 호출이 묻지 않고 거부됩니다." 표 2-2 사람 확인 행: "…(대화형 세션 기준)" |
| 7 | 표 2-2 "3 권한 확인" 행(50행), tool-scope 42행 | "호출마다 금지, 확인 요청, 허용 순서로 대조해 처음 일치하는 규칙으로 처리하고, 일치하는 규칙이 없으면 권한 모드로 처리" | 기본 흐름으로는 일치하나 모드별 예외가 빠짐. 일치 부분: permissions 문서 "Rules are evaluated in order: deny, then ask, then allow. The first match…"(Manage permissions 절). 예외: Agent SDK permissions 문서 "How permissions are evaluated"는 훅 → deny → ask → 권한 모드 → allow → canUseTool 순서로, 모드가 allow 규칙보다 먼저 적용됨. bypassPermissions는 이 단계에 이른 호출을 모두 승인하고 allow 규칙은 효과가 없음(permission-modes: "Allow rules have no effect in bypassPermissions"). acceptEdits는 파일 편집을 승인. plan 모드에서는 allow 규칙이 일치해도 파일 편집은 자동 승인되지 않음. 도구가 스스로 승인하는 호출(작업 폴더 안의 읽기, 읽기 전용 Bash)은 규칙이 필요 없음. 42행의 "모드에 따라 사람에게 묻거나 자동으로 승인하거나 거부"는 일치. 상세는 ch10이 맡으므로 한정어만 필요 | 권고 | 표 2-2: "…처음 일치하는 규칙으로 처리하고, 규칙으로 결정되지 않으면 권한 모드로 처리(모드에 따라 허용 규칙보다 먼저 승인하거나 편집을 자동 승인하지 않는 경우가 있음)". 또는 42행 끝에 "모드별 처리 순서의 예외는 Chapter 10에서 다룹니다" |
| 8 | instruct-enforce 둘째 단락(ch02.html:60) | "Claude Code의 메모리 문서와 설정 점검 문서는 CLAUDE.md를 강제 설정이 아닌 컨텍스트로 규정하고, 일어나면 안 되는 동작에는 권한 규칙이나 훅을 쓰라고 안내합니다[memory][debug-config]" | 사실은 둘 다 일치하나 한 문장에 문서 둘, 각주 둘이 연달아 붙음(R11). memory 문서: "Claude treats them as context, not enforced configuration. To block an action regardless of what Claude decides, use a PreToolUse hook instead", 그리고 특정 시점에 실행해야 하면 훅으로 쓰라고 함(권한 규칙 대안은 managed settings의 permissions.deny 안내에 있음). debug-config 문서 Note: "Permissions and hooks enforce limits regardless of what Claude decides… Use permissions or hooks for security boundaries and anything that must never happen". "컨텍스트로 규정"은 memory 문서, "권한 규칙이나 훅"은 debug-config 문서가 직접 말함. memory 문서는 훅(PreToolUse)만 직접 언급 | 권고 | 문장을 둘로 나눔: "Claude Code의 메모리 문서는 CLAUDE.md를 강제 설정이 아닌 컨텍스트로 설명하고, 동작을 막으려면 훅을 쓰라고 안내합니다[memory]. 설정 점검 문서는 권한과 훅이 Claude의 결정과 무관하게 한계를 강제하므로 일어나면 안 되는 일에는 이 둘을 쓰라고 안내합니다[debug-config]." |
| 9 | tool-scope 40행, 57행 셋째 항목, 표 2-2 둘째 행 | "하위 에이전트의 정의 파일에 그 에이전트가 사용할 도구를 따로 적을 수 있습니다" / "필요한 도구만 적습니다" | 사실은 일치(sub-agents 문서 frontmatter 표: "tools … Inherits every tool available to subagents if omitted"; "To restrict tools, use the tools field as an allowlist or the disallowedTools field as a denylist"; 위치 .claude/agents/). 빠진 주의점: tools를 생략하면 제한이 아니라 사용 가능한 도구를 모두 상속하고, 허용 목록과 별도로 disallowedTools(거부 목록)가 있음. 예제 reviewer.example.md는 tools: Read, Grep, Glob으로 문서의 읽기 전용 검토 에이전트 예와 같은 구조. https://code.claude.com/docs/en/sub-agents (2026-10-24, 앞 100,000자와 끝 부분 열람) | 권고 | 40행 끝에 한 문장: "tools를 적지 않으면 제한 없이 사용 가능한 도구를 모두 상속하므로, 제한하려면 반드시 적습니다." |
| 10 | 표 2-5 앞 설명(ch02.html:82), 표 2-5 | "표의 Edit(./data/**)는 data 폴더 아래 모든 파일의 수정을 가리킵니다" | 세션 시작 위치 조건이 빠짐(실무 주의점 3). permissions 문서 경로 표기 표: "path or ./path → Path relative to current directory"(예 Read(*.env) → <cwd>/*.env), "/path → Path relative to the settings source". 즉 ./data/**는 Claude Code를 실행한 폴더 기준이므로 expense-app 폴더가 아닌 상위나 하위 폴더에서 시작하면 data/가 다른 곳을 가리킬 수 있음. 장은 표 2-7 앞에서 "프로젝트 폴더에서 Claude Code를 실행한 뒤"라고만 씀(103행). 예제 값 자체(Edit(./data/**) 등)는 settings.example.json과 일치. https://code.claude.com/docs/en/permissions | 권고 | 82행에 "경로 앞의 ./는 Claude Code를 실행한 폴더 기준이므로, 예제는 프로젝트 폴더에서 실행하는 것을 전제로 합니다" |
| 11 | 예제 73행 링크 | `<a href="ch10.html#criteria">Chapter 10의 비교 기준</a>`; 문장 "다른 제품이 같은 구성 요소를 어떤 장치로 구현하는지는 …에서 다룹니다" | 링크 문구와 제목은 같으나(절 제목 "비교 기준") 도착 절이 문장이 말하는 내용을 다루지 않음. ch10.html:5 비교 기준 절은 비교 기준 네 가지(규칙 문서, 권한, 격리, 설정 파일)를 정하고 "이 기준은 Chapter 2의 다섯 구성 요소(역할, 도구, 권한, 기록, 검증)와 달리, 정책이 제품의 어디에 적히는지에 따른 정리"라고 밝힘. 표 10-1도 다섯 구성 요소별 구현을 보여 주지 않음(역할, 도구, 기록, 검증 대응 없음). 플레이북 12장 "링크 문구와 도착한 절의 내용이 같아야" 위반 | 권고 | 문장을 도착 절 내용에 맞춰 "다른 제품은 같은 정책을 규칙 문서, 권한, 격리, 설정 파일의 네 곳에 어떻게 나누어 적는지는 Chapter 10의 비교 기준에서 다룹니다"로 고치거나, 다섯 구성 요소별 대응이 필요하면 작가 확인(AUTHOR_QUEUE) |
| 12 | 예제 71행 링크 | `<a href="ch03.html#example">Chapter 3의 예제</a>`; "…에서 자세히 설계할 변경 요청 사항" | 내용은 일치(ch03.html:19~22 절이 CR의 작업 단위, 수용 기준, 아홉 항목 명세를 다룸). 링크 문구 "Chapter 3의 예제"와 도착 절 제목 "기능 추가 에이전트: CR 구현"이 다름(플레이북 12장 링크 문구 = 도착 절 내용, 사용자 지시의 문구 = 제목 점검) | 권고 | "Chapter 3의 기능 추가 에이전트: CR 구현"으로 문구를 도착 절 제목에 맞춤 |
| 13 | 구성 요소 35행 | `<a href="ch08.html">Chapter 8</a>`; "기록을 남기는 방법은 …에서 자세히 다룹니다" | 쪽 맨 위로 가는 링크(플레이북 12장은 목차와 장 전체 요약 링크만 예외). ch08에는 실제 내용 절이 있음: #kinds "기록의 세 종류", #decisions "결정 기록의 형식", #handover "인계 메모 작성" | 권고 | 링크를 ch08.html#kinds 등 내용이 있는 절로 걸고 문구를 그 절 제목에 맞춤("Chapter 8의 기록의 세 종류") |
| 14 | 표 2-7 검증 행(ch02.html:109) | "테스트가 실패하는 편집 뒤 대화 화면에 훅 오류가 보이며" | 미확인(R4). PostToolUse에서 종료 코드 2의 동작은 hooks 문서 표 "PostToolUse: can block No, Shows stderr to Claude; the tool already ran"까지만 확인. 대화 화면(transcript)에 "hook error" 알림이 나온다는 문장은 PreToolUse 예와 SessionStart 등 일부 이벤트에만 있고 PostToolUse에는 없음. hooks-guide "Check what a hook did"는 Blocking error는 "on most events you see the message that came with the block", Non-blocking error는 "<hook name> hook error" 알림이라고만 씀. 실제 Claude Code를 실행한 확인은 이 환경에서 못 함 | 참고 | 실행 기록(RUNLOG) 전까지는 "훅이 보낸 오류 메시지가 대화 화면에 보이며"로 낮추거나, 부록 실습 확인 후 확정. research에 미확인으로 기록 |
| 15 | 예제 81행 | "모델이 응답을 마치려 할 때 완료 기준을 검사하는 Stop 훅" | 일치. hooks 문서 이벤트 표 "Stop: When Claude finishes responding"; 종료 코드 2 표 "Stop: Yes, Prevents Claude from stopping, continues the conversation". 참고할 한계(hooks-guide Learn more, Stop hook hits the block cap): Stop 훅은 작업 완료 때만이 아니라 응답이 끝날 때마다 실행되고, 사용자 인터럽트에는 실행되지 않으며, 연속 8번 막으면 Claude Code가 훅을 무시하고 끝내므로 stop_hook_active 확인이 필요. "완료 판정까지 훅에 맡기려면 Stop 훅을 더합니다"는 이 한계를 빼면 단순화로 읽힐 수 있음 | 참고 | 필요하면 한 문장: "Stop 훅은 응답을 마칠 때마다 실행되므로, 작업 단위가 끝났는지는 훅 스크립트가 따로 판단해야 합니다." (Chapter 7 몫이면 생략) |
| 16 | 구성 요소 도구 항목(ch02.html:13), 표 2-1 도구 행 | "너무 많으면 도구 설명이 컨텍스트를 차지하고, 비슷한 도구 사이에서 무엇을 쓸지 선택하기 어려워집니다" | 각주 없음(R4). 뒤 tool-scope 절에서 같은 내용을 각주와 함께 다루고(행 4의 정정 반영), 근거는 agent-loop("Every tool definition takes context space")와 context-engineering 글. 정의 절이므로 중복 각주는 필수 아님 | 참고 | 유지. 뒤 절 각주를 행 4처럼 바로잡으면 충분 |
| 17 | 예제 92행 | "규칙 문서만 있을 때는 …막지 못할 수 있고(실습 2), 금지 규칙을 더하면 수용 시험과 원본 자료의 수정 시도가 모두 거부됩니다(실습 3)" | 금지 규칙의 동작은 permissions 문서와 일치(Edit deny는 내장 편집 도구에 적용). 다만 부록 실습의 응답과 화면은 practice.html:21에 "실행 기록을 확인하기 전의 예상"이라고 밝혀 둔 상태이고 RUNLOG.md는 실행 전. "거부됩니다"는 문서 근거의 서술이지 실행 관찰이 아님. Claude Code를 실행해야 하는 실습이라 이 점검에서는 실행하지 못함 | 참고 | RUNLOG 기록 전까지 현재 문장 유지 가능. 실습 실행 후 research에 실행 기록 추가 |
| 18 | 표 2-4 역할 행, 표 2-6 첫 행, 표 2-7 역할 행 | "규칙 문서에 사람이 승인할 작업 단위(작업 5) 명시" / "규칙 문서에 사람이 승인할 작업이 적혀 있으며" | CLAUDE.example.md 작업 순서 절은 "작업 5의 '통과' 값은 변경하지 않는다"와 "commit은 사람 확인 후"만 적고 "승인"이라는 말과 작업 1 합의, 수용 기준 확정은 적지 않음. 사람의 몫 목록(example-facts.md 39~40행)은 사실이나 규칙 문서에 모두 적힌 것은 아님. 표 2-4 역할 행은 "…통과 값 변경 금지를 적고, …사람이 맡음"으로 쓰여 적는 것과 사람이 맡는 것을 구분해 읽으면 일치 | 참고 | 표 2-6, 2-7의 "사람이 승인할 작업이 적혀"를 "작업 5의 통과 값을 에이전트가 변경하지 않는다고 적혀"로 맞추는 것을 검토 |
| 19 | 예제 79행, 표 2-7 | 훅 명령 "python -m unittest discover tests -q \|\| exit 2" | 설정 파일과 글자까지 일치. 운영체제 주의점: hooks 문서 command 훅의 shell은 macOS와 Linux는 sh -c, Windows는 Git Bash이고 Git Bash가 없으면 PowerShell을 쓰며 Bash용 스크립트는 그대로 안 돌 수 있음("Failed hooks on Windows without Git Bash"). 이 환경(Linux)에서 python과 python3 모두 있고 단위 테스트 3건 통과(OK)를 확인. 이 책의 research는 Windows PowerShell 동작을 "미시험"으로 기록해 둠 | 참고 | 장 본문 수정은 불필요. 부록 실습 준비의 운영체제 안내(python3 대체 포함)에서 다룰지 practice-checker에 전달 |
| 20 | research/ch02-sources.md | S1, S2(프롬프트 작성 문서, 확인일 2026-10-04) 및 S36 | 현재 ch02 본문에서 쓰지 않는 내용(S1, S2는 프롬프트 작성 문서 요약)이 장 기록 맨 앞에 남아 있음. S36(OpenAI Harness engineering 403 미열람)은 ch02 본문에 쓰이지 않음. 본문 각주 키 15개(memory, permissions, how-cc-works, costs, context-window, context-engineering, mcp, sub-agents, agent-loop, permission-modes, sdk-user-input, hooks, debug-config, commands, hooks-guide)는 모두 research/bibliography.json에 있고 저자, 제목, 매체, URL이 일치. context-engineering은 날짜 2025.9.29, 저자 Prithvi Rajasekaran 외로 원문과 일치 | 참고 | 정리는 작가 판단. 본문 영향 없음 |

## 일치 확인 표(지적 없음)

| # | 위치 | 문장 | 확인 결과와 근거 | 판정 |
|---|---|---|---|---|
| V1 | 38행 | context-engineering 글은 겹치는 도구가 많으면 어느 도구를 쓸지 판단하기 어렵다고 보고 최소한의 도구만 두라고 권한다 | https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents (2025-09-29, Anthropic Applied AI 팀): "bloated tool sets that cover too much functionality or lead to ambiguous decision points", "minimal viable set of tools". 주체를 글로 쓴 것도 R3에 맞음 | 일치 |
| V2 | 39행 | Claude Code는 기본 설정에서 MCP 서버의 도구 설명을 처음부터 불러오지 않고 도구 이름과 서버 안내만 컨텍스트에 둔 뒤 필요할 때 불러온다 | mcp 문서 "Scale with MCP tool search": "Only tool names and server instructions load at session start", 기본 켜짐. 예외(이전 모델, ENABLE_TOOL_SEARCH=false, Azure Foundry 배포, 게이트웨이)는 "기본 설정에서"로 한정되어 있음 | 일치 |
| V3 | 39행 | MCP는 외부 시스템의 기능을 에이전트의 도구로 연결하는 규약, 구현 프로그램은 MCP 서버 | 용어 정의. research S39(MCP 사양 2026-07-28)와 모순 없음. 지연 로드는 규약이 아니라 Claude Code의 기능이라는 문장 구분도 일치 | 일치 |
| V4 | 41행 | 모델은 도구 호출을 요청만 하고 실행은 하네스가 맡는다 | agent-loop 문서 "Evaluate and respond"에서 Claude가 도구 호출을 요청, "Execute tools"에서 SDK가 실행. 문서는 harness라는 말을 쓰지 않으며 본문은 1장 정의를 쓴 것 | 일치 |
| V5 | 42행 | 권한 규칙을 금지, 확인 요청, 허용 순서로 대조, 처음 일치하는 규칙이 결과를 정함 | permissions 문서 "Rules are evaluated in order: deny, then ask, then allow. The first match in that order determines the outcome, and rule specificity doesn't change the order" | 일치 |
| V6 | 42행 | 도구 이름만 적은 금지 규칙은 그 도구를 목록에서 제외, Bash(git push *)는 도구를 남기고 일치하는 호출만 거부 | permissions 문서: "A bare tool name like Bash removes the tool from Claude's context entirely… A scoped rule like Bash(rm *) leaves the tool available and blocks matching calls" | 일치 |
| V7 | 42행 | 모드에 따라 사람에게 묻거나 자동으로 승인하거나 거부 | permission-modes 문서(Manual은 묻기, auto는 분류기, dontAsk는 거부) | 일치 |
| V8 | 59행 | 훅은 도구 실행 전후처럼 정해진 시점에 자동으로 실행되는 명령 | hooks-guide: "Hooks are user-defined shell commands. Claude Code runs them at specific points in its lifecycle". 핸들러는 command, http, mcp_tool, prompt, agent 5종이고 장은 셸 명령 훅만 다룬다고 한정함 | 일치 |
| V9 | 60행 | 권한 규칙을 적용하는 주체는 모델이 아닌 Claude Code, 프롬프트나 CLAUDE.md는 시도에 영향을 주나 허용 동작을 바꾸지 않는다 | permissions 문서 Note: "Permission rules are enforced by Claude Code, not by the model. Instructions in your prompt or CLAUDE.md shape what Claude tries to do, but they don't change what Claude Code allows" | 일치 |
| V10 | 61행 | PreToolUse 훅은 도구 실행 전, 권한 규칙 대조보다 먼저 실행되어 호출을 막을 수 있다 | hooks 문서 PreToolUse exit 2 "Blocks the tool call". permissions 문서 "A hook that exits with code 2 stops the tool call before permission rules are evaluated"; Agent SDK permissions 문서 "Run hooks first". 단 PreToolUse의 allow는 deny와 ask 규칙을 넘지 못함(본문은 주장하지 않음) | 일치 |
| V11 | 61행 | PostToolUse 훅은 이미 실행된 편집을 되돌리지 못하나 종료 코드 2로 끝나면 오류 출력을 모델에 전달 | hooks 문서 표 "PostToolUse: No, Shows stderr to Claude; the tool already ran"; hooks-guide "PostToolUse hooks can't undo actions since the tool has already executed" | 일치 |
| V12 | 61행 | 종료 코드 2(Claude Code가 차단 신호로 정한 값) | hooks 문서 "Exit with code 2 to block the action" | 일치 |
| V13 | 69행, 표 2-1 권한 행 | 파일 수정 금지 규칙은 수정 도구와 Bash의 일반적인 파일 명령에는 적용되지만 파일을 스스로 여는 Python 스크립트까지는 막지 못한다 | permissions 문서: Read and Edit deny rules apply to "built-in file tools, to file commands Claude Code recognizes in Bash, such as cat, head, tail, sed, and tee, and to the targets of Bash redirections… They don't apply to… a Python or Node script that opens files itself"; 운영체제 수준 강제는 샌드박스 | 일치 |
| V14 | 69행, 표 2-1 권한 행 | Bash 규칙은 명령 문자열이 일치할 때만 적용, Bash(git push *)는 git -C . push와 일치하지 않는다 | permissions 문서 "What a Bash rule doesn't match" 표: Bash(git push *)는 push origin main은 막고 git -C . push origin main 등은 막지 못함. 보장이 필요하면 샌드박스나 PreToolUse 훅 | 일치 |
| V15 | 69행 | 훅도 실행되지 않거나 실패하면 막지 못한다 | hooks 문서: 종료 코드 2가 아닌 실패는 non-blocking error라 동작이 계속됨("The action goes ahead", 실패 차단 설정 제외) | 일치 |
| V16 | 81행 | 자동 메모리는 로컬 세션에서 기본으로 켜져 있다 | memory 문서 "Auto memory is on by default in local sessions. …a session in a self-hosted environment runs with auto memory off by default" | 일치(본문이 "로컬 세션"으로 한정) |
| V17 | 17행 | 새 세션은 이전 대화를 담지 않은 컨텍스트로 시작 | memory 문서 "Each Claude Code session begins with a fresh context window"; how-claude-code-works "Sessions are independent" | 일치 |
| V18 | 17행 | 긴 대화는 자동으로 압축되어 앞의 내용이 그대로 남지 않을 수 있다 | how-claude-code-works "When context fills up": "clears older tool outputs first, then summarizes… detailed instructions from early in the conversation may be lost" | 일치 |
| V19 | 103행 | 설정은 사용자, 프로젝트, 로컬 등 여러 파일에서 합쳐진다 | debug-config "Settings merge across managed, user, project, and local scopes" | 일치 |
| V20 | 103행, 표 2-7 | /context, /permissions, /mcp, /hooks 명령 | commands 문서 표(/context 컨텍스트 사용량 시각화, /permissions 규칙 관리 대화상자, /mcp 서버 관리, /hooks 훅 구성 보기) 및 debug-config 표(/permissions: 현재 적용 중인 규칙, /hooks: 활성 훅 구성) | 일치 |
| V21 | 105행 | /context의 메모리 파일 항목에 CLAUDE.md | debug-config "/context … memory files"; 하위 폴더 CLAUDE.md는 필요 시 로드되어 안 보일 수 있음(본문 주장과 무관) | 일치 |
| V22 | 111행 | /hooks는 등록된 훅의 읽기 전용 목록, 성공한 훅의 출력은 대화에 나타나지 않으며 실행 기록은 claude --debug | hooks-guide "Check what a hook did": Success "you see nothing"; debug-config "Start a session with claude --debug". /hooks의 "읽기 전용"은 research S23, S33(2026-10-20 기록)과 같고 commands 문서는 "View hook configurations"로 씀 | 일치 |
| V23 | 표 2-4 권한, 표 2-5 | 허용 단위 테스트, 검사 스크립트, git status, git diff / 확인 요청 git commit / 금지 data/, acceptance/, check.py, CLAUDE.md, DECISIONS.md, .claude/ 수정, git push | examples/expense-app/reference/settings.example.json과 같음(allow 6개 중 python과 python3 변형 포함, ask Bash(git commit *), deny Edit 6종과 Bash(git push *), WebFetch, WebSearch) 및 docs/example-facts.md 30~34행 | 일치 |
| V24 | 표 2-4 도구, 표 2-6 둘째 행 | 웹 접근 도구는 이름만 적은 금지 규칙(WebFetch, WebSearch), 검토 하위 에이전트의 도구는 Read, Grep, Glob | settings.example.json deny에 "WebFetch", "WebSearch", reviewer.example.md tools: Read, Grep, Glob | 일치 |
| V25 | 표 2-4 검증, 79행 | 편집 뒤 훅(PostToolUse, Edit\|Write, 단위 테스트 실행, 실패하면 종료 코드 2) | settings.example.json hooks.PostToolUse matcher "Edit\|Write" command "python -m unittest discover tests -q \|\| exit 2". hooks 문서 matcher 표 "Edit\|Write … match either tool exactly" | 일치 |
| V26 | 표 2-4 검증, 표 2-6, 92행 | check.py는 수용 시험이 한 건도 실행되지 않으면 실패 | check.py 마지막 줄 sys.exit(0 if all(count > 0 and failed == 0 …) else 1). 실행 출력 원문은 아래 research 기록 | 일치 |
| V27 | 표 2-7 검증 | 검사 스크립트 출력에 폴더별 실행 건수와 실패 건수 | 실행 출력 "tests: 실행 3건, 실패 0건 / acceptance: 실행 5건, 실패 3건" | 일치 |
| V28 | 71~72행, 9행 | 작업 1은 사람이 마침, 작업 2~4는 에이전트, 작업 5는 에이전트 초안과 사람 승인, 통과 값, tasks.json, 원본 자료 data/projects.csv | docs/example-facts.md 12~21행, tasks.example.json 통과 값 시작 true/false/false/false/false | 일치 |
| V29 | 표 2-5 | 같은 시험이 세 번 연속 실패하면 중단, commit 전에 reviewer 대조 요청, 수정 범위 절(acceptance/, check.py, data/), 작업 순서(사람 확인 뒤 commit) | CLAUDE.example.md 중단 규칙, 작업 순서, 수정 범위 절. push는 규칙 문서에 지시 없음(표의 "없음"과 일치) | 일치 |
| V30 | 링크 | ch01#agent-harness, ch06#multi-agent, ch09#approval, ch09#isolation, ch10#permissions | 도착 절 제목과 문구 일치("에이전트와 하네스의 정의", "여러 에이전트에 나눠 맡기기", "승인 지점 설계", "격리와 샌드박스", "권한과 격리 비교"). 내용 확인: ch06은 "넘길 정보와 도구"에 최소한의 도구 지정을 다룸, ch09#approval은 확인 요청과 금지의 승인 지점, ch09#isolation은 샌드박스와 간접 수정 한계, ch10#permissions는 권한 모드 여섯 값과 선택 기준(버전 주석 포함). 부록 #setup "실습 준비", #lab-2 "실습 2. 규칙 문서 작성", #lab-3 "실습 3. 권한 설정"도 존재 | 일치 |

## 장 전체 검토에서 추가로 본 것(지적 없음)
- 권한 모드 기본값(요금제별, v2.1.283 이상 auto)은 2장이 단정하지 않고 10장 버전 주석에 둠. 재발 주의 항목과 충돌 없음.
- 사용량 화면 금액(정가 기준 추정)은 2장에 해당 문장 없음.
- 사례 주체: 2장에 외부 사례 없음. Anthropic 글과 문서를 주체로 쓴 문장은 R3에 맞음.

## research/ch02-sources.md에 붙일 기록 문안

```
# 2026-10-24 ch02 fact-checker 사실 점검(전체 재확인)

Claude Code 문서는 게시일 표기가 없어 확인일만 적는다. 설정 키와 기본값은 확인일 기준이다.

## S46. Anthropic, Manage costs effectively(Claude Code Docs). S29 재확인
- URL: https://code.claude.com/docs/en/costs, 확인일: 2026-10-24, 작성: Anthropic
- "Reduce token usage > Reduce MCP server overhead": MCP 도구 정의는 기본 지연 로드(이름과 서버 지시만 컨텍스트), /context로 점유 확인. "Prefer CLI tools when available"(gh, aws 등은 도구별 목록을 추가하지 않아 더 효율적). "Disable unused servers: Run /mcp to see configured servers and disable any you're not actively using."
- 본문 "종료하라고 안내"는 불일치. 문서의 동사는 disable(비활성화). 서버를 끄는 이유로 "선택할 대상이 늘어난다"는 설명은 문서에 없음(이 책의 설명)
- mcp 문서(S30): /mcp 패널에서 서버를 끄면 연결을 중단하고 설정은 남김(disabled 표시). 제거는 claude mcp remove

## S47. Anthropic, Configure permissions(Claude Code Docs). S25, S42 재확인
- URL: https://code.claude.com/docs/en/permissions, 확인일: 2026-10-24
- 평가 순서 deny, ask, allow, 처음 일치가 결정. 이름만 쓴 deny는 도구를 컨텍스트에서 제거, 범위 규칙은 도구를 남기고 일치하는 호출만 차단
- "Permission rules are enforced by Claude Code, not by the model."
- Bash 규칙 한계(What a Bash rule doesn't match): Bash(git push *)는 git -C . push origin main 등과 일치하지 않음. Read, Edit deny는 내장 파일 도구, Bash가 인식하는 파일 명령(cat, head, tail, sed, tee), 리다이렉션에 적용되나 파일을 스스로 여는 Python, Node 스크립트는 막지 못함(샌드박스 필요)
- PreToolUse 훅은 deny, ask 규칙을 우회하지 못함. 종료 코드 2인 훅은 권한 규칙 평가 전에 호출을 막음
- 경로 표기: path 또는 ./path는 현재 디렉터리 기준, /path는 설정 파일 출처 기준, //path 절대 경로. ./data/**는 Claude Code를 실행한 폴더 기준이므로 시작 위치 주의

## S48. Anthropic, Configure permissions(Agent SDK, Claude Code Docs). S40 재확인
- URL: https://code.claude.com/docs/en/agent-sdk/permissions, 확인일: 2026-10-24
- 평가 순서: 훅 → deny → ask → 권한 모드 → allow → canUseTool. 모드는 allow보다 먼저 적용되어 bypassPermissions는 이 단계에 이른 호출을 모두 승인(critical-path 제외), acceptEdits는 파일 편집 승인, plan은 allow 규칙이 일치해도 파일 편집을 자동 승인하지 않음, dontAsk는 프롬프트가 필요한 호출을 거부
- 2장 표 2-2 "일치하는 규칙이 없으면 권한 모드로 처리"는 기본 흐름으로만 일치(예외는 이 평가 순서)

## S49. Anthropic, Permission modes(Claude Code Docs)
- URL: https://code.claude.com/docs/en/permission-modes, 확인일: 2026-10-24
- "Allow rules have no effect in bypassPermissions." dontAsk 모드: 명시한 ask 규칙에 일치한 호출은 프롬프트 없이 거부. 자동 모드 진입 시 Bash(*) 등 넓은 allow 규칙은 제외, 좁은 규칙은 유지
- 시작 모드: v2.1.283 이상 대화형 터미널과 VS Code는 auto, v2.1.302 이상 claude -p와 Agent SDK는 모드를 지정하지 않으면 Manual이며 승인이 필요한 호출은 allow 규칙, 훅, canUseTool, --permission-prompt-tool로 승인하지 않으면 거부(2장은 단정하지 않음, 10장 버전 주석)

## S50. Anthropic, Hooks reference와 Automate actions with hooks(Claude Code Docs). S23, S28, S44 재확인
- URL: https://code.claude.com/docs/en/hooks , https://code.claude.com/docs/en/hooks-guide, 확인일: 2026-10-24(hooks는 앞 100,000자)
- 종료 코드 2 표: PreToolUse는 호출 차단, PostToolUse는 차단하지 않고 stderr를 Claude에게 보여 줌(도구는 이미 실행), Stop은 Claude가 멈추는 것을 막고 대화를 계속
- Stop: "When Claude finishes responding"에 실행(작업 완료 때만이 아님), 사용자 인터럽트에는 실행되지 않음, 연속 8번 막으면 Claude Code가 훅을 무시, stop_hook_active 확인 필요(hooks-guide)
- matcher "Edit|Write"는 두 도구 이름을 정확히 일치. PostToolUse는 도구 호출이 성공한 뒤에만 실행(실패는 PostToolUseFailure)
- 성공한 훅은 대화에 아무것도 나타나지 않음(Ctrl+O 대화 기록). Blocking error는 대부분 이벤트에서 차단 메시지가 보임, Non-blocking error는 "<hook name> hook error" 알림. 미확인: PostToolUse 종료 코드 2에서 대화 화면에 hook error 표기가 나오는지(문서에 PostToolUse 항목 없음)
- Windows: command 훅의 shell은 macOS와 Linux는 sh -c, Windows는 Git Bash, Git Bash가 없으면 PowerShell(Bash용 스크립트는 그대로 안 돌 수 있음)
- Bash 등 셸 명령이 파일을 바꾸는 경우는 Edit|Write 훅이 보지 못함(hooks-guide FileChanged, Stop 안내)

## S51. Anthropic, Create custom subagents(Claude Code Docs). S31 재확인
- URL: https://code.claude.com/docs/en/sub-agents, 확인일: 2026-10-24(앞 100,000자와 끝 부분 열람)
- frontmatter tools: 허용 목록(쉼표 문자열 또는 YAML 목록), 생략하면 사용 가능한 도구를 모두 상속. disallowedTools는 거부 목록이며 둘 다 있으면 disallowedTools를 먼저 적용. 위치 .claude/agents/(프로젝트), ~/.claude/agents/(사용자)
- 읽기 전용 검토 예: tools: Read, Glob, Grep 또는 Read, Grep, Glob, Bash. reviewer.example.md와 같은 구조

## S52. Anthropic, Connect Claude Code to tools via MCP(Claude Code Docs). S30 재확인
- URL: https://code.claude.com/docs/en/mcp, 확인일: 2026-10-24(Scale with MCP tool search 절 열람)
- "Only tool names and server instructions load at session start". 도구 검색 기본 켜짐. 예외: Opus 4, Sonnet 4, Haiku 4.5 이전 모델은 처음부터 로드, ENABLE_TOOL_SEARCH=false, Azure의 Foundry 배포, 서버별 alwaysLoad

## S53. Anthropic, How the agent loop works(Agent SDK, Claude Code Docs). S37 재확인
- URL: https://code.claude.com/docs/en/agent-sdk/agent-loop, 확인일: 2026-10-24
- "The Agent SDK lets you embed Claude Code's autonomous agent loop in your own applications", "runs the same execution loop that powers Claude Code". 도구 거부: "Claude receives a rejection message as the tool result". "Every tool definition takes context space"

## S54. Anthropic, Handle approvals and user input(Agent SDK, Claude Code Docs). S41 재확인
- URL: https://code.claude.com/docs/en/agent-sdk/user-input, 확인일: 2026-10-24
- 거부 응답 코드 주석 "Deny: tool doesn't execute, Claude sees the message". "도구 결과로 전달"이라는 표현은 이 문서에 없고 agent-loop(S53)에 있음
- 미확인: 대화형 CLI에서 사람이 거절했을 때 기록되는 방식(문서 대상이 아님)

## S55. Anthropic, 메모리, 설정 점검, 컨텍스트 창, 동작 방식, 명령 문서 재확인
- URL: https://code.claude.com/docs/en/memory , /debug-your-config , /context-window , /how-claude-code-works , /commands, 확인일: 2026-10-24
- memory: 세션은 새 컨텍스트로 시작. CLAUDE.md와 자동 메모리는 "context, not enforced configuration", 동작을 막으려면 PreToolUse 훅. 자동 메모리는 로컬 세션에서 기본 켜짐(self-hosted 환경은 꺼짐), 기기 로컬
- debug-your-config: /context 범주(system prompt, system tools, MCP tools, custom subagents, memory files, skills, conversation messages). "Permissions and hooks enforce limits regardless of what Claude decides." 설정 병합 managed, 그다음 local, project, user. 훅 matcher는 단일 문자열 "Edit|Write", 대소문자 구분
- context-window: /context는 범주별 실시간 분해를 보여 줌(도구 범주 이름은 이 문서에 없음). 시작 때 CLAUDE.md, 자동 메모리, MCP 도구 이름, 스킬 설명이 로드됨
- how-claude-code-works: 오래된 도구 출력을 먼저 지우고 필요하면 요약, 앞쪽의 자세한 지시는 사라질 수 있음. MCP 도구 정의는 기본 지연 로드
- commands: /hooks "View hook configurations", /mcp enable, disable, reconnect, /permissions 규칙 관리, /agents는 안내 문구(v2.1.197 이하는 대화형 화면)

## S56. Anthropic, Effective context engineering for AI agents. S34 재확인
- URL: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents, 게시일 2025-09-29, 확인일: 2026-10-24, 작성: Anthropic Applied AI 팀(Prithvi Rajasekaran 외)
- "bloated tool sets that cover too much functionality or lead to ambiguous decision points about which tool to use", "curating a minimal viable set of tools"

## 실행 확인 기록(2026-10-24, Linux, python 3 가능, 이 환경에는 Claude Code 없음)
- 실행: cd examples/expense-app && python3 check.py
- 출력(요약 원문): tests: Ran 3 tests ... OK / acceptance: Ran 5 tests ... FAILED (failures=3) / 마지막 두 줄 "tests: 실행 3건, 실패 0건", "acceptance: 실행 5건, 실패 3건", 종료 코드 1
- 실패한 시험: test_1_form_offers_project_codes, test_2_unknown_code_rejected_with_reason, test_3_list_shows_project_code. docs/example-facts.md "구현 전 상태: 수용 시험 1, 2, 3 실패, 4, 5 통과, 단위 테스트 3건 통과"와 일치
- 실행: cd examples/expense-app && python -m unittest discover tests -q → "Ran 3 tests ... OK" (훅 명령의 앞부분)
- 실행하지 못한 것: 훅이 실제로 작동하는 화면, 권한 거부 화면, /context 출력(Claude Code 실행 필요). 부록 실습 2~6은 RUNLOG 실행 전

## 확인하지 못한 것(2026-10-24)
- PostToolUse 종료 코드 2에서 대화 화면에 "hook error" 표기가 나오는지
- 대화형 CLI에서 사람이 거절한 호출이 거부 결과로 기록되는 방식
- 예제 훅이 Windows PowerShell(Git Bash 없음)에서 그대로 동작하는지
- hooks 문서 뒷부분(100,000자 이후)은 열람하지 않음
```

필수 2, 권고 11, 참고 7, 확인한 사실 문장 56개
