# 1장 편집장 검토서 "검증 후 확정" 8개 항목 1차 출처 확인 (fact-checker, 2026-10-23)

결론: 8개 항목 중 31, 43, 48, 57, 80, 82는 1차 출처로 사실이 확인됐다. 46은 사실이며 보완할 점이 있다. 68은 편집장 제안 문장의 앞 절반만 맞고, 뒤 절반은 Anthropic 글과 어긋난다. 50은 openai.com이 이 환경에서 열리지 않아 검색 결과에 인용된 본문 발췌로만 일치하며 직접 열람 확인은 못 했다. 원고와 파일은 고치지 않았다.

확인 환경과 한계
- 로컬 Claude Code v2.1.309(기존 기록은 v2.1.302).
- 임시 파일은 스크래치패드(/tmp/claude-0/-home-user-harness-book/4fa31d71-64a2-5605-bad4-d31a3ffd2331/scratchpad)에만 썼다.
- openai.com은 WebFetch(DNS 실패)와 curl(프록시 CONNECT 403)로 모두 열리지 않았다.
- Anthropic 문서는 WebFetch로 열람했다. 인용 문장은 curl로 받은 원본 HTML에서 다시 대조했다(항목 43, 57, 68).

## 확인 결과 표

| 지적 | 확인 결과 | 1차 출처(제목, 주소, 2026-10-23 확인) | 원문 문장(짧게) | 원고에 쓸 문안 제안 |
|---|---|---|---|---|
| 31 | 사실 | (1) Migrate to Claude Agent SDK, https://code.claude.com/docs/en/agent-sdk/migration-guide, Overview 절과 What's Changed 표. (2) Agent SDK overview, https://code.claude.com/docs/en/agent-sdk/overview, License and terms 절과 Branding guidelines 절 | "The Claude Code SDK has been renamed to the **Claude Agent SDK**". 패키지는 `claude-agent-sdk`(Python)와 `@anthropic-ai/claude-agent-sdk`(TypeScript). overview 문서의 "Use of the Claude Agent SDK is governed by…". 문서 제목과 본문은 줄여서 "Agent SDK"라고도 부른다 | 정식 이름은 "Claude Agent SDK"이고, 예전 이름은 "Claude Code SDK"다. 편집장 풀이는 "프로그램에서 실행하는 개발 도구"인데, overview가 "라이브러리"라고 쓰므로 그쪽이 더 정확하다. 제안: "Claude Agent SDK(Claude Code를 구동하는 것과 같은 도구, 에이전트 루프, 컨텍스트 관리를 Python과 TypeScript로 쓰게 하는 라이브러리)". 이후에는 "Agent SDK"로 줄여 써도 문서 표기와 같다. 본문의 "Claude Code의 Agent SDK"는 Claude Code 제품의 하위 기능처럼 읽히므로 이 표기를 피한다 |
| 43 | 사실 | (1) Anthropic Engineering, "Beyond permission prompts: making Claude Code more secure and autonomous"(페이지 제목 "Making Claude Code safer with sandboxing"), https://www.anthropic.com/engineering/claude-code-sandboxing, 게시 2025-10-20, 1절 "Keeping users secure on Claude Code". (2) "How we built Claude Code auto mode: a safer way to skip permissions", https://www.anthropic.com/engineering/claude-code-auto-mode, 게시 2026-03-25, 작성 John Hughes | (1) "Constantly clicking "approve" slows down development cycles and can lead to 'approval fatigue', where users might not pay close attention to what they're approving, and in turn making development less safe." (2) "Over time that leads to approval fatigue, where people stop paying close attention to what they're approving." 같은 글: "users accept 93% of them anyway"(S14 기록과 일치) | 원문은 "내용을 보지 않고"가 아니라 "주의를 기울이지 않을 수 있다"(might not pay close attention)다. 현재 문장의 "내용을 보지 않고 승인할 수 있어"는 한 단계 강하다. 제안: "확인 요청이 지나치게 잦으면 사람이 승인하는 내용에 주의를 기울이지 않게 되는 승인 피로(approval fatigue)가 생길 수 있다고 Anthropic은 설명합니다.[sandboxing]" R11(각주 하나에 근거 문서 하나)에 따라 이 문장에는 샌드박스 글 하나만 붙인다. 93%는 auto mode 글을 따로 붙인다 |
| 46 | 사실, 보완 필요 | How Claude remembers your project, https://code.claude.com/docs/en/memory, "CLAUDE.md vs auto memory" 표 위 문단, "Import additional files" 절, "How CLAUDE.md files load" 절, AGENTS.md 절, Auto memory 절 | "Both are loaded at the start of every conversation. Claude treats them as context, not enforced configuration." "CLAUDE.md files can import additional files using `@path/to/import` syntax. Imported files are expanded and loaded into context alongside the CLAUDE.md that references them." 작업 위치와 상위 폴더의 CLAUDE.md는 launch 때 로드된다. 하위 폴더의 CLAUDE.md는 Claude가 그 폴더의 파일을 읽거나 쓸 때 로드된다. 자동 메모리의 주제 파일은 "Claude reads them on demand using its standard file tools" | 편집장 제안 문안("역할은 규칙 문서로 컨텍스트 구성 단계에서 모델의 입력이 되고, 기록은 규칙 문서가 가져오도록 정하거나 모델이 읽기 도구로 열 때 입력이 됩니다")은 맞다. 보완할 점 셋. (a) @import한 파일은 가져오는 규칙 문서와 함께 시작 때 같이 로드되므로 컨텍스트 비용이 줄지 않는다(문서 명시). "가져오게 한다"를 "나중에 필요할 때만 들어온다"로 읽히지 않게 한다. (b) 하위 폴더의 규칙 문서는 시작 때가 아니라 그 폴더의 파일을 읽을 때 들어간다. "세션 시작 때 자동"은 작업 위치와 상위 폴더의 규칙 문서에 한정한다. (c) 문서가 "context, not enforced configuration"이라고 직접 쓴다. 편집장이 지적 64로 문제 삼은 "규칙 문서가 컨텍스트냐 설정이냐"에 답하는 1차 근거다. 제안: "규칙 문서(CLAUDE.md)는 세션을 시작할 때 컨텍스트에 들어가는 지침이고, 진행 기록 같은 다른 문서는 규칙 문서가 @로 가져오게 정하거나 모델이 읽기 도구로 열 때 컨텍스트에 들어갑니다." 6장 이후에서 깊이 다룰 내용은 이 장에 넣지 않는다 |
| 48 | 사실 | How the agent loop works, https://code.claude.com/docs/en/agent-sdk/agent-loop, "Turns and messages" 절, "Turns and budget" 표, "Budget headroom" 절. CLI는 https://code.claude.com/docs/en/headless 와 S29 기록 | "You can cap the loop with `max_turns` / `maxTurns`, which counts tool-use turns only." 표: Max turns(`max_turns` / `maxTurns`) 기본값 "No limit", Max budget(`max_budget_usd` / `maxBudgetUsd`) 기본값 "No limit". "Setting a budget is a good default for production agents." 예산은 하위 에이전트 지출을 합산하고, 응답 하나분만큼 상한을 넘을 수 있다. 상한을 강제하는 동작은 Claude Code v2.1.217 이상 | 옵션 이름은 Python `max_turns`, `max_budget_usd`, TypeScript `maxTurns`, `maxBudgetUsd`이고 기본값은 둘 다 제한 없음이다. `max_turns`는 도구 사용 턴만 센다. CLI에도 `--max-turns`, `--max-budget-usd`가 있고 로컬 v2.1.309에서 작동했다. 제안: "상한은 Agent SDK의 옵션으로 정합니다. Python에서는 최대 턴 수를 max_turns, 추정 지출 한도를 max_budget_usd로 두며, 둘 다 기본값은 제한 없음입니다." 괄호 안에 쓸 때는 "(Python의 max_turns, max_budget_usd. 기본값은 제한 없음)"이다. 예산 상한은 응답 하나분만큼 넘을 수 있다는 점을 덧붙이는 것이 실무에 안전하다. 본문의 "턴" 정의는 이 문서 기준(도구 호출 왕복 한 번)으로 쓴다 |
| 50 | 일치(검색 결과가 인용한 openai.com 본문 발췌 기준). 직접 열람 확인은 못 함 | OpenAI, Michael Bolin, "Unrolling the Codex agent loop", https://openai.com/index/unrolling-the-codex-agent-loop/, 게시 2026-01-23. 직접 열람은 WebFetch(DNS 실패)와 curl(프록시 403)에서 모두 실패. WebSearch가 돌려준 openai.com 본문 발췌로만 확인 | 발췌 1: "The journey from user input to agent response shown in the diagram is referred to as one turn of a conversation (a thread in Codex). Though this conversation turn can include many iterations between the model inference and tool calls." 발췌 2: "an agent could decide to make hundreds of tool calls in a single turn, potentially exhausting the context window. For this reason, context window management is one of the agent's many responsibilities." 발췌 3: 대화가 길어질수록 프롬프트도 길어지고, 토큰 수가 임계값을 넘으면 compact한다 | 편집장 제안 문장은 발췌와 일치한다. 다만 (a) 턴 정의는 "사용자 입력부터 에이전트 응답까지"로 Claude Code 용어집의 Turn과 같고 Agent SDK의 턴(도구 호출 왕복 한 번)과 다르다. 이 차이를 본문에 한 문장으로 밝혀야 지적 49(턴 정의 두 곳)와 충돌하지 않는다. (b) 원문은 "수백 번 호출할 수 있다"가 아니라 "그렇게 결정할 수도 있어 컨텍스트 윈도를 소진할 수 있다"(could decide, potentially)다. 제안: "Codex의 에이전트 루프 글은 사용자 입력부터 에이전트 응답까지를 한 턴으로 부르고, 한 턴 안에서 모델 추론과 도구 호출이 여러 번 반복될 수 있다고 설명합니다. 에이전트가 한 턴에 수백 번의 도구 호출을 하기로 해 컨텍스트 윈도를 소진할 수도 있으므로 컨텍스트 윈도 관리는 에이전트의 책임이라고 씁니다." R4 처리: 원문을 직접 열지 못했으므로 Q-040, Q-090은 유지한다. 작가가 브라우저에서 열어 위 세 발췌를 대조하기 전에는 이 문장을 "검색 결과 발췌 기준"으로 둔다(research에 그렇게 기록). 3턴(발췌 2)은 이미 본문에 있는 "수백 번 도구 호출, 컨텍스트 소진"과 같은 내용이다 |
| 57 | 사실(강조점은 팀이 정하는 장치) | Anthropic Engineering, Justin Young, "Effective harnesses for long-running agents", https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents, 게시 2025-11-26(페이지 "Published Nov 26, 2025"), 절 "The long-running agent problem", "Environment management", "Getting up to speed" | "a specialized prompt that asks the model to set up the initial environment: an init.sh script, a claude-progress.txt file that keeps a log of what agents have done, and an initial git commit". 핵심 통찰은 에이전트가 새 컨텍스트 윈도에서 시작할 때 작업 상태를 빨리 파악하게 하는 방법이며, 이를 진행 파일과 git 이력으로 한다. 기능 목록 JSON, 한 번에 한 기능, 종단 간 검증("do all testing as a human user would")도 강조한다. "they must work in discrete sessions, and each new session begins with no memory" | 이 글이 강조하는 것은 진행 파일, 기능 목록, init.sh, git 이력, 종단 간 검사다. 모두 팀(글쓴이)이 초기화 프롬프트와 코딩 프롬프트로 정한 절차이고, 에이전트가 그 절차에 따라 만들고 갱신한다. 제품이 남기는 세션 기록(JSONL)을 강조한 글이 아니다. 따라서 현재 문장의 "세션 기록"은 틀리고 편집장 제안이 맞다. 제안: "장기 실행 글이 강조한 진행 기록과 기능 목록, 검사는 이 정의에서 설정의 기록과 검증에, 에이전트 루프 글이 강조한 루프 실행은 실행 장치에 해당합니다." 추가로 이 글은 하네스를 따로 정의하지 않으며(S12 기록), 이 책의 "설정의 기록과 검증"은 이 책의 분류다. 글이 그렇게 나눈 것처럼 읽히지 않도록 "이 정의에서"를 유지한다. "에이전트 루프 글"은 글이 아니라 Agent SDK 문서이므로 "에이전트 루프 문서"가 정확하다(주체 표기, R3) |
| 68 | 부분 사실. 정의문 자체에는 "시스템 프롬프트"가 없고, 같은 절 다음 문장에 있다 | Effective context engineering for AI agents, https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents, 게시 2025-09-29(메타데이터 수정 2026-10-18), 절 "Context engineering vs. prompt engineering". 원본 HTML로 대조 | 정의: "Prompt engineering refers to methods for writing and organizing LLM instructions for optimal outcomes". 바로 뒤 문장: "As the term implies, the primary focus of prompt engineering is how to write effective prompts, particularly system prompts." 컨텍스트 엔지니어링: "the set of strategies for curating and maintaining the optimal set of tokens (information) during LLM inference, including all the other information that may land there outside of the prompts." 같은 글은 관리 대상인 "entire context state"를 "system instructions, tools, Model Context Protocol (MCP), …"로 나열한다 | 편집장 제안 첫 문장 "원문의 지시문에는 시스템 프롬프트도 들어갑니다"는 정의문만 보면 단정이 지나치다. 정의문은 "LLM instructions"라고만 쓴다. 그러나 같은 절의 다음 문장이 시스템 프롬프트를 프롬프트 엔지니어링의 주된 대상으로 밝히므로 취지는 맞다. 편집장 제안 뒷부분 "시스템 프롬프트와 규칙 문서는 컨텍스트 엔지니어링에서 다룹니다"는 원문과 어긋난다. Anthropic은 시스템 프롬프트를 프롬프트 엔지니어링의 주된 대상으로 두면서, 컨텍스트 상태의 한 요소(system instructions)로도 나열한다. 한쪽으로 확정하는 문장은 쓰지 않는다. 제안: "원문은 프롬프트 엔지니어링의 중심을 프롬프트, 특히 시스템 프롬프트를 쓰는 일이라고 설명합니다. 앞 절에서 프롬프트를 사람이 입력하는 요청으로 좁혔으므로, 이 장에서는 원문의 프롬프트 엔지니어링 가운데 그 요청을 설계하는 부분만 다루고, 시스템 프롬프트와 규칙 문서는 컨텍스트 구성의 일부로 다룹니다." 범위를 "이 장의 구분"으로 못 박는 것은 작가 확정 사항(핵심 정의)이므로 AUTHOR_QUEUE에 질문으로 남기고 권장안을 쓴다 |
| 80 | 사실(SDK 문서, 그리고 Claude Code CLI 실행으로 일부 확인) | (1) How the agent loop works, https://code.claude.com/docs/en/agent-sdk/agent-loop, "Handle the result" 절 표. (2) Run Claude Code programmatically, https://code.claude.com/docs/en/headless, "Get structured output" 절. (3) 로컬 실행 v2.1.309(아래 실행 기록) | "The `subtype` field (available in both SDKs) is the primary way to check termination state." 표: success, error_max_turns, error_max_budget_usd, error_during_execution, error_max_structured_output_retries. 모든 subtype에 total_cost_usd, usage, num_turns, session_id가 있다. headless 문서는 `--output-format json`을 "structured JSON with result, session ID, and metadata"라고만 쓰고 subtype은 명시하지 않는다 | 필드 이름은 `subtype`, 값은 위 5개다. Claude Code CLI에서도 같은 값이 나오는 것을 실행으로 확인했다(`success`, `error_max_turns`, `error_max_budget_usd`). `error_during_execution`은 CLI에서 재현하지 못했고 SDK 문서 기준이다. 편집장 제안 확인 칸 "Agent SDK 결과 메시지의 subtype 값", 기준 칸 "success, error_max_turns, error_max_budget_usd, error_during_execution으로 구분됨"은 맞다. 끝 문장도 맞지만 headless 문서가 subtype을 명시하지 않으므로 "claude -p에 --output-format json을 주면 결과 JSON의 subtype 필드로 같은 값을 확인할 수 있습니다(v2.1.309에서 확인)"로 버전을 밝힌다. 따라 할 수 있는 예: `claude -p "작업" --max-turns 1 --output-format json`을 실행하고 결과의 `"subtype"`을 본다. 이 결과에는 `terminal_reason`(예: max_turns, budget_exhausted, completed)도 함께 나온다. 이 필드는 문서에서 확인하지 못했으므로 본문에 쓰지 않는다 |
| 82 | 사실(차이가 문서에 있음) | Commands, https://code.claude.com/docs/en/commands, `/context [all]` 행. Fullscreen rendering, https://code.claude.com/docs/en/fullscreen, 도입부와 "Enable fullscreen rendering"과 "Fullscreen by default" 절 | "In fullscreen mode, `/context` collapses the per-item breakdown to keep the grid visible. Pass `all` to expand it". fullscreen 문서: "The term fullscreen describes how Claude Code takes over the terminal's drawing surface, the way `vim` does. It has nothing to do with maximizing your terminal window." 켜는 방법은 `/tui fullscreen`(되돌리기 `/tui default`) 또는 환경 변수 `CLAUDE_CODE_NO_FLICKER=1`. 2026-05-06 이후 처음 쓴 사용자(기능 플래그를 받는 세션)는 기본이 fullscreen이고, 그 밖의 설정에서는 classic이 기본이다 | 편집장이 본 "두 명령의 구성이 같다"는 비전체화면(classic)에서 `claude -p`로 돌렸기 때문이다. 문서상 차이는 있다. 전체 화면 모드에서는 `/context`가 항목별 분류를 접고, `/context all`이 펼친다. 이 차이를 전체 화면 모드로 직접 실행해 보지는 못했다(비대화형 `-p`에는 전체 화면이 없다). 제안: "(전체 화면 모드에서는 항목별 분류가 접혀 보이므로 /context all로 펼칩니다. 전체 화면 모드는 터미널 창 최대화가 아니라 Claude Code의 화면 표시 방식으로, /tui fullscreen으로 켭니다.)" 독자 부담이 크면 괄호를 지우고 "분류가 접혀 있으면 /context all"로 줄일 수 있다. 신규 사용자가 기본으로 전체 화면에 들어갈 수 있으므로 이 괄호는 실제로 부딪히는 주의점이다 |

## 실행 기록(R8)

환경: 로컬 Claude Code 2.1.309, 작업 폴더 /home/user/harness-book, 2026-10-23. 모든 호출에 `--output-format json`을 썼다.

1. `claude -p "Read the file /home/user/harness-book/README.md and summarize it in one sentence" --allowedTools Read --max-turns 1 --output-format json`
   - 결과(발췌): `"subtype":"error_max_turns"`, `"is_error":true`, `"terminal_reason":"max_turns"`, `"stop_reason":"tool_use"`, `"num_turns":2`, `"errors":["Reached maximum number of turns (1)"]`, `total_cost_usd` 0.0715.
   - `--max-turns 1`인데 `num_turns`가 2로 나왔다. 문서의 "tool-use turns만 센다"와 이 숫자의 관계는 확인하지 못했다. 본문에 num_turns 값을 쓰지 않는다.
2. `claude -p "Reply with the single word ok" --output-format json --tools ""`
   - 결과(발췌): `"subtype":"success"`, `"is_error":false`, `"terminal_reason":"completed"`, `"stop_reason":"end_turn"`.
   - 반환된 `result` 문자열은 요청과 무관한 내용(이 저장소 작업의 진행 문장)이었고, `session_id`도 이 점검 세션과 같았다. 이 샌드박스에서 `claude -p`가 호출 세션의 상태를 이어받는 것으로 보이나 원인은 확인하지 못했다. 따라서 `subtype` 필드의 존재와 값만 근거로 쓰고 `result` 내용은 근거로 쓰지 않는다.
3. `claude -p "Read /home/user/harness-book/README.md and summarize" --allowedTools Read --max-budget-usd 0.0001 --output-format json`
   - 결과(발췌): `"subtype":"error_max_budget_usd"`, `"is_error":true`, `"terminal_reason":"budget_exhausted"`, `"errors":["Reached maximum budget ($0.0001)"]`.
4. 이 폴더가 신뢰되지 않았다는 경고가 나왔다("Ignoring 32 permissions.allow entries from .claude/settings.json: this workspace has not been trusted"). `-p` 실행에서는 저장소의 허용 규칙이 적용되지 않을 수 있다. 본문의 예시 명령은 `--allowedTools`를 명령줄에 직접 주는 형태가 안전하다.

## research/ch01-sources.md에 덧붙일 기록 문안

```
# 2026-10-23 ch01 편집 검토서 "검증 후 확정" 확인(fact-checker, 1장 플레이북 시범 PR #103)
확인일: 2026-10-23. 원문을 직접 열어 확인한 내용만 적는다. 로컬 Claude Code v2.1.309. 보고 전문은 reviews/agents/2026-10-23-ch01-chief-editor-verify.md

## S44. Anthropic, Migrate to Claude Agent SDK / Agent SDK overview(Claude Code Docs)
- URL: https://code.claude.com/docs/en/agent-sdk/migration-guide , https://code.claude.com/docs/en/agent-sdk/overview
- 게시일: 표기 없음, 확인일: 2026-10-23, 작성: Anthropic
- 사용한 내용: "The Claude Code SDK has been renamed to the Claude Agent SDK"(Overview 절). 패키지 claude-agent-sdk(Python), @anthropic-ai/claude-agent-sdk(TypeScript). overview는 "Use of the Claude Agent SDK is governed by…"로 정식 이름을 쓰고 본문은 "Agent SDK"로 줄여 부름. 브랜딩 지침: 협력사 제품에 "Claude Code" 이름은 허용되지 않음 → 루프 절 1문단 "Claude Agent SDK" 표기(지적 31)

## S45. Anthropic, Making Claude Code safer with sandboxing(제목 표기 "Beyond permission prompts: making Claude Code more secure and autonomous")
- URL: https://www.anthropic.com/engineering/claude-code-sandboxing
- 게시일: 2025-10-20(페이지 "Published Oct 20, 2025"), 확인일: 2026-10-23, 작성: Anthropic(Engineering, 개인 byline 미확인)
- 사용한 내용: "Constantly clicking "approve" slows down development cycles and can lead to 'approval fatigue', where users might not pay close attention to what they're approving, and in turn making development less safe." → 루프 절 확인 요청 문장(지적 43). 원문은 "주의를 기울이지 않을 수 있다"이며 "내용을 보지 않는다"는 아님

## S14 재확인(How we built Claude Code auto mode), 2026-10-23
- URL: https://www.anthropic.com/engineering/claude-code-auto-mode , 게시 2026-03-25, 작성 John Hughes(페이지 "Written by John Hughes")
- "Over time that leads to approval fatigue, where people stop paying close attention to what they're approving", "users accept 93% of them anyway" 일치. 93% 수치는 이 글에만 귀속

## S46. Anthropic, How Claude remembers your project(Claude Code Docs) 재확인
- URL: https://code.claude.com/docs/en/memory , 확인일: 2026-10-23
- 사용한 내용: CLAUDE.md는 launch 때 로드(작업 위치와 상위 폴더), 하위 폴더의 CLAUDE.md는 그 폴더의 파일을 읽거나 쓸 때 로드. "Claude treats them as context, not enforced configuration." @path import는 가져오는 파일과 함께 로드되어 컨텍스트 비용이 줄지 않음. 자동 메모리 MEMORY.md는 처음 200줄 또는 25KB를 시작 때 로드, 주제 파일은 "reads them on demand using its standard file tools". CLAUDE.md가 AGENTS.md를 읽으라고 말로만 적으면 Claude가 파일을 열기로 결정할 때만 봄 → 루프 절 규칙 문서와 진행 기록 문장(지적 46, 64)

## S5 재확인(How the agent loop works), 2026-10-23
- "Turns and budget" 표: max_turns/maxTurns(최대 도구 사용 왕복, 기본 No limit), max_budget_usd/maxBudgetUsd(추정 지출 한도, 기본 No limit). max_turns는 "counts tool-use turns only". 예산은 하위 에이전트 지출 합산, 응답 하나분 초과 가능, 강제 동작은 Claude Code v2.1.217 이상. "Handle the result" 표 subtype: success, error_max_turns, error_max_budget_usd, error_during_execution, error_max_structured_output_retries. 결과 필드 stop_reason(end_turn, max_tokens, refusal)과 subtype은 다름 → 지적 48, 80

## S47. Anthropic, Run Claude Code programmatically(Claude Code Docs) 재확인
- URL: https://code.claude.com/docs/en/headless , 확인일: 2026-10-23
- --output-format json: "structured JSON with result, session ID, and metadata". subtype은 문서에 명시 없음. 실행 확인은 아래 실행 기록

## 실행 기록(지적 80), v2.1.309, 2026-10-23, 작업 폴더 /home/user/harness-book
- claude -p "(읽기 요청)" --allowedTools Read --max-turns 1 --output-format json → subtype error_max_turns, is_error true, terminal_reason max_turns, num_turns 2
- claude -p "Reply with the single word ok" --output-format json --tools "" → subtype success, is_error false, terminal_reason completed. 이 환경에서 result 문자열은 요청과 무관했고 session_id가 호출 세션과 같았음(원인 미확인, subtype만 근거로 씀)
- claude -p "(읽기 요청)" --allowedTools Read --max-budget-usd 0.0001 --output-format json → subtype error_max_budget_usd, is_error true, terminal_reason budget_exhausted
- error_during_execution은 CLI에서 재현하지 못함(SDK 문서 기준)
- 작업 폴더가 신뢰되지 않은 상태라 .claude/settings.json의 permissions.allow 32개가 무시됨(경고 출력)

## S48. Anthropic, Commands / Fullscreen rendering(Claude Code Docs)
- URL: https://code.claude.com/docs/en/commands , https://code.claude.com/docs/en/fullscreen , 확인일: 2026-10-23
- 사용한 내용: "/context [all]": "In fullscreen mode, /context collapses the per-item breakdown to keep the grid visible. Pass all to expand it". fullscreen은 vim처럼 터미널의 대체 화면 버퍼를 쓰는 렌더링 방식이며 창 최대화와 무관. 켜기: /tui fullscreen(되돌리기 /tui default) 또는 CLAUDE_CODE_NO_FLICKER=1. 2026-05-06 이후 처음 쓴 사용자(기능 플래그를 받는 세션)는 기본이 fullscreen. 연구 미리보기 기능 → 표 1-9 컨텍스트 행(지적 82). 비전체화면의 claude -p 실행은 /context와 /context all 구성이 같았음(전체 화면에서 직접 실행은 못 함)

## S12 재확인(Effective harnesses for long-running agents), 2026-10-23
- URL: https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents , 게시 2025-11-26(페이지 "Published Nov 26, 2025")
- 강조한 장치: 초기화 프롬프트가 만드는 init.sh, claude-progress.txt, 첫 git 커밋. 기능 목록 JSON, 한 번에 한 기능, 종단 간 검증. 모두 글쓴이 팀이 프롬프트로 정한 절차이며 제품의 세션 기록(JSONL)은 다루지 않음. "they must work in discrete sessions, and each new session begins with no memory of what came before" → 정의 절 마지막 문장(지적 57)

## S9 재확인(Effective context engineering for AI agents), 2026-10-23
- 원본 HTML 대조. 게시 2025-09-29, 메타데이터 수정 2026-10-18, 저자 표기 Organization Anthropic
- 정의문은 "LLM instructions"라고만 쓰고 시스템 프롬프트를 명시하지 않음. 바로 다음 문장: "the primary focus of prompt engineering is how to write effective prompts, particularly system prompts." 관리 대상 "entire context state (system instructions, tools, MCP, …)"에도 system instructions 포함 → 프롬프트 절(지적 68). 시스템 프롬프트를 컨텍스트 엔지니어링 쪽에만 분류하는 문장은 원문과 맞지 않음

## S3 재확인 시도(OpenAI, Unrolling the Codex agent loop), 2026-10-23
- URL: https://openai.com/index/unrolling-the-codex-agent-loop/ , 게시 2026-01-23, Michael Bolin
- 직접 열람 실패(WebFetch DNS 실패, curl 프록시 CONNECT 403). WebSearch가 돌려준 openai.com 본문 발췌로만: "one turn of a conversation (a thread in Codex)", "this conversation turn can include many iterations between the model inference and tool calls", "an agent could decide to make hundreds of tool calls in a single turn, potentially exhausting the context window. For this reason, context window management is one of the agent's many responsibilities." 확인 수준: 검색 결과 발췌(직접 열람 아님). Codex 턴 = 사용자 입력부터 에이전트 응답까지로 Claude Code 용어집의 Turn과 같고 Agent SDK 턴(도구 호출 왕복)과 다름. Q-040, Q-090 유지, 작가의 브라우저 대조 필요
```

## bibliography.json에 필요한 새 키

현재 키 가운데 아래 5개에 해당하는 것이 없다(기존 키: codex-agent-loop, long-running-harness, context-engineering, agent-loop, memory, commands 등은 이미 있음). 형식은 기존 항목을 따랐다.

```
  "agent-sdk-overview": {"type": "web", "author": "Anthropic", "title": "Agent SDK overview", "venue": "Claude Code Docs", "url": "https://code.claude.com/docs/en/agent-sdk/overview"},
  "agent-sdk-migration": {"type": "web", "author": "Anthropic", "title": "Migrate to Claude Agent SDK", "venue": "Claude Code Docs", "url": "https://code.claude.com/docs/en/agent-sdk/migration-guide"},
  "sandboxing": {"type": "article", "author": "Anthropic", "title": "Beyond permission prompts: making Claude Code more secure and autonomous", "venue": "Anthropic", "date": "2025.10.20", "url": "https://www.anthropic.com/engineering/claude-code-sandboxing"},
  "auto-mode": {"type": "article", "author": "John Hughes", "title": "How we built Claude Code auto mode: a safer way to skip permissions", "venue": "Anthropic", "date": "2026.3.25", "url": "https://www.anthropic.com/engineering/claude-code-auto-mode"},
  "headless": {"type": "web", "author": "Anthropic", "title": "Run Claude Code programmatically", "venue": "Claude Code Docs", "url": "https://code.claude.com/docs/en/headless"},
  "fullscreen": {"type": "web", "author": "Anthropic", "title": "Fullscreen rendering", "venue": "Claude Code Docs", "url": "https://code.claude.com/docs/en/fullscreen"}
```

참고: 새 키는 6개다(위 5개 헤더는 agent-sdk-overview, agent-sdk-migration, sandboxing, auto-mode, headless 5개에 fullscreen을 더한 것). 장 본문에 인용하지 않을 키(fullscreen, auto-mode)는 쓰는 문장이 정해질 때만 추가하면 된다.

## 부수 발견 (이번 확인 범위 밖, 참고)

- /home/user/harness-book/research/bibliography.json에 키 `memory`, `commands`, `sub-agents`, `context-window`, `costs`가 두 번씩 정의되어 있다(예: memory는 20행과 31행, commands는 25행과 32행). 중복 키는 JSON 파서에 따라 뒤의 값이 앞의 값을 덮어쓴다. 현재는 두 항목의 내용이 같아 영향이 없으나, 정리가 필요하다.
- 항목 80의 확인 방법 칸에 쓸 `claude -p` 예시는 작업 폴더가 신뢰되지 않으면 저장소의 permissions.allow가 무시된다는 경고가 나온다(위 실행 기록 4번). 독자가 실습할 때 같은 경고를 만날 수 있다.

필수 0, 권장 3(항목 43 "내용을 보지 않고" 표현 완화, 항목 57 "에이전트 루프 글"을 "문서"로, 항목 68 뒷문장 정정), 참고 3(항목 50 원문 직접 열람 미확인, 항목 80 error_during_execution의 CLI 재현 미확인, 항목 82 전체 화면 모드 직접 실행 미확인), 확인한 사실 문장 28개
