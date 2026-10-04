---
description: 한 장의 검수 일괄 실행. 사용법 /review-chapter ch02
---
대상 장: $ARGUMENTS
1. `python tools/build.py`, lint 3종, 금칙어 grep을 실행하고 출력 원문을 기록한다.
2. fact-checker, style-reviewer 에이전트를 병렬로 실행한다.
3. /reader-sim $ARGUMENTS 를 실행한다.
4. 세 결과를 합쳐 reviews/$ARGUMENTS-review.md를 만든다: 읽은 범위, 검사 출력 원문, 수정 필요(위치, 인용, 수정안), 권장, 사용자 결정 필요.
5. 수정 필요 항목은 writer 에이전트에 넘길 수 있게 번호를 붙인다. 원고는 고치지 않는다.
