# Chapter 11 fact-checker 점검(2026-10-20, PR #44, 개정 원고)

ch11 사실 확인 보고 (src/chapters/ch11.html, 브랜치 ch11-write, PR #44). 확인일 2026-10-20. 파일은 고치지 않았습니다. 이 세션에는 Bash가 없어 check_all.py를 실행하지 못했고 git log도 보지 못했습니다. 코드 읽기와 .git/logs/HEAD 일부 열람만 했습니다.

| # | 심각도 | 발견 | 위치 | 근거 | 제안 | 확신 |
|---|---|---|---|---|---|---|
| 1 | 필수 | 표 11-3 5행과 본문(그림 방침 재작업 예)이 서로 다른 두 실패를 한 줄로 섞었습니다. 근거 "F-08, D-114 → D-115 → D-116"에서 F-08은 2026-10-15~18의 그림 방침 변경(원인 기록, 장치 FIGURE_STYLE.md와 대체 관계)입니다. D-114~D-116은 모두 2026-10-20이고 F-17(원리 그림에 예제 사실을 섞음)의 연쇄이며, F-17의 원인 구성 요소는 기록이 아니라 검증입니다. 본문은 "며칠 사이", "원인 구성 요소를 기록으로 판단", "D-116이 D-114와 D-115를 대체"를 한 사건처럼 이어 씁니다. | 표 11-3 5행, "그림 방침의 재작업을 예로 들면" 문단 | FAILURES.md F-08, F-17 행. DECISIONS.md D-114~D-116 행 | 둘 중 하나로 맞춥니다. (a) F-08만 쓰고 근거를 "F-08"로 하며 D-114~D-116 문장을 빼거나, (b) 예를 F-17로 바꿔 원인 구성 요소를 검증, 장치를 그림 명세의 "예제 사실 없음" 확인 줄과 editor와 figure-checker의 필수 점검, D-115, D-116으로 고칩니다. 본문 끝의 "큰 결정의 반복 변경이 다시 나왔고 같은 기록 장치로 막은 것"도 (b)에서는 어긋나므로 함께 고칩니다. D-116이 D-114와 D-115를 대체한다는 문장 자체는 DECISIONS 대체 열("D-115(예외 삭제), D-114(폐지)")과 일치합니다. | 높음 |
| 2 | 필수 | 표 11-5 4행의 확인 기준 "결정을 변경한 행에 대체한 결정의 번호가 있음"은 저장소에서 지켜지지 않습니다. D-110은 D-099, D-101의 병합 주체와 구조를 바꿨는데 대체 열이 비어 있습니다. D-100의 "6개"(현재 8개)와 D-107의 "작가가 시안을 고른다"(현재 CLAUDE.md는 editor와 alt-reviewer 의견)도 대체 열이 비어 있습니다. D-108은 본문에 "D-088을 바꿈"이 있으나 대체 열은 비어 있습니다. 대체 번호가 있는 것은 D-115와 D-116 등 일부뿐입니다. 표 11-3 5행의 "결정마다 대체 관계 기록"도 같은 사정입니다. | 표 11-5 4행, 표 11-3 5행 | DECISIONS.md D-099~D-110, D-114~D-116 대체 열 | 기준을 "결정을 대체할 때 대체 열에 번호를 적는다(예: D-116)"로 쓰고, 현재 저장소에는 비어 있는 행이 있음을 한 문장으로 밝힙니다. 아니면 D-110 등의 대체 열을 작가 확인 뒤 채웁니다(작가 확인 사항). | 높음 |
| 3 | 필수 | 점검 에이전트가 "읽기와 판정만"이고 "정의에 파일 수정 도구가 없다"는 문장이 editor와 figure-checker에는 단서가 필요합니다. 8개 정의에 Edit, Write는 없습니다(맞음). 그러나 editor는 tools에 Bash가 있고(Read, Grep, Glob, Bash), figure-checker도 Bash가 있습니다. 두 정의의 Bash 제한은 도구 설정이 아니라 본문 지시("읽기 명령과 check_all 실행에만 쓴다")입니다. 나머지 6개(researcher, fact-checker, flow-reviewer, reader-novice, reader-expert, alt-reviewer)는 Read, Grep, Glob 중심이고 researcher, fact-checker, reader-expert만 WebSearch와 WebFetch가 있습니다. | 표 11-2 권한 행, 그림 11-1 권한 묶음과 점검 에이전트 카드, 본문 "권한은 점검 에이전트가 원고를 수정할 수 없게" | .claude/agents/*.md 머리말 tools 줄, editor.md와 figure-checker.md 첫 문단 | "파일 수정 도구(Edit, Write)가 없고, Bash가 있는 editor와 figure-checker는 정의 본문이 읽기와 검사 실행만 하도록 지시함"처럼 지시와 강제를 구분해 씁니다. 그림 안 문구는 "쓰기 도구 없음"을 "편집 도구 없음"으로 바꾸는 방안이 있습니다. | 높음 |
| 4 | 필수 | 본문 "같은 종류의 실수를 찾는 검수가 73차례 동안 반복되었습니다"는 근거 범위를 넘습니다. 73차는 검수 누적 횟수이고, 반복 실수는 다섯 실패 중 하나입니다. 플레이북에는 검수마다 같은 실수를 찾았다는 기록이 없습니다. | "장치는 코드가 없어도 시작할 수 있습니다" 문단 | NEW_BOOK_PLAYBOOK.md 3행과 5행("73차례 검수", "검수 누적 73차"), 0장 표 5행 | "검수를 73차례 거치는 동안 같은 종류의 실수를 사람이 매번 찾았다고 작가는 정리했습니다(작가의 검수 기록 기준)"처럼 주체와 범위를 좁히거나, 근거가 되는 검수 기록을 지정합니다. | 높음 |
| 5 | 필수 | "그 결과 사람의 검수는 판단이 필요한 항목에 집중되었습니다"는 결과 주장인데 측정 근거가 없습니다. 플레이북 0장 5행은 "사람은 판단이 필요한 것만 봅니다"라는 원칙이고 결과 기록이 아닙니다. docs/metrics.md는 표 머리글만 있고 값이 없습니다. | 표 11-1 아래 문단 | NEW_BOOK_PLAYBOOK.md 0장 5행, docs/metrics.md | "집중하도록 했습니다(원칙)"처럼 의도 서술로 바꾸거나 삭제합니다. | 높음 |
| 6 | 권장 | 지난 책 수치(73차례, 26건, 세 번)의 근거 표시가 첫 문단 1곳뿐입니다. 요약 불릿, 54행의 "73차례", 표 11-1과 목록의 "세 번", "26건"에는 주체 표시가 없습니다. 값은 플레이북 0장(3행, 5행, 14행, 15행)과 FAILURES F-04("26건")와 일치합니다. 지난 책 저장소(ai-book)의 원 검수 기록은 이 저장소에 없어 직접 대조하지 못했습니다. | 요약 첫 불릿, "지난 책에서 반복된 실패" 절 목록 | 플레이북, FAILURES.md F-04 | 값은 일치로 판정하되, 첫 문단의 "(작가의 검수 기록 기준)"을 수치가 나오는 목록 항목에도 이어 쓰고, 원 기록은 research/ch11-sources.md S-C11-7에 "작가 진술, 원 기록 미보유"로 남깁니다. 지난 책 원 기록은 참고(미확인)입니다. | 중간 |
| 7 | 권장 | 감독 대화 설명 "원고는 수정하지 않음"에는 예외가 있습니다. D-110이 PR #6, #7은 Neo가 직접 반영한 예외로 적고 있습니다. 현재 규칙(CLAUDE.md)은 원고를 고치지 않는 것이 맞습니다. | 표 11-2 역할 행, 그림 11-1 감독 카드 | DECISIONS.md D-110, CLAUDE.md 표 | 현재 구성 기준이므로 본문은 유지해도 됩니다. 사실 서술을 엄밀하게 하려면 "현재 규칙은 원고를 수정하지 않음"으로 씁니다. | 중간 |
| 8 | 권장 | "훅은 ... 검사를 추가합니다"는 4종 중 SessionStart에는 맞지 않습니다. SessionStart 훅은 현재 브랜치, 지난 검사 실패, HANDOFF.md 앞부분, 최근 결정 10건을 보여 주는 것이고 검사가 아닙니다(research S-C11-2, 이번에 session_start.py 본문은 다시 열지 않았고 settings.json 등록만 확인). 훅 네 종류(SessionStart, PreToolUse Bash, PostToolUse Edit/Write/MultiEdit, Stop)는 settings.json과 일치합니다. | "도구는 에이전트, 명령, 절차를 파일로 정의해" 문단 | .claude/settings.json hooks 절 | "세션 시작과 종료, 도구 실행 전후에 정보 제공과 검사를 추가합니다"로 고칩니다. Stop 훅은 같은 멈춤의 두 번째 호출에서는 통과시키는 한계가 있으나(stop_check.py), 본문이 "강제"라고 쓰지 않아 지금은 문제 없습니다. | 중간 |
| 9 | 권장 | 표 11-3의 "기본 브랜치 직접 반영 금지(설정, 훅)"과 표 11-2 권한 행은 일치합니다. 다만 설정 deny는 `git push origin main`, `--force`, `-f`뿐이고, main에서의 `git commit` 금지와 `git push -u origin main` 같은 변형 차단은 PreToolUse 훅(pre_bash.py)이 맡습니다. FAILURES F-03과 D-101은 브랜치 보호도 세 번째 장치로 적지만 GitHub 설정이라 확인하지 못했습니다(미확인, 본문은 브랜치 보호를 주장하지 않아 문제 없음). | 표 11-2 권한 행, 표 11-3 4행 | settings.json permissions.deny, tools/hooks/pre_bash.py | 본문 유지. 브랜치 보호는 쓰지 않는 현재 서술을 유지합니다. | 높음 |
| 10 | 권장 | 표 11-3 3행 "설치한 에이전트와 훅을 사용하지 않음"은 F-05 원문 "장치(에이전트, 훅, Skill)를 설치만 하고 쓰지 않음"에서 Skill이 빠졌습니다. 장치(작동 시험, 세션 시작 훅)와 근거 번호는 일치합니다. | 표 11-3 3행 | FAILURES.md F-05 | "설치한 장치(에이전트, 훅, Skill)를 사용하지 않음"으로 맞추거나 현 표현을 유지합니다. | 중간 |
| 11 | 참고 | Lopopolo(2026) 인용 문장("실패하면 어떤 능력이 누락되었는지를 묻고, 그 능력을 에이전트가 읽을 수 있고 강제되는 형태로 추가")은 원문을 열지 못했습니다(openai.com 이름 해석 실패 ENOTFOUND). research/ch01-sources.md S2 28행의 기록과는 일치합니다. 발표 주체는 "OpenAI의 글"로 문장에 밝혀져 있고 ref-lopopolo-2026 링크와 참고 자료 항목(저자, 2026년 2월 11일, 제목, OpenAI)이 있습니다. 게시일 2026-02-11과 저자는 S2와 같습니다. | "표 11-1은 지난 책의 실패별 ..." 앞 문장, 참고 자료 | research/ch01-sources.md S2(2026-10-04 열람), docs/AUTHOR_QUEUE.md Q-030 | 판정 미확인(기록과 일치). 확인한 범위는 S2 기록, 이번 WebFetch 시도, S-C11-6입니다. Q-030의 작가 직접 재확인에 이어 둡니다. | 낮음 |
| 12 | 참고 | "2026년 10월 4일 저장소를 처음부터 다시 만들고": D-001(2026-10-04)이 "설계 인터뷰부터 새로 시작, 기존 원고는 태그 v0-before-reset에 보존"을 기록하므로 날짜와 설계 인터뷰는 일치합니다. 다만 "저장소를 새로 만든" 것인지 같은 저장소를 되돌린 것인지는 D-001에 명시가 없습니다. 이 저장소의 첫 커밋 날짜는 git log를 못 봐서 확인하지 못했습니다(.git/logs/HEAD에는 2026-10-20 작업만 보임). "처음부터 두었다"는 설계서, 결정 기록, 분리, lint, CI는 D-001, D-005와 research/ch03-10-sources.md 58행(초기 기록의 GitHub Actions book-check, verify-site)과 맞습니다. 훅과 Stop 훅은 D-102(2026-10-19)라서 이 목록에 없는 것이 맞습니다. | "이 책은 2026년 10월 4일 ..." 문장 | DECISIONS.md D-001, D-005, D-102 | 일치(중간). "다시 만들고"를 "처음부터 다시 시작하고"로 바꾸는 방안이 D-001 표현에 더 가깝습니다. git log로 첫 커밋 확인을 권합니다. | 중간 |
| 13 | 참고 | lint/check_structure.py 48행의 앵커 없는 장 링크 검사 정규식이 `ch0\d|epilogue`라서 ch10, ch11 링크는 이 검사 대상이 아닙니다. 표 11-1 4행은 지난 책 장치 서술이고 이 장의 링크는 모두 앵커가 있어 본문 오류는 아닙니다. | 표 11-1 4행(참고용) | lint/check_structure.py 48행 | 본문 무관. 표 11-5의 확인 방법에서 "앵커 검사"를 이 책의 현재 보장으로 쓰지 않는 한 변경 불필요합니다. | 중간 |

## 일치로 판정한 사실 문장(근거 위치)
- 에이전트 정의 8개: editor, researcher, fact-checker, flow-reviewer, figure-checker, reader-novice, reader-expert, alt-reviewer. 모두 model sonnet. .claude/agents 8개 파일 확인.
- 명령 7개: next, autopilot, plan-chapter, write-chapter, review-chapter, apply-review, handoff. .claude/commands 확인.
- Skill 5개: book-structure, fact-check, originality-check, ko-book-style, example-design. .claude/skills 확인.
- 훅 네 종류(SessionStart, PreToolUse(Bash), PostToolUse(Edit|Write|MultiEdit), Stop): settings.json.
- 기본 브랜치 직접 반영 금지(설정의 deny, 훅): settings.json deny와 pre_bash.py.
- 병합 조건(editor "병합 가능"(필수 0), check_all, CI 통과): D-110, CLAUDE.md.
- 검사 요약 항목 이름(빌드, 금칙어, 번호, 구조, 문체, 그림 안 이름): check_all.py 출력부. 그림 체계와 글자 크기는 --strict-figures일 때만 항목이 되어 표에 없는 것이 맞습니다. "검사 요약", "통과", "실패" 표시도 check_all.py 92~94행과 일치합니다.
- 제출 때 검사: check.yml은 pull_request와 push(main)에서 `check_all.py --ci`를 실행하고, --ci일 때만 "빌드 결과와 커밋 일치"(git diff --exit-code)가 더해집니다. 표 11-2, 표 11-5와 일치합니다.
- 배포 뒤 확인: verify-site.yml은 page_build와 workflow_dispatch에서 실행하고 최대 5회, 30초 간격입니다. 표 11-2, 표 11-5와 일치합니다.
- 표 11-3 1행(F-06, D-099, D-110), 2행(F-16, D-107; 현재 선택 주체는 CLAUDE.md 기준 editor와 alt-reviewer 의견), 4행(F-03), 6행(F-18, D-117)의 실패, 원인 구성 요소, 장치, 근거 번호가 FAILURES와 DECISIONS와 일치합니다. 3행은 F-05와 장치가 일치하고 Skill 누락만 위 #10입니다. 5행은 위 #1입니다.
- 표 11-3의 "다섯 구성 요소가 모두 나옵니다": 역할, 도구, 권한, 기록, 검증 모두 있음.
- 표 11-5: 1행(FAILURES.md 각 행에 원인 구성 요소와 장치 있음, F-19 장치 칸은 제안과 해소 서술 형태), 2행(원인 구성 요소 열의 값이 다섯 가운데 하나), 3행(검사 요약과 CI 이름), 4행의 D-116 예시는 참입니다. 4행의 일반 기준만 위 #2입니다.
- 실패 기록 "두 번째 기준 + 위험한 실패는 첫 발생도"와 "첫 발생으로 남긴 행이 있음": FAILURES.md 3행 규칙, F-13, F-14, F-17, F-18, F-19가 첫 발생 기록입니다.
- 지난 책 다섯 실패 목록과 표 11-1의 장치(집필 전 설계 확정, "○○ 문장 뒤", 코드 상자, 절 앵커, lint 자동화): 플레이북 0장 표와 일치. 이웃 문장 중복 검사는 lint/check_style.py 74~96행(단어 겹침 65% 이상), 앵커 검사는 check_structure.py 48~49행에 있습니다.

## research/ch11-sources.md에 추가할 기록 문안
## S-C11-8. 이 저장소, 11장 개정 원고 대조(editor, settings, 훅, 워크플로, FAILURES, DECISIONS)
- URL: 저장소 파일(.claude/agents/*.md, .claude/settings.json, tools/hooks/pre_bash.py, tools/hooks/stop_check.py, tools/check_all.py, .github/workflows/check.yml, verify-site.yml, lint/check_style.py, lint/check_structure.py, FAILURES.md, DECISIONS.md D-001, D-005, D-099~D-118, NEW_BOOK_PLAYBOOK.md 0장, docs/metrics.md)
- 게시일: 해당 없음, 확인일: 2026-10-20(작업 트리 기준, Bash 없이 파일 열람, check_all 실행과 git log는 못 함)
- 작성: 작가와 작성 에이전트(fact-checker 대조)
- 이 장에서 사용할 내용
  - 에이전트 8개, 명령 7개, Skill 5개, 훅 4종, deny 규칙(git push origin main, --force, -f), pre_bash 훅(main 커밋, 강제 push, main push 차단), book-check(pull_request, push main, --ci), verify-site(page_build, workflow_dispatch)가 원고와 일치합니다.
  - editor와 figure-checker의 tools에는 Bash가 있고 Edit, Write는 없습니다. Bash 제한은 정의 본문 지시입니다.
  - F-08(2026-10-15~18, 원인 기록)과 F-17(2026-10-20, 원인 검증, D-114~D-116)은 다른 실패입니다.
  - D-110, D-100, D-107, D-108의 변경은 대체 열이 비어 있습니다. D-115와 D-116은 대체 번호가 있습니다.
  - docs/metrics.md는 표 머리글만 있고 값이 없어 "검수가 판단 항목에 집중됨"의 근거가 되지 않습니다.
  - Lopopolo 원문은 openai.com 이름 해석 실패로 열지 못해 research/ch01-sources.md S2 기록과의 일치만 확인했습니다(미확인).
- 확신: 높음(파일 내용), 낮음(Lopopolo, 브랜치 보호, 지난 책 원 기록)

필수 5, 권장 5, 참고 3, 확인한 사실 문장 약 45개

## 처리(2026-10-20, 메인 세션)
| # | 처리 | 내용 |
|---|---|---|
| 1 | 반영 | 표 11-3 5행 근거를 F-08로, 풀어 쓴 예는 F-08(그림 방침, 원인 기록, 그림 규칙 문서와 대체 관계)로 쓰고 D-116은 "그 뒤 그림 방침을 다시 변경한 결정"의 결과로 한정 |
| 2 | 반영 | 표 11-5 결정 기록 행 "결정을 대체할 때 대체 열에 번호를 적음(예: D-116). 이 책 저장소에도 대체 열이 비어 있는 이전 행이 있어 보완하고 있음", Q-061 |
| 3 | 반영 | 표 11-2 권한 행에 편집 도구 없음과 셸 도구가 있는 두 에이전트의 지시 구분, 그림 "편집 도구 없음" |
| 4 | 반영 | "같은 종류의 실수를 사람이 매번 찾는 일이 검수에서 반복되었다고 작가는 정리했습니다" |
| 5 | 반영 | "작가는 이렇게 해서 사람의 검수가 판단이 필요한 항목에 집중하도록 했습니다"(의도) |
| 6 | 반영 | failures 첫 문단 "수치는 모두 작가의 검수 기록 기준", Q-064 |
| 7 | 반영 | "현재 규칙에서는 원고를 수정하지 않음" |
| 8 | 반영 | "정보 제공과 검사를 추가하는 훅" |
| 9 | 유지 | |
| 10 | 반영 | "설치한 장치(에이전트, 훅, Skill)" |
| 11 | 보류 | Q-030 |
| 12 | 반영 | "집필을 처음부터 다시 시작하고" |
| 13 | 해당 없음 | |
- 기록 문안 S-C11-8은 research/ch11-sources.md에 추가
