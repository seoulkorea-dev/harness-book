
## 2026-10-24 fact-checker 재확인(부록)

범위: src/appendix/terms.html(용어 풀이), src/appendix/practice.html(실습). 브랜치 appendix-playbook, bbf1459 이후 문안. 확인 날짜는 모두 2026-10-24. 게시일은 공식 문서가 게시일을 표시하지 않아 "표시 없음"으로 적고 확인일만 남긴다.

- S-AP-1. Set up Claude Code(Advanced setup). https://code.claude.com/docs/en/setup . 게시일 표시 없음. 작성 Anthropic. 확인 2026-10-24.
  - 사용한 내용: Authenticate 절에 "Pro, Max, Team, Enterprise, or Console account가 필요하고 무료 claude.ai 요금제는 Claude Code를 포함하지 않는다". 설치 명령은 macOS, Linux, WSL이 `curl -fsSL https://claude.ai/install.sh | bash`, Windows PowerShell이 `irm https://claude.ai/install.ps1 | iex`(CMD용 install.cmd도 있음). Verify your installation 절에 `claude --version`이 버전 번호를 출력. Windows에서 Git for Windows가 있으면 Bash 도구가 Git Bash를 쓰고, 없으면 PowerShell 도구를 쓴다. Git for Windows가 있을 때 PowerShell 도구는 claude.ai와 Console 계정에서 기본 켜짐. 로그인은 claude 실행 후 브라우저 안내.
- S-AP-2. Plans & pricing. https://claude.com/pricing . 게시일 표시 없음. 작성 Anthropic. 확인 2026-10-24.
  - 사용한 내용: Free는 Claude Code 미포함("No"), Pro, Max(5x, 20x), Team, Enterprise는 포함. FAQ에 "Claude Code is included in all paid plans".
- S-AP-3. Manage costs effectively. https://code.claude.com/docs/en/costs . 게시일 표시 없음. 작성 Anthropic. 확인 2026-10-24.
  - 사용한 내용: Using the /usage command 절에서 Session 블록의 금액은 로컬에서 정가(list price)로 계산한 추정치이며 API 사용자용이고, Pro와 Max 구독자는 사용량이 구독에 포함되어 요금제 사용량 막대를 본다. 실제 청구는 Claude Console Usage 페이지. Add usage credits to your subscription 절에서 사용 크레딧으로 요금제 한도를 넘어 계속 사용 가능. /cost는 /usage의 별칭(commands 문서).
- S-AP-4. Terminal guide for new users. https://code.claude.com/docs/en/terminal-guide . 게시일 표시 없음. 작성 Anthropic. 확인 2026-10-24.
  - 사용한 내용: macOS는 Cmd+Space로 Spotlight에서 Terminal, Linux는 Ctrl+Alt+T 또는 응용 프로그램 메뉴, Windows는 Win+X에서 Windows PowerShell(또는 Terminal). Git for Windows는 선택 사항.
- S-AP-5. Tools reference(PowerShell tool 절, Bash deny rules also turn off the PowerShell tool 절). https://code.claude.com/docs/en/tools-reference . 게시일 표시 없음. 작성 Anthropic. 확인 2026-10-24.
  - 사용한 내용: Windows에서 Git Bash가 있으면 PowerShell 도구는 claude.ai와 Console 계정에서 기본 켜짐. Windows에서 Git Bash가 있을 때 `Bash(git push *)` 같은 범위 지정 규칙을 포함한 Bash 금지 규칙은 그 세션에서 PowerShell 도구를 끈다(CLAUDE_CODE_USE_POWERSHELL_TOOL=1이나 PowerShell 규칙으로 유지 가능). 실습 준비의 해당 문장과 일치.
- S-AP-6. Security. https://code.claude.com/docs/en/security . 게시일 표시 없음. 작성 Anthropic. 확인 2026-10-24.
  - 사용한 내용: Trust verification 항목에 신뢰하지 않은 폴더에서 대화형 세션을 시작하면 workspace trust 대화상자가 나온다. 홈 디렉터리에서 시작하면 신뢰가 디스크에 저장되지 않는다(실습은 expense-practice에서 시작하므로 해당 없음). Manual mode는 파일 수정과 명령 실행 전에 묻는다.
- S-AP-7. Explore the context window. https://code.claude.com/docs/en/context-window . 게시일 표시 없음. 작성 Anthropic. 확인 2026-10-24.
  - 사용한 내용: Check your own session 절에 /context가 어떤 CLAUDE.md와 자동 메모리 파일이 적재됐는지 포함한 범주별 내역을 보여 준다. "Memory files" 표시 이름은 이 문서에 없음. 실습 2의 해당 인용은 memory 문서로 바꾸는 것을 제안(지적 24번).
- S-AP-8. How Claude remembers your project. https://code.claude.com/docs/en/memory . 게시일 표시 없음. 작성 Anthropic. 확인 2026-10-24.
  - 사용한 내용: Troubleshoot memory issues 절에 "/context를 실행하고 Memory files 아래 목록을 확인". Auto memory 절에 로컬 세션에서 기본 켜짐, 보관 위치 ~/.claude/projects/<project>/memory/, 컴퓨터 간에 공유되지 않음("machine-local"). View and edit with /memory 절에 /memory가 CLAUDE.md 목록, 자동 메모리 토글, 메모리 폴더 열기를 제공. AGENTS.md 절에 기본으로 작업 폴더와 그 위에 CLAUDE.md, .claude/CLAUDE.md, CLAUDE.local.md가 없을 때만 AGENTS.md를 읽고, 직접 읽기는 v2.1.277 이상.
- S-AP-9. Permission modes. https://code.claude.com/docs/en/permission-modes . 게시일 표시 없음. 작성 Anthropic. 확인 2026-10-24.
  - 사용한 내용: 모드는 default(Manual), acceptEdits, plan, auto, dontAsk, bypassPermissions. default는 읽기만 묻지 않음. v2.1.283 이상의 터미널과 VS Code 세션 시작 모드는 auto, claude -p와 Agent SDK는 Manual. 금지 규칙은 모든 모드에서 적용.
- S-AP-10. Configure permissions. https://code.claude.com/docs/en/permissions (Manage permissions 절). 게시일 표시 없음. 작성 Anthropic. 확인 2026-10-24.
  - 사용한 내용: 규칙은 deny, ask, allow 순서로 평가하고 처음 일치한 것이 결과를 정한다.
- S-AP-11. Sandboxing. https://code.claude.com/docs/en/sandboxing . 게시일 표시 없음. 작성 Anthropic. 확인 2026-10-24. (문서 끝 약 3,000자는 읽지 못함)
  - 사용한 내용: 샌드박스는 기본 꺼짐이고 /sandbox 또는 sandbox.enabled로 켠다. 셸 명령과 그 하위 프로세스가 대상이며 Read, Edit, Write 같은 내장 파일 도구는 권한 규칙을 따른다. 네이티브 Windows는 미지원이고 macOS, Linux, WSL2에서 동작.
- S-AP-12. Automate actions with hooks. https://code.claude.com/docs/en/hooks-guide . 게시일 표시 없음. 작성 Anthropic. 확인 2026-10-24.
  - 사용한 내용: /hooks가 hooks 브라우저를 연다. 성공한 훅은 아무것도 보이지 않는다(Ctrl+O 대화 기록 보기에서 결과 확인). exit 2는 stderr를 사유로 쓰며 이벤트에 따라 Claude가 피드백으로 받는다. PostToolUse의 세부(도구는 이미 실행됨)는 research/ch02-sources.md의 기존 기록을 따랐고 이번에 hooks 레퍼런스 문서를 다시 열지는 않음.
- S-AP-13. Commands, CLI reference. https://code.claude.com/docs/en/commands , https://code.claude.com/docs/en/cli-reference . 게시일 표시 없음. 작성 Anthropic. 확인 2026-10-24.
  - 사용한 내용: /permissions(허용, 확인 요청, 금지 규칙 관리), /hooks, /memory, /context [all], /usage(별칭 /cost, /stats), /exit(별칭 /quit), /clear 모두 존재. `claude -c`는 현재 디렉터리의 가장 최근 대화를 이어 감. --permission-mode 플래그 존재.
- S-AP-14. 실행 기록(R8). 환경 Linux, Python 3.13.16, git 2.43.0, 2026-10-24. examples/expense-app을 스크래치 폴더에 복사해 실습 1을 실행(원본 저장소 변경 없음).
  - 명령과 출력 원문(요약):
    $ cp -r harness-book/examples/expense-app expense-practice && cd expense-practice && git init && git add -A && git commit -m "실습 시작 상태"
    $ git log --oneline
    573a937 실습 시작 상태
    $ ls -a  -> .gitignore DECISIONS.md README.md RUNLOG.md acceptance app.py check.py data docs expense reference tests (.claude 폴더와 CLAUDE.md 없음)
    $ python3 -m unittest discover tests -q
    Ran 3 tests in 0.003s
    OK
    $ python3 check.py ; echo exit=$?
    tests: 실행 3건, 실패 0건, 건너뜀 0건, project_code 시험 0건   (출력 앞쪽, 6번째 줄 부근)
    FAIL: test_1_form_offers_project_codes / test_2_unknown_code_rejected_with_reason / test_3_list_shows_project_code
    Ran 5 tests in 0.006s
    FAILED (failures=3)
    acceptance: 실행 5건, 실패 3건, 건너뜀 0건(정한 수 5건)
    exit=1
  - 판정: bbf1459 이후 practice.html의 요약 줄 순서(tests → FAILED → acceptance)와 "2026년 10월 24일 Linux에서 실행"이 실제와 일치. reference/tasks.example.json은 작업 1 true, 작업 2~5 false. reference/settings.example.json의 deny에 Edit(./data/**), Edit(./acceptance/**), Edit(./check.py), Edit(./CLAUDE.md), Edit(./DECISIONS.md), Edit(./.claude/**), Bash(git push *), WebFetch, WebSearch가 있음(실습 3, 4 설명과 일치). app.py는 localhost:8000과 /new 경로를 사용. https://github.com/seoulkorea-dev/harness-book.git 은 열리고 기본 브랜치 main에 examples/expense-app이 있음.
  - 실행하지 못한 것: 실습 2~6의 Claude Code 화면(로그인과 요금제가 필요). 해당 문장의 확인은 공식 문서 대조까지이며 화면 문구는 미확인(부록이 "예상"이라고 밝힌 부분).
- S-AP-15. 본문 대조(R7, 용어 풀이). src/chapters/ch01~ch11, prologue, epilogue에서 "…라고 합니다" 정의 문장과 절 앵커를 대조. terms.html과 practice.html의 모든 내부 링크(href, 앵커)가 실제로 존재하고 링크 문구가 해당 절 제목과 일치함을 스크립트로 확인.
