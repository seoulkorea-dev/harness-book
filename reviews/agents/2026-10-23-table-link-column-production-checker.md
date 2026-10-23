# PR #90 제작 점검(production-checker, 2026-10-23)

## 결론: 필수 0, 권장 3(기준 문서 잔존 표현 3곳), 참고 2

실행한 명령 출력 요약
- `python3 tools/check_all.py`: 빌드, 금칙어, 번호, 구조, 문체, 그림 안 이름, 검수 규칙 모두 통과. 정비 전 장의 R1, R3 경고와 R6 공백 2건(작업 2, 3)은 이번 변경과 무관
- `python3 lint/check_rules.py`: 규칙 적용 장 ch01, 실패 0. 정비 전 장은 경고만
- 변경 범위는 ch01 src와 빌드 결과, 기준 문서, check_rules, editor 새 판, DECISIONS, HANDOFF. 범위 밖 변경 없음

| 발견 | 위치 | 근거 | 제안 | 확신 |
|---|---|---|---|---|
| (권장) STYLE.md 41행 옛 규칙 "해설 열("본문의 절")은 …"이 53행과 어긋남 | STYLE.md 41행 | D-136, 기준서 9절 | 삭제하거나 "표에 본문 연계 열을 두지 않음(D-136)" | 높음 |
| (권장) .claude/agents/editor.md 42행은 현재 판(옛 "위치(관련 절)") | .claude/agents/editor.md | 새 판은 docs/staged-claude에만 있음 | PR 설명에 "적용 전" 표기 | 중간 |
| (권장) production-checker 지침 24행과 templates/figure-spec.md 23행이 "구성 요소 / 무엇인가 / 본문의 절" | .claude/agents/production-checker.md, templates/figure-spec.md | D-136, FIGURE_STYLE 73행 | 세트 A로 | 높음 |
| (참고) 표 1-2는 3열, 표 1-5는 2열, table-wrap 안. 360px에서도 이전보다 읽기 쉬움(CSS와 마크업 기준 판단) | chapters/ch01.html | | 조치 불필요 | 중간 |
| (참고) 소개 문장, 캡션, 설명 줄이 표와 맞음. 옛 열 이름 없음 | ch01 표 1-2, 1-5 | 기준서 10절 | 조치 불필요 | 높음 |

## 링크 안내
- ch02.html#components(ch01 37행), #tool-scope(38행)가 본문에 이미 있어 끊기지 않음. 표에 있던 같은 장 절 이름은 원래 링크가 아니었음

## 새 패턴 `절$|본문|다루는 곳`
- src 전체 표 열 이름에서 오탐 없음. 걸린 것은 모두 본문 연계 열(2장 표 2-2, 3장 표 3-3, 4~10장 해설표, 11장 표 11-2, 11-4의 "본문의 절", 시작하며 "먼저 볼 절")
- 미탐 1건: 3장 표 3-1 "다루는 장". `다루는 (곳|장)`으로 넓히기 권함
- 시작하며 "다루는 내용"은 본문 연계가 아닌 내용 열

## 기준 문서 사이 세트 A, C
- 세트 A, C 열 이름은 기준서, FIGURE_STYLE, STYLE 53행, REVIEW_RULES, editor 새 판, D-136이 같음. 어긋남은 위 권장 3건뿐
- 열 수 하한 2는 check_rules가 검사하지 않음(1열 표 없음, 실무상 문제없음)
