---
description: PR 전 점검: 하위 에이전트 점검을 한 번에 실행한다
---
Chapter $ARGUMENTS에 대해 하위 에이전트 점검을 한다. 원고는 고치지 않는다.
1. 이번 작업에서 새로 쓰거나 바꾼 문장 목록을 git diff로 만든다.
2. fact-checker, flow-reviewer, figure-checker(그림을 바꿨을 때만), reader-novice, alt-reviewer를 동시에 부른다. 각 에이전트에 다음을 넘긴다.
   - 범위: src/chapters/ch$ARGUMENTS.html(바꾼 절 이름)
   - 바꾼 문장 목록(flow-reviewer), 관련 research/ 파일(fact-checker), 그림 번호(figure-checker, alt-reviewer), 장 명세와 그림 명세(alt-reviewer)
   - 보고 형식: 각 에이전트 파일의 "출력 형식"
3. 각 결과를 reviews/agents/YYYY-MM-DD-ch$ARGUMENTS-<에이전트>.md로 저장한다.
4. 모든 의견을 하나의 표로 모아 반영, 보류, 작가 확인으로 나눈다. 필수는 반영하거나 작가 확인으로만 둘 수 있다(보류 불가).
5. 표를 보여 주고 끝낸다.
