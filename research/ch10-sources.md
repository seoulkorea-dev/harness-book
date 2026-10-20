# Chapter 10 출처 기록

2026-10-20 researcher 조사(10장 개정, PR #43). 이전 10장 출처는 research/ch03-10-sources.md에 있음.
### 먼저 알릴 것
- Claude Code 문서(code.claude.com)는 5건 모두 원문을 직접 열어 확인했습니다. 열린 곳은 memory, permissions, sandboxing, permission-modes입니다.
- OpenAI 문서는 열리지 않았습니다. developers.openai.com과 learn.chatgpt.com 모두 WebFetch에서 `getaddrinfo ENOTFOUND`가 났습니다(agents-md, agent-approvals-security, fr-FR 번역 페이지, 그 밖의 경로 모두 같음). 그래서 Codex 사실은 이번에 원문으로 대조하지 못했습니다.
- 확인한 것은 세 가지뿐입니다.
  - WebSearch의 요약 문장. 검색 요약이라 원문 확인으로 치지 않고 "단서"로만 적습니다.
  - github.com/openai/codex의 docs/sandbox.md와 docs/agents_md.md. 안내 한 줄뿐이고 developers.openai.com으로 넘깁니다.
  - raw.githubusercontent.com의 codex-rs/protocol/src/protocol.rs. OpenAI 저장소 소스이고 문서 원문은 아닙니다. 앞 100,000자만 읽었습니다.
- Codex 관련 문장은 모두 "이전 기록 의존"으로 표시합니다. 이전 기록은 research/ch03-10-sources.md의 2026-10-04 확인(S6)과 2026-10-20 ch10 fact-checker 보강 확인입니다.

---

## 기록

### S-C10-1. Anthropic, How Claude remembers your project (Claude Code Docs)
- URL: https://code.claude.com/docs/en/memory
- 게시일: 표기 없음, 확인일: 2026-10-20 (원문 열어 확인)
- 작성: Anthropic
- 이 장에서 사용할 내용
  - CLAUDE.md 범위 4가지: 관리형 조직 정책, 사용자 `~/.claude/CLAUDE.md`, 프로젝트 `./CLAUDE.md` 또는 `./.claude/CLAUDE.md`, 로컬 `./CLAUDE.local.md`. 본문의 "조직, 사용자, 프로젝트, 개인" 네 범위와 맞음.
  - 작업 디렉터리와 그 위 모든 디렉터리의 CLAUDE.md, CLAUDE.local.md를 시작 때 읽음. 하위 디렉터리 파일은 필요할 때 읽음.
  - 파일은 덮어쓰지 않고 "concatenated" 되며, 파일 시스템 루트에서 작업 디렉터리 순으로 배치됨. 가까운 지침이 나중에 읽힘.
  - 크기 지침: CLAUDE.md는 파일당 200줄 미만 목표(길면 컨텍스트를 더 쓰고 준수율이 떨어짐). 하드 한도는 아님.
  - AGENTS.md 기본 동작은 표와 같음. 작업 디렉터리나 그 위에 CLAUDE.md, `.claude/CLAUDE.md`, CLAUDE.local.md 중 하나도 없고 AGENTS.md만 있으면 AGENTS.md를 읽음. 둘 다 있으면 CLAUDE.md만 읽음.
  - 위 검사에서 `~/.claude/CLAUDE.md`, 조직 관리형 CLAUDE.md, `.claude/rules/`는 "세지 않음". 이들은 AGENTS.md와 함께 계속 읽힘.
  - CLAUDE.local.md가 있으면 AGENTS.md를 읽지 않음. 이 경우 Project instructions 설정을 `claude-md-and-agents-md`로 바꾸면 둘 다 읽음. 기본값은 `claude-md-or-agents-md`(설정은 `/config` 또는 `pluginConfigs`의 `cc-plugin-agents-md@builtin`).
  - AGENTS.md 직접 읽기는 v2.1.277 이상. v2.1.281 이전의 Bedrock, 텔레메트리 끈 세션 등은 CLAUDE.md만 읽음. 그런 세션은 CLAUDE.md의 `@AGENTS.md` 불러오기를 씀(그 아래에 Claude 전용 지침을 적는 방식도 원문 안내).
  - `@AGENTS.md` 불러오기를 두어도 AGENTS.md를 두 번 읽지 않음. 심볼릭 링크 방식은 Windows에서 권한 문제가 있어 `@AGENTS.md` 불러오기를 권장.
  - CLAUDE.md는 강제 설정이 아닌 컨텍스트. 막으려면 PreToolUse 훅.
- 확신: 높음

### S-C10-2. Anthropic, Configure permissions (Claude Code Docs)
- URL: https://code.claude.com/docs/en/permissions
- 게시일: 표기 없음, 확인일: 2026-10-20 (원문 열어 확인)
- 작성: Anthropic
- 이 장에서 사용할 내용
  - 평가 순서 deny, ask, allow. 먼저 일치한 것이 결정. allow가 deny의 예외를 만들 수 없음. 어느 범위(사용자, 프로젝트)의 deny든 allow보다 먼저 평가됨.
  - 권한 규칙은 Claude Code가 적용하며 모델이나 CLAUDE.md로 바뀌지 않음.
  - `/permissions`는 모든 권한 규칙과 각 규칙이 나온 settings.json 파일을 보여 줌.
  - 설정 파일 위치: 프로젝트 `.claude/settings.json`, 로컬 `.claude/settings.local.json`, 사용자 `~/.claude/settings.json`, 관리형.
  - `Bash(git push *)` 규칙은 `git push origin main`과 일치함. `git -C . push origin main`, `git -c push.default=current push ...`, `git 'push' origin main`은 일치하지 않음. Bash 규칙은 명령 문자열을 대조함.
  - 기본 접근은 실행한 디렉터리(작업 디렉터리). 추가 디렉터리는 `/add-dir` 등으로 확장.
  - 도구별 기본 승인 표(Manual 모드 기준): WebFetch는 승인 필요(내장 문서 도메인 예외), WebSearch는 승인 필요, 파일 수정은 승인 필요, Bash는 읽기 전용 명령 외 승인 필요.
  - 규칙 이름은 `WebFetch`, `WebSearch`, `Bash(...)`, `Edit(...)`, `Read(...)` 형식. 예제의 deny 배열과 일치.
  - 프로젝트 `.claude/settings.json`의 allow 규칙은 작업 폴더 신뢰 대화상자를 수락해야 적용됨. deny와 ask 규칙은 영향 없음.
- 확신: 높음

### S-C10-3. Anthropic, Choose a permission mode (Claude Code Docs)
- URL: https://code.claude.com/docs/en/permission-modes
- 게시일: 표기 없음, 확인일: 2026-10-20 (원문 열어 확인)
- 작성: Anthropic
- 이 장에서 사용할 내용
  - 권한 모드 설정값 6개: default(CLI 별칭 manual), acceptEdits, plan, auto, dontAsk, bypassPermissions. 본문의 여섯 가지와 일치.
  - 시작 모드: 터미널과 VS Code 확장은 v2.1.283 이상에서 `auto`.
  - `auto`가 아닌 경우: `disableAutoMode`를 `"disable"`로 설정한 경우, `claude -p`와 Agent SDK, HIPAA 구성 세션(v2.1.285 이상)은 `default`. v2.1.302부터는 권한 모드를 지정하지 않은 `claude -p`와 SDK도 Manual로 시작.
  - 우선순위: `--permission-mode` 플래그, `permissions.defaultMode`, 내장 기본값.
  - 프로젝트 `.claude/settings.json` 또는 `settings.local.json`의 `"auto"`와 `"bypassPermissions"`는 효력이 없고 Manual로 시작. 사용자 설정(`~/.claude/settings.json`)에서는 적용됨.
  - v2.1.283 이전에는 Pro, Max, Team의 기능 플래그 세션만 auto로 시작.
  - 버전 주석의 "모든 요금제"는 이번 원문에 요금제 조건이 없어서 직접 대조되지 않음. 기록은 2026-10-04 릴리스 노트(v2.1.284)에 근거함.
- 확신: 높음(모드 이름, 시작 모드). 중간("모든 요금제" 표현)

### S-C10-4. Anthropic, Configure the sandboxed Bash tool (Claude Code Docs)
- URL: https://code.claude.com/docs/en/sandboxing
- 게시일: 표기 없음, 확인일: 2026-10-20 (원문 열어 확인)
- 작성: Anthropic
- 이 장에서 사용할 내용
  - 샌드박스는 "off by default". 켜는 방법은 세션에서 `/sandbox` 실행, 또는 settings 파일의 `sandbox.enabled`를 `true`로 설정.
  - 운영 체제가 적용하는 경계이고 대상은 Bash, PowerShell, Monitor 명령과 그 하위 프로세스. Claude의 파일 도구, MCP 서버, 훅은 샌드박스 밖에서 실행됨.
  - macOS, Linux, WSL2에서 동작. 네이티브 Windows에서는 샌드박스 없이 실행. 의존성이 없거나 플랫폼이 미지원이면 기본적으로 샌드박스 없이 명령을 실행하고, `sandbox.failIfUnavailable`을 true로 하면 시작 때 종료함.
  - 기본 쓰기 범위: 작업 디렉터리, 사용자별 임시 디렉터리, `--add-dir`, `/add-dir`, `permissions.additionalDirectories`로 추가한 디렉터리.
  - 네트워크: 직접 경로 없음. 로컬 프록시가 허용 도메인(처음엔 비어 있음)과 대조함. 새 도메인이 필요하면 처음에 승인을 묻고, 허용 후 접근됨(권한 모드에 따라 처리가 다름). 즉 샌드박스를 켜는 것만으로 네트워크가 완전히 차단되지 않음.
  - `sandbox.autoAllowBashIfSandboxed`는 기본 true(샌드박스 안 명령은 프롬프트 없이 실행).
  - 샌드박스 안에서 실패한 명령은 `dangerouslyDisableSandbox`로 샌드박스 밖 재시도를 시도할 수 있음. `allowUnsandboxedCommands: false`로 막음.
  - 확인 방법 원문 예: `touch ~/sandbox-probe`가 macOS에서 `Operation not permitted`, Linux와 WSL2에서 `Read-only file system`으로 실패하면 정상.
  - 구현은 오픈소스 `@anthropic-ai/sandbox-runtime`. Linux와 WSL2는 bubblewrap과 socat을 씀.
- 확신: 높음

### S-C10-5. OpenAI, Codex 문서 (AGENTS.md, Agent approvals and security, Permissions, Config basics, Rules, Slash commands)
- URL(이전 기록): https://developers.openai.com/codex/guides/agents-md , .../codex/agent-approvals-security , .../codex/permissions , .../codex/config-basic , .../codex/rules , .../codex/guides/slash-commands/ . 이전 확인에서 learn.chatgpt.com/docs/...로 308 이전됨(예: https://learn.chatgpt.com/docs/agent-configuration/rules , .../docs/agent-approvals-security , .../docs/cli/slash-commands/)
- 게시일: 표기 없음, 확인일: 2026-10-20 (열기 실패, 이번에 원문 확인 못함)
- 작성: OpenAI
- 이번 시도 결과: developers.openai.com과 learn.chatgpt.com 모두 DNS 오류(`ENOTFOUND`). 재시도 경로는 fr-FR 번역, github.com/openai/codex 문서(링크 안내뿐), raw 소스 protocol.rs. 열린 것은 protocol.rs뿐이고 문서 원문이 아님.
- 이 장에서 사용할 내용(모두 이전 기록 의존, 이번 재확인 안 됨)
  - 2026-10-04 기록(S6): AGENTS.md는 작업 전에 읽음. `~/.codex`의 AGENTS.override.md 또는 AGENTS.md, 디렉터리마다 AGENTS.override.md, AGENTS.md, 대체 이름 순. 로컬은 운영 체제 수준 샌드박스와 승인 정책, 기본은 네트워크 차단과 작업 공간 쓰기 제한. Auto 프리셋 `--sandbox workspace-write --ask-for-approval on-request`. `sandbox_workspace_write.network_access`(스페인어판 확인). untrusted 미지원(프랑스어판 확인). 권한 프로필 `:read-only`, `:workspace`, `:danger-full-access`. 사용자 설정 `~/.codex/config.toml`, 프로젝트 `.codex/`는 신뢰한 프로젝트에서만 읽음. Rules는 실험 단계, `~/.codex/rules/default.rules`, `prefix_rule`의 `decision` forbidden은 확인 없이 차단, 여러 규칙 일치 시 forbidden > prompt > allow.
  - 2026-10-20 기록: `/status`는 활성 모델, 승인 정책, 쓰기 가능 경로(writable roots), 남은 컨텍스트 용량을 보여 주고 샌드박스 모드와 네트워크 항목은 없음. on-request에서는 네트워크가 필요한 명령에 승인 요청.
  - 이번 검색 요약(단서, 원문 아님)이 위와 일치하는 부분: AGENTS.md는 디렉터리마다 AGENTS.override.md, AGENTS.md, `project_doc_fallback_filenames` 순으로 보고 디렉터리당 한 파일만 포함, 루트에서 아래로 이어 붙임, 합산 크기는 `project_doc_max_bytes`(기본 32 KiB)에서 멈춤. 프로젝트 `.codex/config.toml`은 신뢰한 프로젝트에서만 읽음. rules의 `decision` 기본은 allow, 값은 allow, prompt, forbidden. 위치는 활성 설정 층 옆 `rules/`. 샌드박스 네트워크는 `[sandbox_workspace_write].network_access`로 켬.
  - OpenAI 저장소 소스(protocol.rs, 문서 아님): 승인 정책 값은 `untrusted`(내부 UnlessTrusted), `on-request`(별칭 `on-failure`), `granular`, `never`. 샌드박스 정책은 `read-only`, `workspace-write`, `danger-full-access`, `external-sandbox`. 소스에 untrusted 폐지 표기는 없음(읽은 부분 기준). 본문 "untrusted를 더 이상 지원하지 않는다"는 문서 문구 대조가 필요함.
  - 같은 소스의 `OnRequest`는 기본 variant로 보이나 문서의 기본값과 같다고 단정하지 않음. 신뢰 여부에 따라 기본 프리셋이 달라진다는 단서(미러 문서)가 있어 기본 승인 정책은 미확인.
- 확신: 낮음(이번 열기 실패, 이전 기록과 단서가 일치하는 정도)

---

### 본문 사실 문장 판정 표

| 발견 | 위치 | 근거 | 제안 | 확신 |
|---|---|---|---|---|
| CLAUDE.md 4범위, 상위 디렉터리부터 이어 읽음, 세션마다 읽음 | rule-docs 1문단 | S-C10-1 일치. 이어 붙이기이고 덮어쓰기가 아님. 하위 디렉터리는 필요할 때 읽음 | 유지. "작업 디렉터리까지"가 정확하며 하위 디렉터리는 언급하지 않음 | 높음 |
| CLAUDE.md가 없으면 AGENTS.md를 읽음 | 표 10-1, rule-docs, 표 10-2, 표 10-3 3행 | S-C10-1 일치. 단 CLAUDE.local.md나 `.claude/CLAUDE.md`도 CLAUDE.md로 셈. `~/.claude/CLAUDE.md`와 조직 관리형은 안 셈. v2.1.277 이상 조건 | 조건 한 줄 추가 권장(v2.1.277 이상, CLAUDE.local.md가 있으면 안 읽음). 표 10-3 3행 원인에 "CLAUDE.md가 있으면 AGENTS.md를 읽지 않음"을 쓰는 것이 backlog 지적과 일치 | 높음 |
| CLAUDE.md에서 AGENTS.md를 불러오고 아래에 Claude 전용 지침 추가 | rule-docs 3문단, 표 10-3 3행 | S-C10-1 일치. `@AGENTS.md` 형식이 원문의 기준. 본문은 `@` 표기를 쓰지 않음 | `@AGENTS.md` 표기를 한 번 보여 줌. Project instructions 설정(`claude-md-and-agents-md`) 대안은 선택 사항 | 높음 |
| Claude Code 규칙 문서 크기 한도 | 본문에 없음 | S-C10-1: 200줄 미만 목표, 하드 한도 아님 | 비교 기준 추가 시 "권장"으로 씀. Codex 32 KiB는 열기 실패라 미확인(검색 요약 단서만 있음) | 높음(Claude), 낮음(Codex) |
| Codex는 작업 시작 전에 AGENTS.md를 읽음 | 표 10-1, rule-docs 2문단 | 이전 기록(S6) 의존. 이번 열기 실패 | 재확인 필요 표시 | 중간 |
| Codex 읽는 순서: `~/.codex/AGENTS.md`, 저장소 루트, 하위 디렉터리 차례 | rule-docs 2문단 | 이전 기록 의존. 검색 요약은 루트에서 현재 디렉터리 방향으로 이어 붙이고 디렉터리당 한 파일이라고 함 | 재확인 필요. "하위 디렉터리"는 작업 디렉터리까지 이르는 경로로 표현하는 것이 정확할 수 있음 | 중간 |
| AGENTS.override.md가 있으면 AGENTS.md 대신 읽음 | rule-docs 2문단 | 이전 기록, 검색 요약 단서와 일치 | 재확인 필요 | 중간 |
| 권한 규칙 allow, ask, deny와 권한 모드 6개 | 표 10-1, permissions 1문단 | S-C10-2, S-C10-3 일치. default의 CLI 별칭 manual이 있음 | 유지. 모드 이름은 설정값 기준이라고 명시하면 안전 | 높음 |
| 샌드박스는 셸 명령의 파일, 네트워크 접근을 제한하는 별도 계층, 설정으로 활성화(선택) | 표 10-1, permissions 1문단, 표 10-3 2행 | S-C10-4 일치(기본 꺼짐, `/sandbox` 또는 `sandbox.enabled`) | 유지. "파일 도구, MCP, 훅은 샌드박스 밖"을 한 줄 넣으면 정확함 | 높음 |
| 시작 권한 모드는 v2.1.283 이상 대화형 터미널과 VS Code에서 auto, 모든 요금제 | 버전 주석 | S-C10-3: 터미널과 VS Code는 v2.1.283 이상에서 auto. 예외: disableAutoMode, `-p`와 SDK, HIPAA. 프로젝트 settings의 auto는 효력 없음. "모든 요금제"는 이번 원문에 없음 | "대화형 터미널과 VS Code"에 `claude -p`와 SDK는 default라는 단서, 프로젝트 설정의 auto 무효 추가 검토. "모든 요금제"는 2026-10-04 릴리스 노트 근거 | 중간 |
| Claude Code는 도구별 규칙에서 출발, 격리는 추가 설정 | permissions 3문단 | S-C10-2, S-C10-4. 출발점 표현은 책의 해석 | 유지. 해석이므로 단정은 피함 | 중간 |
| Claude 예제: deny에 `Bash(git push *)`, WebFetch, WebSearch, sandbox.enabled true | example-claude 예제 | S-C10-2, S-C10-4. 키 이름과 형식 모두 유효 | 유지 | 높음 |
| "git push 금지는 deny 규칙" | example-claude 설명 | S-C10-2: `git -C . push`, `git -c ... push`는 일치하지 않음. 규칙 하나로 모든 push를 막지는 못함 | "git push로 시작하는 명령"으로 한정하거나 우회 형태 단서 한 줄. 표 10-4 3행의 "Claude Code는 거부함"도 `git push` 형태에 한정(backlog와 일치) | 높음 |
| 작업 폴더 밖 수정은 Claude Code의 기본 동작이 제한하고 샌드박스가 보강 | example-claude 설명 | S-C10-2: 기본 접근은 작업 디렉터리. 작업 디렉터리 밖 쓰기는 거부가 아니라 승인 필요(프롬프트). 샌드박스는 쓰기를 작업 디렉터리, 임시 디렉터리, 추가 디렉터리로 제한. 파일 도구는 샌드박스 밖 | "제한"을 "승인 대상"으로 표현 정정. 임시 디렉터리 예외 단서 | 중간 |
| Claude 예제만으로 네트워크 접근이 없음 | example 정책, 예제 설명 | S-C10-4: 샌드박스 네트워크는 허용 도메인 프록시. 새 도메인이면 승인을 묻고 허용하면 접근됨. deny는 WebFetch와 WebSearch만 막음. Bash의 curl은 deny 대상 아님 | 가장 큰 문제. 정책 "네트워크에 접근하지 않음"과 Claude 예제가 같지 않음. `sandbox.network.allowedDomains`가 비어 있고 프롬프트에서 거부한다는 한계를 쓰거나, "WebFetch와 WebSearch 도구의 접근 차단"으로 정책 표현을 맞춤. 키 이름은 settings-reference(`sandbox.network.allowedDomains`, `deniedDomains`)로 재확인 필요 | 높음 |
| Codex 승인 정책과 샌드박스의 두 계층 | permissions 2문단 | 이전 기록(S6, Sandbox) 의존 | 재확인 필요 | 중간 |
| 로컬 기본값: 네트워크 차단, 작업 공간 안 수정만 허용 | permissions 2문단 | 이전 기록 의존. 단서: 신뢰하지 않은 프로젝트는 read-only로 시작하고 신뢰하면 workspace-write와 on-request 기본(미러 문서 설명, 원문 아님) | 기본값은 "신뢰한 프로젝트 기준" 같은 조건 가능성이 있어 원문 재확인 전까지 "미확인". 확인 날짜 표기 유지 | 낮음 |
| Codex 기본 권한 프로필 3가지(읽기 전용, 작업 공간 수정 허용, 제한 없음) | permissions 2문단 | 이전 기록(`:read-only`, `:workspace`, `:danger-full-access`) 의존. 검색 결과는 권한 프로필이 베타라고 안내함 | 재확인 필요. 베타 여부 확인되면 단서 추가. 샌드박스 모드(`read-only`, `workspace-write`, `danger-full-access`)와 권한 프로필 이름은 별개로 구분해서 씀 | 중간 |
| Codex 운영 체제 수준 샌드박스 "기본 적용" | 표 10-1, 표 10-2, 그림 10-1 | 이전 기록 의존 | 재확인 필요. 기본 적용 범위(Windows 등 플랫폼 조건)는 미확인 | 중간 |
| 설정 파일 `~/.codex/config.toml`, 프로젝트 `.codex/` | 표 10-1, 표 10-2 | 이전 기록 의존. 검색 요약은 프로젝트 범위는 `.codex/config.toml`이며 신뢰한 프로젝트에서만 읽는다고 함 | 재확인 필요. "신뢰한 프로젝트에서만" 단서 추가 검토 | 중간 |
| Claude 설정: `.claude/settings.json`, 사용자 설정, 관리형 설정 | 표 10-1, 표 10-2 | S-C10-2 일치(`.claude/settings.json`, `settings.local.json`, `~/.claude/settings.json`, 관리형). 로컬 `settings.local.json`은 표에 없음 | 유지. 필요하면 로컬 설정 추가 | 높음 |
| Codex 예제 `sandbox_mode = "workspace-write"`, `approval_policy = "on-request"`, `[sandbox_workspace_write] network_access = false` | example-codex 예제 | 이전 기록, 검색 요약, 소스(`on-request`, `workspace-write`)와 일치. 문서 원문 대조 못함 | 재확인 필요 | 중간 |
| push는 네트워크가 필요하므로 샌드박스 안에서 실행되지 않고 승인 정책에 따라 확인 요청 | example-codex 설명 | 이전 기록(on-request에서 네트워크가 필요한 명령은 승인 요청) 의존. 원격 push가 네트워크를 쓴다는 점은 일반 지식 | 재확인 필요. "push는 항상 네트워크가 필요"는 로컬 경로 원격(file://) 등 예외가 있어 "일반적으로"로 표현 검토 | 중간 |
| 금지하려면 `~/.codex/rules/default.rules`에 `prefix_rule(... decision = "forbidden")` | example-codex 후반 | 이전 기록 일치. 검색 요약도 위치, decision 값, 가장 엄격한 규칙 우선과 일치. 규칙은 실험 단계 | 구문 예제(`pattern = ["git","push"]`) 문서 대조 필요 | 중간 |
| 버전 주석: untrusted 승인 정책 더 이상 지원하지 않음 | 버전 주석, 표 10-3 | 이전 기록(프랑스어판) 의존. 소스(protocol.rs)에는 `untrusted`가 아직 정의돼 있음 | 문서와 소스가 다를 수 있음. 문서 원문 재확인 전까지 "문서 기준"으로 명시 | 낮음 |
| Codex 규칙 기능은 실험 단계 | 버전 주석 | 이전 기록, 검색 요약("experimental")과 일치 | 재확인 필요 | 중간 |
| `/permissions`로 deny에 git push, WebFetch, WebSearch 확인 | 표 10-4 1행 | S-C10-2: `/permissions`는 규칙과 출처 settings.json을 보여 줌 | 유지. 화면에 규칙이 표시됨 | 높음 |
| `/status`는 승인 정책과 수정 가능 경로(writable roots)를 보여 주고 네트워크는 config.toml로 확인 | 표 10-4 2행 | 2026-10-20 이전 기록(learn.chatgpt.com slash-commands) 의존. 이번 열기 실패 | 재확인 필요. 샌드박스 모드 항목이 없다는 점은 backlog의 "샌드박스 확인 행"과 연결됨 | 중간 |
| 인용과 발표 주체 "Anthropic, 2026", "OpenAI, 2026" | 참고 자료 | 원문에 게시일 표기 없음. 확인일은 2026-10-04로 적혀 있고 이번 확인일은 2026-10-20. 참고 자료에 Sandboxing, Choose a permission mode, Slash commands가 빠짐 | 확인일을 2026년 10월 20일로 갱신하고 사용 문서를 추가(backlog와 일치). Codex 문서는 이전됨(learn.chatgpt.com) | 높음 |
| 본문 첫머리 "2026년 10월 4일에 확인한" | criteria 절 | 이번 확인일 2026-10-20(Claude Code), Codex는 이번 열기 실패로 10-04 기록 의존 | 날짜를 둘로 가를지 작가와 정함. Codex를 재확인하지 못하면 "10월 4일"을 그대로 두는 편이 사실과 맞음 | 높음 |

### 미확인 목록
- Codex 문서 전체(AGENTS.md, 승인 정책, 샌드박스 모드, 권한 프로필, config.toml, rules, /status)는 이번에 원문을 열지 못했습니다. 찾아본 곳은 developers.openai.com과 learn.chatgpt.com의 여러 경로, fr-FR 번역, github.com/openai/codex docs, raw protocol.rs입니다.
- Codex 기본 승인 정책과 기본 샌드박스가 프로젝트 신뢰 여부에 따라 달라지는지.
- `project_doc_max_bytes` 기본 32 KiB(검색 요약 단서만).
- 권한 프로필 `:read-only`, `:workspace`, `:danger-full-access`가 현재도 이 이름인지, 베타인지.
- untrusted 폐지가 현재 문서에 적혀 있는지.
- Claude Code settings-reference의 `sandbox.network.*` 키 이름(sandboxing 문서의 링크로만 확인, 해당 페이지는 열지 않음).
- Claude Code에서 작업 디렉터리 밖 파일 수정의 정확한 동작(모드별 프롬프트, deny 아님). permissions 문서의 일부 긴 줄은 생략되어 전체 표현을 대조하지 못했습니다.
- v1.1-backlog Chapter 10의 5개 항목 중 Windows 샌드박스 건은 S-C10-4(네이티브 Windows는 샌드박스 없이 실행)로 근거가 확보됐습니다. 예제 파일(examples/)의 sandbox 키는 이번 범위가 아니어서 열지 않았습니다.

### 장의 주장을 뒷받침하기에 근거가 부족한 곳
1. "Codex는 운영 체제 수준 격리를 기본으로 적용하고, Claude Code는 추가 설정"이라는 대비는 Claude 쪽만 이번에 확인됨. Codex 쪽 기본값은 이전 기록뿐.
2. 같은 정책이라는 예제 대비: Claude 예제가 네트워크를 완전히 막지 못해 두 설정이 같은 정책이 아님(위 표 참조).
3. "Codex는 push를 금지하지 않고 확인을 요청"하는 결론은 on-request 동작에 대한 이전 기록에 의존. 표 10-4 3행의 확인 기준도 마찬가지.
4. "선택 기준은 격리 기본 요구 여부 또는 도구별 규칙 관리"는 책의 해석이며 출처 없음.
