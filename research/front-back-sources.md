# 시작하며, 마치며, 부록 출처 기록

2026-10-20 fact-checker 대조(PR #45). 공통: 게시일 없음(상시 갱신 문서), 확인일 2026-10-20, 작성 Anthropic(Claude Code Docs).

공통 규칙입니다. 게시일은 상시 갱신 문서라 없고, 확인일은 모두 2026-10-20입니다. 작성은 Anthropic(Claude Code Docs)입니다.

- **S-FB-1. How Claude remembers your project** (https://code.claude.com/docs/en/memory). 작업 폴더와 그 위 모든 폴더의 CLAUDE.md, CLAUDE.local.md를 시작 때 읽습니다. AGENTS.md는 작업 폴더나 위에 CLAUDE.md 계열이 없을 때만, v2.1.277 이상에서 읽습니다. 자동 메모리는 로컬 세션에서 기본 켜짐이고 MEMORY.md는 앞 200줄 또는 25KB를 읽습니다. 사용처: L1, L14, T6.
- **S-FB-2. Advanced setup** (https://code.claude.com/docs/en/setup). PowerShell 설치 명령은 `irm https://claude.ai/install.ps1 | iex`입니다. Git for Windows가 있으면 Bash 도구가 Git Bash를 쓰고, 없으면 PowerShell 도구를 씁니다. 인증은 Pro, Max, Team, Enterprise, Console 계정이고 무료 claude.ai 요금제는 불포함입니다. 사용처: 실습 준비.
- **S-FB-3. Configure permissions** (https://code.claude.com/docs/en/permissions). 평가 순서는 deny → ask → allow입니다. `Edit(path)` 규칙은 내장 편집 도구 전체에 적용됩니다. Bash 출력 리디렉션(`>`, `>>`, `tee`)은 Edit 허용, 금지 규칙으로 검사합니다. Bash 규칙은 PowerShell 도구를 제한하지 않아 `PowerShell(...)` 규칙이 따로 있습니다. `/permissions`는 규칙과 출처 설정 파일을 보여 줍니다. 사용처: L6.
- **S-FB-4. Tools reference** (https://code.claude.com/docs/en/tools-reference). Git Bash가 없는 Windows에서는 PowerShell 도구가 자동으로 켜집니다. Git Bash가 있으면 claude.ai, Console 계정에서 기본으로 켜집니다. Bash 금지 규칙이 있으면 Git Bash 환경에서 PowerShell 도구가 꺼집니다. 사용처: L6, L15.
- **S-FB-5. Hooks reference, Automate actions with hooks** (https://code.claude.com/docs/en/hooks, /hooks-guide). 성공한 훅의 stdout은 SessionStart, UserPromptSubmit 등 예외를 빼고 대화에 보이지 않습니다. PostToolUse의 종료 코드 2는 stderr를 Claude에 보여 주지만 도구는 이미 실행된 뒤입니다. 훅 명령은 macOS, Linux에서 `sh -c`, Windows에서 Git Bash(없으면 PowerShell)로 실행됩니다. `/hooks`는 읽기 전용 목록입니다. 훅 type은 command 외에 http, mcp_tool, prompt, agent가 있습니다. hooks 페이지는 앞 100,000자만 열람했습니다. 사용처: L3, L7, T9.
- **S-FB-6. Commands** (https://code.claude.com/docs/en/commands). `/context`, `/permissions`(별칭 `/allowed-tools`), `/hooks`, `/memory`, `/sandbox`, `/exit`(별칭 `/quit`)를 확인했습니다. `/usage`는 세션 비용, 요금제 한도, 활동 통계를 보여 주며 `/cost`, `/stats`가 별칭입니다. 사용처: L9, T2, T8.
- **S-FB-7. Configure the sandboxed Bash tool** (https://code.claude.com/docs/en/sandboxing). 샌드박스는 기본 꺼짐이고 `/sandbox`나 `sandbox.enabled`로 켭니다. macOS, Linux, WSL2에서 동작하고 네이티브 Windows에서는 없습니다. 셸 명령만 대상이고 파일 도구, MCP, 훅은 샌드박스 밖입니다. 사용처: T5.
- **S-FB-8. Choose a permission mode** (https://code.claude.com/docs/en/permission-modes). 터미널과 VS Code는 v2.1.283 이상에서 auto로 시작합니다. `claude -p`와 SDK는 default입니다. 프로젝트 설정의 auto, bypassPermissions는 무시됩니다. 보호 경로(.claude, .git 등)는 default와 acceptEdits에서 확인 요청입니다. 사용처: 실습 3, 5의 권한 동작.
- **S-FB-9. Create custom subagents** (https://code.claude.com/docs/en/sub-agents). 프로젝트 하위 에이전트는 작업 폴더에서 저장소 루트까지 올라가며 찾습니다. `tools: Read, Grep, Glob` 형식은 유효합니다. 두 번째 열람은 앞 100,000자까지입니다. 사용처: L1.
- **S-FB-10. Manage costs effectively** (https://code.claude.com/docs/en/costs). `/usage` 첫 화면의 Session 블록은 토큰 사용 통계이고 API 사용자용입니다. 금액은 로컬에서 정가 기준으로 계산한 추정치이고 청구는 Console에서 봅니다. 사용처: L9, T2.
- **S-FB-11. Plans & pricing** (https://claude.com/pricing). Free 요금제는 Claude Code 미포함, Pro부터 포함입니다. 작성은 Anthropic(Claude)입니다. 사용처: L10, L16.
- **S-FB-12. Terminal guide for new users** (https://code.claude.com/docs/en/terminal-guide). PowerShell 설치 명령, Git for Windows 선택 사항(없으면 PowerShell 사용), `exit`로 종료를 확인했습니다. 사용처: L16.
- **S-FB-13. 실습 저장소** (https://github.com/seoulkorea-dev/harness-book). 작성은 seoulkorea-dev입니다. 공개 저장소이고 examples/expense-app 항목이 있습니다. 이 브랜치 변경이 main에 있는지는 미확인입니다. 사용처: L16.
- **S-FB-14. 미확인 기록**. (a) Codex 문서(developers.openai.com의 slash-commands, agent-approvals-security)는 DNS 오류로 열지 못했습니다(검색 요약만 있어 판정 근거로 쓰지 않음). (b) arXiv 2210.03629 재열람 실패(기존 S11 기록 유지). (c) 부모 폴더의 .claude/settings.json이 하위 폴더 세션에 적용되는지는 settings 문서에서 찾지 못했습니다. (d) `/context` 화면의 하위 에이전트 항목과 `/hooks` 목록의 matcher 표시는 실습 4 실행 때 확인합니다.

Sources: https://code.claude.com/docs/en/memory, /setup, /terminal-guide, /permissions, /permission-modes, /tools-reference, /hooks, /hooks-guide, /commands, /sandboxing, /sub-agents, /costs, https://claude.com/pricing, https://github.com/seoulkorea-dev/harness-book. Codex 승인 정책과 `/status`에 관한 검색 결과는 제3자 요약이라 판정 근거로 쓰지 않았습니다.
