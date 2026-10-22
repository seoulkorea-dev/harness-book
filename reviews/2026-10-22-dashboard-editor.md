# 검수: 작업 대시보드(dashboard, PR #75, 이슈 #66 작가 요청 15:00)

결론: **병합 가능** (필수 0, 권장 3, 작가 확인 2)

확인: check_all 통과, autorun --selftest 통과, src/와 .claude/ 변경 없음, 바뀐 파일 8개 모두 요청 범위. 본문 구성 5가지(지금, 에이전트 표 10행 7열, 장별 표 14행 9열, 오늘 병합 PR, 멈춤)와 갱신 방법(start, end, refresh, now, six, stop, resume, gh issue edit로 덮어쓰기, --write-file, autorun 단위 시작과 끝, next와 review-chapter 한 줄) 구현. 이슈 #74 본문에서 editor 행이 "진행 중"으로 바뀐 것 확인.

Q-095 평가: 2장 옛 인용 15는 Neo 수치와 같음. 3장 CR은 원문 HTML 전체의 \bCR\b가 11(Neo 수치), 코드와 경로를 뺀 본문의 \bCR\b가 9, R12 기준 17. 기준 차이이고 R12 기준이 정비에 맞음(작가 확인).

| # | 판정 | 위치 | 발견 | 근거 | 제안 | 확신 | 처리 |
|---|---|---|---|---|---|---|---|
| 1 | 권장 | docs/staged-claude/commands/next.md | CRLF로 저장돼 diff 잡음 | diff --strip-trailing-cr로 2줄만 추가 | LF로 저장 | 높음 | 반영(next, review-chapter LF) |
| 2 | 권장 | AUTHOR_QUEUE Q-095 | 분해 수치("본문 문단 12, 목록, 표, 캡션 5")는 검증 못 함 | 직접 센 값(원문 11, 본문 9, 17) | 확인된 값만 | 중간 | 반영 |
| 3 | 권장 | tools/dashboard.py 여섯 확인 열 | 1장도 "아니오"라 모순으로 읽힘 | 표 출력 | D-129 이후부터 기록한다는 설명 | 중간 | 반영 |
| 4 | 작가 확인 | Q-094 | 설정 허용 목록 추가는 권한 확대라 작가가 함 | D-119 | 작가가 permissions.allow에 추가 | 높음 | Q-094 |
| 5 | 작가 확인 | Q-095 | CR 수 기준 | 위 평가 | R12 기준 유지 권장 | 높음 | Q-095 |
