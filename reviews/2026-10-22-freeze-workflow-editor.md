# 검수: 작업 체계 마지막 변경과 동결(freeze-workflow, PR #72, 이슈 #66 0단계)

## 1차(2026-10-22)
결론: **병합 불가** (필수 1, 권장 3, 작가 확인 0). 필수 1건은 한 줄 수정.

| # | 판정 | 위치 | 발견 | 근거 | 제안 | 확신 | 처리 |
|---|---|---|---|---|---|---|---|
| 1 | 필수 | docs/staged-claude/agents/flow-reviewer.md 64행 | 삭제한 figure-checker를 가리키는 옛 참조 | 이슈 #66 0단계, D-129 | "production-checker 몫" | 높음 | 반영 |
| 2 | 권장 | production-checker.md 24, 33, 37행 | 해설표 누락을 필수로 판정하나 해설표 유지 여부는 1단계 기준서에서 작가가 정함 | 이슈 #66 1단계 | 조건을 달거나 필수에서 뺌 | 중간 | 반영(기준서 전까지 조건부 필수로 분리) |
| 3 | 권장 | editor, reader-novice, fact-checker, review-chapter | 병합 전의 BOOK_STANDARD.md와 용어표를 "있으면", "확정 전에는"으로 가리킴 | 이슈 #66 1단계 | 지금 형태 유지, 1단계에서 정리 | 높음 | 유지(1단계에서 정리) |
| 4 | 권장 | .claude/commands/next.md, review-chapter.md, .claude/agents/editor.md | 병합과 --apply-only 사이에 옛 판이 지운 에이전트를 가리킴 | D-119 | 병합 직후 --apply-only, 그 전에는 /next 쓰지 않음을 HANDOFF에 | 중간 | 반영 |

확인한 항목: 이슈 0단계 표(editor 총평, 가장 큰 문제 셋, 점검 질문, 등급, 수정 전과 수정 후. flow-reviewer 내용 정리표 열과 문맥 점검. fact-checker, reader-expert 조건과 근거. practice-checker 실제 실행과 판정만. reader-novice 교정. production-checker 화면, 각주, 링크, 코드, 빌드 HTML) 반영. 여섯 확인 표 일치. src/ 변경 없음, BOOK_STANDARD.md는 참조만. autorun 반영 형식(새 에이전트 tools 줄, 기존 판 tools와 model 같음, 명령에 권한 키 변경 없음), 에이전트 수 8. check_all 종료 코드 0.
