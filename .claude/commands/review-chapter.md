---
description: PR 전 점검: 하위 에이전트 점검을 한 번에 실행한다
---
Chapter $ARGUMENTS에 대해 하위 에이전트 점검을 한다. 원고는 고치지 않는다. 진행 순서는 HARNESS_SETUP.md 3장, 기준은 book-kit/book/PLAYBOOK.md(../book-kit)와 BOOK_SPEC.md다.
1. 이번 작업에서 새로 쓰거나 바꾼 문장 목록을 git diff로 만든다.
2. 점검 에이전트를 동시에 부른다: fact-checker(사실, 명령 실행, 장 전체), 예제나 실습이 있으면 practice-checker, 그림이 바뀌었으면 production-checker. 각 에이전트에 다음을 넘긴다.
   - 범위: src/chapters/ch$ARGUMENTS.html(바꾼 절 이름)
   - 기준: ../book-kit/book/PLAYBOOK.md, BOOK_SPEC.md, 장 명세(docs/specs/ch$ARGUMENTS-spec.md), 관련 research/ 파일(fact-checker), 관련 실습 파일과 docs/example-facts.md(practice-checker), 그림 번호와 빌드된 chapters/ch$ARGUMENTS.html(production-checker)
   - 보고 형식: 각 에이전트 정의의 결과 표
   - 대시보드: 각 에이전트를 부르기 직전 python tools/dashboard.py start <에이전트> "ch$ARGUMENTS <범위>", 결과를 받은 직후 python tools/dashboard.py end <에이전트> "<필수 n, 권장 n>"
3. 점검 지적을 반영한 뒤 chief-editor에게 장 전체 편집 검토를 1회 맡긴다(같은 기준 경로를 넘김).
4. 각 결과를 reviews/agents/YYYY-MM-DD-ch$ARGUMENTS-<에이전트>.md로 저장한다.
5. 모든 의견을 하나의 표로 모아 반영, 보류, 작가 확인으로 나눈다. 필수는 반영하거나 작가 검수 목록(docs/AUTHOR_QUEUE.md)으로만 둘 수 있다(보류 불가).
6. PR 설명에 에이전트 실행 기록 표(에이전트, 실행 여부, 필수 건수, 반영 여부)를 넣는다. 실행하지 않은 점검은 이유를 적는다.
7. 표를 보여 주고 끝낸다.
