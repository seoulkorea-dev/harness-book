# 검수: 마지막 체계 조정(final-adjust, PR #77, 이슈 #66 Neo 06:12)

결론: **병합 가능** (필수 0, 권장 3, 작가 확인 1)

실행: check_all 종료 코드 0(정비 전 장의 기존 경고만), dashboard.py refresh --dry 정상(reader-expert 행 없음, 자동 실행 "사용 중지", 오늘 병합 PR에 원고 변경 열과 비율). src/ 변경 없음.

| 요청 | 반영 | 위치 |
|---|---|---|
| reader-expert를 fact-checker에 합침(실무 정확성, R1, R3, R4, R8, R13, R16, 점검 질문 10개 표) | 반영 | staged fact-checker |
| 에이전트 8 → 7, 기술 확인은 fact-checker 하나 | 반영 | .claude/agents 7개, REVIEW_RULES 37행, 대시보드 |
| 원고 작업만, 한 단위 = 장 하나(기준서 예외) | 반영 | staged next |
| editor 재검수 최대 2회, 그 뒤 멈추고 남은 필수 기록 | 반영 | next, autopilot, editor |
| /autopilot만, autorun 사용 중지(파일은 둠, HANDOFF) | 반영 | autopilot, HANDOFF, D-130, 대시보드 |
| 대시보드 원고 변경 여부 | 반영 | dashboard.py |
| 기록 | 반영 | D-130, Q-096, HANDOFF, README |

| # | 판정 | 위치 | 발견 | 근거 | 제안 | 확신 | 처리 |
|---|---|---|---|---|---|---|---|
| 1 | 권장 | .claude/ 현행 next, review-chapter, editor | 병합과 --apply-only 사이에 reader-expert 참조가 남음 | D-119 | 병합 직후 --apply-only, 그 전에는 /next와 /review-chapter를 쓰지 않음 | 높음 | 반영(병합 직후 실행) |
| 2 | 권장 | DASHBOARD.md | 옛 생성물에 reader-expert 행 | refresh --dry에는 없음 | 병합 전 refresh --write-file | 높음 | 반영 |
| 3 | 권장 | .claude/agents/reader-expert.md | 직접 삭제(staged에는 삭제 경로 없음) | D-119 | README와 PR 설명에 밝힘 | 중간 | 유지(README에 밝힘) |
| 4 | 작가 확인 | Q-096, CLAUDE.md | autorun 사용 중지와 --apply-only, CLAUDE.md 옛 이름 | | 권장안대로 진행 | 높음 | Q-096 |
