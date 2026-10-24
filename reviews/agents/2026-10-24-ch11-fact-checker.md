# 11장 사실 점검(fact-checker)

# ch11 fact-checker 보고 (2026-10-24, 원고와 파일은 고치지 않음)

요약: 필수 4, 권고 4, 참고 4. 사실 문장 약 46개를 확인했습니다. 그중 일치가 약 34개이고, 나머지는 아래 표에 정리했습니다.

실행 확인
- `python tools/check_all.py`의 검사 요약은 빌드, 금칙어, 번호, 구조, 문체, 그림 안 이름, 검수 규칙이 모두 "통과"입니다.
- `python tools/check_all.py --ci`는 위 일곱 항목에 "빌드 결과와 커밋 일치"가 더해져 모두 "통과"입니다.
- ch11은 `lint/rules_applied.txt`에 없어서 R1 단정 표현 후보 3곳이 경고입니다. 실패는 아닙니다.
- 이 실행으로 표 11-5의 확인 기준("검사 요약의 모든 항목이 통과")은 성립합니다.

## 불일치와 보완 목록

| 번호 | 위치(절, 문장 첫머리) | 원문 | 확인 결과와 출처(확인일 2026-10-24) | 고친 문안 | 등급 |
|---|---|---|---|---|---|
| 1 | 표 11-2 권한 칸 "점검 에이전트의 정의에…" | "검사를 실행하는 두 에이전트는 셸 도구가 있어" | 불일치. `.claude/agents/*.md` frontmatter에서 `tools`에 Bash가 있는 것은 editor, fact-checker, practice-checker, production-checker 네 개입니다. Edit, Write, MultiEdit가 있는 정의는 없고, chief-editor, flow-reviewer, reader-novice, researcher에는 Bash가 없습니다. editor, practice-checker, production-checker 본문은 Bash 사용을 읽기 명령과 검사 실행으로 한정합니다. fact-checker 본문도 Bash를 읽기와 실행 확인에만 쓰라고 합니다. | "검사를 실행하는 네 에이전트(editor, fact-checker, practice-checker, production-checker)는 셸 도구가 있어, 정의 본문이 읽기와 검사 실행만 지시" | 필수 |
| 2 | 표 11-2 역할 칸 "점검 에이전트 8개(하위 에이전트, 정식 검수를 맡는 editor 포함)" | 같음 | 개수 8은 일치합니다(`.claude/agents/`에 8개 파일). 그러나 구성이 "점검 에이전트 8개"와 다릅니다. 8개는 chief-editor(편집장), editor, fact-checker, flow-reviewer, practice-checker, production-checker, reader-novice, researcher입니다. researcher는 장을 쓰기 전 조사 담당이고(researcher.md description), chief-editor는 본문에 이름이 없습니다. CLAUDE.md는 편집 검토를 chief-editor가 장마다 1회 한다고 적습니다. | "하위 에이전트 8개(편집장 chief-editor, 정식 검수 editor, 점검 fact-checker, flow-reviewer, practice-checker, production-checker, reader-novice, 조사 researcher)". "하위 에이전트"는 장 첫 등장에 앞 장처럼 병기(Subagent, 특정 작업을 맡도록 따로 정의한 에이전트)를 붙입니다. | 필수 |
| 3 | 표 11-2 검증 칸 "점검 판정(editor의 '병합 가능')", 그 아래 문단 "지금은 PR을 병합하려면 점검 판정과 자동 검사, 제출 때 검사를 모두 통과해야 합니다." | 같음 | 낡음. "병합 가능" 필수 0을 병합 조건으로 두는 것은 D-110(2026-10-20)입니다. 현재 규칙은 다릅니다. `.claude/commands/next.md` 23행은 check_all과 CI가 통과하면 병합하고, 편집장의 필수가 남아도 작가 검수 목록에 적었으면 병합한다고 합니다. DECISIONS.md D-139도 반영하지 못한 필수는 병합하고 PR과 AUTHOR_QUEUE에 적는다고 합니다. CLAUDE.md는 편집 검토 주체를 chief-editor로 적는데, D-139는 editor로 적습니다. 두 문서의 편집 검토 주체가 어긋나 있어 작가 확인이 필요합니다. 그림 11-1의 "점검 판정" 단계는 일반 이름이라 영향이 적습니다. | "병합 조건은 자동 검사와 제출 때 검사의 통과이고, 편집 검토(editor, 편집장)의 필수는 반영하거나 작가 검수 목록에 적은 뒤 병합합니다". 또는 버전 주석(2026년 10월)으로 D-110 이후의 변경을 덧붙입니다. 작가 확인 필요: AUTHOR_QUEUE에 질문 등록. | 필수 |
| 4 | 작업 중 더한 장치 마지막 문단 "그림 방침의 재작업을 예로 들어…(1)~(4)" | "그림의 글자 크기와 색, 예제를 그림에 담을지에 대한 방침이 며칠 사이에 여러 번 변경", "그 뒤 D-116은 D-114와 D-115를 대체", "지난 책의 첫 실패인 …을 … 보강해 막은 것" | 불일치(인과 연결). FAILURES.md의 F-08은 2026-10-15~18의 그림 방침 변경(원인 기록, 장치 FIGURE_STYLE.md와 결정마다 대체 관계)입니다. "예제를 그림에 담을지"와 D-114, D-115, D-116은 F-17(2026-10-20, 원인 검증)의 연쇄입니다. D-116의 대체 열은 "D-115(예외 삭제), D-114(폐지)"로 일치합니다. 다만 D-114, D-115, D-116이 F-08 장치가 생긴 뒤 같은 날 안에 잇따라 바뀌었으므로, F-08 장치가 반복을 "막았다"는 근거는 없습니다. research/ch11-sources.md 16번도 효과는 미확인이라고 적습니다. | (1)~(4)를 F-08(글자 크기, 색 방침, FIGURE_STYLE.md)로 한정하고 D-116은 "F-17에서 같은 종류의 방침 변경이 다시 나왔을 때 D-116이 D-114, D-115를 대체한다고 적어 현재 방침이 하나로 남았다"로 분리합니다. 마지막 "막은 것"은 "기록 장치로 보강한 것"으로 바꿉니다. | 필수 |
| 5 | 표 11-2 검증 칸 "자동 검사(빌드, 금칙어, 번호, 구조, 문체, 그림 안 이름)" | 같음 | 부분 불일치. 실행 출력의 검사 요약은 일곱 항목이고, 마지막이 "검수 규칙"입니다(`lint/check_rules.py`, `tools/check_all.py` 88~90행). 표 11-5가 "검사 요약의 모든 항목"을 기준으로 삼으므로 목록이 빠지면 독자가 출력과 맞춰 볼 때 한 줄이 남습니다. | "자동 검사(빌드, 금칙어, 번호, 구조, 문체, 그림 안 이름, 검수 규칙)" | 권고 |
| 6 | 같은 문단 (2) "결정 기록은 있었지만 그림 방침이 여러 결정에 흩어져 있어, 어느 것이 현재 유효한지 알 수 없었습니다" | 같음 | 근거 없음. FAILURES.md F-08은 "그림 방침이 여러 번 바뀌어 재작업"만 적고 원인 서술이 없습니다. 흩어진 결정 번호(D-096, D-097, D-098은 있음)와 "유효한 것을 알 수 없었다"는 작가 진술이므로 근거 표기가 필요합니다. | "작가의 판단으로는 …" 형태로 주체를 밝히거나, F-08 행에 원인 설명을 한 줄 더하는 문안을 research에 남깁니다. | 권고 |
| 7 | 지난 책 문단들 "73차례 검수", "26건", "첫 문단의 틀은 세 번 변경" | "수치는 모두 작가의 검수 기록 기준입니다" | "작가 기록 기준" 표기는 있습니다(8행). 그러나 research/ch11-sources.md S-C11-7이 근거로 든 NEW_BOOK_PLAYBOOK.md 0장 표에는 현재 73차, 26건, 세 번이 없습니다(grep 결과 0건. git log -S 결과로 보면 ca4dd0c에서 들어가 a21e7b1의 플레이북 개편에서 빠진 것으로 보입니다). 현재 이 저장소 안에서 확인되는 것은 research/ch03-10-sources.md 57행과 research/ch01-sources.md 36행의 기록, FAILURES.md F-04의 "생성형 AI 책 26건", ch01.html 170행의 같은 표기입니다. 지난 책 저장소(ai-book)의 원 검수 기록은 열 수 없습니다. | 본문 유지. research의 근거를 현재 파일 기준으로 갱신합니다(아래 기록 블록). | 권고 |
| 8 | 표 11-2 도구·역할 칸 "훅 네 종류", 표 11-3 직전 "훅(Hook)"과 "하위 에이전트" | 같음 | 개수와 종류는 일치합니다(아래 일치 목록). 표기만 문제입니다. 다른 장은 "하위 에이전트(Subagent, …)"로 병기하는데 ch11은 표 11-2에서 병기 없이 씁니다. "훅"도 표 11-2에서 먼저 쓰고 "훅(Hook)"은 그 뒤 문단(33행)에서 병기합니다. | 첫 등장 위치(표 11-2 앞의 본문)에서 병기합니다. | 권고 |
| 9 | 매핑 절 첫 문단 "Codex의 하네스 엔지니어링 글도 … 묻고, … 읽을 수 있고 강제되는 형태로 추가했다고 밝힙니다" | 같음 | 미확인(1차). openai.com은 WebFetch에서 `getaddrinfo ENOTFOUND`로 열리지 않았습니다(2026-10-24 재시도, 10-20과 같음). 웹 검색에서는 2차 글에만 영어 문구 "what capability is missing, and how do we make it both legible and enforceable for the agent?"가 나왔고, 원문 페이지는 결과에 없었습니다. research/ch01-sources.md S2(2026-10-04 열람 기록)와 본문 문장은 일치합니다. bibliography.json의 harness-engineering 항목(Ryan Lopopolo, 2026.2.11, OpenAI, URL)도 research와 같습니다. 주어는 D-108의 "각 제품과 함께 그 제품에 관해 발표한 엔지니어링 글" 기준으로 허용됩니다. | 본문 유지. 가능하면 "OpenAI의 Lopopolo는 글에서"로 발표 주체를 밝힙니다(권장, 작가 확인). | 참고 |
| 10 | 표 11-1 문장 추가 행 "이웃 문장 중복 검사" | 같음 | 존재는 확인됩니다(`lint/check_style.py` 74~96행, 같은 절 안 단어 겹침 65% 이상 문장 쌍). 단, 이 검사는 "경고"로 집계하며 check_all의 실패 항목이 아닙니다. 본문의 "자동 검사가 확인합니다"는 경고 수준임을 밝히지 않습니다. | 본문 유지. 필요하면 "경고로 알려 줍니다". | 참고 |
| 11 | 이번 책 저장소 첫 문단 "처음부터 두었습니다(설계서, 결정 기록, 작성과 검수의 분리, lint, 지속적 통합)" | 같음 | 부분 미확인. D-001(2026-10-04)이 "지난 책의 플레이북과 자동화를 처음부터 적용"이라고 적습니다. 그러나 이 저장소의 git 이력은 2026-10-16부터 시작해(`git log --reverse`) check.yml, lint/check_style.py의 최초 추가가 10-16으로 나옵니다. 10-04 시점의 존재는 이력으로 확인할 수 없습니다. 작성과 검수 분리의 저장소 규칙은 D-099(2026-10-19)입니다. | 본문 유지. 찾은 범위는 D-001, git 이력, D-099입니다. | 참고 |
| 12 | 지난 책 정의 문장 "검수 한 차례는 원고 전체를 검토하고 …", 다섯 실패의 세부(쪽 맨 위로만 이동 등) | 같음 | 미확인. 작가가 정한 정의와 작가 진술로 저장소에서 대조할 기록이 없습니다. 본문의 "작가는 … 정리했습니다"로 주체가 밝혀져 있어 형식은 충족합니다. | 본문 유지. | 참고 |

## 일치로 판정한 사실(근거)
- 에이전트 정의 8개, 명령 정의 7개(apply-review, autopilot, handoff, next, plan-chapter, review-chapter, write-chapter), Skill 5개(book-structure, example-design, fact-check, ko-book-style, originality-check): `.claude/` 디렉터리 목록.
- 훅 네 종류와 시점: `.claude/settings.json`에 SessionStart, PreToolUse(Bash), PostToolUse(Edit|Write|MultiEdit, hook_lint.py), Stop(stop_check.py)이 있고, 파일은 `tools/hooks/session_start.py`, `pre_bash.py`, `stop_check.py`와 `tools/hook_lint.py`입니다. 본문 "세션 시작과 종료, 도구 실행 전후"와 일치합니다.
- 기본 브랜치 직접 반영 차단: settings.json deny에 `git push origin main`, `--force`, `-f`가 있습니다. `pre_bash.py`는 main에서의 커밋, 강제 push, main으로의 push(`HEAD:main` 형태 포함)를 종료 코드 2로 막습니다. 점검 에이전트에 편집 도구가 없다는 것도 일치합니다.
- book-check: `.github/workflows/check.yml`의 `name: book-check`, 트리거는 `pull_request`와 `push` 중 main, 실행은 `python tools/check_all.py --ci`입니다. verify-site: `verify-site.yml`의 `name: verify-site`, 트리거는 `page_build`와 `workflow_dispatch`입니다. 표 11-2의 "PR과 main 반영 때"와 "배포된 사이트 검사"가 일치합니다.
- 기록 구성 요소: CLAUDE.md, DECISIONS.md, FAILURES.md, HANDOFF.md, reviews/가 저장소에 있습니다.
- 설계 인터뷰와 재시작: D-001(2026-10-04, "설계 인터뷰부터 새로 시작", 기존 원고는 태그 v0-before-reset에 보존), D-007(집필 목적), D-008(범위), D-014(목차 가안), D-017(문체 기준)이 있습니다.
- 표 11-3의 F 번호와 D 번호: F-06(D-099, D-110), F-16(D-107, 그림 1-1, 1-2, 열 번 넘게, 2026-10-16~20), F-05(작동 시험, 세션 시작 훅), F-03(main 반영 금지: 설정, 훅), F-08(FIGURE_STYLE.md, 결정마다 대체 관계), F-18(D-117, 논지 사슬 표, 흐름 첫째 기준)이 FAILURES.md, DECISIONS.md의 행과 맞습니다. 행 내용도 대응합니다(D-107의 시안 선택 주체는 "작가", 이후 CLAUDE.md와 next.md는 의견을 받아 고르는 방식으로 바뀌었는데, 본문은 "점검 에이전트 의견과 함께 고름"이라고만 써서 모순은 없습니다).
- 표 11-5: FAILURES.md의 열은 ID, 실패, 반복, 원인 구성 요소, 추가한 장치, 상태이고, 원인 구성 요소 열은 19행 모두 다섯 구성 요소 중 하나입니다. "D-116은 D-114와 D-115를 대체"와 "대체 열이 비어 있는 이전 행"(D-099, D-100, D-101, D-107, D-110 등)도 일치합니다.
- 장의 "FAILURES.md는 같은 종류가 두 번째일 때 표시하고 위험이 큰 실패는 첫 발생도 올림"은 FAILURES.md 머리 문장과 F-13~F-19의 단발 행으로 확인됩니다.
- 앞 장 표기: 지속적 통합(Continuous Integration, CI)은 ch01, ch07과 같은 형태입니다. 독립 검수의 정의(만들지 않은 에이전트나 사람의 검토)는 ch07과 같고, 결정 기록의 대체 관계는 ch08 링크와 같은 뜻입니다.
- 참고: 브랜치 보호(D-101, F-03 "브랜치 보호")는 GitHub 설정이라 저장소에서 확인할 수 없습니다(본문은 이를 주장하지 않아 문제 없음).

## research/ch11-sources.md에 덧붙일 기록 블록

```
## 2026-10-24 fact-checker 재확인
확인일: 2026-10-24. 저장소 파일은 작업 트리 기준. 원고와 파일은 고치지 않았다.

### S-C11-9. 이 저장소, ch11 최종 원고 대조(플레이북 정리, 이슈 #119)
- URL: 저장소 파일(.claude/agents/*.md, .claude/commands/*.md, .claude/skills/, .claude/settings.json, tools/hooks/pre_bash.py, tools/check_all.py, lint/check_style.py, .github/workflows/check.yml, verify-site.yml, FAILURES.md, DECISIONS.md D-001, D-099, D-107, D-110, D-114~D-117, D-129, D-139, CLAUDE.md, .claude/commands/next.md 23행)
- 작성: 작성 에이전트(저장소), 확인: fact-checker
- 사용한 내용
  - 에이전트 정의 8개: chief-editor, editor, fact-checker, flow-reviewer, practice-checker, production-checker, reader-novice, researcher. Bash가 있는 것은 editor, fact-checker, practice-checker, production-checker 네 개이고 Edit, Write가 있는 정의는 없다. (표 11-2 "검사를 실행하는 두 에이전트"는 네 개로 정정 대상)
  - 명령 7개, Skill 5개, 훅 4종(SessionStart, PreToolUse Bash, PostToolUse Edit|Write|MultiEdit, Stop)은 본문과 일치.
  - settings.json deny: git push origin main, --force, -f. pre_bash 훅: main 커밋, 강제 push, main 대상 push를 종료 코드 2로 차단.
  - python tools/check_all.py 실행 출력(검사 요약): 통과 빌드 / 금칙어 / 번호 / 구조 / 문체 / 그림 안 이름 / 검수 규칙. --ci는 여기에 "빌드 결과와 커밋 일치" 추가, 모두 통과. ch11은 rules_applied.txt에 없어 R1 후보 3곳이 경고.
  - 병합 규칙 현재형: next.md 23행(check_all과 CI 통과면 병합, 편집장 필수가 남아도 작가 검수 목록에 적으면 병합), D-139(반영하지 못한 필수는 병합). D-110의 "editor 병합 가능이 병합 조건"은 낡음. 편집 검토 주체는 CLAUDE.md(chief-editor)와 D-139(editor)가 다름 -> 작가 확인.
  - F-08(2026-10-15~18, 기록)과 F-17(2026-10-20, 검증, D-114~D-116)은 다른 실패. D-116 대체 열 = "D-115(예외 삭제), D-114(폐지)". F-08 원인 서술(결정이 흩어져 유효한 것을 알 수 없었다)은 FAILURES.md에 없음(작가 진술).
  - 지난 책 수치: 현재 NEW_BOOK_PLAYBOOK.md에는 73차, 26건, 세 번이 없다(S-C11-7의 플레이북 0장 표 근거는 낡음, 이력상 ca4dd0c에서 추가되어 a21e7b1 개편에서 빠진 것으로 보임). 현재 확인 가능한 기록: research/ch03-10-sources.md 57행, research/ch01-sources.md 36행, FAILURES.md F-04("생성형 AI 책 26건"), ch01.html 170행. 지난 책 저장소(ai-book)의 원 기록은 열람 불가. 본문은 "작가의 검수 기록 기준"으로 표기함.
  - git 이력은 2026-10-16부터 시작. 10-04 시점의 장치 존재는 D-001로만 확인(이력으로 미확인).
- 확신: 높음(파일 내용, 실행 출력), 낮음(지난 책 원 기록, 브랜치 보호, 10-04 시점 장치)

### S-C11-6 재확인(OpenAI, Lopopolo, Harness engineering)
- URL: https://openai.com/index/harness-engineering/
- 확인일: 2026-10-24. WebFetch는 getaddrinfo ENOTFOUND로 실패(10-20과 같음). 웹 검색(standard)에서 원문 페이지는 나오지 않고, 2차 글(codenote.net, latent.space, InfoQ 등)에서만 "what capability is missing, and how do we make it both legible and enforceable for the agent?" 문구가 보임. 2차 출처이므로 판정 근거로 쓰지 않는다.
- 판정: 미확인(1차). research/ch01-sources.md S2(2026-10-04 열람 기록)와 본문 문장은 일치. bibliography.json harness-engineering 항목(Ryan Lopopolo, 2026.2.11, OpenAI)과 research가 일치.
- 찾은 범위: openai.com, 웹 검색 결과 요약
```

필수 4, 권고 4, 참고 4, 확인한 사실 문장 약 46개
