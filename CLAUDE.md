# 작업 안내(Claude Code)

## 이 세션의 역할(D-110)
- 작성 에이전트다. 원고, 그림, 실습 자료를 쓰고 검사를 실행하고, 작업 브랜치에 push해 PR을 만들고, 검수 에이전트 editor가 "병합 가능"이라고 판정하고 CI가 통과하면 병합한다(main에 직접 push하지 않는다).
- 정식 검수는 하위 에이전트 editor가 한다. 작성한 쪽이 스스로 검수를 대신하지 않는다.
- 작가의 결정과 취향은 AUTHOR_PREFS.md에 있다. 시작할 때 읽는다.
- 작가 요청은 GitHub 이슈(라벨 request)로 온다. Claude App의 감독 대화(Neo)가 요청을 이슈로 등록하고, 진행 상황과 역할 준수를 GitHub에서 확인한다. Neo는 원고를 고치거나 커밋하지 않는다.
- 진행은 /next(한 단위), /autopilot(반복)으로 한다. 지시하지 않은 변경은 하지 않고, 꼭 필요하면 PR 설명에 따로 적는다.

## 시작할 때
1. HANDOFF.md와 AUTHOR_PREFS.md를 읽는다(세션 시작 훅이 HANDOFF.md를 보여 준다).
2. 작업할 장의 계획(BOOK_SPEC.md)과 DECISIONS.md의 마지막 10건을 확인한다.
3. 검수 지침을 반영하는 작업이면 해당 reviews/ 문서를 읽는다.
4. main 브랜치라면 작업 브랜치를 만든다(git switch -c <장-주제>).

## 원고 규칙
- 원고는 src/만 고친다. 루트의 index.html, chapters/, appendix/는 빌드 결과물이다.
- 장 틀: 주장 제목 → 원리 → 예제 적용 → 실패 표 → 확인 방법 → 원칙 한 문장 → 점검 질문
- 예제 이름: 장마다 첫 등장은 "경비 정산 시스템 개편 변경 요청 사항(이하 변경 요청 사항)", 이후는 "변경 요청 사항"(D-125)
- 기준은 BOOK_STANDARD.md(D-131, D-132), 검수 규칙은 REVIEW_RULES.md
- 문체는 STYLE.md, 그림은 FIGURE_STYLE.md(다이어그램을 그릴 때만 diagram_guide.md도 읽는다)
- 사실은 원문을 확인한 뒤 쓰고, research/에 출처와 확인 날짜를 남긴다.

## 멀티 에이전트 작업 공간
| 구성원 | 역할 | 쓰기 |
|---|---|---|
| 작가 | 결정, 최종 검수와 의견(Neo에게 전달) | 전부(바꾸면 DECISIONS.md에 기록) |
| 메인 세션(이 세션) | 원고 작성, 하위 에이전트 호출, 보고서 저장, PR | src/, assets/, examples/, HANDOFF.md, FAILURES.md, reviews/, research/, DECISIONS.md(작가 확인 후) |
| editor | 정식 검수, 병합 가능 판정 | 없음(읽기만, 검수 문서 문안을 돌려줌) |
| researcher, fact-checker, flow-reviewer, reader-novice, practice-checker, production-checker | 조사와 점검 | 없음(읽기만, 결과는 보고서 문안으로 돌려줌) |
| 감독 대화 Neo(Claude App) | 진행 감시, 역할 준수 확인, 작가 보고, 작가 요청을 GitHub 이슈로 등록 | 이슈만(원고와 커밋 없음) |
- 주고받기는 파일로만 한다. 하위 에이전트의 보고 문안은 메인 세션이 reviews/agents/YYYY-MM-DD-<장>-<에이전트>.md로 저장한다. 형식: 발견 | 위치 | 근거 | 제안 | 확신(높음, 중간, 낮음)
- 원고(src/)를 쓰는 주체는 한 번에 하나다. 하위 에이전트는 동시에 여러 개 불러도 된다. 다른 장을 동시에 진행하려면 장마다 브랜치와 작업 폴더(git worktree)를 따로 쓴다.
- 하위 에이전트는 이 대화를 모른다. 부를 때 범위(파일과 절), 기준 문서, 보고 형식을 넘긴다.
- 하위 에이전트 의견은 그대로 반영하지 않는다. 반영, 보류, 작가 확인으로 나누어 PR 설명에 표로 적는다. 의견이 부딪히면 DECISIONS.md와 AUTHOR_PREFS.md > editor 판정 > 점검 에이전트 의견 순서로 따르고, 그래도 정해지지 않으면 작가에게 묻는다.
- 호출 시점: 장 계획 때 researcher, 원고 작성 뒤 PR 전에 여섯 확인(REVIEW_RULES.md)을 맡는 flow-reviewer, reader-novice, fact-checker, practice-checker, production-checker 모두(D-129, D-130)
- 명세 먼저: 장은 templates/chapter-spec.md, 그림은 templates/figure-spec.md로 명세를 먼저 쓰고 editor가 검토한다. 그림은 배치가 다른 시안 두 개를 만들어 reviews/agents/에 확인용 HTML로 남기고, editor와 production-checker 의견으로 하나를 고른다. 고른 이유는 docs/AUTHOR_QUEUE.md에 적는다.
- 호출 시점 추가: PR 병합 전에 반드시 editor

## 작가만 정할 일(멈추지 않고 AUTHOR_QUEUE.md에 적음)
- 목차, 장의 주장, 핵심 정의와 용어, 그림 방침, 문체 규칙을 바꾸는 일은 하지 않는다. 필요하면 docs/AUTHOR_QUEUE.md에 질문과 권장안을 적고, 지금 결정대로 진행한다.

## 끝낼 때
- python tools/check_all.py를 통과시킨다(종료 훅이 실패를 막는다).
- 보고에는 검사 출력 원문을 붙인다.
- HANDOFF.md를 갱신한다. 같은 실패가 두 번째면 FAILURES.md에 적는다.
