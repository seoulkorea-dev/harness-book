# Chapter 9 출처 기록

2026-10-20 researcher 조사(9장 개정, PR #42). 이전 9장 출처는 research/ch03-10-sources.md에 있음.
조사 범위: ch09 본문 전체와 backlog Chapter 9 항목을 Claude Code 공식 문서 원문(permissions, permission-modes, sandboxing, costs), Anthropic Prompting best practices 원문과 대조했다.
OpenAI Codex 문서(developers.openai.com, learn.chatgpt.com)는 이 환경에서 DNS 오류(ENOTFOUND)로 열리지 않아 오늘 원문 확인에 실패했다. 아래 S-C9-6, S-C9-7은 "원문 미개봉"이다.

## 기록

### S-C9-1. Anthropic, Configure permissions (Claude Code Docs)
- URL: https://code.claude.com/docs/en/permissions
- 게시일: 표기 없음, 확인일: 2026-10-20
- 작성: Anthropic(Claude Code 문서)
- 이 장에서 사용할 내용
  - 평가 순서는 deny, ask, allow이고 처음 일치한 규칙이 결과를 정한다. "rule specificity doesn't change the order". 넓은 deny `Bash(aws *)`는 더 좁은 allow `Bash(aws s3 ls)`가 있어도 막는다. "An allow rule can't carve an exception out of a deny rule". ask와 allow 사이에도 같은 우선순위가 적용된다. (사용처: 권한 절 3문장, 그림 9-1 평가 순서) 확신 높음
  - 범위 간 우선순위. 어느 범위(사용자, 프로젝트)에서든 deny는 다른 범위의 allow보다 먼저 평가되고, 관리형(managed) 설정이 가장 높다. PreToolUse 훅이 "allow"를 반환해도 deny, ask 규칙은 그대로 평가된다. (사용처: 보강 문장 후보) 확신 높음
  - Bash 규칙은 Claude가 쓴 명령 텍스트와 일치할 때만 적용된다. "isn't a security boundary around the program". `Bash(git push *)`는 `git push origin main`을 막지만 `git -C . push origin main`, `git -c push.default=current push origin main`, `git 'push' origin main`은 막지 못한다. (사용처: 한계 문단, 표 9-4 2행) 확신 높음
  - Read, Edit deny는 내장 파일 도구, Bash가 인식하는 파일 명령(cat, head, tail, sed, tee), 리다이렉션 대상에 적용된다. Python이나 Node 스크립트처럼 파일을 간접으로 읽고 쓰는 하위 프로세스에는 적용되지 않는다. OS 수준 강제는 샌드박스를 켜라고 안내한다. (사용처: 표 9-4 1행) 확신 높음
  - 파일 경로 규칙은 `Edit(path)`, `Read(path)`만 참조한다(Write, NotebookEdit 경로 규칙은 참조되지 않음). `Edit(src/**)`를 deny로 쓰면 어느 깊이의 src에도 일치한다. 예제의 `Edit(./data/**)`는 현재 디렉터리 기준 경로다. (사용처: JSON 예제 읽는 법) 확신 높음
  - 맨 `WebFetch` deny는 모든 URL을 덮는다. 맨 `WebFetch`는 샌드박스의 도메인 목록에는 반영되지 않고, `domain:` 형식만 반영된다. (사용처: JSON 예제의 "WebFetch") 확신 높음
  - `/permissions`는 모든 규칙과 각 규칙이 나온 settings.json 파일을 보여 준다. 규칙은 모델이 아니라 Claude Code가 강제한다. "Permission rules are enforced by Claude Code, not by the model". (사용처: 표 9-5 1행, 보강 문장 후보) 확신 높음
  - 권한과 샌드박스는 보완 계층이다. "complementary security layers". 권한은 Bash, Read, Edit, WebFetch, MCP 등 모든 도구에 적용되고, 샌드박스는 Bash, PowerShell, Monitor 명령과 그 자식 프로세스의 파일, 네트워크를 OS 수준에서 제한한다. 둘을 함께 쓰라는 근거는 "sandbox restrictions still apply even if a prompt injection bypasses Claude's decision-making"이다. (사용처: 보완 계층 문단) 확신 높음
  - 승인 프롬프트의 "Yes, and don't ask again" 동작. Bash는 저장소와 명령 단위로 영구 적용되고, 파일 수정은 세션 종료까지만 적용된다. 읽기는 작업 디렉터리 안에서 승인이 필요 없다. (사용처: 승인 지점 절에서 승인 프롬프트를 다룰 경우) 확신 높음

### S-C9-2. Anthropic, Choose a permission mode (Claude Code Docs)
- URL: https://code.claude.com/docs/en/permission-modes (permissions 페이지의 모드 표와 일치)
- 게시일: 표기 없음, 확인일: 2026-10-20
- 작성: Anthropic(Claude Code 문서)
- 이 장에서 사용할 내용
  - 모드 6개의 설정값과 UI 이름: default(Manual, CLI 별칭 manual), acceptEdits, plan, auto, dontAsk, bypassPermissions. (사용처: 권한 모드 설명 시) 확신 높음
  - 시작 모드는 `--permission-mode` 플래그, `permissions.defaultMode`, 내장 기본값 순으로 첫 일치가 정한다. 내장 기본값은 대화형 터미널과 VS Code에서 auto(v2.1.283 이상, 그 이전 버전에서는 Pro, Max, Team 요금제만)다. `claude -p`와 Agent SDK는 default(Manual)(v2.1.302 이상)다. 조직이 HIPAA 구성이면 default다. `.claude/settings.json`과 `.claude/settings.local.json`에 쓴 `"auto"`와 `"bypassPermissions"`는 효력이 없다. (사용처: 기본값을 쓴다면 버전 주석 필수) 확신 높음
  - auto 모드는 별도 분류기(classifier) 모델이 실행 전에 동작을 검토한다. 사용자 요청을 넘어서는 확대, 알 수 없는 인프라, 읽은 내용에 의해 유도된 것으로 보이는 동작을 막는다. 문서 원문은 "reduces permission prompts but does not guarantee safety"라고 쓴다. 전 요금제에서 가능하고, 지원 모델과 클라이언트 버전 조건이 있으며, 관리자는 `permissions.disableAutoMode: "disable"`로 끈다. (사용처: 자동 모드를 본문에 넣을 때. 승인 피로 문제의 한 대응으로 쓸 수 있으나 "안전을 보장하지 않음" 단서 필수) 확신 높음
  - bypassPermissions는 "disables permission prompts and safety checks"이고, "Only use this mode in isolated environments like containers, VMs, or dev containers without internet access"라고 쓴다. deny 규칙은 이 모드에서도 계속 막는다. Linux와 macOS에서 root나 sudo로는 시작하지 않는다. 관리자는 `permissions.disableBypassPermissionsMode`로 막을 수 있다. (사용처: 보완 계층 문단 마지막 문장) 확신 높음
  - dontAsk는 프롬프트가 뜰 동작을 모두 자동 거부하고, 사전 승인한 도구와 allow 규칙은 그대로 실행한다. CI와 제한된 환경용이다. plan은 조사와 계획만 하고 소스는 수정하지 않는다. acceptEdits는 작업 디렉터리 안의 파일 편집과 mkdir, touch, rm, rmdir, mv, cp, sed를 자동 승인한다. (사용처: 모드 설명이 필요할 때) 확신 높음

### S-C9-3. Anthropic, Configure the sandboxed Bash tool (Claude Code Docs)
- URL: https://code.claude.com/docs/en/sandboxing
- 게시일: 표기 없음, 확인일: 2026-10-20
- 작성: Anthropic(Claude Code 문서)
- 이 장에서 사용할 내용
  - 샌드박스는 OS가 강제하는 경계다. 사용자가 명령이 닿는 파일과 네트워크 도메인을 정하고, 제한은 Bash, PowerShell, Monitor 명령과 그 자식 프로세스에 적용된다. 파일 도구, MCP 서버, 훅은 샌드박스 밖에서 실행된다. (사용처: 표 9-2 샌드박스 행, 표 9-4 1행의 "Edit 규칙과 샌드박스의 역할 분담") 확신 높음
  - 지원 OS는 macOS, Linux, WSL2다. 네이티브 Windows에서는 샌드박스 없이 실행된다. Windows에서는 WSL2 안에서 Claude Code를 실행하라고 안내한다. (사용처: backlog "네이티브 Windows" 항목) 확신 높음
  - 기본값은 꺼짐이다. "The sandbox is off by default". `/sandbox`로 켜거나 `sandbox.enabled`를 true로 설정한다. 의존성이 없거나 플랫폼이 미지원이면 기본은 샌드박스 없이 명령을 실행한다. `sandbox.failIfUnavailable: true`로 시작 시 종료하게 바꿀 수 있다. Linux와 WSL2는 bubblewrap과 socat이 필요하다. (사용처: 예제 설정에 샌드박스가 없는 이유 설명, 실습 3) 확신 높음
  - 두 모드가 있다. auto-allow는 샌드박스 안 명령을 프롬프트 없이 실행하고, regular permissions는 일반 프롬프트를 유지한다. 두 모드 모두 파일과 네트워크 제한은 같다. 기본 쓰기 범위는 작업 디렉터리, 사용자별 임시 디렉터리, `--add-dir`로 추가한 디렉터리다. (사용처: 격리 설명 보강) 확신 높음
  - 검증 방법. `touch ~/sandbox-probe`가 macOS에서는 `Operation not permitted`, Linux와 WSL2에서는 `Read-only file system`으로 실패하면 샌드박스가 동작하는 것이다. (사용처: 표 9-5에 샌드박스 확인 행을 추가할 때) 확신 높음

### S-C9-4. Anthropic, Manage costs effectively (Claude Code Docs)
- URL: https://code.claude.com/docs/en/costs
- 게시일: 표기 없음, 확인일: 2026-10-20
- 작성: Anthropic(Claude Code 문서)
- 이 장에서 사용할 내용
  - 개요 문장은 "Track token usage, set team spend limits, and reduce Claude Code costs with context management, model selection, extended thinking settings, and preprocessing hooks"다. 본문의 4개 방법 중 토큰 추적, 팀 지출 한도, 컨텍스트 관리, 모델 선택은 일치한다. 문서는 확장 사고 설정과 훅도 함께 든다. 확신 높음
  - "Claude Code charges by API token consumption". 구독(Pro, Max, Team, Enterprise)은 요금제 한도와 사용 크레딧 체계이고, 같은 문서가 Claude Code 사용량은 구독에 포함된다고도 쓴다. 따라서 "비용은 토큰 사용량에 비례"는 API 과금 기준이다. 구독에는 "session cost figure isn't relevant for billing purposes"라고 쓴다. 확신 높음
  - `/usage`의 Session 블록은 현재 세션의 토큰 사용량을 보여 주며 API 사용자용이다. 금액은 로컬에서 토큰 수로 정가(list price)를 곱해 계산한다. `modelPricing` 관리형 설정이 있으면 계약 요율로 계산하며(v2.1.242 이상), 이때도 추정치다. 실제 청구는 Console의 Usage 페이지를 보라고 안내한다. 구독자는 같은 화면에서 요금제 사용량 막대, 활동 통계, 사용량 내역을 본다. `/clear`로 새 세션이 시작되면 합계가 0으로 돌아간다(v2.1.211 이상, 그 이전에는 프로세스 수명 동안 누적). (사용처: 비용 절 /usage 문단, 표 9-5 3행) 확신 높음
  - 상태 줄(status line)에 컨텍스트 사용량을 계속 표시할 수 있다. `/context`는 컨텍스트 점유 확인, `/clear`는 작업 사이 비우기, `/compact`는 요약이다. (사용처: 비용 절) 확신 높음
  - 지출 한도. Teams, Enterprise는 사용 크레딧을 켜고 조직, 그룹, 개인 단위로 한도를 정한다. Console(API)은 워크스페이스 지출 한도, 클라우드 제공자(Bedrock, Google Cloud Agent Platform, Foundry)는 해당 클라우드의 예산 통제를 쓴다. 한도에 도달하면 메시지가 뜨고 관리자가 한도를 올리거나 리셋을 기다린다. 개인 요금제에서는 한도에 이르면 CLI에서 한도를 올리거나 해제하라고 안내한다. 책의 "한도에 이르면 승인자가 계속 여부를 결정"은 이 동작을 설계 관점으로 푼 문장이라 문서가 직접 말한 내용은 아니다. (사용처: 지출 한도 항목, 점검 질문 3) 확신 높음
  - 상한 옵션. `--max-budget-usd` CLI 플래그가 있다(이 페이지는 언급만 하고, cli-reference에 정의됨). Agent SDK의 `max_budget_usd`는 research/ch03-10-sources.md 보강 1에 기록되어 있다(오늘 재확인하지 않음). (사용처: "비용 상한"을 본문에 넣을 때. 근거 추가 필요) 확신 중간
  - 규모 참고 수치. 엔터프라이즈 평균은 개발자당 활성일 하루 약 $13, 월 $150-250이고, 사용자의 90%는 활성일 $30 미만이다. 조직에 따라 크게 달라지므로 파일럿으로 기준선을 잡으라고 한다. 이 수치를 본문에 쓰려면 "Anthropic 문서 기준"과 확인일을 붙인다. 확신 높음
  - 기타 비용 요인. 긴 컨텍스트, 캐시 미스, 하위 에이전트, 에이전트 팀(plan 모드에서 표준 세션의 약 7배 토큰)이 사용량을 키운다. 확신 높음

### S-C9-5. Anthropic, Prompting best practices (Claude Platform Docs)
- URL: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
- 게시일: 표기 없음, 확인일: 2026-10-20
- 작성: Anthropic
- 이 장에서 사용할 내용
  - "Balancing autonomy and safety" 절. 지시 없이는 Opus 4.6이 파일 삭제, force push, 외부 서비스 게시처럼 되돌리기 어렵거나 공유 시스템에 영향을 주는 동작을 할 수 있다고 쓴다. 확인을 받게 하려면 프롬프트에 지침을 넣으라고 안내한다. 이 절은 해당 모델 기준의 안내이고, 본문의 세 분류는 이 지침의 예시 목록을 그대로 옮긴 것이다.
  - 확인 대상 세 분류와 예. 파괴적 동작은 파일, 브랜치 삭제, 데이터베이스 테이블 삭제, rm -rf다. 되돌리기 어려운 동작은 git push --force, git reset --hard, 게시된 커밋의 amend다. 다른 사람에게 보이는 동작은 코드 push, PR과 이슈 댓글, 메시지 발송, 공유 인프라 변경이다. 본문의 세 분류와 예시가 원문과 일치한다. 본문은 rm -rf와 git reset --hard를 생략했다.
  - 지침은 로컬의 되돌릴 수 있는 동작(파일 수정, 테스트 실행)은 하도록 권장한다. 본문의 "되돌릴 수 있는 동작은 승인 없이" 문장의 근거가 된다. 장애물을 만났을 때 `--no-verify`로 우회하거나 낯선 파일을 버리는 식의 파괴적 지름길을 쓰지 말라는 문장도 있다. 확신 높음

### S-C9-6. OpenAI, Agent approvals and security (Codex 문서) — 오늘 원문 미개봉
- URL: https://developers.openai.com/codex/agent-approvals-security (learn.chatgpt.com/docs/agent-approvals-security로 308 이전됐다고 research/ch03-10-sources.md의 ch10, ch11 기록에 있음)
- 게시일: 표기 없음, 확인일: 2026-10-20(오늘 두 호스트 모두 DNS 실패로 열지 못함)
- 이 장에서 사용할 내용(기존 기록 인용)
  - 승인 정책은 멈추는 시점, 샌드박스는 접근 가능한 파일과 네트워크. 검색 결과에 나온 공식 페이지 발췌도 정책 3개(untrusted, on-request, never)와 샌드박스 모드(workspace-write, danger-full-access)를 별개의 설정으로 설명한다. 이 발췌는 원문 직접 확인이 아니다. 확신 중간
  - 기존 기록에는 로컬 기본값이 네트워크 차단, 쓰기는 작업 공간으로 제한이고, Auto 프리셋은 `--sandbox workspace-write --ask-for-approval on-request`라고 되어 있다. 같은 날짜의 ch10 기록은 on-request에서 네트워크가 필요한 명령에 승인을 요청한다고 적는다. 확신 중간
  - 충돌. ch10 기록은 "untrusted는 폐지"라고 적었는데 오늘 검색 발췌는 untrusted를 정책으로 나열한다. ch09 본문은 값 이름을 쓰지 않아 영향이 없다. 값을 쓰게 되면 원문을 다시 열어야 한다.

### S-C9-7. OpenAI, Slash commands (Codex 문서) — 오늘 원문 미개봉
- URL: https://developers.openai.com/codex/guides/slash-commands (learn.chatgpt.com/docs/cli/slash-commands/로 이전)
- 확인일: 2026-10-20(열지 못함)
- 이 장에서 사용할 내용
  - 같은 날짜의 ch10 기록(learn.chatgpt.com 확인)은 `/status`가 활성 모델, 승인 정책, 쓰기 가능 경로(writable roots), 남은 컨텍스트 용량을 보여 주고 샌드박스 모드 항목은 없다고 적는다. 이 기록에는 토큰 사용량이 없다.
  - 오늘 검색 결과로 확인한 것은 IDE 확장 문서의 `/status`가 "thread ID, context usage, rate limits"를 보여 준다는 점뿐이다(IDE 문서이고 CLI가 아님). ch09 본문의 "세션 설정과 토큰 사용량, 남은 컨텍스트 용량"은 2026-10-15 기록(research/ch03-10-sources.md 68행)에 근거하고, 10-20 ch10 기록과 표현이 다르다. 확인 필요. 확신 낮음

### 본문 사실 문장 판정 표

| 발견 | 위치 | 근거 | 제안 | 확신 |
|---|---|---|---|---|
| deny, ask, allow 순서, 처음 일치한 규칙, 구체적인 allow도 deny 예외 불가: 원문과 일치 | permissions 절 1문단, 그림 9-1 | S-C9-1 | 유지. "구체성은 순서를 바꾸지 않는다"를 더하면 의미가 선명해짐 | 높음 |
| 규칙 3종 정의(allow 확인 없이 허용, ask 매번 확인, deny 금지): 일치 | permissions 절 | S-C9-1 | 유지 | 높음 |
| "모든 권한 확인을 생략하는 bypassPermissions": 원문은 "prompts and safety checks를 끈다"이고 deny 규칙은 이 모드에서도 막는다. "모든 권한 확인 생략"은 과장 소지 | 보완 계층 문단 | S-C9-2 | "권한 프롬프트와 안전 확인을 끄는"으로 바꾸고, 원문의 "인터넷 없는 컨테이너, VM" 조건 반영 검토 | 중간 |
| Bash 규칙 문자열 일치 한계와 `git -C . push` 예: 일치. 원문은 그 밖에 `git -c ... push`, `git 'push'`도 불일치로 든다. 문서의 설명은 "보안 경계가 아니다" | permissions 절 한계 문단, 표 9-4 2행 | S-C9-1 | 유지. 원문 표현("deny, ask는 Claude가 보통 만드는 형태를 막을 뿐 보안 경계가 아님")을 근거로 쓸 수 있음 | 높음 |
| Edit deny는 스크립트의 간접 쓰기에 적용 안 됨, 샌드박스로 보완: 일치. 단 샌드박스는 Bash 계열만 덮고 파일 도구는 샌드박스 밖에서 실행됨 | 표 9-4 1행 | S-C9-1, S-C9-3 | 유지. 파일 도구는 Edit deny, 스크립트와 셸은 샌드박스라는 역할 분담을 한 줄로 명시하면 정확 | 높음 |
| 샌드박스 정의(셸 명령과 하위 프로세스, OS 수준, 파일과 네트워크): 일치. Bash, PowerShell, Monitor까지 확장된 점이 새 사실 | 표 9-2, 보완 계층 문단 | S-C9-3 | 유지. 필요하면 "셸 명령(Bash, PowerShell)" | 높음 |
| 샌드박스의 기본 꺼짐, 지원 OS(macOS, Linux, WSL2, 네이티브 Windows 불가)가 본문에 없음. 예제 설정에도 `sandbox` 키 없음. 샌드박스가 꺼진 상태에서는 표 9-4의 "샌드박스로 보완"이 실제로는 보완이 안 됨. backlog 지적과 일치 | 예제 JSON, 표 9-4 1, 2행, 실습 3 | S-C9-3 | "샌드박스는 기본 꺼짐, `/sandbox` 또는 `sandbox.enabled`로 켬, 네이티브 Windows는 미지원(WSL2 사용)"을 한 문장으로 추가. 예제에 `"sandbox": {"enabled": true}` 추가 여부는 작가 확인(예제 설정 변경) | 높음 |
| 권한과 샌드박스는 보완 계층: 일치 | 보완 계층 문단 | S-C9-1 | 유지. "프롬프트 주입으로 모델 판단이 뚫려도 샌드박스 제한은 남는다"를 근거로 더 쓸 수 있음 | 높음 |
| 규칙은 모델이 아니라 Claude Code가 강제한다. 지시문이나 CLAUDE.md는 허용 범위를 바꾸지 못함: 본문에 없으나 장의 주장(범위와 승인 지점이 사고 크기를 정함)의 직접 근거 | 장 주장, 승인 절 | S-C9-1 | 승인 절 또는 권한 절에 한 문장 인용 후보. 근거 보강 | 높음 |
| 확인 대상 세 분류와 예시: 일치. 단 원문 절은 Opus 4.6 대상 안내이며 프롬프트 지침이지 제품 설정이 아님. 본문은 "프롬프트 작성 문서 예"로 서술했으므로 정확 | 승인 절 1~2문단 | S-C9-5 | 유지. 최신 모델을 일반화하지 않는다는 점만 주의 | 높음 |
| "승인 단계가 많으면 승인자가 검토하지 않고 승인한다"는 일반화: 문서 근거 없음, 논리적 주장 | 승인 절 3문단, 표 9-4 3행 | 1차 출처 없음(backlog 지적과 동일) | 근거가 필요하면 "승인 피로" 근거를 찾거나 설계 판단임을 표시. auto 모드 설명(프롬프트를 줄이는 도구이나 "does not guarantee safety")을 대안으로 인용 가능 | 중간 |
| 자동 모드, 권한 모드 기본값이 ch09에 없음. 기본 시작 모드가 auto(v2.1.283 이상, 대화형)로 바뀌어 "처음 일치하지 않는 요청은 매번 묻는다"는 전제가 틀릴 수 있음. 표 9-2 "권한 모드: 어느 규칙에도 맞지 않는 요청의 처리"는 표현상 맞지만 구체 동작은 모드마다 다름 | 표 9-2, 그림 9-1 | S-C9-2 | 기본 모드를 쓴다면 버전 주석 필수("v2.1.283 이상 대화형 기본 auto, `claude -p`는 default"). 확인 날짜 명시 | 높음 |
| `/permissions`로 규칙 확인, deny에 data/, acceptance/, git push, ask에 git commit: 일치. 단 `/permissions`가 보여 주는 형식은 문서에 있어 deny 항목은 규칙 문자열 그대로 나타남 | 표 9-5 1행 | S-C9-1 | 유지 | 높음 |
| 표 9-5 2행의 "대화 화면에 파일 수정이 거부되었다는 메시지": 문서에 거부 메시지 문구는 없음. 거부 메시지가 결과로 모델에 전달된다는 설명은 SDK 문서에 있음(research/ch03-10-sources.md 보강 1) | 표 9-5 2행 | 간접 | 문구를 고정하지 말고 "거부되었다는 메시지" 수준 유지. 실제 화면은 실습 3에서 확인 | 중간 |
| 우회 명령(`git -C . push`) 확인 행 없음 | 표 9-5 | backlog 지적 | 행 추가는 원고 작업. 확인 기준은 deny 규칙이 우회 형태를 막지 못함을 보이는 것이므로, 샌드박스를 켠 상태의 네트워크 차단 확인(`touch ~/sandbox-probe` 계열) 사용 가능(S-C9-3) | 중간 |
| "에이전트의 비용은 토큰 사용량에 비례": API 과금 기준에서만 정확. 구독은 요금제 한도와 사용 크레딧 체계 | 비용 절 첫 문장 | S-C9-4 | "API 과금에서는"을 붙이거나 구독을 구분 | 중간 |
| 비용 관리 방법 4개(토큰 추적, 팀 지출 한도, 컨텍스트 관리, 모델 선택): 문서 개요 문장과 일치. 문서에는 확장 사고, 훅도 있음 | 비용 절 | S-C9-4 | 유지. "대표 방법"으로 | 높음 |
| `/usage`의 Session 항목, 상태 줄 표시, 구독 요금제 사용량, API 사용자용, 정가 기준 추정치: 일치 | 비용 절, 표 9-3, 9-5 | S-C9-4 | 유지. 첫 화면 위쪽 Session 블록이라고 위치를 적으면 독자 도움(backlog "/usage에서 볼 곳") | 높음 |
| 지출 한도: "팀이나 사용자별 한도": 문서는 Teams, Enterprise의 조직, 그룹, 개인 한도(사용 크레딧 기준), Console의 워크스페이스 한도. 한도에 이르면 승인자가 계속 여부 결정은 문서에 없는 설계 문장 | 비용 절 목록 3, 점검 질문 3 | S-C9-4 | 유지하되 제품별 위치를 한 문장으로(Teams: 관리자 설정 > Usage, Console: 워크스페이스). "승인자 결정"은 책의 권고임을 문장 구조로 구분 | 중간 |
| 비용 상한(`--max-budget-usd`), 모델 요금: 본문에 문장 없음. 모델별 요금표는 이번에 확인하지 않음 | 비용 절 | S-C9-4 | 상한을 넣으려면 S-C9-4의 `--max-budget-usd` 근거를 cli-reference 원문으로 재확인한 뒤 사용. 요금 수치는 본문에 넣지 않는 것이 안전 | 중간 |
| Codex: "승인 정책은 동작 전 멈추고 확인하는 시점, 샌드박스는 접근 가능한 파일과 네트워크": 기존 기록과 오늘 검색 발췌와 일치하나 오늘 원문 미개봉 | 권한 절 Codex 문단 | S-C9-6 | 원문 재개봉 전까지 확신 중간으로 표시. 참고 자료의 "OpenAI. Agent approvals and security" URL은 이전 후 주소로 갱신 여부 확인 | 중간 |
| Codex `/status`: "세션 설정과 토큰 사용량, 남은 컨텍스트 용량". 10-20 ch10 기록과 표현 불일치("활성 모델, 승인 정책, 쓰기 가능 경로, 남은 컨텍스트 용량"), 토큰 사용량 언급 없음 | 비용 절 /usage 문단, 표 9-3 4행, 그림 9-2 | S-C9-7 | 원문 재확인 전에는 "남은 컨텍스트 용량" 중심으로 낮추는 안을 권함. 메인 세션이 네트워크가 되는 환경에서 다시 열어 확정 | 낮음 |
| 참고 자료 확인일: Anthropic 문서는 10월 4일, 15일 | 참고 자료 | 오늘 재확인 | permissions, sandboxing, costs, prompting best practices 모두 2026-10-20으로 갱신(원문 개봉 완료). Codex 두 건은 원문을 열 때까지 갱신 보류 | 높음 |
| 한도: 기본 접근 범위가 실행한 작업 디렉터리(기존 기록). 오늘 재확인: 읽기는 작업 디렉터리와 추가 디렉터리 안에서 승인 불필요, 샌드박스 쓰기 기본은 작업 디렉터리, 임시 디렉터리, `--add-dir` 디렉터리 | 표 9-1 "작업 디렉터리 제한" | S-C9-1, S-C9-3 | 유지. 표 9-1의 "작업 디렉터리 제한"은 권한 기능이 아니라 기본 동작과 샌드박스의 쓰기 범위임을 구분하면 정확 | 중간 |

### 미확인 목록
- Codex 승인 정책 값(untrusted의 폐지 여부), 샌드박스 값(read-only, workspace-write, danger-full-access), 권한 프로필(:read-only, :workspace 등), `/status` 표시 항목의 오늘 원문 확인. 찾아본 곳은 developers.openai.com과 learn.chatgpt.com의 4개 URL이고 모두 DNS 오류였다. 대신 웹 검색 발췌와 기존 research/ch03-10-sources.md 기록을 사용했다(둘 다 2차 기록).
- 모델별 요금(Anthropic pricing 페이지)은 확인하지 않았다. 본문에 요금 문장이 없어 범위에서 제외했다.
- `--max-budget-usd`와 Agent SDK `max_budget_usd`의 정의 원문(cli-reference, agent-loop)은 오늘 열지 않았다.
- 승인 프롬프트의 실제 화면과 거부 메시지 문구는 문서에 고정 문구가 없다.
- 지출 한도에 도달했을 때 Claude Code가 개인 요금제에서 CLI로 한도를 올리도록 안내한다는 내용은 costs 페이지에서 확인했지만 팀 요금제에서 "승인자가 결정"하는 절차는 문서에 없다.

### 장의 주장을 뒷받침하기에 근거가 부족한 곳
1. "승인 단계가 많으면 승인자가 검토 없이 승인한다"(승인 절, 표 9-4 3행)는 1차 출처 없이 책의 논리로만 서 있다. 근거를 찾거나 설계 판단임을 표시해야 한다.
2. "사고의 크기를 정하는 것은 판단력이 아니라 권한 범위와 승인 지점"이라는 장 주장은 S-C9-1의 "규칙은 모델이 아니라 Claude Code가 강제한다"와 "prompt injection이 뚫어도 샌드박스는 남는다"가 가장 가까운 직접 근거다. 현재 본문에는 둘 다 인용되지 않았다.
3. 격리 효과 중 샌드박스 기본 꺼짐과 네이티브 Windows 미지원이 본문에 없어 "샌드박스로 보완"이 기본 설정에서는 성립하지 않는다(backlog 항목과 일치).
4. Codex 쪽 문장은 오늘 원문 대조가 불가능했으므로 Codex 관련 판정은 모두 잠정이다.

## 2026-10-20 fact-checker 점검(9장 개정 원고, PR #42)

### S-C9-8. 원문 재대조 결과 (Claude Code Docs, 4건과 Anthropic Prompting best practices)
- URL: https://code.claude.com/docs/en/permissions, /permission-modes, /sandboxing, /costs, https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
- 게시일: 표기 없음, 확인일: 2026-10-20
- 작성: Anthropic
- 확인한 내용
  - permissions: 평가 순서 단락의 "rule specificity doesn't change the order"와 예시는 Bash(aws *) 대 Bash(aws s3 ls)이며 git 예시는 원문에 없음(본문의 git 예시는 책의 적용). Permission system Note: "Permission rules are enforced by Claude Code, not by the model". Bash 규칙 한계 표에 git -C . push origin main, git -c push.default=current push, git 'push'가 불일치로 있음. Read and Edit deny는 내장 파일 도구, 인식된 셸 파일 명령(cat, head, tail, sed, tee), 리다이렉션 대상에 적용되고 Python이나 Node 스크립트의 간접 쓰기에는 미적용. Warning: WebFetch만으로는 네트워크 접근이 막히지 않고 Bash가 허용되면 curl로 도달 가능.
  - sandboxing: off by default, /sandbox 또는 sandbox.enabled. 대상은 Bash, PowerShell, Monitor와 하위 프로세스, 파일 도구와 MCP와 훅은 밖. 지원은 macOS, Linux, WSL2(네이티브 Windows는 샌드박스 없이 실행, WSL1 미지원). Linux와 WSL2는 bubblewrap과 socat 필요. 검증 표의 touch ~/sandbox-probe는 macOS Operation not permitted, Linux와 WSL2 Read-only file system. 허용 도메인은 비어 있는 상태로 시작하고 새 도메인은 권한 모드에 따라 처리. Edit 규칙과 sandbox 설정의 경로는 샌드박스 설정에 합쳐진다.
  - permission-modes: bypassPermissions는 "disables permission prompts and safety checks", "Deny rules block in every mode, including bypassPermissions", 인터넷 없는 컨테이너, VM, 개발 컨테이너에서만 사용. 명시적 ask 규칙은 이 모드에서도 묻는다.
  - costs: 개요에 여섯 가지(토큰 추적, 팀 지출 한도, 컨텍스트 관리, 모델 선택, 확장 사고 설정, 전처리 훅). Teams와 Enterprise 한도는 사용 크레딧을 켠 뒤 조직, 그룹, 개인 단위. Console은 워크스페이스 한도. /usage 첫 화면 위쪽 Session 블록은 API 사용자용, 정가 기준 추정치(modelPricing 설정 시 계약 요율 기준 추정치, v2.1.242 이상). 구독자는 같은 화면에서 요금제 사용량 막대 등을 봄.
  - Prompting best practices "Balancing autonomy and safety": Claude Opus 4.6 대상 안내, 세 분류와 예시, 로컬 되돌릴 수 있는 동작 권장.
- 본문 사용: 위 문장 모두 일치 또는 단순화 허용 범위. 필요한 보강은 보고서 18, 19, 22, 23, 24행.

### S-C9-6 보강(Codex). 확인일 2026-10-20
- developers.openai.com/codex/agent-approvals-security와 .md 주소를 다시 열었으나 DNS 오류(ENOTFOUND). 웹 검색 발췌(2차)는 승인 정책과 샌드박스를 독립 설정으로 설명. 본문 Codex 문장은 여전히 미확인(원문 미개봉). 참고 자료의 확인일 10월 4일은 유지.
