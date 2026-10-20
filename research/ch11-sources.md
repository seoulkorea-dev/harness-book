# Chapter 11 출처 기록

2026-10-20 researcher 조사(11장 개정, PR #44). 이전 11장 관련 기록은 research/ch03-10-sources.md(작가 경험, ch10, ch11 v1.0 보강 확인), research/ch01-sources.md(S2, 작가 경험)에 있음.

11장 개정(PR #44) 조사 결과입니다. 파일은 고치지 않았습니다. 확인일은 모두 2026-10-20입니다. 기존 research/ch11 전용 파일은 없습니다. ch11 관련 기록은 research/ch03-10-sources.md의 "작가 경험" 절(57~60행)과 "ch10, ch11 v1.0 보강 확인" 절(136~141행), research/ch01-sources.md의 S2와 "작가 경험(지난 책)" 절(34~36행), reviews/agents/2026-10-20-ch11-fact-checker.md에 있습니다. 새 항목은 S-C11-1부터 매겼습니다. 저장소 파일은 로컬 작업 트리 기준으로 대조했습니다. git ls-files와 원격 저장소는 확인하지 못했습니다.

## S-C11-1. 이 저장소, .github/workflows/check.yml(book-check)와 verify-site.yml(verify-site), tools/check_all.py, tools/verify_site.py
- URL: 저장소 파일(.github/workflows/check.yml, .github/workflows/verify-site.yml, tools/check_all.py, tools/verify_site.py)
- 게시일: 해당 없음(저장소 파일), 확인일: 2026-10-20
- 작성: 작가와 작성 에이전트
- 이 장에서 사용할 내용
  - **v1.1-backlog 첫 항목 확인 결과: 본문 문장은 부정확하고, 높음 확신으로 확인했습니다.**
    - book-check(check.yml)의 트리거는 `pull_request`(모든 PR)와 `push` 중 `branches: [main]`입니다. 실행 내용은 `python tools/check_all.py --ci` 한 줄입니다.
    - verify-site(verify-site.yml)의 트리거는 `page_build`(GitHub Pages 배포 뒤)와 `workflow_dispatch`(수동)입니다. PR과 push에서는 돌지 않습니다.
    - verify-site는 `tools/verify_site.py https://seoulkorea-dev.github.io/harness-book/`를 최대 5회, 30초 간격으로 실행합니다.
  - 본문 "저장소에 반영하면 GitHub Actions가 같은 검사와 사이트 검증을 다시 실행합니다"는 어긋납니다.
    - 사이트 검증은 반영 때가 아니라 Pages 배포가 끝난 뒤에 따로 돕니다.
    - "같은 검사"는 맞지 않습니다. CI 검사는 로컬 검사에 빌드 결과와 커밋 일치가 더해진 것입니다.
    - "저장소에 반영"의 시점도 나눠야 합니다. PR을 열 때와 main에 병합될 때 book-check가 돕니다. 병합 뒤 배포가 끝나면 verify-site가 돕니다.
  - check_all.py의 검사 항목
    - 요약에 항상 나오는 항목은 빌드, 금칙어, 번호, 구조, 문체, 그림 안 이름입니다.
    - 그림 체계와 그림 글자 크기는 `--strict-figures`일 때만 실패 항목이 됩니다. 기본은 "[경고]" 출력입니다.
    - `--ci`일 때만 "빌드 결과와 커밋 일치"(`git diff --exit-code --stat -- index.html chapters appendix`)가 추가됩니다.
  - **그림 11-1의 "빌드 → lint 4종 → 재빌드 결과 일치 → 작가 승인 뒤 push → CI" 순서와 본문 "같은 원고를 다시 빌드했을 때 결과가 같은지 확인합니다"도 어긋납니다.**
    - "재빌드 결과 일치"는 로컬 check_all에는 없고 CI(`--ci`)에서만 실행됩니다. 방식은 CI가 빌드한 뒤 커밋된 결과물과 diff를 보는 것입니다.
    - check_all.py의 docstring은 "lint 3종"이라고 쓰고 있습니다. 실제 항목은 금칙어(lint/banned.txt와 check_all 안의 정규식 검사), lint/check_numbers.py, lint/check_structure.py, lint/check_style.py입니다. 이 넷을 lint 4종으로 센 것은 맞지만, 금칙어는 별도 스크립트가 아닙니다.
  - 확신: 높음. 표 11-4 2행은 이미 이 사실에 맞게 고쳐져 있습니다(book-check는 PR과 main 반영 때, verify-site는 사이트 배포 뒤).
  - 브랜치 보호의 실제 설정은 저장소 안에서 확인할 수 없습니다. 근거는 HARNESS_SETUP.md 2절의 작가 설정 안내와 RUNBOOK.md 5절의 예시뿐입니다. check.yml 주석은 "브랜치 보호에서 이 검사를 필수로 지정한다"고만 적고 있습니다. GitHub 설정은 확인 불가(미확인).

## S-C11-2. 이 저장소, 훅과 설정(.claude/settings.json, tools/hooks/*.py, tools/hook_lint.py)
- URL: 저장소 파일(.claude/settings.json, tools/hooks/session_start.py, tools/hooks/pre_bash.py, tools/hooks/stop_check.py, tools/hook_lint.py)
- 게시일: 해당 없음, 확인일: 2026-10-20
- 작성: 작가와 작성 에이전트
- 이 장에서 사용할 내용
  - SessionStart 훅(session_start.py)은 현재 브랜치, 지난 세션의 검사 실패, HANDOFF.md(앞 4000자), 최근 결정 10건을 출력합니다.
  - PreToolUse(Bash) 훅(pre_bash.py)은 main에서의 `git commit`, 강제 push, main으로의 push를 종료 코드 2로 막습니다.
  - PostToolUse(Edit|Write|MultiEdit) 훅은 tools/hook_lint.py를 실행합니다(timeout 120초). 내용은 이번에 읽지 않았습니다(미확인, 아래 참고).
  - Stop 훅(stop_check.py)은 저장소에 변경이 있으면 check_all.py를 실행합니다. src/를 바꿨는데 HANDOFF.md가 없으면 종료를 막습니다(종료 코드 2). 같은 멈춤에서 두 번째 호출이면 통과시키고 .claude/last_check_failed.txt에 남깁니다.
    - 따라서 "종료 훅이 실패를 막는다"는 한 번만 막고, 두 번째에는 통과시키고 기록으로 넘기는 장치입니다. 장에서 "강제"라고 쓸 때 이 단서가 필요합니다.
  - settings.json의 allow에는 git add, commit, `git push -u origin`, `git push origin`, gh pr create, gh pr merge, gh pr ready, gh pr edit 등이 있습니다. deny는 `git push origin main`, `--force`, `-f`, examples/**/acceptance/**와 data/**의 Edit와 Write, .env 읽기입니다.
    - **표 11-2와 그림 11-1의 "권한: 저장소 push는 작성 채팅만, 작가 승인을 받은 뒤 실행"은 현재 구성과 다릅니다.** 현재는 작성 에이전트가 작업 브랜치 push와 PR 병합까지 허용 목록으로 수행합니다. 작가 승인은 매번 받지 않습니다. 병합 조건은 editor "병합 가능"(필수 0)과 check_all, CI 통과입니다(D-110, CLAUDE.md, AUTHOR_PREFS.md "작업 방식").
    - 금지(main push, 강제 push)는 설정 deny, PreToolUse 훅, 브랜치 보호(D-101)의 세 겹이라고 HARNESS_SETUP.md 30행에 적혀 있습니다. 브랜치 보호 부분은 GitHub 설정이라 확인하지 못했습니다.
  - 확신: 높음(파일 내용). 브랜치 보호는 낮음.

## S-C11-3. 이 저장소, 구성 요소 개수(.claude/agents, commands, skills, lint, reviews)
- URL: 저장소 파일(.claude/agents/*.md, .claude/commands/*.md, .claude/skills/*/SKILL.md, lint/, reviews/)
- 게시일: 해당 없음, 확인일: 2026-10-20(작업 트리 기준 Glob과 Grep)
- 작성: 작가와 작성 에이전트
- 이 장에서 사용할 내용
  - **에이전트 정의는 8개입니다.** 장 본문, 그림 11-1, 표 11-2의 "에이전트 6개"와 어긋납니다.
    - 8개는 editor, researcher, fact-checker, flow-reviewer, figure-checker, reader-novice, reader-expert, alt-reviewer입니다. 점검 에이전트 7종과 editor 1개를 합친 수입니다.
    - 모델은 모두 sonnet입니다. editor는 도구에 Read, Grep, Glob, Bash가 있고, figure-checker도 Bash가 있습니다.
    - researcher, fact-checker, reader-expert만 WebSearch와 WebFetch가 있습니다.
    - 변경 이력은 D-100(6개: researcher, fact-checker, flow-reviewer, figure-checker, reader-novice, reader-expert), D-107(alt-reviewer 추가), D-110(editor)입니다.
    - D-100은 "하위 에이전트는 6개"라고 적은 채로 두었고, D-107과 D-110은 대체 열이 비어 있습니다. 개수 변경의 대체 관계가 결정 기록에 명시되지 않았습니다.
  - **명령 정의는 7개입니다.** "명령 3개"와 어긋납니다. 7개는 next, autopilot, plan-chapter, write-chapter, review-chapter, apply-review, handoff입니다.
    - CLAUDE.md의 "/next(한 단위), /autopilot(반복)"과 .claude/commands/next.md가 일치합니다.
    - tools/autorun.py는 명령이 아니라 한 단위마다 새 세션(`claude -p "/next"`)을 띄우는 반복 실행 스크립트입니다(HANDOFF.md 자동 반복 실행 절).
  - **Skill은 5개이고 맞습니다.** 5개는 book-structure, fact-check, originality-check, ko-book-style, example-design입니다.
  - lint 4종은 위 S-C11-1과 같습니다. 이 가운데 check_structure.py는 참고 자료 항목과 링크, 앵커 없는 장 링크, 장마다 첫 등장 병기를 검사합니다.
    - 첫 등장 병기 검사 대상은 코드상 `chapters/ch[0-9]*.html`입니다. 파일 주석은 "ch01~ch10"이라고 적혀 있고 D-041도 ch10까지로 적혀 있어, 현재 ch11이 포함되는 것과 문서가 어긋납니다(경미).
    - 그림 11-1의 "구조(참고 자료 링크, 장마다 첫 등장 병기 포함)"는 맞습니다.
  - reviews/ 구조: reviews/*.md(editor 판정과 과거 검수 기록), reviews/agents/(하위 에이전트 보고서와 그림 시안 HTML, v1.1-backlog.md), reviews/flow/(장별 논지 사슬 표 ch01~ch10-flow.md, README.md).
    - 저장 규칙은 보고서가 reviews/agents/YYYY-MM-DD-<장>-<에이전트>.md, editor 판정이 reviews/YYYY-MM-DD-<작업>-editor.md입니다.
    - reviews/flow/ch11-flow.md는 아직 없습니다. 11장 개정 때 생깁니다.
  - 그림 11-1의 "검수 문서: reviews/"는 맞습니다. "규칙 문서, 문체 규칙"에서 규칙 문서는 CLAUDE.md이고 문체 규칙은 STYLE.md입니다. 이 밖에 AUTHOR_PREFS.md, FIGURE_STYLE.md, BOOK_SPEC.md가 있고 templates/(chapter-spec.md, figure-spec.md, issue-report.md)도 있습니다. 두 칸만 적은 것이 현재 규칙 문서 구성을 다 담지는 못합니다.
  - 확신: 높음.

## S-C11-4. 이 저장소, 작업 방식 관련 결정 D-099~D-118과 작업 방식 문서(DECISIONS.md, CLAUDE.md, AUTHOR_PREFS.md)
- URL: 저장소 파일(DECISIONS.md, CLAUDE.md, AUTHOR_PREFS.md, HARNESS_SETUP.md, templates/)
- 게시일: DECISIONS.md 표기 2026-10-19~2026-10-20, 확인일: 2026-10-20
- 작성: 작가(결정), 작성 에이전트(기록)
- 이 장에서 사용할 내용
  - **현재 작업 방식(D-110, CLAUDE.md, AUTHOR_PREFS.md)**
    - 구성원은 작가, 작성 에이전트(VS Code의 Claude Code), 정식 검수 하위 에이전트 editor, 점검 하위 에이전트 7종, 감독 대화 Neo(Claude App)입니다.
    - Neo는 진행 감시, 역할 준수 확인, 작가 보고, 작가 요청을 GitHub 이슈(라벨 request)로 등록하는 일만 합니다. 원고를 고치거나 커밋하지 않습니다.
    - D-110은 "PR #6, #7은 Neo가 직접 반영한 예외"라고 적고 있습니다. HANDOFF.md 진행 기록의 editor 결론 열도 이 두 건은 "(Neo 검수)"입니다.
    - 원고 쓰기는 한 번에 한 주체입니다(CLAUDE.md, F-06). 하위 에이전트는 읽기만 하고 보고 문안을 메인 세션에 돌려줍니다.
    - 병합 조건은 editor "병합 가능"(필수 0), check_all, CI 통과입니다.
    - **D-101("main 반영은 PR과 CI 통과 뒤 작가 병합으로만")과 D-110·CLAUDE.md("editor 병합 가능과 CI 통과면 작성 에이전트가 병합")는 병합 주체가 다릅니다.** D-110은 D-101을 대체한다고 적지 않았습니다. 장에서 병합 주체를 쓸 때 이 점을 고려해야 하며, 작가 확인이 필요합니다.
  - **D-099(2026-10-19)**: 원고 작업은 VS Code의 Claude Code에서만 하고, 검수 Project(Claude App)는 읽기와 검수 문서 작성만 합니다. 이것이 11장의 "작성 채팅, 검수 채팅"에 대응하는 옛 구조입니다. D-110이 이를 작성 에이전트와 editor로 바꿨지만 D-099와의 대체 관계는 적혀 있지 않습니다(대체 열 비어 있음).
  - **D-106(그림 문구와 화살표)**: 그림 1-1에 하네스 → 모델 "입력과 컨텍스트"를 먼저, 모델 → 하네스 "응답 또는 도구 호출"을 다음에 두는 화살표를 둡니다. 그림 1-2는 2차원 흐름으로 바꿉니다. 그림 안 문구는 개조체이고 요약은 상자 없이 "*" 한 줄입니다. 외부 검토 의견 중 관계 화살표, 결론 줄, 2차원 흐름만 채택했습니다.
  - **D-107(명세 먼저, 시안 두 개, alt-reviewer)**: 장은 templates/chapter-spec.md, 그림은 templates/figure-spec.md로 명세를 먼저 씁니다. 그림은 배치가 다른 시안 두 개를 만들고, 작가가 고릅니다(이후 CLAUDE.md는 editor와 alt-reviewer 의견으로 고르고 이유를 AUTHOR_QUEUE에 적는다고 변경). alt-reviewer를 더하고, 외부 AI 검토는 장이 끝날 때 한 번 제안으로만 받습니다.
    - 근거 기록은 F-16입니다. 그림 1-1, 1-2를 2026-10-16~20 사이에 같은 그림을 열 번 넘게 다시 그렸습니다. 원인 구성 요소는 "역할"이고, 장치는 명세 먼저, 시안 두 개, alt-reviewer입니다.
    - D-107의 "작가가 고른다"와 D-110 이후 CLAUDE.md의 "editor와 alt-reviewer 의견으로 고르고 이유를 AUTHOR_QUEUE에 적는다"는 다릅니다. 변경이 결정 기록에 명시되어 있지 않습니다. 장에서 쓰려면 현재 규칙(CLAUDE.md, next.md)을 따르는 것이 안전합니다.
  - **D-108**: 본문과 표의 주체는 제품명을 기본으로 합니다. 시작하며에 표기 원칙을 둡니다. 11장의 Lopopolo 문장 "Codex도 ... 밝혔습니다"도 이 기준과 관련됩니다(아래 S-C11-6).
  - **D-109**: 2장 개정(표 2-1, 표 2-4 신설, 그림 2-1 시안 A, 2-2 시안 A 채택). 11장에서 직접 쓸 필요는 없고 "시안 두 개와 선택" 실행 사례입니다.
  - **D-110**: 위 첫 항목. 작성과 검수 분리의 현재 형태입니다. 11장의 "작성 채팅, 검수 채팅" 표현은 현재 구성과 어긋나므로 바꿔야 합니다.
  - **D-111~D-116(그림 방침 연쇄)**: 모두 2026-10-20입니다.
    - D-111: 1장 기준 일관성, 비용 규칙.
    - D-112: 진행 상태 공개(아래).
    - D-113: 이슈 보고 형식.
    - D-114: 그림 안 "예제:" 표기.
    - D-115: 원리 그림과 예제 그림.
    - D-116: 그림은 모두 일반 내용으로, D-115 예외 삭제, D-114 폐지.
    - F-17의 근거인 반복 변경 사례입니다. 11장의 "큰 결정의 반복 변경"과 같은 종류입니다.
    - D-116(예외 없이 일반 내용)과 D-114, D-115는 서로를 대체하는 관계가 DECISIONS.md 대체 열에 번호로 적혀 있습니다. 이 책의 "결정 기록에 대체 관계 기록" 장치가 실제로 작동한 예입니다.
  - **D-112(초안 PR 진행 공개, 작가 요청 이슈 #13, Neo 등록)**
    - 작업을 정하면 바로 작업 브랜치와 초안 PR(`gh pr create --draft`)을 엽니다.
    - PR 설명의 체크 목록(명세, 그림 시안과 선택, 원고, check_all, 점검 에이전트, editor 검수, CI, 병합)을 단계마다 `gh pr edit`로 갱신합니다.
    - 멈추면 PR 설명 맨 위에 "멈춤: 이유"를 적습니다.
    - editor "병합 가능"과 CI 통과 뒤 `gh pr ready`로 초안을 해제하고 병합합니다.
    - 실제 규칙은 .claude/commands/next.md 3-0절과 3-1절에 있습니다. 설정 allow에 gh pr edit, gh pr ready가 있습니다(settings.json 확인).
    - 11장 개정 PR #44의 번호와 실제 열림 여부는 로컬 저장소에서 확인하지 못했습니다(미확인). HANDOFF.md는 브랜치 ch11-write를 적고 있습니다.
  - **D-113**: 이슈 보고 형식입니다(templates/issue-report.md). 작업 시작 댓글에 대상 chapter와 초안 PR 번호, 결과 댓글에 진행 완료 chapter 표와 수정 내용을 적습니다.
  - **D-117(흐름과 이해도가 첫째 필수 기준)**
    - 근거 실패는 F-18입니다. 흐름과 독자 이해도를 책임지는 점검이 없어, 4장 "요청의 네 요소" 절이 "병합 가능"으로 통과했습니다(4장 PR #20, 이슈 #31).
    - 장치는 AUTHOR_PREFS 맨 위 기준 셋, editor와 flow-reviewer의 장 전체 통독, reviews/flow/<장>-flow.md 논지 사슬 표(끊기면 필수), reader-novice 상시 호출(sonnet)입니다.
    - 1~5장 재점검은 PR #35~#39로 완료되었고, 6~10장은 개정 PR #30, #40~#43에서 적용되었습니다. 11장이 마지막 적용 대상입니다.
    - 장 개정 PR에서 논지 사슬이 끊긴 곳은 1장 3건, 2장 2건, 3장 2건, 4장 2건, 5장 3건, 6장 1건, 7장 4건, 8장 2건, 9장 3건, 10장 4건이 0건으로 해소되었다고 HANDOFF.md에 적혀 있습니다.
  - **D-118**: 3장 reader-novice 반영 방침입니다. 앞 장 정의는 다시 정의하지 않고 한 줄 상기와 링크를 쓰고, 사실 표현 기준을 둡니다. 11장도 앞 장 정의를 다시 쓰지 않는 기준의 적용 대상입니다.
  - 근거 한계: D-110, D-112, D-117의 "이슈 #13, #31" 번호와 "PR 번호"는 DECISIONS.md와 HANDOFF.md의 기록입니다. GitHub의 이슈와 PR 원문은 이번에 열지 않았습니다(미확인).

## S-C11-5. 이 저장소, FAILURES.md와 HANDOFF.md의 실패 사례 번호와 날짜
- URL: 저장소 파일(FAILURES.md, HANDOFF.md)
- 게시일: 해당 없음, 확인일: 2026-10-20
- 작성: 작성 에이전트
- 이 장에서 사용할 내용
  - FAILURES.md는 F-01~F-19 19건입니다. 11장 표 11-4 4행("두 번째로 나온 실패마다 원인 구성 요소와 추가한 장치가 적혀 있음")과 형식이 일치합니다.
    - 열은 ID, 실패, 반복, 원인 구성 요소, 추가한 장치, 상태입니다.
    - 상태는 "장치 추가", "규칙", "진행 중", "해소" 네 종류입니다.
  - 사례로 쓸 수 있는 행과 사실
    - F-01(검수 지침 일부만 반영, 검증): check_review(반영 n / n), PR과 CI 필수. tools/check_review.py 존재 확인.
    - F-02(검수 문서 설명문이 원고에 섞임, 역할): 지침은 "교체" 코드 상자만 옮김(/apply-review). 11장 표 11-1 3행과 연결됩니다.
    - F-06(원고를 여러 곳에서 고침, 역할): 원고를 쓰는 주체는 하나. 11장 "작성 채팅"과 "검수 채팅" 구분의 현재 형태입니다.
    - F-07(세션을 바꾸며 미커밋 변경과 맥락 소실, 기록, 2026-10-15): HANDOFF.md와 종료 훅의 인계 확인.
    - F-13(2026-10-19 작동 시험): Windows 경로 처리 결함으로 구조 검사가 항상 실패하고, 오류 출력 때문에 종료 훅의 차단이 무력화되었습니다. 검증이 검증을 못 한 사례입니다.
    - F-14(2026-10-20 v1.0 작업 세션): 훅 명령이 상대 경로라서 셸이 하위 폴더로 이동하자 모든 Bash 명령이 막혔습니다. 도구 구성 요소의 실패입니다.
    - F-16(그림을 열 번 넘게 다시 그림, 2026-10-16~20, 역할): 명세 먼저, 시안 두 개, alt-reviewer(D-107). 3절 D-107 사례와 같습니다.
    - F-17(원리 그림에 예제 사실을 섞음, 2026-10-20, 이슈 #18, #21, #25, 검증): D-114, D-115, D-116으로 이어졌습니다.
    - F-18(흐름 검수 부재, 2026-10-20, 이슈 #31, 검증): D-117. 4장 PR #20이 병합 가능으로 통과한 것이 계기입니다.
    - F-19(.claude/ 쓰기 권한이 없는 세션에 반영 작업이 배정되어 네 번 멈춤, 2026-10-20, PR #32, #33): 작가가 쓰기를 허용한 대화형 세션에서 반영해 "해소"로 표시되었습니다. 표 11-4 4행의 "원인 구성 요소와 추가한 장치" 확인에 쓸 수 있는 도구와 권한 사례입니다.
  - F-09(그림 글자 크기, 8개, 검증)는 "진행 중"입니다. 11장 개정 때 그림 11-1 글자 크기를 고치는 일이 이 상태와 연결됩니다. HANDOFF.md는 "그림 글자 크기 기준 미달 그림 8개(2-2, 4-2, 5-2, 6-2, 7-2, 8-2, 9-2, 11-1)"라고 적고 있고, 11-1이 마지막 남은 장 쪽 개정 대상입니다. 이 목록은 HANDOFF.md 기록 기준이며 check_all 출력은 이번에 실행하지 않았습니다.
  - **표 11-4 4행과 FAILURES.md의 어긋남**: 이 책 저장소 FAILURES.md에는 "같은 실패가 두 번째 나오면 한 행을 추가"한다고 적혀 있습니다. 그러나 F-13, F-14, F-17, F-18, F-19처럼 첫 발생 기록인 행이 있습니다. 두 번째 반복 여부는 행마다 "반복" 열에 서술형으로만 적혀 있어 기계적으로 확인할 수 없습니다. 표 11-4 4행은 fact-checker가 이미 권장으로 지적한 사항입니다.
  - 확신: 높음.

## S-C11-6. OpenAI(Ryan Lopopolo), Harness engineering: leveraging Codex in an agent-first world (재확인 실패)
- URL: https://openai.com/index/harness-engineering/
- 게시일: 2026-02-11(research/ch01-sources.md S2의 기록, 이번 검색 결과 요약에서도 같은 날짜와 저자 표기 확인), 확인일: 2026-10-20
- 작성: Ryan Lopopolo
- 확인 수준: **원문 열람 실패. 2차 단서만 있고 1차 확인이 아닙니다.**
  - WebFetch는 openai.com, www.openai.com 모두 이름 해석 실패(ENOTFOUND)로 열리지 않았습니다. 앞선 7, 8, 5장 기록(research/ch05, ch07, ch08-sources.md)의 열람 실패와 같은 상태입니다.
  - 웹 검색 결과 요약으로 확인한 것은 제목, 저자(Ryan Lopopolo), 게시일 2026-02-11, 글 머리의 "5개월, 직접 작성한 코드 0줄"뿐입니다. 요약에는 11장이 쓰는 "어떤 능력이 누락되었는가를 묻고, 그 능력을 읽을 수 있고 강제되는 형태로 추가" 문장이 나오지 않았습니다.
  - 검색에서 확인한 요약 내용은 InfoQ, ZenML, yage.ai 등 2차 글이 대부분입니다. 이 책은 ZenML 등 2차 요약 사이트를 수치가 다르다는 이유로 쓰지 않기로 했습니다(research/ch01-sources.md S2 비고).
  - 이 장에서 쓸 수 있는 내용(research/ch01-sources.md S2 기록, 2026-10-04 열람 내용을 그대로 인용)
    - 11장 표 11-1 뒤 문장 "Codex도 에이전트가 실패하면 어떤 능력이 누락되었는지를 묻고, 그 능력을 에이전트가 읽을 수 있고 강제되는 형태로 추가했다고 밝혔습니다"는 ch01-sources.md S2 28행의 요약과 일치합니다. 이번 재확인은 되지 않았습니다.
    - 이 문장 하나만 11장이 외부 출처에서 가져온 사실입니다.
  - 표기 문제(D-108 기준, 이미 research/ch08-sources.md S-C8-8과 research/ch05-sources.md가 같은 지적)
    - 원문 저자는 OpenAI의 Ryan Lopopolo이고 Codex는 글의 주제 제품입니다.
    - 11장 본문의 "Codex도 ... 밝혔습니다"는 주체가 제품입니다. D-108의 시작하며 표기 원칙 "Codex와 Claude Code는 각 제품과 함께, OpenAI와 Anthropic이 그 제품에 관해 발표한 엔지니어링 글의 내용도 가리킨다"에 따라 허용될 수는 있습니다. 다만 원문 확인이 안 된 문장이라 "OpenAI는 ... 글에서"로 바꿀지 작가 확인이 필요합니다.
  - 참고 자료 형식 점검: 11장 참고 자료는 "Lopopolo, R. (2026년 2월 11일). Harness engineering: leveraging Codex in an agent-first world. OpenAI" 한 건입니다. 링크(URL)가 없습니다. 다른 장 항목과 형식이 같은지는 이번에 비교하지 않았습니다.
  - 이번 조사에서는 11장에 다른 외부 인용이 없는 것을 본문 전체를 읽어 확인했습니다. 장의 외부 출처는 Lopopolo 한 건뿐입니다.
  - 확신: 낮음(원문 미확인).

## S-C11-7. 이 저장소, NEW_BOOK_PLAYBOOK.md 0장과 DECISIONS.md D-005(지난 책 73차 검수와 다섯 실패)
- URL: 저장소 파일(NEW_BOOK_PLAYBOOK.md 0장, research/ch01-sources.md "작가 경험(지난 책)", research/ch03-10-sources.md "작가 경험")
- 게시일: 파일 표기 "기준: seoulkorea-dev/ai-book 저장소(2026-10-04, 검수 누적 73차)", 확인일: 2026-10-20
- 작성: 작가와 작성 에이전트(지난 책 저장소 ai-book)
- 이 장에서 사용할 내용
  - 11장 "73차례 검수"는 플레이북 3행과 5행의 "73차례 검수", "검수 누적 73차"와 일치합니다. 근거는 플레이북 한 문서뿐이고, 지난 책 저장소(ai-book)의 검수 기록 73건은 이 저장소에 없어 직접 대조하지 못했습니다.
  - 다섯 실패와 플레이북 0장 표(5행)의 대응 확인
    - 큰 결정의 반복 변경(플레이북 1행): "첫 문단 틀 세 번 변경"이 같은 행에 있습니다. 장치도 같습니다(집필 전 설계 확정, 결정 기록에 대체 관계).
    - 문장 추가 때의 연결 단절(2행): "26건"이 있습니다. 장치는 플레이북에는 "'○○ 문장 뒤' 위치 지정, 추가 전 같은 내용 검색"입니다. 11장 표 11-1의 "이웃 문장 중복 검사"는 이 저장소의 lint/check_style.py(단어 겹침 65% 이상, 2026-10-03 60차 규칙)에 있습니다.
    - 검수 문서의 혼입(3행): 장치는 "코드 상자에만" 담기와 반영 확인 검사입니다. 11장의 "작성과 검수의 분리"는 플레이북 3행이 아니라 D-005와 F-02, F-06에서 옵니다.
    - 설명 없는 링크(4행): 장치는 "그 장에서 먼저 설명, 절 앵커로 링크"입니다. lint/check_structure.py 49행이 앵커 없는 장 링크를 검사합니다.
    - 사람이 찾는 반복 실수(5행): 어휘, 조사, 표 번호, 가운뎃점은 lint/banned.txt, check_numbers.py(번호 뒤 조사), check_style.py가 대응합니다. 가운뎃점은 AUTHOR_PREFS.md "쉼표를 쓴다"로 남아 있습니다.
  - 장에서 "사람이 찾던 실수를 lint가 대신 찾는다"고 쓴 문장은 플레이북 0장 5행과 일치합니다.
  - **본문 "작가는 결정과 승인을 맡고, 원고 작성과 검수는 에이전트가 맡았습니다"**는 지난 책의 역할 분리입니다. 이 책 현재 구성(D-110)과는 구별해서 써야 합니다.
  - 확신: 중간. 지난 책의 73차 검수와 26건 수치의 원 기록은 이 저장소에 없습니다.

## 장의 주장에 대한 근거 부족과 불일치 목록

### 사실 불일치(저장소와 대조, 높음)
1. 본문 "저장소에 반영하면 GitHub Actions가 같은 검사와 사이트 검증을 다시 실행합니다"는 두 워크플로의 트리거가 달라 부정확합니다(S-C11-1). book-check는 PR과 main push, verify-site는 Pages 배포 뒤(page_build)와 수동 실행입니다.
2. 그림 11-1과 표 11-2의 "에이전트 6개"는 현재 8개이고, "명령 3개"는 현재 7개입니다(S-C11-3). "Skill 5개"는 맞습니다.
3. 그림 11-1과 표 11-2의 "작성 채팅, 검수 채팅" 구분과 "검수 문서 작성(저장소에 반영 안 함)"은 D-099의 옛 구조입니다. 현재는 작성 에이전트(Claude Code), editor, 점검 에이전트 7종, 감독 대화 Neo입니다(D-110, CLAUDE.md).
   - editor의 판정 결과(reviews/YYYY-MM-DD-<작업>-editor.md)와 하위 에이전트 보고서(reviews/agents/)는 모두 저장소에 저장됩니다. 그림의 "저장소에 반영 안 함"은 현재와 반대입니다.
4. 그림 11-1과 표 11-2의 "권한: 저장소 push는 작성 채팅만, 작가 승인을 받은 뒤 실행"은 현재 구성과 다릅니다.
   - 작성 에이전트가 작업 브랜치 push, PR, 병합까지 허용 목록으로 수행합니다.
   - 병합 조건은 editor "병합 가능"과 check_all, CI 통과입니다.
   - 작가는 매 push마다 승인하지 않습니다.
   - D-101의 "작가 병합"과 D-110 이후 규칙의 차이가 결정 기록에 대체로 명시되지 않았습니다.
5. 그림 11-1과 본문의 검증 흐름 "빌드 → lint 4종 → 재빌드 결과 일치 → 작가 승인 뒤 push → CI"는 현재 순서와 다릅니다.
   - 현재는 /next가 작업 브랜치를 만들고 초안 PR을 열고, check_all과 editor를 거쳐 CI를 기다린 뒤 병합합니다.
   - "재빌드 결과 일치"는 로컬이 아니라 CI(`--ci`)의 검사입니다.
6. 표 11-2 "역할: 작가, 작성 채팅, 검수 채팅이 결정, 반영, 검토를 나눠 맡음"은 현재 역할 분담과 다릅니다(위 3번).
7. 본문 "작성 채팅은 원고 수정, 빌드, 검사, 커밋을 맡습니다"와 그림의 "작성 채팅: 원고 수정, 빌드, 검사, 승인 뒤 push"는 현재 구성에서 작성 에이전트의 일 중 일부만 설명합니다. 현재는 명세, 시안, 점검 에이전트 호출, PR 생성, 병합, HANDOFF 갱신까지 맡습니다.
8. "lint 4종" 중 금칙어는 별도 lint 스크립트가 아니라 check_all.py 안의 검사입니다(S-C11-1). 4종이라는 표현은 유지할 수 있으나, 파일 수로 센 "lint 3종"(check_all.py docstring)과 어긋납니다.

### 결정 기록의 정합성(작가 확인 필요)
9. D-100("하위 에이전트는 6개"), D-101("작가 병합"), D-107("작가가 시안을 고른다")과 D-110 이후 규칙(editor, CI로 병합, editor와 alt-reviewer 의견으로 시안 선택) 사이에 대체 관계가 명시되어 있지 않습니다. 11장에서 "결정 기록에 대체 관계를 남긴다"는 장치를 사례로 쓰는데, 이 저장소의 해당 행들이 그 기준을 지키지 않은 것이 됩니다.
10. 표 11-4 3행의 확인 기준("변경한 결정에 대체한 결정의 번호와 이유가 있음")은 DECISIONS.md 전체에서 지켜지지 않습니다. D-100, D-107, D-110, D-111 등은 대체 열이 비어 있거나 문장입니다(fact-checker 보고에서도 지적).
11. F-12("저장소 구성은 git ls-files 기준")에 따라 장의 저장소 구성 문장은 git ls-files로 다시 확인해야 합니다. 이번 대조는 작업 트리 Glob 기준이며, 100개 한도를 넘는 목록은 파일 종류별 Glob과 Grep을 따로 해서 보완했습니다.

### 근거 부족
12. 11장 핵심 주장("완성도는 실패를 어디로 옮겼는가로 정해진다")에 대한 외부 근거는 Lopopolo 문장 한 건이고, 그 원문은 열지 못했습니다(S-C11-6). 나머지는 모두 작가 자신의 기록입니다. 일반화한 주장으로 쓰려면 근거가 한 사례(두 권의 책)입니다.
13. "73차례 검수", "26건", "첫 문단 틀 세 번 변경"은 플레이북에만 있고 지난 책 저장소의 원 기록을 이 저장소에서 확인할 수 없습니다. 작가 진술로 표시하거나 작가 확인이 필요합니다.
14. 이 장이 쓰려는 "작성과 검수 분리의 효과", "자동 검사로 사람 검수가 판단 항목에 집중됨"은 효과를 측정한 자료가 없습니다. 저장소에는 docs/metrics.md가 있으나 이번에 읽지 않았습니다(미확인). 효과 문장은 "~로 옮겼다"는 사실 서술까지만 쓸 수 있습니다.
15. 이 책 작업 방식(D-106~D-118)이 실패를 줄였는지의 증거(예: D-117 이후 논지 사슬 끊김 수의 변화)는 HANDOFF.md에 장별 "끊김 N → 0" 형태로 있습니다. 그러나 같은 장에서 개정 전후를 비교한 것이고, 다른 장끼리 비교하거나 인과를 주장할 수는 없습니다.
16. F-16, F-17, F-18은 같은 날(2026-10-20) 사이에 이어진 실패입니다. "반복된 실패를 구성 요소로 옮겼다"의 사례로는 쓸 수 있으나, 옮긴 장치가 다음 실패를 막았는지는 아직 시간이 짧아 확인되지 않았습니다(F-16 장치 이후 그림 재작업 횟수는 기록 없음).

### 미확인
- GitHub 브랜치 보호 설정, 이슈 #13, #31 등과 PR #44의 GitHub 원문(저장소 파일에만 의존). 찾아본 곳: RUNBOOK.md, HARNESS_SETUP.md, check.yml 주석.
- tools/hook_lint.py(PostToolUse 훅)와 tools/check_review.py의 내용(이번에 읽지 않음). 11장은 이 둘을 직접 다루지 않습니다.
- Lopopolo 원문(S-C11-6). 찾아본 곳: openai.com, www.openai.com(이름 해석 실패), 웹 검색 요약.
- check_all.py의 현재 실행 결과(요약 출력). 이번 조사에서는 실행하지 않았습니다.
- docs/metrics.md(작업 효과 수치가 있는지).
- .claude/ 아래 에이전트 정의 8개의 본문 전체(이름, 설명, 도구, 모델 줄만 확인).

## S-C11-8. 이 저장소, 11장 개정 원고 대조(fact-checker, PR #44)
- URL: 저장소 파일(.claude/agents/*.md, .claude/settings.json, tools/hooks/pre_bash.py, tools/hooks/stop_check.py, tools/check_all.py, .github/workflows/check.yml, verify-site.yml, lint/check_style.py, lint/check_structure.py, FAILURES.md, DECISIONS.md D-001, D-005, D-099~D-118, NEW_BOOK_PLAYBOOK.md 0장, docs/metrics.md)
- 확인일: 2026-10-20(작업 트리 기준)
- 사용한 내용: 에이전트 8개, 명령 7개, Skill 5개, 훅 4종, 설정의 금지 규칙(main으로의 push, 강제 옵션), pre_bash 훅(main 커밋, 강제 push, main push 차단), book-check(pull_request, push main, 검사 스크립트의 CI 옵션), verify-site(page_build, workflow_dispatch). editor와 figure-checker의 도구에는 Bash가 있고 Edit, Write는 없음(Bash 제한은 정의 본문 지시). F-08(2026-10-15~18, 원인 기록)과 F-17(2026-10-20, 원인 검증, D-114~D-116)은 다른 실패. D-110, D-100, D-107, D-108의 변경은 대체 열이 비어 있고 D-115, D-116은 대체 번호가 있음. docs/metrics.md는 값이 없어 "검수가 판단 항목에 집중됨"의 근거가 되지 않음. Lopopolo 원문은 열지 못함(S2 기록과 일치만)
- 확신: 높음(파일 내용), 낮음(Lopopolo, 브랜치 보호, 지난 책 원 기록)
