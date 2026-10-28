---
description: 다음 한 단위(작가 요청 이슈 하나)를 HARNESS_SETUP.md 3장 순서로 끝까지 진행한다
---
다음 한 단위를 끝까지 진행한다. 기준은 book-kit/book/PLAYBOOK.md(원고, ../book-kit), BOOK_SPEC.md(이 책), HARNESS_SETUP.md(진행)이다. 작가에게 묻지 않고 진행하며, 작가만 정할 일은 docs/AUTHOR_QUEUE.md에 질문과 진행한 권장안을 적는다. 셸에서 cd를 쓰지 않는다. 체계(.claude/, 규칙 문서)는 바꾸지 않는다.

0. 준비: git switch main, git pull --ff-only origin main. 실패하면 이유를 HANDOFF.md "## 지금 상태"에 적고 멈춘다.
1. 이번 작업 정하기
   - gh issue list --label request --state open 에서 번호가 가장 작은 이슈 하나가 이번 작업이다.
   - 그 이슈의 작업 브랜치로 열린 초안 PR이 있으면 그 PR을 체크하지 않은 첫 단계부터 마무리한다.
   - 열린 요청 이슈가 없으면 "할 일 없음"이라고 보고하고 끝낸다.
   - 브랜치 이름이 ccr-로 시작하는 PR은 대상이 아니다.
2. 초안 PR: 작업 브랜치를 만들고(git switch -c <작업>, 브랜치 만들기와 커밋은 따로 실행) 초안 PR을 연다(gh pr create --draft). 이슈에 "작업 시작"(대상, 초안 PR 번호) 댓글을 남긴다. PR 설명에 HARNESS_SETUP.md 부록 D의 단계 체크 목록을 둔다. 단계가 끝날 때마다 커밋, push하고 gh pr edit로 그 단계를 체크하고 짧은 결과를 적는다. 해당하지 않는 단계는 체크하고 "해당 없음"이라고 적는다.
3. 단계(HARNESS_SETUP.md 3장)
   a. 장 명세(docs/specs/<장>-spec.md, 플레이북 부록 B)와 필요한 그림 명세. 그림 구조를 바꾸지 않으면 시안 단계는 "해당 없음(구조 유지)".
   b. 원고: 이슈 본문의 지시와 플레이북으로 고친다. 이미 정리된 1장, 시작하며와 정의, 용어, 형식을 맞춘다. 작가가 확정한 문안은 그대로 둔다.
   c. python tools/check_all.py 통과.
   d. 점검: fact-checker(사실, 명령 실행), 예제나 실습이 있으면 practice-checker, 그림이 바뀌었으면 production-checker. 지적을 반영, 보류, 작가 확인으로 나눠 PR 설명의 점검 처리 표에 적고 반영한다.
   e. 편집 검토 1회: chief-editor에게 장 전체를 맡긴다(플레이북, 설계서, 장 명세 경로를 넘김). chief-editor가 실행되지 않으면 멈추지 말고 .claude/agents/chief-editor.md 본문 지침을 그대로 일반 하위 에이전트에 넘겨 검토한다. 결과를 reviews/agents/YYYY-MM-DD-<장>-chief-editor.md로 저장한다.
   f. 편집 검토의 지적을 한 번에 모두 반영한다. 다시 검토받지 않는다. 반영하지 못한 필수는 docs/AUTHOR_QUEUE.md "작가 검수 목록"과 PR 설명에 적는다.
   g. check_all과 플레이북 21장 반영 확인 체크리스트. 기준이 바뀌어 이미 쓴 장에도 적용해야 하는 것이 있으면 같은 PR에서 전파한다.
   h. 기록: HANDOFF.md(지금 상태, 진행 기록 한 행), DASHBOARD.md(python tools/dashboard.py refresh --write-file), 같은 실패가 두 번째면 FAILURES.md.
   i. 커밋, push. PR 설명에 바뀐 곳 표(위치 | 이전 | 이후 | 근거 원칙), 편집장의 고칠 문장 비율, 반영하지 못한 필수, 검사 출력 원문 요약을 넣는다.
   j. gh pr checks --watch 로 CI를 기다린다. check_all과 CI가 통과하면 gh pr ready 후 gh pr merge --merge --delete-branch. 편집장의 필수가 남아도 작가 검수 목록에 적었으면 병합한다.
   k. 이슈에 결과 댓글(PR 주소, 바뀐 절과 표와 그림, 편집장 결과, 작가 검수 목록 번호, 걸린 시간)을 남기고 닫는다.
4. 막혔을 때(HARNESS_SETUP.md 5.3): 같은 실패가 세 번 이어지면 PR 설명 맨 위와 이슈에 "멈춤: 이유"를 적고, 초안 PR로 둔 채 이 단위를 끝낸다(다음 단위는 /autopilot이 이어 감).
5. 끝에 한 줄로 보고한다: 작업 이름, PR 주소, 병합 여부, 걸린 시간.
