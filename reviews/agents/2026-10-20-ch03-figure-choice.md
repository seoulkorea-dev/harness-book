# 그림 3-1 시안 선택(2026-10-20, editor와 alt-reviewer)

시안: reviews/agents/2026-10-20-ch03-figures.html. 두 에이전트 모두 시안 A를 고름.

| 발견 | 위치 | 근거 | 제안 | 확신 | 출처 | 처리 |
|---|---|---|---|---|---|---|
| "*" 줄이 두 줄 | A, B 맨 아래 | FIGURE_STYLE 7절, AUTHOR_PREFS | 한 줄로 | 높음 | editor(필수) | 반영 |
| "다음 단위"가 본문 용어 "다음 작업 단위"와 다름 | A 흐름 띠 끝 상자 | FIGURE_STYLE 5절 | 상자 폭 늘림 | 높음 | editor(필수) | 반영 |
| 교체 시 aria-label, 표 3-3을 새 구성에 맞춤 | ch03 그림 3-1, 표 3-3 | D-109 | 해설표 행대로 고침 | 높음 | editor(필수) | 반영 |
| commit 확인 → 다음 작업 단위 화살표에 "사람 확인 후" 없음 | A 흐름 띠 | FIGURE_STYLE 4절 | 선 위 글자 | 중간 | editor, alt-reviewer | 반영 |
| 흐름 띠에서 단계별 주체가 안 보임 | A 흐름 띠 | AUTHOR_PREFS(주체) | 상자마다 주체 표기 | 높음 | alt-reviewer | 반영(구현 에이전트, 편집 뒤 자동 실행, 사람) |
| 사람 행이 권한과 행동을 섞음, "관리"는 명세에 없는 말 | A 행렬 사람 행 | 명세 구성 요소 표 | "승인(commit 확인, push)", "작성(사람만)" | 중간 | editor, alt-reviewer | 반영 |
| 검증 기준 상자와 check.py 실행 단계의 연결 | A | 결론 두 절의 연결 | 같은 연한 파랑으로 연결 | 중간 | alt-reviewer | 반영(두 곳 모두 연한 파랑, 본문 문장으로 check.py가 수용 시험을 실행함을 밝힘) |
| B는 다음 작업 단위, 중단, 금지 연결이 없음, 검토 단계가 명세에 없음 | B | 명세 관계표 | B 제외 | 높음 | editor, alt-reviewer | B 제외 |
| 경고 색 0, 상자 요약 0, 곡선 0, 제품명 0, 최소 20px, 폭 960, 선과 글자 겹침 0 | A, B | FIGURE_STYLE 3, 4, 5, 9절 | 없음 | 높음 | editor | 통과 |

선택: 시안 A(이유는 docs/AUTHOR_QUEUE.md Q-010)
