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

## 개정 후 대조(2026-10-20, fact-checker 2차)
공통: 게시일 없음(상시 갱신 문서), 확인일 2026-10-20, 작성 Anthropic(Claude Code Docs), 개정 후 대조(PR #45).

- **S-FB-15. Quickstart** (https://code.claude.com/docs/en/quickstart). 첫 실행에서 로그인 안내가 나오고(Pro, Max, Team, Enterprise, Console 계정, 브라우저 인증), `claude -c`는 현재 폴더의 가장 최근 대화를 이어 엽니다. Git for Windows가 없으면 PowerShell을 셸 도구로 씁니다. 사용처: 실습 준비, 실습 6, 막혔을 때.
- **S-FB-16. CLI reference** (https://code.claude.com/docs/en/cli-reference). `--continue`, `-c`는 현재 폴더의 가장 최근 대화를 불러옵니다. `claude doctor`는 설정 파일 검증 오류를 포함한 읽기 전용 진단을 출력합니다. 사용처: 실습 6, 막혔을 때.
- **S-FB-17. Security, Configure permissions** (https://code.claude.com/docs/en/security, /permissions). 신뢰하지 않은 폴더에서 시작하면 워크스페이스 신뢰 확인이 나옵니다. 프로젝트 `.claude/settings.json`의 allow 규칙은 신뢰를 수락한 뒤에만 적용되고 deny, ask는 영향을 받지 않습니다. 저장소 안에서는 저장소 루트 단위로 신뢰를 저장하고, 홈 폴더에서 시작하면 세션 동안만 유지합니다. 평가 순서는 deny → ask → allow이고 `/permissions`는 규칙과 출처 설정 파일을 보여 줍니다. 사용처: 실습 2, 3.
- **S-FB-18. Explore the context window, Commands** (https://code.claude.com/docs/en/context-window, /commands). `/context`는 어떤 CLAUDE.md와 자동 메모리 파일이 적재됐는지를 포함한 범주별 내역을 보여 주고, 전체 화면에서는 항목별 내역을 접으며 `all`로 펼칩니다. `/memory`는 CLAUDE.md 편집, 자동 메모리 켜고 끄기, 자동 메모리 항목 열람입니다. 화면의 "메모리 파일" 항목 이름은 문서에서 못 찾았고 실습 2 실행 때 확인합니다. 사용처: 실습 2, 6.
- **S-FB-19. Hooks reference, Automate actions with hooks** (https://code.claude.com/docs/en/hooks, /hooks-guide). `/hooks`는 읽기 전용 목록이고 이벤트별로 묶여 보이며, 훅을 선택하면 실행 명령 전문과 정의된 파일이 보입니다. 종료 코드 0이면 대부분의 이벤트에서 stdout이 transcript에 보이지 않습니다. PostToolUse의 종료 코드 2는 "Shows stderr to Claude; the tool already ran"입니다. 사용자 화면에 `hook error` 알림이 뜨는지는 PostToolUse에 대해 명시되지 않았습니다(미확인, 실습 4 실행 때 확인). 사용처: 실습 4.
- **S-FB-20. Choose a permission mode** (https://code.claude.com/docs/en/permission-modes). 터미널과 VS Code는 v2.1.283 이상에서 auto로 시작합니다. auto에서는 작업 폴더 안의 파일 수정이 자동 승인되고, 명시한 ask 규칙은 여전히 묻고, deny 규칙은 모든 모드에서 막습니다. 보호 경로(`.git`, `.claude` 등)는 분류기로 보냅니다. S-FB-8의 재확인입니다. 사용처: 실습 2, 3의 확인 화면 서술(L6).
- **S-FB-21. Set up, Tools reference, Terminal guide, Plans & pricing 재확인** (https://code.claude.com/docs/en/setup, /tools-reference, /terminal-guide, https://claude.com/pricing). Git for Windows는 선택 사항이고, 있으면 Bash 도구가 Git Bash를 쓰며 claude.ai와 Console 계정에서는 PowerShell 도구도 기본으로 함께 켜집니다. Git Bash가 있는 Windows에서 Bash 금지 규칙(범위 지정 포함)이 있으면 PowerShell 도구가 꺼집니다. 터미널 열기는 Windows `Win + X`, macOS `Cmd + Space`입니다. 인증은 Pro, Max, Team, Enterprise, Console이고 무료 claude.ai는 불포함이며, pricing은 Free 미포함, 모든 유료 요금제 포함입니다. `/usage` 세션 금액은 정가 기준 추정치이고 구독 사용자에게는 청구 근거가 아니라는 점을 costs 문서에서 재확인했습니다. 사용처: 실습 준비, 실습 6(L1~L3, L12).
- **S-FB-22. 실습 저장소 재확인** (https://github.com/seoulkorea-dev/harness-book). 작성 seoulkorea-dev. 로그인 없이 열리는 공개 저장소입니다. 루트에 CLAUDE.md, .claude/, DECISIONS.md, FAILURES.md, reviews/, research/가 있고, examples/expense-app에는 reference/(CLAUDE.example.md, reviewer.example.md, settings.example.json, tasks.example.json), RUNLOG.md(2026-10-16 기록만, 10-20 기록은 병합 전), tasks.example.json(작업 1 true)이 있습니다. 사용처: 시작하며 목적 셋째 항목, 실습 1.
- **S-FB-23. 미확인 기록(개정 후)**. (a) developers.openai.com, arxiv.org, git-scm.com이 DNS 오류로 열리지 않았습니다(승인 정책 Codex 정의, ReAct 연도, `git config --global` 범위). (b) 부모 폴더의 `.claude/settings.json`이 하위 폴더 세션에 적용되는지는 settings 문서를 열지 않아 확인하지 못했습니다. (c) 실습 3의 "설정 JSON 형식 오류 때 Claude Code가 설정을 읽지 못함" 증상. (d) PostToolUse 종료 코드 2의 사용자 화면 알림(S-FB-19). (e) `/context`의 "메모리 파일" 항목 이름(S-FB-18).

Sources: https://code.claude.com/docs/en/memory, /setup, /terminal-guide, /permissions, /permission-modes, /tools-reference, /hooks, /hooks-guide, /commands, /sandboxing, /sub-agents, /costs, https://claude.com/pricing, https://github.com/seoulkorea-dev/harness-book. Codex 승인 정책과 `/status`에 관한 검색 결과는 제3자 요약이라 판정 근거로 쓰지 않았습니다.

## 시작하며 사실 점검(2026-10-23, fact-checker, PR #108)
공통: 게시일 없음(저장소 내부 대조), 확인일 2026-10-23, 작성 fact-checker. 외부 문서는 열지 않았고 이전 기록의 확인일을 인용했습니다.

- **S-FB-24. 시작하며와 Chapter 1~11, 부록 실습 대조** (src/chapters/prologue.html, ch01~ch11.html, src/appendix/practice.html, BOOK_SPEC.md 1, 3, 4, 5, 6, 7, 9절, docs/specs/prologue-spec.md). 정의 문장은 Chapter 1과 BOOK_SPEC 4, 5절과 같은 뜻. Chapter 10 비교 기준은 네 기준(규칙 문서, 권한, 격리, 설정 파일)이라 "같은 구성 요소를 대조"를 "같은 정책을 두 제품의 설정으로 옮긴 결과를 대조"로 고침(ch10.html:6). 사용처: 시작하며 message 마지막 문단, guide 제품 도입 경로.
- **S-FB-25. 링크와 앵커 검사** (src와 빌드 결과의 chapters/prologue.html). 링크 11개의 도착 파일, 앵커, 링크 문구와 도착 절 제목 모두 일치.
- **S-FB-26. 인용 체계 대조** (tools/build.py 6~7, 26~60행, appendix/references.html, src/site.json). 위첨자 번호는 책 전체 번호, 참고 문헌은 nav의 마지막 부록. 위첨자 인용은 ch01, 02, 04, 05, 06에만 있고 ch03, 07~11, 부록 실습은 (저자, 연도) 방식이 남음(정비 중). 사용처: 시작하며 scope 셋째 문단.
- **S-FB-27. 기준 일자 확인** (research/ch01~ch11-sources.md). Claude Code 문서 확인일 2026-10-20, Codex 문서 2026-10-04(ch10.html:8). OpenAI 문서는 2026-10-20 DNS 오류로 재확인 대기(research/ch10-sources.md:6, 84). 사용처: 시작하며 "2026년 10월에 확인한 공식 문서".
- **S-FB-28. 저장소 공개 재확인 시도** (https://github.com/seoulkorea-dev/harness-book). gh repo view가 GraphQL 제한(HTTP 403)으로 실패. 공개 여부는 S-FB-22(2026-10-20)에 따름. 사용처: 집필 목적 셋째 항목.
- **S-FB-29. 실습 비용** (src/appendix/practice.html:5~9). 실습 2부터 Claude Code 사용, 유료 요금제 또는 API 키 필요. 사용처: 시작하며 scope 둘째 문단.

## 2026-10-26 마치며(옛 Chapter 11 이동, D-144)
- 새 인용 키 harness-design-apps: Prithvi Rajasekaran, Harness design for long-running application development, Anthropic, 2026-03-24, https://www.anthropic.com/engineering/harness-design-long-running-apps. 근거 기록 research/ch01-sources.md S13(확인일 2026-10-19): 구성 요소는 모델이 혼자 못 하는 일에 대한 가정이고 새 모델마다 다시 시험, "the space of interesting harness combinations doesn't shrink as models improve", 자기 결과를 후하게 평가하는 실패
- "작업하며 겪은 어려움" 근거: 이슈 #66(2026-10-22 작가 승인 통합 계획의 원인 네 가지), D-131, D-132(기준서와 동결), D-139(검토 장마다 한 번), D-137(클라우드 GraphQL 차단), research/ 각 장의 열람 실패 기록, HANDOFF.md 장별 고칠 문장 비율(24.0~55.2%)
- "잘된 점" 근거: FAILURES.md F-07(인계 메모), HANDOFF.md(2~11장, 마치며, 부록 PR #124~#136 모두 2026-10-24 병합), seoulkorea-dev/genai-book PR #15~#26(2026-10-25)
