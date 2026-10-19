---
description: 검수 지침 반영: 지침대로 고치고 반영 n / n을 확인한다
---
검수 문서 $ARGUMENTS를 반영한다.
1. 문서를 읽고, "교체" 코드 상자의 내용만 옮긴다. 표의 이유 칸과 설명은 옮기지 않는다.
2. 지시하지 않은 변경은 하지 않는다.
3. python tools/check_all.py와 python tools/check_review.py $ARGUMENTS를 통과시킨다(반영 n / n).
4. 검수 문서를 reviews/에 별도 커밋으로 등록하고, HANDOFF.md를 갱신한다.
5. 작가 확인을 받아 같은 PR에 push하고, 출력 원문을 PR에 댓글로 남긴다.
