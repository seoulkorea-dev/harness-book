---
description: 독자 시뮬레이션. 사용법 /reader-sim ch02
---
대상 장: $ARGUMENTS
1. reader-novice와 reader-expert 에이전트를 각각 3회(회차 1, 2, 3) 병렬로 실행한다. 각 실행은 서로의 결과를 보지 않는다.
2. 6개 결과 파일(reviews/reader/$ARGUMENTS-*.json)을 읽고 같은 인용 문장(또는 같은 절의 같은 유형)을 묶는다.
3. 채택 기준: 같은 독자 유형에서 3회 중 2회 이상, 또는 두 유형 모두에서 나온 지적.
4. BOOK_SPEC.md의 해당 장 "주장"과 독자 요약을 비교해 일치도(상, 중, 하)와 빠진 내용을 적는다.
5. reviews/reader/$ARGUMENTS-summary.md에 `채택 지적 표(절, 인용, 유형, 독자, 회차)`, `주장 일치도`, `질문 상위 5개`, `이탈 지점`을 쓰고, 채택 건수와 버린 건수를 맨 위에 적는다.
원고는 고치지 않는다.
