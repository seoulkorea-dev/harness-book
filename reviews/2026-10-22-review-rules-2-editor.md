# 검수: R13~R17, 판정 등급, 장별 점검 질문(PR #70, 브랜치 review-rules-2)

결론: **병합 가능**(필수 0, 권장 4, 작가 확인 0)

## 확인한 것
- 이슈 #66 Neo 보충 두 댓글(12:12, 12:15)과 대조: R13~R17(규칙, 판단 질문, 담당), R5 판단 질문, 판정 등급 세 행, 공식 권고 수치 주의, 장별 점검 질문 10개가 REVIEW_RULES.md와 editor, reader-expert에 옮겨짐
- 에이전트 새 판은 의도한 줄만 추가, 머리말(tools) 그대로
- 변경은 규칙 문서, 에이전트 새 판 셋, staged README, D-128, HANDOFF뿐
- check_all 통과

## 필수
없음.

## 권장
| 발견 | 위치 | 처리 |
|---|---|---|
| REVIEW_RULES.md 줄바꿈이 섞임 | REVIEW_RULES.md | LF로 통일 |
| editor 첫 항목 "R1~R12" | staged editor.md | "R1~R17" |
| "새 유형이 나오면 R13, R14…" | REVIEW_RULES.md 머리말 | "R18, R19…" |
| HANDOFF 행이 검수 전에 이 문서를 가리킴 | HANDOFF.md | 이 문서를 같은 경로로 저장 |

참고: flow-reviewer의 R5 질문과 R13은 댓글의 담당에는 없지만 흐름 점검에 도움이 되고 판정에 영향이 없어 범위 안으로 봄.
