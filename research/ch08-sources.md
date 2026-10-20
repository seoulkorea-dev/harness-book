# Chapter 8 출처 기록

2026-10-20 researcher 조사(8장 개정, PR #41). 이전 8장 출처는 research/ch03-10-sources.md에 있음.
요약
- 1차 원문을 연 것: Claude Code 문서 5건과 Young(2025).
- 열지 못한 것: Lopopolo(OpenAI)와 Nygard(2011). openai.com, www.openai.com, cognitect.com, www.cognitect.com, www.infoq.com, adr.github.io는 이름 해석(ENOTFOUND)이 실패했고, web.archive.org는 차단됐다. 이 환경에는 셸이 없어 다른 경로로 접속하지 못했다.
- 본문 사실 문장 대부분은 원문과 일치한다. 고칠 점은 두 가지다. (1) 대화 이력이 같은 세션 안에서만 유효하다는 문장은 `--resume`/`--continue` 때문에 부정확하다. (2) 세션이 끝난 뒤 남는 것이 문서와 커밋뿐이라는 문장은 JSONL 기록과 자동 메모리를 빠뜨렸다.

---
## 기록

### S-C8-1. Anthropic, How Claude Code works (Claude Code Docs)
- URL: https://code.claude.com/docs/en/how-claude-code-works
- 게시일: 표기 없음, 확인일: 2026-10-20
- 작성: Anthropic
- 이 장에서 사용할 내용
  - 대화를 로컬에 저장함. 메시지, 도구 사용, 결과가 `~/.claude/projects/` 아래 "plaintext JSONL file"에 기록됨. 되감기, 이어 가기, 갈라 시작하기가 가능함
  - "Sessions are independent." 새 세션은 이전 세션의 대화 이력 없이 새 컨텍스트 창으로 시작함. 자동 메모리와 CLAUDE.md로 세션 사이에 내용을 전달함
  - `claude --continue` 또는 `claude --resume`은 같은 세션 ID로 다시 열고 새 메시지를 기존 대화에 덧붙임. `--fork-session` 또는 `/branch`는 이력을 새 세션 ID로 복사함
  - 컨텍스트가 차면 자동 압축함. "detailed instructions from early in the conversation may be lost." 지속할 규칙은 CLAUDE.md에 둘 것을 안내함
  - 자동 메모리 MEMORY.md는 첫 200줄 또는 25KB 중 먼저 닿는 쪽까지 세션 시작 때 로드됨
  - 체크포인트(파일 스냅숏)는 git과 별개이고 파일 변경만 다룸
- 확신: 높음

### S-C8-2. Anthropic, Explore the .claude directory (Claude Code Docs)
- URL: https://code.claude.com/docs/en/claude-directory (Application data 절)
- 게시일: 표기 없음, 확인일: 2026-10-20
- 작성: Anthropic
- 이 장에서 사용할 내용
  - `projects/<project>/<session>.jsonl`은 전체 대화 기록(모든 메시지, 도구 호출, 도구 결과)임
  - 하위 에이전트 기록은 `projects/<project>/<session>/subagents/`에 있고, 부모 세션 기록이 만료될 때 함께 삭제됨
  - `cleanupPeriodDays`보다 오래된 파일을 삭제함. 기본값 30일, 최솟값 1, 0을 설정하면 검증 오류. 시작 시 삭제한다는 표현은 costs 문서에 있음
  - 자동 메모리 디렉터리 `projects/<project>/memory/`는 이 정리에서 삭제하지 않음. 비어 있는 채로 보존 기간이 지나면 디렉터리만 제거함(v2.1.228 이전에는 오래된 파일이 지워질 수 있었음)
  - Claude Desktop과 Cowork에서 시작한 세션 기록은 `desktopSessionCleanupPeriodDays` 미설정 시 나이와 관계없이 보관됨(v2.1.248 이상). 관리형 설정이 `cleanupPeriodDays`를 정하면 이 예외가 적용되지 않음
- 확신: 높음. 문서가 길어 해당 절만 확인했다.

### S-C8-3. Anthropic, How Claude remembers your project (Claude Code Docs)
- URL: https://code.claude.com/docs/en/memory
- 게시일: 표기 없음, 확인일: 2026-10-20
- 작성: Anthropic
- 이 장에서 사용할 내용
  - 첫 문장 "Each Claude Code session begins with a fresh context window." 세션 사이에 지식을 전달하는 것은 두 가지임. CLAUDE.md(사람이 씀)와 자동 메모리(Claude가 씀)
  - CLAUDE.md와 자동 메모리는 강제 설정이 아니라 컨텍스트임. 동작을 막으려면 PreToolUse 훅을 씀
  - 문제 해결 절 "Instructions seem lost after /compact": 프로젝트 루트 CLAUDE.md는 압축 뒤 디스크에서 다시 읽어 주입됨. 지시가 사라졌다면 대화에서만 준 것이거나 하위 디렉터리 CLAUDE.md이거나 경로별 규칙이기 때문임. "Add conversation-only instructions to CLAUDE.md to make them persist."
  - CLAUDE.md가 없고 AGENTS.md만 있으면 AGENTS.md를 읽음(AGENTS.md 절, 2026-10-04 기록에 v2.1.277 이상으로 적혀 있음. 이번에 해당 절은 다시 열지 않음)
- 확신: 높음

### S-C8-4. Anthropic, How the agent loop works (Agent SDK, Claude Code Docs)
- URL: https://code.claude.com/docs/en/agent-sdk/agent-loop
- 게시일: 표기 없음, 확인일: 2026-10-20
- 작성: Anthropic
- 이 장에서 사용할 내용
  - ResultMessage는 최종 텍스트, 토큰 사용량, 비용, 세션 ID를 담음
  - "All result subtypes carry total_cost_usd, usage, num_turns, and session_id so you can track cost and resume even after errors."
  - 결과 subtype: success, error_max_turns, error_max_budget_usd, error_during_execution, error_max_structured_output_retries
  - 단서: 세션이 충돌하면 최종 결과는 error_during_execution이고 비용 필드가 0으로 채워질 수 있음. `stop_reason`은 null일 수 있음. Python에서는 비용 필드가 None일 수 있음
  - `usage`는 주 에이전트 루프만 다룸. 하위 에이전트까지 합산하려면 `modelUsage`/`model_usage`를 씀
  - 훅 표: PostToolUse(도구 반환 뒤, 출력 감사), SubagentStart / SubagentStop(병렬 작업 결과 추적과 집계), PreCompact(압축 전, "Archive full transcript before summarizing"), Stop(결과 검증, 세션 상태 저장). 훅은 에이전트 컨텍스트 밖의 애플리케이션 프로세스에서 실행되어 컨텍스트를 쓰지 않음
  - 압축: 이른 대화의 지시는 보존되지 않을 수 있음. 지속 규칙은 CLAUDE.md에 둠. 압축 지침 절을 CLAUDE.md에 넣어 요약기가 보존할 것을 알릴 수 있음. PreCompact 훅은 `trigger`(manual 또는 auto)를 받음
  - 세션 ID(`ResultMessage.session_id`)로 이어 가거나(resume) 갈라 시작함(fork). 이어 가면 이전 턴의 컨텍스트가 복원됨
- 확신: 높음

### S-C8-5. Anthropic, Manage costs effectively (Claude Code Docs)
- URL: https://code.claude.com/docs/en/costs
- 게시일: 표기 없음, 확인일: 2026-10-20
- 작성: Anthropic
- 이 장에서 사용할 내용
  - "OpenTelemetry export works on every setup and is the only option that streams per-user token and cost metrics into your own observability stack in near real time." 여기서 setup은 Teams/Enterprise, Console, 클라우드 제공자 같은 이용 방식을 가리킴
  - Bedrock, Google Cloud Agent Platform, Foundry에서는 Claude Code가 지표를 Anthropic으로 보내지 않아 분석 대시보드가 이 사용량을 다루지 않음. 사용자별 귀속에는 OpenTelemetry, Claude apps gateway, LLM gateway가 있음
  - `/usage`의 비용은 목록 가격 기준 추정치이며 청구 근거가 아님
  - `/insights` 보고서도 `cleanupPeriodDays`에 따라 삭제됨
  - 배경 토큰 사용: `--resume` 기능을 위한 이전 대화 요약 작업이 백그라운드에서 돎. 보통 세션당 0.04달러 미만
- 확신: 높음

### S-C8-6. Anthropic, Monitoring (OpenTelemetry), Claude Code Docs
- URL: https://code.claude.com/docs/en/monitoring-usage
- 게시일: 표기 없음, 확인일: 2026-10-20 (앞 100,000자까지 읽음, 뒤 56,414자는 미열람)
- 작성: Anthropic
- 이 장에서 사용할 내용
  - 지표(metrics): `claude_code.session.count`, `claude_code.cost.usage`, `claude_code.token.usage`, `claude_code.lines_of_code.count`, `claude_code.commit.count`, `claude_code.pull_request.count`, `claude_code.active_time.total` 등
  - 이벤트(logs): `claude_code.user_prompt`, `claude_code.tool_result`, `claude_code.tool_decision`, `claude_code.api_request`, `claude_code.api_error` 등. `prompt.id`로 프롬프트와 묶임
  - 추적(traces)은 베타임. `CLAUDE_CODE_ENABLE_TELEMETRY=1`과 `CLAUDE_CODE_ENHANCED_TELEMETRY_BETA=1`이 둘 다 필요함
  - 켜는 방법: `CLAUDE_CODE_ENABLE_TELEMETRY=1`과 `OTEL_METRICS_EXPORTER`, `OTEL_LOGS_EXPORTER`, 엔드포인트 지정. 즉 기본으로 켜져 있지 않음
  - 저장소의 `.claude/settings*.json`에 있는 OTLP 내보내기 변수는 무시됨. 관리자는 관리형 설정으로 배포함
  - 프롬프트 내용은 `OTEL_LOG_USER_PROMPTS=1`을 줘야 기록되고, 도구 매개변수는 `OTEL_LOG_TOOL_DETAILS=1`이 있어야 기록됨
  - 사용자 식별: `user.id`(첫 실행 때 만든 익명 값), `user.email`(가능할 때), `session.id` 등. `OTEL_RESOURCE_ATTRIBUTES`로 팀과 부서 속성을 붙임
- 확신: 높음

### S-C8-7. Anthropic(Justin Young), Effective harnesses for long-running agents
- URL: https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
- 게시일: Nov 26, 2025, 확인일: 2026-10-20
- 작성: Justin Young
- 이 장에서 사용할 내용
  - 에이전트는 "must work in discrete sessions, and each new session begins with no memory of what came before."
  - 초기화 에이전트가 `init.sh`(개발 서버를 실행하는 스크립트), `claude-progress.txt`("keeps a log of what agents have done"), 기능 목록 JSON(모두 failing으로 시작), 첫 git 커밋을 만듦
  - 코딩 에이전트는 시작 때 "Read the git logs and progress files to get up to speed."
  - 설명이 있는 커밋: "commit its progress to git with descriptive commit messages". 효과는 "use git to revert bad code changes and recover working states of the code base"
  - 실험은 "Opus 4.5 running on the Claude Agent SDK"에서 진행함. 본문에 "Claude Code"로 표기한 실험 주체는 없음(S-C6-8과 같은 사안이며 Q-039 대기)
  - 이 책 실습의 "작업 단위마다 commit"은 Young의 사실이 아니라 이 책 실습의 확인 방법임
- 확신: 높음(이번 확인은 요약 질의 수준이며 원문 전체를 다시 읽지는 않음)

### S-C8-8. OpenAI(Ryan Lopopolo), Harness engineering: leveraging Codex in an agent-first world
- URL: https://openai.com/index/harness-engineering/
- 게시일: 2026-02-11(검색 결과 표기), 확인일: 2026-10-20 (원문 열람 실패, openai.com과 www.openai.com 이름 해석 실패, 2차 요약도 해당 문장을 확인해 주지 않음)
- 작성: Ryan Lopopolo
- 이 장에서 사용할 내용
  - 미확인. 6행 "실행 중 접근할 수 없는 지식은 에이전트에게 없는 것과 같다(문서 도구, 채팅, 사람의 머릿속)"은 research/ch01-sources.md S2의 2026-10-04 기록에만 의존함
  - 검색 결과에서 확인된 것은 게시일, 작성자, 5개월 실험이라는 개요까지임
- 확신: 낮음

### S-C8-9. Michael Nygard, Documenting Architecture Decisions (2011)
- URL: http://thinkrelevance.com/blog/2011/11/15/documenting-architecture-decisions (원 주소는 GitHub ADR 저장소 페이지가 가리킨 것, 지금은 cognitect.com 블로그로 옮겨진 것으로 보이나 열지 못함)
- 게시일: 2011-11-15(2차 출처 표기), 확인일: 2026-10-20 (원문 열람 실패)
- 작성: Michael Nygard
- 이 장에서 사용할 내용
  - 8장 본문은 Nygard나 ADR을 인용하지 않음. 결정 기록 형식(번호, 날짜, 결정, 대체, 이유)은 이 책의 형식임
  - 인용하려면 원문을 직접 열어야 함. 2차 출처가 전하는 구성(제목, 맥락, 결정, 상태, 결과)과 상태에 "superseded"가 있는 점은 판정에 쓰지 않음
- 확신: 낮음

---
## 본문 사실 문장 판정 표

| 발견 | 위치 | 근거 | 제안 | 확신 |
|---|---|---|---|---|
| "대화 이력은 같은 세션 안에서만 유효합니다"가 부정확함 | 8행 | S-C8-1, S-C8-4. `--continue`/`--resume`은 같은 세션 ID로 다시 열어 이전 대화를 이어 가고, SDK에서도 resume하면 이전 컨텍스트가 복원됨. 대화에서만 준 지시가 압축 뒤 사라질 수 있다는 문장 자체는 맞음 | "새 세션은 이전 대화를 갖고 있지 않다"로 한정하고, 이어 받은 세션도 압축되면 이른 지시를 잃을 수 있다는 점을 남김. 요약 3항("새 세션과 다른 에이전트는 이전 대화를 읽지 못합니다")과 주장 문장은 새 세션 기준이라 유지 가능 | 높음 |
| "세션이 끝난 뒤에도 남는 것은 저장소에 기록된 문서와 커밋뿐"이 과함 | 7행 | S-C8-1, S-C8-2, S-C8-3. 대화 JSONL(기본 30일 보관)과 자동 메모리가 세션 뒤에도 로컬에 남음. 이 장 20행이 JSONL을 직접 설명하므로 장 안에서도 모순됨 | "에이전트가 새 세션에서 신뢰하고 읽을 수 있는 것은 저장소의 문서와 커밋"으로 한정하거나, 자동 메모리와 JSONL은 보관 기간이 있는 로컬 기록임을 한 문장 추가 | 높음 |
| Codex 인용의 1차 확인 없음 | 7행, 참고 자료 Lopopolo | S-C8-8. 원문 열람 실패 | 문장 유지하되 "미확인"으로 표시하고 작가 확인(Q-030과 같은 사안). 주체는 "OpenAI는 Codex로 ... 글에서"가 정확함. 원문은 Lopopolo(OpenAI)의 글이고 Codex가 글을 쓴 것이 아님 | 중간 |
| "Claude Code가 장시간 실행 실험에서" 주체 | 6행, 17행 | S-C8-7. 원문 주체는 Claude Agent SDK 위의 Opus 4.5이고 Claude Code 표기는 감사의 말에만 있음 | D-108대로 유지하는 것이 작가 결정 대기(Q-039). 중립 표기안은 "Anthropic의 장시간 실행 에이전트 실험" | 중간 |
| Young 서술(진행 기록 파일, git 이력, 설명 있는 커밋, 되돌리기와 복구) | 17행 | S-C8-7과 일치 | 유지. 필요하면 파일 이름 `claude-progress.txt`와 `init.sh`를 원문 근거로 쓸 수 있음(8장 본문에는 아직 없음). 표 8-1의 "작업 목록 파일"은 Young의 기능 목록 JSON에 대응함 | 높음 |
| "세션마다 새 컨텍스트에서 시작, CLAUDE.md와 자동 메모리가 지식을 전달" | 6행 | S-C8-3과 일치 | 유지 | 높음 |
| 대화에서만 전달한 지시는 압축 뒤 사라질 수 있고, 유지할 지시는 CLAUDE.md에 추가 | 8행, 표 8-3 3행 | S-C8-1, S-C8-3, S-C8-4와 일치. 루트 CLAUDE.md는 압축 뒤 디스크에서 다시 주입됨 | 유지. 표 8-3 3행의 막는 장치에 "루트 CLAUDE.md는 압축 뒤 다시 주입됨"을 덧붙일 수 있음. 하위 디렉터리 CLAUDE.md나 경로별 규칙은 다시 로드되기 전까지 사라진 것처럼 보일 수 있음 | 높음 |
| JSONL, 메시지, 도구 사용, 결과, 되감기, 이어 가기, 갈라 시작하기 | 20행, 표 8-2 | S-C8-1과 일치 | 유지. 위치를 쓰려면 `~/.claude/projects/` 아래 `<project>/<session>.jsonl`, 하위 에이전트 기록은 `<session>/subagents/` | 높음 |
| Agent SDK 결과에 비용, 토큰, 턴 수, 세션 ID, 오류로 끝나도 남음 | 20행, 그림 8-2, 표 8-2 | S-C8-4. 원문은 "all result subtypes"에 네 필드가 있다고 함 | 유지. 단서로 세션 충돌 시 비용 필드가 0일 수 있음. 그림 8-2의 "종료 사유"는 `subtype`과 `stop_reason`에 해당하나, 원문은 '종료 사유'라는 말을 쓰지 않음(이 책의 표현) | 높음 |
| 훅: PostToolUse는 출력 감사, SubagentStart/Stop은 병렬 작업 추적, PreCompact는 압축 전 대화 보관 | 21행 | S-C8-4 훅 표와 일치. 원문은 Agent SDK 문서이고 참고 자료 Anthropic 2026b에 포함됨 | 유지. 21행이 "문서는"이라고만 쓰므로 SDK 문서의 훅 표임을 밝히면 정확함 | 높음 |
| 훅을 "추적 지점"으로 부르고 "훅으로 구현"한다는 정리 | 21행, 33행 | 원문은 훅의 용도를 감사, 집계, 보관으로 설명하며 '추적 지점' 개념은 이 책의 정리 | 유지 가능. 이 책의 설명임을 해치지 않는 선에서 둠 | 중간 |
| OpenTelemetry는 모든 환경에서 동작하고 사용자별 토큰과 비용을 거의 실시간으로 보내는 유일한 선택지 | 22행, 그림 8-2, 표 8-2 | S-C8-5. 원문은 "every setup"이고 맥락은 Teams, Console, 클라우드 같은 이용 방식 | "모든 환경"을 "모든 이용 방식(Teams, Console, 클라우드)"으로 바꾸면 실행 환경과 헷갈리지 않음. "유일한 선택지"는 원문 그대로(자체 관측 시스템으로 흘려보내는 방식에 한정) | 높음 |
| OpenTelemetry가 기본으로 켜져 있는 것처럼 읽힐 수 있음 | 22행, 그림 8-2 | S-C8-6. `CLAUDE_CODE_ENABLE_TELEMETRY=1`과 내보내기 설정이 필요함. 프롬프트 내용과 도구 매개변수는 기본으로 기록하지 않음 | "켜야 한다"와 개인정보 기본값(프롬프트 마스킹)을 한 문장 추가하면 정확함. 이벤트(tool_result 등)와 베타 추적도 가능하다는 점은 선택 | 중간 |
| 기본 30일이 지난 세션 데이터를 시작할 때 삭제 | 33행, 그림 8-2, 표 8-2 | S-C8-2, S-C8-5와 일치. 설정 키는 `cleanupPeriodDays`(기본 30, 최솟값 1) | 유지. 키 이름을 쓰면 '보관 기간을 정한다'가 구체적이 됨. 단서: 자동 메모리 디렉터리는 삭제 대상이 아님. 값을 크게 해 보존하려면 이 설정을 바꿔야 함 | 높음 |
| AGENTS.md를 규칙 문서로 둠 | 표 8-1 | S-C8-3. Claude Code는 CLAUDE.md가 없으면 AGENTS.md를 읽음(함께 있으면 CLAUDE.md만. ch03-10 기록, 2026-10-20 확인). Codex는 AGENTS.md를 읽음 | 유지. 제품별 차이는 5장과 9장에서 다룸 | 높음 |
| 규칙 문서가 "시작할 때 자동"으로 읽힘 | 그림 8-1 | S-C8-3. CLAUDE.md는 매 세션 시작 때 로드됨 | 유지 | 높음 |
| `--resume`/`--continue`가 본문에 없음 | 8행, 42행 이하 | S-C8-1. 이어 받기에는 resume으로 이전 대화를 그대로 복원하는 방법이 있음. 원고 표 8-4는 새 세션에서 "HANDOFF.md를 읽고 이어서 작업해 줘"로 확인함 | 비교 문장 한 줄 권장. 대화 복원은 세션 하나를 이어 가는 일이고, 인계 메모는 새 세션이나 다른 에이전트에게 넘기는 일임. 주장 문장은 유지 | 높음 |
| 결정 기록 형식(번호, 날짜, 결정, 대체, 이유)과 "이 책의 저장소도 같은 형식" | 35~40행 | DECISIONS.md 머리글이 번호, 날짜, 결정, 대체, 이유이고 D-001부터 118건이 있음 | 유지. 건수를 쓰려면 갱신 시점에 맞춰 확인 필요. Nygard(2011)는 원문을 열지 못해 인용 근거로 쓰지 않음 | 높음 |
| D-012와 D-015 예시 표 | 36~39행 | 이 책 예제. 실습 폴더의 DECISIONS.md에는 D-012 한 건만 있음(2026-10-20 대조 기록) | 유지 | 높음 |

---
## 미확인
- Lopopolo(OpenAI) 원문의 "에이전트가 실행 중 접근할 수 없는 지식은 없는 것과 같다" 문장. 찾아본 곳: openai.com 세 경로(index, blog, www), InfoQ, 검색 결과(요약에 해당 문장 없음)
- Nygard(2011) 원문과 ADR 형식(Title/Status/Context/Decision/Consequences, superseded 상태). 찾아본 곳: cognitect.com 두 경로, adr.github.io(이름 해석 실패), web.archive.org(차단), GitHub ADR 저장소 메인 페이지(원 주소만 확인, 형식 설명은 없음), 템플릿 파일(404)
- monitoring-usage 문서 뒤 56,414자(보조 설정, 개인정보 상세 등)
- memory 문서의 AGENTS.md 절 재확인(이전 기록 v2.1.277 이상 인용)
- Codex의 세션 기록 저장 위치와 이어 가기(resume) 방식(8장 본문에 없어 이번에 조사하지 않음)

## 장의 주장을 뒷받침하기에 근거가 부족한 곳
- 장의 주장("작업이 이어지는지를 정하는 것은 대화 이력의 길이가 아니라 문서로 남은 결정과 진행")은 Young(2025)의 실험 서술과 Claude Code 문서의 압축 안내를 합쳐 이 책이 정리한 것이다. "대화 이력의 길이"와 작업 연속성을 직접 비교한 1차 출처는 없다. 이 책의 주장임을 밝히는 편이 안전하다.
- `--resume`이 있어 "대화 이력은 같은 세션 안에서만 유효"는 Claude Code에서 정확하지 않다(위 표 첫 행).
- 실행 로그가 완료 보고를 확인하는 증거가 된다는 것(그림 8-2 하단)은 이 책의 설계 판단이다. Anthropic 문서는 로그 필드의 존재만 설명한다.
- Young 글은 Claude Code가 아닌 Claude Agent SDK 위의 실험이다(D-108, Q-039 대기).
- "인계 메모"라는 형식 자체의 1차 출처는 없다. Young의 진행 파일과 git 이력이 가장 가까운 근거이고, 인계 메모의 다섯 항목은 이 책의 설계이다.

참고한 이전 기록: /home/user/harness-book/research/ch03-10-sources.md, /home/user/harness-book/research/ch01-sources.md, /home/user/harness-book/research/ch07-sources.md
