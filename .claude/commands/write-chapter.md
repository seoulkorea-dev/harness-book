---
description: 장 작성: 원고와 그림을 쓰고 점검한 뒤 PR을 만든다
---
Chapter $ARGUMENTS를 작성한다(작가가 확인한 개요 기준).
1. 작업 브랜치를 만든다(git switch -c ch$ARGUMENTS-write).
2. src/의 원고와 그림을 쓴다. 그림은 FIGURE_STYLE.md를 따른다.
3. python tools/check_all.py를 통과시킨다.
4. fact-checker, flow-reviewer, figure-checker, reader-novice를 동시에 부르고, 보고 문안을 reviews/agents/에 저장한다.
5. 의견을 반영, 보류, 작가 확인으로 나누어 반영하고 다시 check_all을 통과시킨다.
6. HANDOFF.md를 갱신하고 커밋한 뒤, 작가 확인을 받아 브랜치를 push하고 PR을 만든다. PR 설명에 check_all 출력 원문과 의견 분류 표를 넣는다.
