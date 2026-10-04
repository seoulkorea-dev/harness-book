---
description: 검수 결과 반영. 사용법 /apply-review ch02
---
reviews/$ARGUMENTS-review.md의 "수정 필요" 항목을 writer 에이전트로 반영한다.
- 항목마다 고친 뒤 훅 결과가 통과해야 다음 항목으로 넘어간다.
- "사용자 결정 필요" 항목은 고치지 않고 목록으로 남긴다.
- 끝나면 `git diff --stat`과 항목별 반영 여부 표를 출력한다.
