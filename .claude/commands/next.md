---
description: 다음 한 단위를 진행한다(작가 요청 → 열린 PR 마무리 → HANDOFF의 다음 할 일)
---
다음 한 단위를 끝까지 진행한다. 셸에서 cd를 쓰지 않는다. 작가에게 묻지 않고 진행하며, 작가만 정할 일은 docs/AUTHOR_QUEUE.md에 권장안과 함께 적는다.

0. 준비: git switch main, git pull --ff-only origin main. 실패하면 멈추고 이유를 HANDOFF.md 맨 위 "## 지금 상태"에 적는다.
1. 작가 요청: gh issue list --label request --state open 으로 열린 요청을 확인한다(라벨이 없으면 gh label create request). 있으면 가장 오래된 것 하나를 이번 작업으로 정하고, 이슈에 "작업 시작"을 댓글로 남긴다.
2. 열린 PR: gh pr list 로 이 저장소의 열린 PR을 확인한다. 있으면 그 PR을 마무리하는 것이 이번 작업이다(3-d부터).
3. 1, 2가 없으면 HANDOFF.md "## 작업 목록"에서 체크하지 않은 첫 항목을 이번 작업으로 정한다.
   a. 장 작업이면 /plan-chapter와 같은 순서로 장 명세와 그림 명세를 만든다. 작가 확인 대신 editor에게 명세 검토를 맡기고, 작가만 정할 일은 AUTHOR_QUEUE.md에 적는다.
   b. 작업 브랜치를 만들고 원고와 그림을 쓴다. 그림은 시안 두 개를 만들어 reviews/agents/YYYY-MM-DD-<작업>-figures.html에 남기고, editor와 alt-reviewer의 의견으로 하나를 고른다.
   c. python tools/check_all.py 통과 → /review-chapter(점검 에이전트) → 필수 반영 → check_all 다시 통과
   d. editor에게 정식 검수를 맡긴다. 결과를 reviews/YYYY-MM-DD-<작업>-editor.md로 저장한다.
   e. "병합 불가"면 필수를 반영하고 d로 돌아간다(최대 3회. 넘으면 멈추고 HANDOFF.md에 이유를 적는다).
   f. HANDOFF.md를 갱신한다: "## 진행 기록" 표에 한 행(날짜, 작업, PR, editor 결론, check_all, 작가 확인 추가 여부), 작업 목록 체크, 다음 할 일.
   g. 커밋, push, PR 생성(아직 없으면). PR 설명에 editor 결론, 바뀐 파일, check_all 출력 원문 요약, 작가 확인 항목을 넣고, editor 검수 문서를 PR 댓글로 올린다(gh pr comment).
   h. gh pr checks --watch 로 CI를 기다린다. editor "병합 가능", check_all 통과, CI 통과일 때만 gh pr merge --merge --delete-branch.
   i. 작가 요청 작업이었다면 이슈에 PR 주소와 결과를 댓글로 남기고 닫는다.
4. 끝에 한 줄로 보고한다: 작업 이름, PR 주소, 병합 여부, 작가 확인 추가 항목 수.
