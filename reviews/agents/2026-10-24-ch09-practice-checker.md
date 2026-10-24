# 9장 실습 점검(practice-checker)

# 9장 예제·실패·확인 표와 실습 3 감수 (실습 감수자, 이슈 #66 0단계)

**요약: 필수 3, 권고 5, 참고 4** (원고·실습 파일은 고치지 않았고, 임시 복사본에서만 실행했습니다.)

설정 사실(표 9-4)은 일치합니다. 필수는 모두 표 9-6 쪽에서 나왔습니다. 표 9-6 앞 문장에 확인 시점이 없고, 확인 요청 행이 구현 전에도 통과하며, 샌드박스 행은 Windows에서 실행할 수 없는데 안내가 없습니다.

| 번호 | 위치 | 원문 | 확인 결과(실행한 명령과 출력) | 고친 문안 | 등급 |
|---|---|---|---|---|---|
| 1 | ch09 `#check` 첫 문단(77행), 표 9-6 | "요청은 Claude Code 입력창에, 명령은 ... 실습 폴더(expense-practice)에서 실행합니다. ... 실습 3에 있습니다." | 플레이북 확인 표 규칙은 확인 표 앞 문장에 확인 시점을 쓰라고 합니다(8장 `#check`는 "실습 5를 마치고 실습 6의 1단계에서 ..."로 씁니다). 9장은 시점이 없습니다. 실습 파일로 대조하면 /permissions와 금지 동작 행(PRJ-2604, 파일 삭제, push)은 실습 3 3~4단계 뒤에 확인합니다(practice.html 68~73행). 확인 요청 행은 lab-3-check 73행이 "commit 확인 요청은 실습 5에서 만납니다"라고 하므로 실습 5입니다. 샌드박스, 지출 한도, 사용량 행은 어느 실습에도 없습니다. | 앞 문장에 추가: "처음 두 행은 실습 3의 4단계를 마친 뒤, 확인 요청 행은 실습 5에서 commit 확인 화면이 나올 때 확인합니다. 샌드박스, 지출 한도, 사용량 행은 실습 단계에 없으므로 필요할 때 따로 확인합니다." 또는 이 세 행을 실습 3 선택 단계로 옮깁니다(작가 결정 사항). | 필수 |
| 2 | 표 9-6 "확인 요청" 행 | 방법: "변경을 commit해 달라는 요청" / 기준: "실행 전에 승인하거나 거절하는 확인 화면이 뜸" | 구현 전에 실패하는지 판정되지 않습니다(플레이북 3.5, 591행). 이 책이 설명하는 기본(default) 권한 모드에서는 allow에 없는 Bash 명령(git commit 포함)이 ask 규칙이 없어도 확인 화면을 띄웁니다. 그래서 ask 규칙이 없는 구현 전에도 같은 화면이 떠서 규칙의 효과를 증명하지 못합니다. 이 판정은 문서 근거로 한 것이고 Claude Code 화면은 실행하지 못했습니다. 반면 금지 동작 행은 규칙이 없으면 거부 메시지 대신 수정 확인 화면이 뜨므로 구현 전 실패가 성립합니다. | 둘 중 하나를 택합니다. (a) 기준을 "화면에 git commit 규칙(ask)이 확인 이유로 표시되고, /permissions의 확인 요청에 Bash(git commit *)가 있음"으로 바꿉니다. 단, 화면 문구는 실행 확인 전에는 단정하지 않습니다. (b) 표에 "이 행은 확인 화면이 뜨는지만 보며, 규칙의 유무는 /permissions 행이 확인한다"고 적습니다. | 필수(확신 중간, 실행 못 함) |
| 3 | 표 9-6 "샌드박스" 행, 77행, 버전 주석(28행) | "touch ~/sandbox-probe", "macOS는 Operation not permitted, Linux와 WSL2는 Read-only file system" | Windows 안내가 확인 표에 없습니다. 28행은 네이티브 Windows가 샌드박스를 지원하지 않는다고 하지만, 확인 표와 실습에는 이 행을 Windows에서 건너뛰라는 말이 없습니다. Git Bash에서는 touch와 ~가 되지만 샌드박스가 없어 성공만 하고, 그러면 "성공하면 만든 파일을 삭제" 분기만 타서 확인 기준이 의미를 잃습니다. PowerShell에는 touch가 없고 ~ 경로도 다르게 해석됩니다. 이 책 방식(부록은 Git Bash 기준, PowerShell은 따로 표기)과 맞지 않습니다. | 행 끝에 추가: "네이티브 Windows(Git Bash, PowerShell)는 샌드박스를 지원하지 않으므로 이 행을 건너뛰거나 WSL2에서 확인합니다. PowerShell에는 touch가 없습니다." | 필수 |
| 4 | 표 9-6 "샌드박스" 행, 오류 문구 | Operation not permitted / Read-only file system | 실행 못 함. 샌드박스를 켤 수 있는 Claude Code 대화형 화면이 필요하고, 홈 폴더에 파일을 만드는 명령이라 감수 범위 밖입니다. 문구는 OS별 오류 메시지로, 버전 주석(2026년 10월)과 확인일이 필요합니다. | 실행 확인 뒤 확정. 확인일을 행이나 주석에 붙입니다. | 참고(검증 후 확정) |
| 5 | 표 9-4 전체 | 표 9-4의 6개 행과 56행 "python3 형식의 허용 규칙도 있으며 표에서는 생략했습니다" | `python3 -c`로 reference/settings.example.json을 파싱한 결과, ask는 `['Bash(git commit *)']`, deny는 9개, allow는 6개(python 2개, python3 2개, git status, git diff *)입니다. 표와 일치합니다. 허용은 단위 테스트, check.py, git status, git diff, 확인 요청은 commit, 금지는 push, data/, acceptance/, check.py, CLAUDE.md, DECISIONS.md, .claude/, WebFetch, WebSearch로 모두 맞습니다. 예제 사실(docs/example-facts.md 32~36행)과 ch03(80행)·ch02 표 2-5와도 일치하며, 표에 규칙 문자열은 없고 이유는 ch02와 모순되지 않습니다. python3를 "생략"한다는 설명은 ch03 목록(python3 없음)과 파일(있음)의 차이를 제대로 알립니다. | 변경 없음 | 참고 |
| 6 | 표 9-5 2행 | "샌드박스를 켜서 네트워크 접근을 운영 체제 수준에서 제한(허용 도메인에 저장소 주소를 포함하지 않음)" | 두 가지가 걸립니다. (1) "허용 도메인"이 9장에서 정의되지 않고 10장 85행에만 "샌드박스의 허용 도메인 목록(추가 설정)"으로 나옵니다. 예제 설정에는 그 설정이 없는데 9장 표는 설정이 이미 있는 것처럼 읽힙니다. (2) 목록 밖 도메인은 접근 확인 요청이 올 수 있어, 승인하면 막히지 않는다는 점이 없습니다(10장 85행은 "목록 밖은 확인 요청(default 모드)"). 또 실습 폴더는 `git remote -v`가 비어 있어(복사본에서 확인) 이 행은 실습으로 재현할 수 없습니다. | "샌드박스를 켜서 ... 제한(샌드박스의 허용 도메인 목록에 저장소 주소를 넣지 않고, 새 도메인 접근 확인이 오면 거절. 예제 설정에는 없는 추가 설정, <a href="ch10.html#permissions">Chapter 10</a>)" | 권고 |
| 7 | ch09 65행 "git -C . push 같은 다른 형태의 명령이 막히지 않음", 표 9-5 1행 | "금지 규칙은 문자열이 일치하는 명령만 막고, git -C . push ..." | 설명은 ch03 77행과 같고 규칙 문자열 `Bash(git push *)`와 맞습니다. `git -C . push`는 "git push"로 시작하지 않아 일치하지 않습니다. 전체 문자열 대조는 Claude Code 없이 단정할 수 없어 문서 근거로만 확인했고, 실행으로는 못 했습니다. 표 9-5 1행의 방지 장치 `Edit(./data/**)`는 설정과 일치합니다. | 변경 없음 | 참고 |
| 8 | 표 9-6 "금지 동작" 행 기준 | "git status 출력에 data/projects.csv가 나타나지 않음" | 임시 복사본(경로 `.../scratchpad/ep/expense-practice`)에서 `git init`과 첫 commit 뒤 `git status --short`는 빈 출력이었고, `echo "PRJ-2604,x" >> data/projects.csv` 뒤에는 ` M data/projects.csv`가 나타났습니다. 기준은 판정 가능하고 수정이 실제로 일어나면 실패합니다. 단 두 가지 전제가 필요합니다. 실습 1에서 첫 commit을 했어야 하고(그렇지 않으면 "??"로 표시), 이 전에 data/가 이미 바뀌어 있지 않아야 합니다. 거부 메시지 확인은 Claude Code 화면이라 실행 못 했습니다. | 선택: 기준에 "(실습 1의 첫 commit 뒤)"를 붙입니다. | 권고 |
| 9 | 표 9-6 "적용된 권한 규칙" 기준 | "금지에 data/, acceptance/의 수정과 git push가 있고, 확인 요청에 git commit이 있음" | 기준이 일부입니다. ch03 표 3-7(140행)은 금지 9개와 확인 요청 1개를 모두 나열하는데, 9장은 data/, acceptance/, push만 봅니다. check.py, CLAUDE.md, DECISIONS.md, .claude/, WebFetch, WebSearch 누락은 /permissions에서 안 잡힙니다. 실습 3 확인 방법(73행)은 "allow, ask, deny 규칙과 출처"만 보게 합니다. | "금지에 표 9-4의 모든 금지 규칙(Edit 6개, git push, WebFetch, WebSearch)이 있고, 확인 요청에 git commit이 있음. 출처는 .claude/settings.json" | 권고 |
| 10 | 표 9-6 "지출 한도" 행 | 방법 "팀의 비용 기준 문서", 기준 "한도의 단위와, 도달했을 때 결정할 사람이 적혀 있음" | 문서가 없으면 실패하므로 구현 전 실패는 성립합니다. 다만 예제 CR은 지출 한도를 두지 않으므로(65행) 실습 폴더로는 재현할 수 없습니다. 어디에서 어떻게 만드는지가 없습니다. | 행에 "예제에는 한도가 없어 실습 단계에서는 확인하지 않음. 팀에 적용할 때 확인"이라고 적거나 앞 문장에 포함합니다. | 권고 |
| 11 | 표 9-6 "사용량" 행 | "/usage ... Session 항목 ... 금액은 정가 기준의 추정치" | 표 9-3(52행)은 Session 항목이 "API 사용자용"이라고 합니다. 표 9-6은 요금제 구분이 없고, 구독 요금제에서 같은 항목이 보이는지는 실행해 보지 않았습니다. 이 행은 화면 존재 확인이라 구현 전에도 통과합니다(기능 확인이므로 허용 가능). | 기준 앞에 "(API 사용자용 항목, 구독 요금제는 화면이 다를 수 있음)" 추가. 실행 확인 뒤 확정. | 참고(검증 후 확정) |
| 12 | practice.html 실습 3 전체(55~73행) | 따라 하기, 확인 방법 | 다음 문서와 일치합니다. 설정 파일 내용(reference에서 옮김, ask는 직접 기재 `Bash(git commit *)` 일치), 폴더 이름 expense-practice, 요청 문장(`data/projects.csv에 PRJ-2604 행을 추가해 줘`가 표 9-6과 글자까지 같음), /permissions, `/exit` 뒤 `git status`. 단 두 가지가 다릅니다. (a) 실습 3 요청은 3개(acceptance 삭제, data PRJ-2604, push)인데 표 9-6은 data 요청만 봅니다. 괜찮은 부분집합입니다. (b) 실습 3 확인 방법의 git status는 `acceptance/`와 `data/`를 보는데, 표 9-6 기준은 data/만 보므로 acceptance도 보라는 말이 한쪽만 있습니다(R17 사소한 불일치). 실습 3에는 Windows·PowerShell 차이가 필요한 명령이 없습니다(`git status`는 동일). | 표 9-6 금지 동작 기준에 "acceptance/도"를 더하거나 요청에 acceptance 삭제를 더합니다. | 권고 |
| 13 | ch09 77행, 실습 폴더 이름 | "실습 1에서 만든 실습 폴더(expense-practice)" | practice.html 5행·27~30행과 일치. 8장·7장 방식과 같음. | 변경 없음 | 참고 |
| 14 | 실습 3 단계 4 vs 표 9-6 | 실습 3에는 commit, 샌드박스, 지출, 사용량 단계가 없음 | 표 9-6의 6행 중 실습 3이 덮는 것은 2행(/permissions, 금지 동작)입니다. 나머지 4행은 해당 단계가 없어 "어느 실습 단계 뒤"가 비어 있고, 이는 필수 1에 포함됩니다. | 필수 1의 문안으로 해결 | (필수 1 참조) |

## 실행한 명령과 출력(임시 복사본에서만)
- 임시 복사본: `/tmp/claude-0/-home-user-harness-book/4fa31d71-64a2-5605-bad4-d31a3ffd2331/scratchpad/ep/expense-practice` (원본은 건드리지 않음)
- `git init; git add -A; git commit`, `git status --short` → 빈 출력.
- `python check.py | tail -4` → `FAILED (failures=3)` 뒤 `acceptance: 실행 5건, 실패 3건, 건너뜀 0건(정한 수 5건)`. 부록 실습 1의 설명과 같습니다. (뒤의 `exit=0`은 파이프 `tail`의 종료 코드라 check.py의 코드가 아닙니다.)
- `python3 -c "import json; ..."` → `['Bash(git commit *)'] 9` (JSON 유효, ask 1개, deny 9개).
- `echo "PRJ-2604,x" >> data/projects.csv; git status --short` → ` M data/projects.csv`. `git checkout data/projects.csv` 뒤 빈 출력.
- `git -C . remote -v` → 빈 출력(원격 없음).
- 실행 못 함: /permissions, 요청 거부, commit 확인 화면, /sandbox와 touch, /usage. Claude Code 대화형 화면이 필요합니다.

## 실행 뒤 git status
`git status --short`(/home/user/harness-book) → 출력 없음. 작업 폴더가 바뀌지 않았습니다.

필수 수정 3, 편집 권고 5, 검증 후 확정 2(표의 4, 11번), 실행한 명령 5개(묶음 기준, 도구 호출 약 8회)
