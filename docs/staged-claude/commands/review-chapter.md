---
description: PR 전 점검: 하위 에이전트 점검을 한 번에 실행한다
---
Chapter $ARGUMENTS에 대해 하위 에이전트 점검을 한다. 원고는 고치지 않는다.
1. 이번 작업에서 새로 쓰거나 바꾼 문장 목록을 git diff로 만든다.
2. 바뀐 내용에 맞는 점검만 동시에 부른다(비용 규칙): flow-reviewer와 reader-novice는 장 개정과 흐름 재점검 때 항상(D-117, 둘 다 장 전체를 통독), fact-checker는 사실 문장을 바꿨을 때만, figure-checker와 alt-reviewer는 그림을 바꿨을 때만. reader-expert는 장 개정과 장별 정비(이슈 #66 ②)마다 필수(실무 관점의 R1, R3, R4, R8. 장 전체). fact-checker는 장별 정비마다 필수(본문의 명령과 예제 확인을 실제 실행). 각 에이전트에 다음을 넘긴다.
   - 범위: src/chapters/ch$ARGUMENTS.html(바꾼 절 이름). flow-reviewer, reader-novice, reader-expert는 장 전체. 모두 REVIEW_RULES.md를 함께 넘긴다
   - 바꾼 문장 목록(flow-reviewer), 장의 주장(BOOK_SPEC.md, flow-reviewer), 관련 research/ 파일(fact-checker), 그림 번호(figure-checker, alt-reviewer), 장 명세와 그림 명세(alt-reviewer)
   - 보고 형식: 각 에이전트 파일의 "출력 형식"
3. 각 결과를 reviews/agents/YYYY-MM-DD-ch$ARGUMENTS-<에이전트>.md로 저장한다. flow-reviewer의 논지 사슬 표는 reviews/flow/ch$ARGUMENTS-flow.md에도 저장한다(같은 장은 덮어쓰고 날짜를 갱신, 고친 뒤 다시 점검하면 끊긴 곳이 0인 표로 갱신).
4. 모든 의견을 하나의 표로 모아 반영, 보류, 작가 확인으로 나눈다. 필수는 반영하거나 작가 확인으로만 둘 수 있다(보류 불가). 논지 사슬 끊김은 필수다.
5. 에이전트 실행 기록 표(에이전트, 실행 여부, 필수 건수, 반영 여부)를 만들어 PR 설명에 넣는다. 필수 에이전트가 실행되지 않았으면 그 사실을 적는다(editor가 병합 불가로 판정).
6. 표를 보여 주고 끝낸다.
