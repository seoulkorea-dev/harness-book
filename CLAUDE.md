# 작업 안내(Claude Code)

## 이 세션의 역할
- 원고 작성 담당이다. 원고, 그림, 실습 자료를 고치고 검사를 실행하고, 작업 브랜치에 push한 뒤 PR을 만든다.
- main에는 반영하지 않는다. 병합은 작가가 PR에서 한다.
- 검수는 Claude App의 검수 Project가 맡는다. reviews/의 검수 지침만 반영하고, 지시하지 않은 변경은 하지 않는다. 꼭 필요한 변경은 PR 설명에 따로 적는다.

## 시작할 때
1. HANDOFF.md를 읽는다(세션 시작 훅이 보여 준다).
2. 작업할 장의 계획(BOOK_SPEC.md)과 DECISIONS.md의 마지막 10건을 확인한다.
3. 검수 지침을 반영하는 작업이면 해당 reviews/ 문서를 읽는다.
4. main 브랜치라면 작업 브랜치를 만든다(git switch -c <장-주제>).

## 원고 규칙
- 원고는 src/만 고친다. 루트의 index.html, chapters/, appendix/는 빌드 결과물이다.
- 장 틀: 주장 제목 → 원리 → CR 적용 → 실패 표 → 확인 방법 → 원칙 한 문장 → 점검 질문
- 예제 이름: 첫 등장은 "경비 정산 시스템 개편 변경 요청(Change Request) CR", 이후는 "CR"
- 문체는 STYLE.md, 그림은 FIGURE_STYLE.md(다이어그램을 그릴 때만 diagram_guide.md도 읽는다)
- 사실은 원문을 확인한 뒤 쓰고, research/에 출처와 확인 날짜를 남긴다.

## 멀티 에이전트 작업 공간
| 구성원 | 역할 | 쓰기 |
|---|---|---|
| 작가 | 결정, 승인, PR 병합 | 전부(바꾸면 DECISIONS.md에 기록) |
| 메인 세션(이 세션) | 원고 작성, 하위 에이전트 호출, 보고서 저장, PR | src/, assets/, examples/, HANDOFF.md, FAILURES.md, reviews/, research/, DECISIONS.md(작가 확인 후) |
| researcher, fact-checker, flow-reviewer, figure-checker, reader-novice, reader-expert, alt-reviewer | 조사와 점검 | 없음(읽기만, 결과는 보고서 문안으로 돌려줌) |
| 검수 Project(Claude App) | 정식 검수 문서 | 없음(작가가 전달, 메인 세션이 reviews/에 등록) |
- 주고받기는 파일로만 한다. 하위 에이전트의 보고 문안은 메인 세션이 reviews/agents/YYYY-MM-DD-<장>-<에이전트>.md로 저장한다. 형식: 발견 | 위치 | 근거 | 제안 | 확신(높음, 중간, 낮음)
- 원고(src/)를 쓰는 주체는 한 번에 하나다. 하위 에이전트는 동시에 여러 개 불러도 된다. 다른 장을 동시에 진행하려면 장마다 브랜치와 작업 폴더(git worktree)를 따로 쓴다.
- 하위 에이전트는 이 대화를 모른다. 부를 때 범위(파일과 절), 기준 문서, 보고 형식을 넘긴다.
- 하위 에이전트 의견은 그대로 반영하지 않는다. 반영, 보류, 작가 확인으로 나누어 PR 설명에 표로 적는다. 의견이 부딪히면 DECISIONS.md > 검수 Project 지침 > 하위 에이전트 의견 순서로 따르고, 그래도 정해지지 않으면 작가에게 묻는다.
- 호출 시점: 장 계획 때 researcher, 원고 작성 뒤 PR 전에 fact-checker, flow-reviewer, figure-checker, reader-novice, alt-reviewer, 마무리 단계에 reader-expert
- 명세 먼저: 장은 templates/chapter-spec.md, 그림은 templates/figure-spec.md로 명세를 먼저 쓰고 작가 확인을 받는다. 그림은 배치가 다른 시안 두 개를 만들어 작가가 고르게 한다(확인용은 SVG를 넣은 HTML 한 장).

## 먼저 작가에게 물을 일
- 목차, 장의 주장, 핵심 정의와 용어, 그림 방침, 문체 규칙을 바꾸는 일
- DECISIONS.md 수정, 브랜치 push, PR 생성(설정이 확인을 요구한다)

## 끝낼 때
- python tools/check_all.py를 통과시킨다(종료 훅이 실패를 막는다).
- 보고에는 검사 출력 원문을 붙인다.
- HANDOFF.md를 갱신한다. 같은 실패가 두 번째면 FAILURES.md에 적는다.
