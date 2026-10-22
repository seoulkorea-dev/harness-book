---
description: PR 전 점검: 하위 에이전트 점검을 한 번에 실행한다
---
Chapter $ARGUMENTS에 대해 하위 에이전트 점검을 한다. 원고는 고치지 않는다.
1. 이번 작업에서 새로 쓰거나 바꾼 문장 목록을 git diff로 만든다.
2. 장 PR(장 정비, 장 개정, 장 작성)이면 여섯 확인을 맡는 에이전트를 모두 동시에 부른다(이슈 #66 0단계, D-129): flow-reviewer(편집, 장 전체, 내용 정리표), reader-novice(교정, 장 전체, sonnet), fact-checker(기술, 명령과 예제를 실제 실행), reader-expert(기술, 장 전체), practice-checker(실습, 본문과 실습 파일과 검사를 실제 실행), production-checker(제작, 그림과 빌드된 HTML). 장이 아닌 작은 변경이면 바뀐 내용에 맞는 점검만 부른다(비용 규칙). 각 에이전트에 다음을 넘긴다.
   - 범위: src/chapters/ch$ARGUMENTS.html(바꾼 절 이름). flow-reviewer, reader-novice, reader-expert는 장 전체. 모두 REVIEW_RULES.md와 BOOK_STANDARD.md(있으면)를 함께 넘긴다
   - 바꾼 문장 목록(flow-reviewer), 장의 주장(BOOK_SPEC.md, flow-reviewer), 관련 research/ 파일(fact-checker), 관련 실습 파일과 docs/example-facts.md(practice-checker), 그림 번호와 빌드된 chapters/ch$ARGUMENTS.html, 그림 시안 확인용 HTML(production-checker)
   - 보고 형식: 각 에이전트 파일의 "출력 형식"
   - 대시보드: 각 에이전트를 부르기 직전 python tools/dashboard.py start <에이전트> "ch$ARGUMENTS <범위>", 결과를 받은 직후 python tools/dashboard.py end <에이전트> "<필수 n, 권장 n>"
3. 각 결과를 reviews/agents/YYYY-MM-DD-ch$ARGUMENTS-<에이전트>.md로 저장한다. flow-reviewer의 내용 정리표는 reviews/flow/ch$ARGUMENTS-flow.md에도 저장한다(같은 장은 덮어쓰고 날짜를 갱신, 고친 뒤 다시 점검하면 끊긴 곳이 0인 표로 갱신).
4. 모든 의견을 하나의 표로 모아 반영, 보류, 작가 확인으로 나눈다. 필수는 반영하거나 작가 확인으로만 둘 수 있다(보류 불가). 내용 정리표의 끊김은 필수다.
5. PR 설명에 에이전트 실행 기록 표(에이전트, 실행 여부, 필수 건수, 반영 여부)와 여섯 확인 표(REVIEW_RULES.md "여섯 확인")를 넣는다. 맡는 에이전트가 실행되지 않은 확인이 있으면 그 사실을 적는다(editor가 병합 불가로 판정).
6. 표를 보여 주고 끝낸다.
