# 작업 안내(Claude Code)

## 먼저 읽을 것(이 순서)
1. book-kit/book/PLAYBOOK.md: 원고 원칙과 규칙, 최종 점검표(모든 원고 작업의 기준). 공통 원본이며 이 저장소 옆 폴더 ../book-kit에 둡니다. 장 명세와 그림 명세 서식도 ../book-kit/book/templates/를 씁니다
2. BOOK_SPEC.md: 이 책의 선택과 예외
3. HARNESS_SETUP.md: 작업 진행 방식(한 장의 순서, 중단 없이 진행하는 규칙)
4. HANDOFF.md 맨 위 "지금 상태"
5. docs/AUTHOR_QUEUE.md, DECISIONS.md 마지막 10건

- 이 저장소에는 원고 작성 기준을 두지 않습니다(D-149). 옛 기준 문서와 옛 에이전트는 지웠습니다(git 기록에만 있음).
- 검사 도구(lint/의 check_*.py와 banned.txt), .claude/agents/, .claude/skills/는 저장소에 두지 않습니다(D-150). 세션 시작 훅과 check_all이 tools/sync_kit.py로 book-kit에서 가져오며 git에는 들어가지 않습니다. 고칠 것은 book-kit에서 고칩니다. lint/rules_applied.txt(정비를 마친 장 목록)만 이 책의 기록으로 남습니다.
- 원고 규칙 검사는 이 세션의 python tools/check_all.py로 합니다. GitHub CI는 공개 저장소라 book-kit을 받지 않고 빌드와 빌드 결과 일치만 봅니다(D-151).
- 책을 쓰다가 원칙이나 규칙을 바꿔야 하면 작가 승인 뒤 이 세션에서 book-kit에 작업 브랜치와 PR로 반영하고(규칙과 검사, 에이전트, 스킬을 같은 PR에서), 변경 내용은 book-kit에만 적습니다. 이 저장소의 DECISIONS.md에는 원칙 문장 없이 book-kit 변경 기록 날짜만 적습니다. 이 책만의 예외는 BOOK_SPEC.md에 적습니다.

## 이 세션의 역할
- 작성 세션이다. 원고를 고치는 유일한 주체다. main에 직접 commit, push하지 않고 작업 브랜치와 PR로 반영한다.
- 장마다 HARNESS_SETUP.md 3장의 순서로 진행한다.
- 편집 검토는 하위 에이전트 chief-editor가 장마다 1회 한다. 지적은 한 번에 모두 반영하고 다시 검토받지 않는다. 반영하지 못한 필수는 docs/AUTHOR_QUEUE.md의 "작가 검수 목록"에 적는다.
- 점검은 fact-checker(사실, 명령 실행), practice-checker(예제나 실습이 있을 때), production-checker(그림이 바뀌었을 때)가 한다. 하위 에이전트는 원고를 고치지 않고 보고 문안만 돌려준다.
- 작가만 정할 일(목차, 장의 주장, 핵심 정의, 용어, 그림 방침, 문체 규칙)은 바꾸지 않고 AUTHOR_QUEUE에 질문과 권장안을 적고 진행한다.
- 작가가 확정한 문안은 그대로 둔다. 바꿔야 하면 AUTHOR_QUEUE에 적는다.
- 지시하지 않은 변경은 하지 않는다. 꼭 필요하면 PR 설명에 따로 적는다.

## 원고 규칙
- 원고는 src/만 고친다. 루트의 index.html, chapters/, appendix/는 빌드 결과물이다.
- 사실은 원문을 확인한 뒤 쓰고 research/에 출처와 확인 날짜를 남긴다.
- 원고를 넘기기 전에 플레이북 25장 최종 점검표를 확인한다.

## 하위 에이전트 부르기
- 하위 에이전트는 이 대화를 모른다. 부를 때 범위(파일과 절), 기준 문서(플레이북 경로 ../book-kit/book/PLAYBOOK.md, 설계서, 장 명세), 보고 형식을 넘긴다.
- 보고 문안은 reviews/agents/YYYY-MM-DD-<장>-<에이전트>.md로 저장하고, 처리(반영, 보류, 작가 확인)를 PR 설명에 표로 적는다.
- 의견이 부딪히면 DECISIONS.md와 BOOK_SPEC.md > chief-editor 판정 > 점검 의견 순서로 따른다.

## 끝낼 때
- python tools/check_all.py를 통과시킨다.
- 보고에는 검사 출력 원문을 붙인다.
- HANDOFF.md를 갱신한다. 같은 실패가 두 번째면 FAILURES.md에 적는다.
