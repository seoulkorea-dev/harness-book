# ch03 명세 검토 editor (2026-10-20)

범위: docs/specs/ch03-spec.md, docs/specs/fig3-1-spec.md. 기준: AUTHOR_PREFS.md, D-104~D-110, FIGURE_STYLE.md, v1.1-backlog 3장, 2장 선례(Q-003~Q-008). 명세가 작가 결정과 취향을 어긴 곳 없음. 목차, 핵심 정의, 그림 방침, 문체 규칙 변경 없음.

| 발견 | 위치 | 근거 | 제안 | 확신 | 판정 | 처리 |
|---|---|---|---|---|---|---|
| "훅 → check.py"는 check.py 실행 주체가 불분명(훅이 실행하는 것처럼 읽힘) | fig3-1-spec 관계표 3행 | AUTHOR_PREFS 그림(주체) | "구현 에이전트 → check.py: 작업 단위 마무리 때 실행" | 높음 | 필수 | 반영 |
| 표 3-5 2행 "실패해도 되돌릴 수 있어 지시로 둠"은 research 근거 없음 | ch03-spec 보강 목록 | AUTHOR_PREFS(확인하지 못한 사실) | 이유를 빼고 "지시, 강제 장치 없음" | 높음 | 필수 | 반영 |
| 행렬 칸 문구 미확정(사람 행의 "병합" 제거) | fig3-1-spec | FIGURE_STYLE 7절, 표 3-2, 3-3 | 칸 문구를 표로 확정 | 중간 | 권장 | 반영(그림 안 문구 표) |
| 사람 승인 범위 변경이 표 3-2, 3-3, 그림, aria-label에 걸침 | ch03-spec | 2장 선례, D-104 | 한꺼번에 맞춘다고 명세에 적음 | 중간 | 권장 | 반영 |
| aria-label과 캡션의 제품명 금지, 캡션 근거 괄호 | fig3-1-spec | FIGURE_STYLE 5, 8절, D-095 | 쓰지 않을 것에 추가 | 높음 | 권장 | 반영 |
| 결론 제목 "다음 작업 단위로", 부제와 중단 문구의 개조체 확정 | fig3-1-spec | FIGURE_STYLE 5, 7절 | 문구 확정 | 높음 | 권장 | 반영 |
| 표 3-3 "설정"과 그림 "설정 폴더" | ch03.html 표 3-3 | FIGURE_STYLE 5절 | "설정 폴더"로 통일 | 높음 | 권장 | 반영 |
| 표 3-6 훅 행은 구성 확인으로 한정, practice.html은 범위 밖 | ch03-spec 확인 방법 | C3-5, backlog 실습 4 | "/hooks 목록에 보임" | 중간 | 권장 | 반영 |
| refs 절 항목 추가를 보강 목록에 | ch03-spec | 2장 선례, D-108 | 한 줄 추가 | 중간 | 권장 | 반영 |
| "작업 단위" 처음 정의 위치 | ch03-spec 용어표 | 정의 전 사용 금지 | "이 장 example(Chapter 6에서 이어서)" | 중간 | 권장 | 반영 |
| 완료 기준에 AUTHOR_QUEUE, HANDOFF, research 기록 | ch03-spec 완료 기준 | CLAUDE.md 끝낼 때 | 추가 | 높음 | 권장 | 반영(DECISIONS는 작가 확인 후라 제외) |
| 첫 문단 둘째 문장 삭제 | ch03-spec 작가 확인 1 | Q-004 선례 | 권장안으로 진행, Q-009 | 높음 | 작가 확인 | AUTHOR_QUEUE Q-009 |
| 그림 3-1 시안 선택(권장 A) | fig3-1-spec | D-107 | 시안 뒤 editor, alt-reviewer 의견으로 | 중간 | 작가 확인 | AUTHOR_QUEUE Q-010 |

명세 결론: 수정 후 진행(필수 2건 반영 완료)
