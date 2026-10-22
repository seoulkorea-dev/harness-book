---
description: 다음 한 단위를 진행한다(작가 요청 → 열린 PR 마무리 → HANDOFF의 다음 할 일)
---
다음 한 단위를 끝까지 진행한다. 셸에서 cd를 쓰지 않는다. 작가에게 묻지 않고 진행하며, 작가만 정할 일은 docs/AUTHOR_QUEUE.md에 권장안과 함께 적는다. 진행 상태는 GitHub의 초안 PR에서 보이게 한다(이슈 #13).

-1. 자동 실행 확인(이슈 #34): 이 명령의 인자가 unit이 아니면(autorun이 띄운 단위 세션은 "/next unit") Read 도구로 logs/autorun.lock을 읽는다. 파일이 있으면 아무 작업도 하지 않고 "자동 실행 중(logs/autorun.lock: pid, 마지막 갱신 시각)"이라고만 답하고 끝낸다. autorun이 실행 중이 아닌데 파일이 남아 있으면(비정상 종료) logs/autorun.lock을 지운 뒤 다시 /next를 실행하라고 덧붙인다. 파일을 직접 지우지는 않는다.
- .claude/(agents, commands, settings.json)를 바꿔야 하면 .claude/에 직접 쓰지 않고, 새 판을 docs/staged-claude/의 같은 경로(agents/<이름>.md, commands/<이름>.md, settings.json)에 두고 보통 PR처럼 editor 검수를 거쳐 병합한다. 병합되면 autorun(python tools/autorun.py)이 .claude/에 반영한다(D-119). settings.json에서 권한을 넓히는 변경은 autorun이 반영하지 않고 작가에게 알린다.

0. 준비: git switch main, git pull --ff-only origin main. 실패하면 멈추고 이유를 HANDOFF.md 맨 위 "## 지금 상태"에 적는다.
1. 작가 요청: gh issue list --label request --state open 으로 열린 요청을 확인한다(라벨이 없으면 gh label create request). 있으면 가장 오래된 것 하나를 이번 작업으로 정한다("작업 시작" 댓글은 3-0에서 초안 PR을 연 뒤에 남김).
2. 열린 PR: gh pr list 로 이 저장소의 열린 PR을 확인한다. 있으면 그 PR을 마무리하는 것이 이번 작업이다(초안 PR이면 체크 목록에서 체크하지 않은 첫 단계부터, 아니면 3-d부터).
3. 1, 2가 없으면 HANDOFF.md "## 작업 목록"에서 체크하지 않은 첫 항목을 이번 작업으로 정한다.

3-0. 작업을 정하면 바로(1, 2, 3 어느 경로로 정했든): 초안 PR
- 작업 브랜치를 만든다(git switch -c <작업>. 훅이 main에서의 커밋을 막으므로 브랜치 만들기와 커밋은 따로 실행한다).
- HANDOFF.md "## 지금 상태" 맨 위에 "작업 시작: <작업 이름>"을 적어 커밋, push한다.
- 초안 PR을 연다(gh pr create --draft). 설명에 아래 체크 목록을 둔다. 작업에 해당하지 않는 단계는 체크하고 "해당 없음"이라고 적는다.
  - [ ] 명세(장 명세, 그림 명세)
  - [ ] 그림 시안 두 개와 선택
  - [ ] 원고 작성
  - [ ] check_all
  - [ ] 점검 에이전트(필수 반영, 논지 사슬 표)
  - [ ] editor 검수(결론)
  - [ ] CI
  - [ ] 병합
- 작가 요청 작업이면 초안 PR을 연 직후 이슈에 "작업 시작" 댓글을 남긴다(대상 chapter와 초안 PR 번호, templates/issue-report.md).
- 단계가 끝날 때마다 그때까지의 변경을 커밋, push하고, gh pr edit <번호> --body-file 로 그 단계를 체크하고 짧은 결과(파일, 결론, 건수)를 적는다.
- 단계(명세, 시안, 원고, check_all, 점검, editor, CI)가 끝날 때마다 이 작업의 요청 이슈와 PR의 새 댓글을 확인한다(gh issue view <번호> --comments, gh pr view <번호> --comments). 작가나 Neo의 정정이 있으면 다음 단계 전에 반영하고, 반영 사실을 PR 체크 목록에 적는다(이슈 #25).
- 멈추거나 실패하면 PR 설명 맨 위에 "멈춤: 이유"를 적고 HANDOFF.md에도 적는다.

3-1. 단계(작가 요청 작업도 같은 단계를 따른다. 해당하지 않는 단계는 체크 목록에 "해당 없음")
   a. 장 작업이면 /plan-chapter와 같은 순서로 장 명세와 그림 명세를 만든다. 작가 확인 대신 editor에게 명세 검토를 맡기고, 작가만 정할 일은 AUTHOR_QUEUE.md에 적는다. → 체크: 명세
   b. 원고와 그림을 쓴다. 그림은 시안 두 개를 만들어 reviews/agents/YYYY-MM-DD-<작업>-figures.html에 남기고, editor와 alt-reviewer의 의견으로 하나를 고른다. → 체크: 그림 시안 두 개와 선택, 원고 작성
   c. python tools/check_all.py 통과 → 체크: check_all. /review-chapter(점검 에이전트. 장 작업이면 flow-reviewer와 reader-novice가 장 전체를 통독하고 논지 사슬 표를 reviews/flow/<장>-flow.md에 저장, D-117) → 필수(논지 사슬 끊김 포함) 반영 → check_all 다시 통과 → 체크: 점검 에이전트 장별 정비와 장 개정에서는 reader-expert와 fact-checker도 필수이고(이슈 #66), PR 설명에 에이전트 실행 기록 표(에이전트, 실행 여부, 필수 건수, 반영 여부)를 넣는다. 장별 정비 PR이면 그 장을 lint/rules_applied.txt에 더하고 python lint/check_rules.py가 그 장에서 실패 0인지 확인한다(REVIEW_RULES.md, D-127).
   d. editor에게 정식 검수를 맡긴다(장 작업이면 장 전체 통독과 논지 사슬 표 경로를 넘김). 결과를 reviews/YYYY-MM-DD-<작업>-editor.md로 저장한다. → 체크: editor 검수(결론)
   e. "병합 불가"면 필수를 반영하고 d로 돌아간다(최대 3회. 넘으면 멈추고 PR 설명 맨 위와 HANDOFF.md에 이유를 적는다).
   f. HANDOFF.md를 갱신한다: "## 진행 기록" 표에 한 행(날짜, 작업, PR, editor 결론, check_all, 작가 확인 추가 여부), 작업 목록 체크, 다음 할 일, "작업 시작" 줄을 결과로 바꿈.
   g. 커밋, push. PR 설명에 체크 목록과 함께 editor 결론, 바뀐 파일, check_all 출력 원문 요약, 작가 확인 항목을 넣고, 장 작업이면 논지 사슬 표(reviews/flow/<장>-flow.md) 링크와 고친 곳(이전, 이후)을 넣는다. editor 검수 문서를 PR 댓글로 올린다(gh pr comment).
   h. gh pr checks --watch 로 CI를 기다린다 → 체크: CI. editor "병합 가능", check_all 통과, CI 통과일 때만 초안을 해제하고(gh pr ready) gh pr merge --merge --delete-branch → 체크: 병합.
   i. 작가 요청 작업이었다면 이슈에 결과 댓글을 남기고 닫는다. 형식은 templates/issue-report.md: PR 주소와 결과, 진행 완료 chapter 표(전체 chapter의 상태와 이번에 바꾼 chapter), chapter별 작업 내용과 수정 내용(절, 표, 그림 단위), 장 밖의 변경. 멈춘 경우에도 "멈춤: 이유"와 같은 형식의 진행 표를 이슈에 댓글로 남긴다.
4. 끝에 한 줄로 보고한다: 작업 이름, PR 주소, 병합 여부, 작가 확인 추가 항목 수.
