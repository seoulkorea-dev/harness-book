# 부록 실습 점검(practice-checker)

## 1. 결론(필수 0, 권장 3)

- 실습 1의 명령은 /tmp/pc-appendix/에서 모두 실행해 설명과 대조했고, 설명과 다른 결과는 없었습니다. 다만 check.py 출력 블록의 줄 순서와 날짜 근거가 실제와 조금 다릅니다(권장 1, 2).
- 실습 2~6의 Claude Code 단계(/context, /permissions, /hooks, /usage, /memory, 에이전트 응답, 확인 화면)는 실행할 수 없어 "검증 후 확정"입니다. 실습 3~4에 쓰는 reference 설정은 파일 수준에서만 확인했습니다. 확인한 내용은 아래 3절에 있습니다.
- 챕터 링크 앵커(ch03·ch05·ch06·ch07·ch08 각 #example 등, ch07 #check, ch09 #permissions·#isolation·#cost, ch10 #perm-claude)는 모두 있습니다.
- docs/example-facts.md의 사실은 실습과 일치합니다. 대조한 항목은 작업 1~5 구성, 작업 2·3·4 확인 방법, 수정 범위, 여섯 절, 허용·확인 요청·금지 규칙, 훅, HEAD~2 계산입니다.
- origin/main과 현재 브랜치의 examples/expense-app 사이에 차이가 없어, `git clone`으로 받아도 같은 자료가 나옵니다.
- 저장소는 변경하지 않았고, git status는 깨끗합니다.

## 2. 지적 표

| 번호 | 등급 | 위치 | 문제 | 원문 | 고친 문안 |
|---|---|---|---|---|---|
| 1 | 권장 | src/appendix/practice.html, 실습 1, check.py 출력 블록 | 블록이 "출력 끝"이라면서 `tests:` 줄을 맨 위에 둡니다. 실제 출력은 `tests:` 줄이 acceptance 실패 출력보다 앞에 나오고, 마지막 두 줄이 `FAILED (failures=3)`와 `acceptance:` 줄입니다. 설명대로 `tail -3`을 실행하면 `tests:` 줄이 보이지 않습니다. | `<p>다음은 check.py의 출력 끝입니다(2026년 10월 20일 실행 기록, 실패한 시험의 자세한 출력은 생략). 첫 줄의 FAILED는 acceptance의 실패 3건 때문입니다.</p>` | `<p>다음은 check.py 출력에서 요약만 뽑은 것입니다(2026년 10월 24일 Linux에서 실행, 실패한 시험의 자세한 출력은 생략). tests 요약 줄은 출력 앞쪽에, FAILED와 acceptance 요약 줄은 맨 끝에 나옵니다. FAILED는 acceptance의 실패 3건 때문입니다.</p>` |
| 2 | 권장 | 같은 곳, 실습 준비 마지막 문단 | "2026년 10월 20일 실행 기록"이라고 하지만, RUNLOG.md의 10-20 기록은 `tests: 실행 3건, 실패 0건`처럼 건너뜀과 project_code 줄이 없는 옛 형식입니다. 블록의 출력 형식은 현재 check.py와 맞고 RUNLOG와는 맞지 않아, 기록 날짜와 내용이 어긋납니다. | `실습 1의 복사, git init, 첫 commit, 단위 테스트, check.py는 2026년 10월 20일 Linux에서 실행해 기록했고` | `실습 1의 복사, git init, 첫 commit, 단위 테스트, check.py는 2026년 10월 24일 Linux에서 다시 실행해 확인했고` (RUNLOG.md도 현재 출력 형식으로 갱신해야 합니다. 갱신하지 않으면 날짜 문구를 바꾸지 말고 RUNLOG와 같은 형식임을 밝혀야 합니다.) |
| 3 | 권장 | 실습 6 준비물 | "CLAUDE.md의 해당 항목"이 가리키는 곳이 불분명합니다. 실습 2는 절 이름만 알려 주고, reference에서 HANDOFF 항목은 `중단 규칙` 절의 둘째 불릿입니다. | `CLAUDE.md에 인계 메모(HANDOFF.md)를 작성하는 항목이 있는지 확인합니다. 없으면 reference/CLAUDE.example.md의 해당 항목을 옮깁니다.` | `CLAUDE.md의 중단 규칙 절에 "세션을 마칠 때 HANDOFF.md에 현재 상태, 읽을 문서, 미결정, 다음 작업, 확인 명령을 적는다."에 해당하는 항목이 있는지 확인합니다. 없으면 reference/CLAUDE.example.md의 중단 규칙 절에서 그 항목을 옮깁니다.` |

검증 후 확정(실행 불가, 문안 수정 없음)
- 실습 2~6의 Claude Code 화면과 응답. 예를 들면 `/context`의 Memory files, `/permissions`와 `/hooks` 화면, 세 요청의 금지 규칙 거부 메시지, 훅 실패를 에이전트가 언급하는지, reviewer 보고, 작업 2·3·4의 commit 흐름과 HEAD~2 결과, `/usage`, `/memory`.
- 실습 4의 `git diff expense/` 출력 없음. 되돌리기 요청 뒤의 결과라 Claude Code 없이는 알 수 없습니다.
- 각 단계의 "응답과 화면은 실행 기록을 확인하기 전의 예상" 문구는 실제 상태를 밝힌 것이라 유지해야 합니다.

## 3. 실행 기록

모든 명령은 /tmp/pc-appendix/expense-practice(저장소 examples/expense-app을 cp -r로 복사한 폴더)에서 실행했습니다.

- `git init && git add -A && git commit -m "실습 시작 상태"` 뒤 `git log --oneline`
  - 결과: 9d6d54d 실습 시작 상태, 한 건. 이름과 이메일은 `-c` 옵션으로 지정했습니다.
- `ls -a`
  - 결과: CLAUDE.md와 .claude/는 없습니다. reference/, .gitignore, RUNLOG.md, README.md가 있습니다.
- `python --version`
  - 결과: Python 3.13.16
- `python -m unittest discover tests -q`
  - 결과: Ran 3 tests, 마지막 줄 OK. 설명과 같습니다.
- `python check.py`
  - 종료 코드: 1
  - 출력 끝: `FAILED (failures=3)` / `acceptance: 실행 5건, 실패 3건, 건너뜀 0건(정한 수 5건)`
  - 앞쪽: `tests: 실행 3건, 실패 0건, 건너뜀 0건, project_code 시험 0건`
  - 실패한 시험은 test_1, test_2, test_3입니다. 설명과 같습니다.
  - 종료 코드는 `python check.py >/dev/null 2>&1; echo $?`로 확인했습니다. 파이프(`| tail`) 뒤의 `$?`는 0으로 나오므로 확인에 쓸 수 없습니다.
  - 실습 1 본문은 "명령 바로 뒤에 echo $?"라고 적었으므로 문제 없습니다.
- `python app.py`를 3초 제한으로 실행하고 curl로 확인했습니다.
  - `/`: HTTP 200, "정산 요청 목록" 표(요청자 열 포함)
  - `/new`: HTTP 200, "정산 요청 등록" 폼(project_code 입력 없음, 구현 전이라 정상)
  - 시작 시 `http://localhost:8000`을 출력합니다.
- reference/tasks.example.json을 tasks.json으로 복사하고 `git add`와 `git commit -m "작업 단위 목록 추가"`를 실행했습니다.
  - 결과: 로그는 b84962e 작업 단위 목록 추가, 9d6d54d 실습 시작 상태. 이후 작업 2·3 commit 두 개가 더 생기면 HEAD~2가 "작업 단위 목록 추가" commit이 되므로, 실습 5의 `git diff HEAD~2 -- tasks.json`과 `git diff HEAD~2 --stat` 설명이 맞습니다.
- reference/settings.example.json을 python으로 읽어 permissions와 hooks 최상위 키를 확인하고 .claude/settings.json으로 저장했습니다.
  - 결과: JSON이 유효하고 최상위 키는 `['permissions', 'hooks']`입니다. 실습 4의 "permissions와 같은 단계" 설명이 맞습니다.
  - `ask`는 `Bash(git commit *)` 하나로, 실습 3 본문 모양과 같습니다.
- `mkdir -p .claude/agents`와 `cp reference/reviewer.example.md .claude/agents/reviewer.md`
  - 결과: 복사됩니다. front matter는 name: reviewer, tools: Read, Grep, Glob입니다.
- 훅 명령 `cd "$PWD" && python -m unittest discover tests -q || exit 2`
  - 결과: OK. 성공 시 종료 코드는 0입니다.
  - 실습 4의 첫 요청(요청자 열 삭제)은 tests/test_basic.py의 test_list_shows_requesters를 깨뜨리는 구조입니다. 실제 실패는 실행하지 않았지만, 훅이 실패하는 시나리오는 맞습니다.
- 앵커와 원격 확인
  - 본문이 가리키는 앵커는 grep으로 확인했고 모두 있습니다.
  - `git ls-tree origin/main`에서 examples/expense-app 파일 19개를 확인했습니다. `git diff --stat origin/main HEAD -- examples/expense-app`의 출력은 없습니다.
- `git status --short`(저장소): 출력 없음, 변경 없음. 실행은 모두 /tmp/pc-appendix 안에서만 했습니다.

필수 수정 0, 편집 권고 3, 검증 후 확정 다수(실습 2~6의 Claude Code 화면), 실행한 명령 약 12개
(보고 형식이 요구한 등급은 필수/권장 두 가지라 위 결론은 필수 0, 권장 3입니다.)
