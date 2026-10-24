# 8장 사실 점검(fact-checker)

# Chapter 8 fact-checker 재확인 보고 (src/chapters/ch08.html 전체, 확인일 2026-10-24)

요약: 필수 1, 권고 8, 참고 6, 확인한 사실 문장 46개(일치 38, 보고 대상 8과 미확인 포함 나머지는 아래 표). 원고와 파일은 고치지 않았습니다.

확인한 방법과 한계
- Claude Code 문서 7건(how-claude-code-works, claude-directory, memory, agent-sdk/agent-loop, costs, monitoring-usage, hooks)을 이번에 다시 열었습니다. monitoring-usage는 앞 100,000자, hooks는 앞 100,000자만 읽었습니다.
- Young(2025) 글도 열었습니다.
- openai.com, www.openai.com, jsonlines.org, opentelemetry.io는 이름 해석 실패(getaddrinfo ENOTFOUND)로 열지 못했습니다. 이 항목은 미확인입니다.
- 예제는 실제로 실행해 확인했습니다. `python3 examples/expense-app/check.py`를 실행하니 종료 코드 1이었습니다. tests는 3건 통과, acceptance는 5건 중 3건 실패(test_1, test_2, test_3)였고 test_4, test_5는 통과했습니다. 기준 상태에서 시험 1~3 실패가 맞습니다.

## 지적 표

| 번호 | 위치(절, 문장 첫머리) | 원문 | 확인 결과와 출처(확인일 2026-10-24) | 고친 문안 | 등급 |
|---|---|---|---|---|---|
| 1 | session, 둘째 문단 "세션이 끝난 뒤에도 남는 것은 여럿입니다…" | "…자동 메모리는 각자의 컴퓨터에만 남아 다른 사람과 다른 컴퓨터의 에이전트가 읽지 못합니다" + claude-directory 위첨자 | 내용은 맞습니다. memory 문서 Auto memory 절에 "Auto memory is machine-local… Files are not shared across machines or cloud environments"가 있습니다(https://code.claude.com/docs/en/memory). 그러나 이 문장의 위첨자 키는 claude-directory 하나입니다. claude-directory는 자동 메모리를 "Global only", 커밋 대상 아님으로 표시할 뿐 "컴퓨터별로만 남는다"는 문장은 없습니다. 같은 문장에 서로 다른 두 사실(30일 삭제, 컴퓨터별)이 한 각주에 묶여 있어 R11 위반입니다. | 문장을 둘로 나눕니다. "대화 기록은 로컬 파일로 남지만 기본 30일이 지나면 삭제됩니다[claude-directory]. 자동 메모리는 컴퓨터별로만 저장되어 다른 컴퓨터나 클라우드 환경에서는 공유되지 않습니다[memory]." (memory 키는 bibliography에 이미 있습니다.) | 필수 |
| 2 | session, 첫 문단 "Claude Code의 장기 실행 글도 이 문제를 다룹니다" | 장기 실행 글을 Claude Code의 글로 표기 | 글 본문은 실험 환경을 "Opus 4.5 running on the Claude Agent SDK"라고 쓰고 Claude Code는 감사의 말에만 나옵니다(https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents, 게시 2025-11-26, 저자 Justin Young). 1장도 같은 꼴("Claude Code의 장기 실행 글", 표 1-5 "Claude Code 장기 실행 글")이라 장 사이는 일치합니다. 다만 R3(주어) 문제는 남습니다. D-108 확정 문안이라 고치지 않고 Q-039와 Q-202에 8장 세 곳(session 첫 문단, 진행 기록 문단, handover)을 추가합니다. | (작가 결정 뒤 1, 6, 7, 8장을 함께) 예: "Anthropic의 장기 실행 에이전트 글" | 권고 |
| 3 | logs, 넷째 문단 "Agent SDK 문서는 도구 실행 뒤에 실행되는 PostToolUse 훅을…" | 훅을 "정해진 시점에 자동으로 실행되는 명령"으로 정의한 뒤 SDK 문서의 훅 표를 인용 | agent-loop 문서의 훅 표는 맞습니다. PostToolUse는 "Audit outputs", SubagentStart/SubagentStop은 "Track and aggregate parallel task results", PreCompact는 "Archive full transcript before summarizing"입니다(https://code.claude.com/docs/en/agent-sdk/agent-loop, Hooks 절). 다만 이 훅은 "애플리케이션 프로세스에서 실행되는 콜백"이고, 이 책 독자가 부록 실습 4에서 쓰는 훅은 settings.json의 command 훅입니다. 네 이벤트는 Claude Code 훅 참조에도 있습니다(https://code.claude.com/docs/en/hooks, 이벤트 표: PostToolUse, SubagentStart, SubagentStop, PreCompact. 핸들러 유형 command, http, mcp_tool, prompt, agent). PreCompact는 공통 입력 `transcript_path`로 대화 파일을 복사해 보관할 수 있습니다. 단 기록 파일이 비동기로 써져 마지막 메시지가 빠질 수 있고, 종료 코드 2는 압축을 막습니다. 미열람 범위에 PreCompact 상세가 있어 이 단서는 개요 수준입니다. | 인용 키에 `hooks`(이미 bibliography에 있음)를 추가하거나 "Agent SDK 문서는 콜백 훅의 예로"로 한정하고, "Claude Code에서도 settings.json의 훅으로 같은 이벤트를 쓸 수 있다"를 한 문장 덧붙입니다. | 권고 |
| 4 | logs, 셋째 문단 "기본으로 남는 것은 세션 기록과 실행 결과입니다" | 실행 결과(Agent SDK 결과 메시지)도 "기본으로 남는 것" | 결과 메시지의 필드는 맞습니다. 모든 subtype(success, error_max_turns, error_max_budget_usd, error_during_execution, error_max_structured_output_retries)이 total_cost_usd, usage, num_turns, session_id를 가지며, 충돌 시 error_during_execution이고 비용 필드가 0일 수 있고 stop_reason은 null입니다(agent-loop 문서, Handle the result 절). 그러나 이 값은 SDK 프로그램이 받는 반환값이지 저장되는 로그가 아닙니다. 저장 여부는 프로그램이 정합니다. "기본으로 남음" 묶음(그림 8-2, 표 8-3)에 넣으면 R16(장치의 역할)에서 부정확합니다. | "기본으로 남는 것은 세션 기록이고, SDK로 만든 프로그램은 매 실행 결과를 값으로 받습니다(저장하려면 프로그램이 기록해야 합니다)." 그림 8-2 묶음 이름도 "기본으로 남거나 받음" 정도로 조정을 검토합니다. | 권고 |
| 5 | logs, 셋째 문단 "/usage 명령이 사용량과 비용 추정치를 보여 주며, 이 금액은 정가 기준 추정치이고…" | /usage = 사용량과 비용 추정치, 정가 기준, 청구 근거 아님 | 큰 틀은 일치합니다. Session 블록의 금액은 토큰 수로 로컬 계산한 목록 가격(list price) 추정치이고 청구 근거는 Console Usage 페이지입니다(https://code.claude.com/docs/en/costs, Using the /usage command). 빠진 조건이 둘 있습니다. 첫째, 관리형 설정 `modelPricing`이 있으면 계약 요율 기준이고 그래도 추정치입니다. 둘째, Session 블록은 API 사용자용이며 Pro/Max 구독자에게는 "session cost figure isn't relevant for billing"이고 구독자는 플랜 사용량 막대를 봅니다. 실습 6(5단계)과 표 8-6 "사용량 표시됨"은 구독 계정에서 모양이 다를 수 있습니다. | "…정가 기준 추정치(관리자가 계약 요율을 설정했다면 그 요율 기준)이며 청구 근거가 아닙니다. 구독 계정에서는 플랜 사용량 막대가 함께 보이고 세션 금액은 청구와 관계가 없습니다." | 권고 |
| 6 | logs, 넷째 문단 "개인 사용자는 주로 세션 기록과 /usage를 보고, 조직 지표는 조직의 설정으로 켭니다" | OpenTelemetry는 환경 변수로 켜야 동작, 조직의 설정으로 켠다 | "환경 변수로 켜야 함"은 일치합니다. monitoring-usage는 "Telemetry is off by default"라고 하고 `CLAUDE_CODE_ENABLE_TELEMETRY=1`과 `OTEL_METRICS_EXPORTER` 등 내보내기 변수가 필요합니다. 추적(traces)은 별도 베타로 `CLAUDE_CODE_ENHANCED_TELEMETRY_BETA=1`이 필요합니다(https://code.claude.com/docs/en/monitoring-usage, Enabling telemetry 절). 빠진 조건이 셋입니다. (a) 개인도 셸이나 `~/.claude/settings.json`에서 켤 수 있고 관리자는 관리형 설정으로 배포합니다. "조직의 설정으로만"으로 읽히면 부정확합니다. (b) 저장소의 `.claude/settings.json`과 `settings.local.json`에 적은 OTEL 변수는 무시됩니다. (c) 프롬프트 본문은 기본으로 내보내지 않고(prompt_length만) `OTEL_LOG_USER_PROMPTS=1`을 줘야 포함되며, 도구 세부는 `OTEL_LOG_TOOL_DETAILS=1`이 필요합니다. 명세 "사실 기준"에 있던 프롬프트 기본 비공개가 본문에 없습니다. 같은 문단의 "유일한 선택지" 문장은 costs 문서 원문과 일치합니다("every setup", "the only option that streams per-user token and cost metrics into your own observability stack in near real time"). 주체("비용 문서에 따르면")도 밝혀져 있습니다. | "…조직 지표는 환경 변수로 켜며, 관리자는 관리형 설정으로 배포합니다. 저장소의 .claude/settings.json에 적은 OpenTelemetry 변수는 적용되지 않고, 프롬프트 내용은 따로 켜지 않으면 내보내지 않습니다[monitoring]." | 권고 |
| 7 | session, 셋째 문단 "그러나 다른 에이전트나 새 세션은 그 대화를 읽지 못합니다" | 새 세션은 이전 대화를 읽지 못함 | 맞지만 단정이 넓습니다. how-claude-code-works: `--continue`/`--resume`은 같은 세션 ID로 다시 열고, `--fork-session`이나 `/branch`는 이력을 새 세션 ID로 복사합니다(Resume or fork sessions 절). 갈라 시작한 "새 세션"은 이전 대화를 갖습니다. "Sessions are independent. Each new session starts with a fresh context window"는 새로 시작한 세션 기준입니다. 압축 시 "detailed instructions from early in the conversation may be lost"는 일치합니다(같은 문서, When context fills up 절). | "…그러나 새로 시작한 세션이나 다른 에이전트는 그 대화를 읽지 못합니다(갈라서 시작한 세션은 이력을 복사해 받지만, 원래 세션과 따로 이어집니다)." | 권고 |
| 8 | 버전 주석 "자동 메모리 폴더는 v2.1.228부터 …오래된 메모리 파일이 함께 지워질 수 있었습니다" | v2.1.228 | 버전은 일치합니다. 원문은 "Before v2.1.228, the sweep treated folders inside the memory directory as session data and could delete old files beneath it"입니다(https://code.claude.com/docs/en/claude-directory, Cleaned up automatically 절). 현재 동작은 메모리 파일을 삭제하지 않고 폴더가 보존 기간 내내 비어 있을 때만 그 폴더를 제거하는 것입니다. 형식("버전 주석 (2026년 10월)", 주체 "Claude Code 문서에 따르면", 사례 뒤 별도 상자)은 BOOK_SPEC 118행과 일치합니다. 다만 "오래된 메모리 파일이 함께"는 원문(메모리 폴더 안의 하위 폴더가 정리 대상)보다 넓게 읽힙니다. | "…v2.1.228 이전에는 메모리 폴더 안의 하위 폴더가 세션 데이터로 취급되어 그 아래 오래된 파일이 지워질 수 있었습니다." | 권고 |
| 9 | logs, "보관 기간" 항목 및 표 8-6 "보관 기간" | cleanupPeriodDays로 변경, 기본 30일 | 일치합니다(기본 30, 최솟값 1, 0은 검증 오류. claude-directory Cleaned up automatically 절). costs 문서도 "at startup, it removes files older than cleanupPeriodDays, 30 days by default"로 시작 시 삭제를 확인합니다. 빠진 주의점이 있습니다. (a) 정리는 `claude -p --bare`에서는 실행되지 않고, 보존 기간을 안전하게 정할 수 없으면 일시 중지되며, 관리형 설정이 값을 정할 수 있습니다. (b) 세션 기록은 평문이고 도구가 읽은 .env 내용이나 출력된 자격 증명도 JSONL에 기록됩니다. 문서는 노출을 줄이려면 기간을 낮추라고 안내합니다(Plaintext storage 절). 기간을 늘리라는 조언에는 이 위험을 함께 적어야 합니다. (c) `CLAUDE_CODE_SKIP_PROMPT_HISTORY`나 `--no-session-persistence`(-p)를 쓰면 기록 자체가 남지 않습니다. | "…확인에 필요한 만큼만 늘리고, 세션 기록은 암호화되지 않은 평문이라 비밀 값이 들어갈 수 있음을 함께 고려합니다." 표 8-6 보관 기간 행에 관리형 설정이 값을 정할 수 있다는 점을 덧붙입니다. | 권고 |
| 10 | session, 첫째 문단 끝 "Codex의 하네스 엔지니어링 글도 에이전트가 실행 중에 접근할 수 없는 지식은… 없는 것과 같다고 밝혔습니다" | 문서 도구, 채팅, 사람의 기억 | 미확인. 이번에도 https://openai.com/index/harness-engineering/ 와 www 도메인이 이름 해석 실패로 열리지 않았습니다. 검색으로는 게시일 2026-02-11, 저자 Ryan Lopopolo, 5개월 실험 개요까지만 확인했고 이 문장은 확인하지 못했습니다. 이 문장은 research/ch01-sources.md S2(2026-10-04 열람)에만 의존합니다(Q-030 유지). 표기("Codex의 하네스 엔지니어링 글")는 1장과 같은 꼴입니다. 인용 키 harness-engineering은 bibliography와 일치합니다(Ryan Lopopolo, OpenAI, 2026.2.11). | 문안 유지. 작가 직접 열람 목록(Q-030, Q-202)에 8장 session 절 문장을 추가합니다. | 참고 |
| 11 | logs, "JSONL은 한 줄에 한 항목씩 적는 텍스트 파일 형식입니다", "OpenTelemetry는 지표와 이벤트를 조직의 관측 시스템으로 보내는 표준 방식" | 용어 풀이 | R8 요구인 1차 출처 확인 미완료. jsonlines.org와 opentelemetry.io가 열리지 않았습니다. Claude Code 문서가 확인해 주는 범위는 "plaintext JSONL file"(저장 형식)과 OpenTelemetry로 지표와 이벤트(logs)를 내보낸다는 것까지입니다(monitoring-usage). OpenTelemetry 자체의 정의(관측 프레임워크, 추적/지표/로그)는 확인하지 못했습니다. "표준 방식"이 프로토콜(OTLP)을 가리키는지 프레임워크를 가리키는지도 미확인입니다. | 다른 환경에서 두 사이트의 정의 문장을 확인한 뒤 풀이를 확정합니다. 임시로 "OpenTelemetry는 지표와 이벤트 같은 관측 자료를 내보내는 공개 표준 도구입니다"처럼 단정을 낮춘 문안을 검토합니다. | 참고 |
| 12 | session, 둘째 문단 "commit으로 변경 이력이 남고, 다른 세션과 다른 에이전트, 사람이 같은 파일을 읽기 때문입니다" | 저장소 문서와 commit이 기준 | 이 책의 판단 문장이라 1차 출처 판정 대상은 아닙니다. 실무 주의점이 있습니다. commit은 로컬 저장소에 남을 뿐이라 다른 컴퓨터의 에이전트나 다른 사람이 읽으려면 push가 필요합니다. 바로 앞 문장이 "다른 컴퓨터의 에이전트가 읽지 못합니다"라고 대비하므로 push 전제를 한 마디 적으면 틀리게 이어지지 않습니다. | "…같은 저장소를 공유하면(push한 뒤) 다른 세션과 다른 에이전트, 사람이 같은 파일을 읽기 때문입니다." | 참고 |
| 13 | example, 마지막 문단 "사용자 폴더의 .claude/projects/ 아래 세션 기록 파일에서 python check.py 실행과 그 출력을 찾아" | 세션 기록 경로, 검사 출력 확인 | 경로는 일치합니다(`~/.claude/projects/<project>/<session>.jsonl`, Windows는 `%USERPROFILE%\.claude`, `CLAUDE_CONFIG_DIR`이 있으면 그 아래). 전체 메시지, 도구 호출, 도구 결과가 기록됩니다(claude-directory). 실습 보조 주의점이 둘 있습니다. 큰 도구 출력은 `<session>/tool-results/`로 따로 저장될 수 있어 check.py 출력이 길면 JSONL 본문에서 바로 보이지 않을 수 있습니다. 하위 에이전트(reviewer) 기록은 `<session>/subagents/`에 따로 있습니다. 이번 실행 기준 check.py 출력은 짧은 편이라 보통 본문에 남을 것으로 보이나, 실제 세션 기록으로는 검증하지 않았습니다. | 표 8-6 세션 기록 행에 "Windows는 %USERPROFILE%\.claude\projects\" 한 줄 추가를 검토합니다(필수 아님). | 참고 |
| 14 | example/check, "작업 2, 3 완료", 표 8-4, 인계 메모의 "확인 명령" | 예제 사실 대조 | 일치합니다(아래 일치 목록). 연관 사실 하나만 알립니다. `python3 tools/check_tasks.py` 요약은 "공백 1건(작업 2)"입니다. 작업 2의 확인 방법("수용 시험 4, 5 통과")은 기준 상태에서도 이미 통과하므로 작업 전 상태와 구분되지 않습니다. 8장 본문 오류는 아니고 예제(tasks.example.json) 쪽 기존 이슈입니다. | 8장은 수정 없음. 실습 폴더 쪽은 작가 확인(기존 도구 출력 그대로 전달). | 참고 |
| 15 | 진행 기록 문단 "세마다 설명이 포함된 commit을 남기고 진행 요약을 기록하도록 하자…복구할 수 있었습니다" | Young 글 | 원문과 일치합니다("commit its progress to git with descriptive commit messages", "allowed the model to use git to revert bad code changes and recover working states"). 다만 글은 정성적 서술이고 효과를 측정한 비교 실험이 아닙니다("하자…수 있었습니다"는 글의 "allowed"와 같은 수준이라 허용 가능). R13 점검 결과 범위 과장은 없습니다. | 문안 유지. | 참고 |

## 일치로 확정한 사실 문장(근거 위치)

| 문장 | 위치 | 근거 |
|---|---|---|
| 세션은 서로 독립이고 세션마다 새 컨텍스트 | session 첫 문단 | how-claude-code-works, Work with sessions: "Sessions are independent. Each new session starts with a fresh context window" |
| 세션 사이 지식은 CLAUDE.md(사람)와 자동 메모리(Claude) | session 첫 문단 | memory 첫 단락 "Two mechanisms carry knowledge across sessions" |
| 새 세션은 이전 세션의 기억 없이 시작 | session 첫 문단 | Young: "each new session begins with no memory of what came before" |
| 대화 기록은 로컬에 저장되고 기본 30일 후 삭제 | session 둘째 문단 | claude-directory Cleaned up automatically (기본 30, 최솟값 1) |
| `--resume`으로 지난 세션을 다시 열어 이어 감 | session 셋째 문단 | how-claude-code-works, Resume or fork sessions |
| 압축되면 앞부분의 지시를 잃을 수 있음 | session 셋째 문단, 표 8-5 | how-claude-code-works, When context fills up. memory 문서는 루트 CLAUDE.md는 압축 뒤 다시 주입된다고 안내 |
| 메시지, 도구 사용, 결과를 로컬 JSONL로 저장. 되감기, 이어 가기, 갈라 시작 | logs 셋째 문단, 표 8-3 | how-claude-code-works Work with sessions |
| 모든 결과에 비용, 토큰 사용량, 턴 수, 세션 ID. 오류로 끝나도 비용 확인과 세션 이어 가기. 충돌 시 비용 0 가능 | logs, 표 8-3 | agent-loop Handle the result("All result subtypes carry total_cost_usd, usage, num_turns, and session_id…"). 책의 "종료 사유=결과 종류(subtype)"는 1장 표기와 같은 이 책의 표현 |
| Claude Agent SDK = Claude Code의 에이전트 루프를 Python/TypeScript에서 실행하는 라이브러리 | logs 셋째 문단 | agent-loop 도입부 "embed Claude Code's autonomous agent loop"(Python, TypeScript SDK). 1장 56행의 풀이와 문구가 같음 |
| PostToolUse(출력 감사), SubagentStart/Stop(병렬 작업 추적), PreCompact(요약 전 전체 대화 보관) | logs 넷째 문단, 표 8-3 | agent-loop Hooks 표(row 3 참고) |
| OpenTelemetry는 모든 이용 방식에서 동작하고 사용자별 토큰, 비용 지표를 거의 실시간으로 내보내는 유일한 선택지 | logs 넷째 문단 | costs, Manage costs for your organization 표 아래 문장 |
| 기본 30일이 지난 세션 데이터를 시작할 때 삭제, cleanupPeriodDays로 변경 | 정할 것 첫 항목, 표 8-3 | costs(/insights 절)와 claude-directory |
| 자동 메모리는 컴퓨터별(machine-local) | session 둘째 문단 | memory Auto memory 절 (인용 키는 row 1 참고) |
| v2.1.228 이전/이후 | 버전 주석 | claude-directory Auto memory 항목(row 8 참고) |
| 실험 시작 때 git 로그와 진행 파일을 읽음 | handover 끝 | Young: "Read the git logs and progress files to get up to speed" |
| 실험의 설명 있는 commit, 되돌리기와 복구 | kinds 끝 | Young(row 15) |
| D-012 줄 | decisions 코드 상자 | examples/expense-app/DECISIONS.md의 D-012 줄과 문자열 완전 일치(파이썬으로 비교, True). 헤더 5열도 같음. D-015는 가상 예시로 본문이 밝힘. 실습 폴더에는 D-012 한 건뿐(표 8-6과 일치) |
| 표 8-4 읽는 순서 CR.md 1, DECISIONS.md 2, tasks.json 3, HANDOFF.md 4 | example | reference/CLAUDE.example.md "읽는 순서" 1~4와 일치 |
| 작업 2~4는 에이전트가 check.py 통과 뒤 통과 값 변경, 작업 5는 사람 | 표 8-4 | CLAUDE.example.md 작업 순서("작업 5의 통과 값은 변경하지 않는다")와 tasks.example.json 작업 5 확인 방법 "사람 승인(통과 값은 사람이 변경)" |
| DECISIONS.md는 에이전트가 수정하지 않음. 수정할 수 있는 것은 expense/, app.py, tests/, tasks.json 통과 값, HANDOFF.md | 표 8-4, example | CLAUDE.example.md 수정 범위 |
| commit은 사람 확인 뒤 | 표 8-4 | CLAUDE.example.md "commit은 사람 확인 후" |
| 인계 메모 다섯 항목(현재 상태, 읽을 문서, 미결정, 다음 작업, 확인 명령) | handover, 표 8-6 | CLAUDE.example.md 중단 규칙 "현재 상태, 읽을 문서, 미결정, 다음 작업, 확인 명령" |
| 작업 4 완료 기준 "화면에서 프로젝트 코드 선택 가능, 목록에 없는 코드 거부" | 인계 메모 예 | tasks.example.json 작업 4 완료 기준과 일치 |
| 작업 2, 3, 4 이름(데이터 항목 추가, 단위 테스트 갱신, 화면 선택 항목) | example 첫 문단 | tasks.example.json과 일치 |
| 시험 1~3은 작업 4의 화면 기능, 작업 전에는 실패 | example | acceptance/test_cr07.py(test_1 폼 코드 제공, test_2 목록 외 코드 거부, test_3 목록 표시) 실행 출력: FAILED (failures=3), 종료 코드 1. 작업 2, 3 완료 뒤 시험 4, 5는 통과해야 한다는 서술과도 모순 없음 |
| 실습 6 요청문 "HANDOFF.md를 읽고 이어서 작업해 줘." | example, 표 8-6 | src/appendix/practice.html 실습 6 2단계와 일치. 실습 5, 6의 "작업 3까지 하고 작업 4는 실습 6" 흐름과 일치 |
| 표 8-6 "git log --oneline로 작업 2, 3 commit 대조", "실습 폴더 expense-practice" | check | 실습 5 확인 방법(commit 두 개 추가), 실습 1(`cp -r harness-book/examples/expense-app expense-practice`)과 일치 |
| 앵커 링크 ch01#loop, ch02#components, ch02#instruct-enforce, ch05#rule-doc, ch05#maintenance, ch06#split, ch06#example, ch07#report | 본문 | 모두 대상 파일에 id가 있음. ch02의 "기록"은 결정 기록과 진행 기록으로 정의되어 8장 서술과 일치 |
| 인용 키 8개(long-running-harness, how-cc-works, memory, claude-directory, agent-loop, costs, monitoring, harness-engineering) | 본문 위첨자 | research/bibliography.json에 모두 존재, 제목, 저자, 주소 일치 |

## 위첨자 키와 문장 대응 점검
- 맞는 곳: 장기 실행 글 세 곳(분리된 세션, 진행 기록과 git 복구, 세션 시작 시 로그 읽기), how-cc-works(독립 세션, --resume과 압축, JSONL), memory(두 전달 수단), agent-loop(결과 필드와 훅 표), costs(/usage와 유일한 선택지, 30일 삭제), monitoring(켜는 방법), harness-engineering(Codex 인용).
- 어긋난 곳: 한 곳(row 1, 자동 메모리 컴퓨터별은 memory 키).
- 위첨자가 없지만 필요해 보이는 사실 문장: 없음. 도입부(1~3문단)의 "새 컨텍스트에서 시작", "압축되면 사라질 수 있음"은 본문 session 절에서 출처가 붙어 있습니다. 용어 풀이(JSONL, OpenTelemetry의 정의)는 row 11 참고.

## research/ch08-sources.md에 덧붙일 기록 블록

```
## 2026-10-24 fact-checker 재확인(8장 플레이북 정리, 이슈 #116)

### S-C8-12. 재확인: Claude Code 문서 7건
- URL: https://code.claude.com/docs/en/how-claude-code-works, /claude-directory, /memory, /agent-sdk/agent-loop, /costs, /monitoring-usage, /hooks
- 게시일: 표기 없음, 확인일: 2026-10-24
- 작성: Anthropic
- 사용한 내용 요약
  - how-claude-code-works Work with sessions, Resume or fork sessions, When context fills up: "Sessions are independent. Each new session starts with a fresh context window." JSONL은 ~/.claude/projects/. --continue/--resume은 같은 세션 ID로 다시 열고 --fork-session과 /branch는 이력을 새 세션 ID로 복사. 압축 시 이른 대화의 상세 지시가 사라질 수 있음
  - claude-directory Application data: cleanupPeriodDays 기본 30, 최솟값 1, 0은 검증 오류. projects/<project>/<session>.jsonl은 전체 대화(메시지, 도구 호출, 도구 결과). 하위 에이전트 기록은 <session>/subagents/, 큰 도구 출력은 <session>/tool-results/. 자동 메모리 디렉터리는 정리 대상이 아니며 v2.1.228 이전에는 메모리 디렉터리 안의 폴더를 세션 데이터로 취급해 그 아래 오래된 파일을 지울 수 있었음. 정리는 --bare(-p)에서 실행하지 않고, 보존 기간을 안전하게 정할 수 없으면 일시 중지. 기록은 평문이며 CLAUDE_CODE_SKIP_PROMPT_HISTORY, --no-session-persistence(-p)로 기록 생략 가능
  - memory: 첫 문장 "Each Claude Code session begins with a fresh context window." 자동 메모리는 "machine-local", 같은 git 저장소의 worktree는 한 디렉터리를 공유하고 다른 컴퓨터나 클라우드 환경과는 공유하지 않음
  - agent-loop Handle the result, Hooks: 모든 result subtype이 total_cost_usd, usage, num_turns, session_id를 가짐. 충돌 시 error_during_execution, 비용 필드 0 가능, stop_reason null. 훅 표 PostToolUse(출력 감사), SubagentStart/SubagentStop(병렬 작업 결과 추적), PreCompact(요약 전 전체 대화 보관). 훅은 애플리케이션 프로세스에서 실행되는 콜백
  - hooks(앞 100,000자만 읽음): 이벤트 표에 PostToolUse, SubagentStart, SubagentStop, PreCompact가 있고 settings.json의 command 훅 등으로 설정. PreCompact 상세 절은 미열람
  - costs: /usage Session 블록 금액은 로컬 계산한 목록 가격 기준 추정치(관리형 modelPricing이 있으면 계약 요율, 그래도 추정치). 구독자에게는 세션 금액이 청구와 무관. OpenTelemetry는 every setup, only option(near real time). /insights 보고서도 시작 때 cleanupPeriodDays로 삭제
  - monitoring-usage(앞 100,000자만 읽음): 텔레메트리 기본 꺼짐. CLAUDE_CODE_ENABLE_TELEMETRY=1과 내보내기 변수 필요. 저장소의 .claude/settings.json, settings.local.json의 OTEL 변수는 무시. 프롬프트 본문은 OTEL_LOG_USER_PROMPTS=1일 때만, 도구 세부는 OTEL_LOG_TOOL_DETAILS=1일 때만 내보냄
- 확신: 높음(hooks, monitoring-usage는 뒤쪽 미열람)

### S-C8-13. 재확인: Young(2025)
- URL: https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
- 게시일: 2025-11-26, 확인일: 2026-10-24
- 작성: Justin Young
- 사용한 내용 요약: discrete sessions, 새 세션은 이전 기억 없음. init.sh, claude-progress.txt, 기능 목록 JSON, 첫 git 커밋. 세션 시작 때 git 로그와 진행 파일 읽기. 설명 있는 커밋으로 되돌리기와 복구. 실험 환경은 "Opus 4.5 running on the Claude Agent SDK". 본문에 Claude Code 언급 없음(감사의 말에만). 정성적 서술이며 측정 비교 실험이 아님
- 확신: 높음

### S-C8-8 갱신(2026-10-24)
- openai.com, www.openai.com이 getaddrinfo ENOTFOUND로 열리지 않음. 검색은 게시일 2026-02-11, 저자 Ryan Lopopolo, 5개월 실험 개요까지만 확인. "접근할 수 없는 지식은 없는 것과 같다" 문장은 계속 미확인(Q-030)

### 미확인(2026-10-24)
- JSONL(JSON Lines) 정의: jsonlines.org 이름 해석 실패
- OpenTelemetry 정의: opentelemetry.io 이름 해석 실패. Claude Code 문서가 확인해 주는 범위는 지표와 이벤트 내보내기까지
- hooks 문서 뒤 179,616자, monitoring-usage 문서 뒤 72,246자 미열람

### 예제 실행 기록(2026-10-24)
- 명령: python3 examples/expense-app/check.py (작업 폴더 examples/expense-app)
- 결과: 종료 코드 1. tests: 실행 3건, 실패 0건, 건너뜀 0건, project_code 시험 0건. acceptance: 실행 5건, 실패 3건, 건너뜀 0건(정한 수 5건). 실패는 test_1_form_offers_project_codes, test_2_unknown_code_rejected_with_reason, test_3_list_shows_project_code. test_4, test_5는 통과
- 명령: python3 tools/check_tasks.py → 마지막 줄 "요약: 공백 1건(작업 2)", 작업 4는 "구현 전 상태에서 실패(FAILED (failures=3))"로 정상, 작업 5는 사람 판단으로 건너뜀
- D-012 줄 비교: src/chapters/ch08.html 코드 상자의 D-012 줄과 examples/expense-app/DECISIONS.md의 D-012 줄은 문자열 완전 일치
```

필수 1, 권고 8, 참고 6, 확인한 사실 문장 46개

관련 파일(모두 절대 경로)
- /home/user/harness-book/src/chapters/ch08.html
- /home/user/harness-book/research/ch08-sources.md
- /home/user/harness-book/examples/expense-app/DECISIONS.md
- /home/user/harness-book/examples/expense-app/reference/CLAUDE.example.md
- /home/user/harness-book/examples/expense-app/reference/tasks.example.json
- /home/user/harness-book/src/appendix/practice.html
- /home/user/harness-book/research/bibliography.json
