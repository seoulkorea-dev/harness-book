---
description: 장 작성: 확인된 명세대로 원고와 그림을 쓰고 점검한 뒤 PR을 만든다
---
Chapter $ARGUMENTS를 작성한다(작가가 확인한 장 명세와 그림 명세 기준).
1. 작업 브랜치를 만든다(git switch -c ch$ARGUMENTS-write).
2. 그림마다 배치가 다른 시안 두 개를 SVG로 만들고, 두 시안을 넣은 확인용 HTML 한 장(reviews/agents/YYYY-MM-DD-ch$ARGUMENTS-figures.html)을 만든다. 작가가 시안을 고를 때까지 그림을 원고에 넣지 않는다. 그림은 FIGURE_STYLE.md를 따른다.
3. src/의 원고를 쓰고, 작가가 고른 그림을 넣는다.
4. python tools/check_all.py를 통과시킨다.
5. /review-chapter $ARGUMENTS 를 실행한다.
6. 필수 의견을 반영하고 다시 check_all을 통과시킨다. 권장 의견은 반영, 보류, 작가 확인으로 나눈다.
7. HANDOFF.md를 갱신하고 커밋한 뒤 브랜치를 push하고 PR을 만든다. PR 설명에 check_all 출력 원문과 의견 분류 표를 넣는다.
