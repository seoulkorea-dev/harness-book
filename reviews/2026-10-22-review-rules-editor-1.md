# 검수 1차: 규칙과 자동 검사 승격(PR #67, 09c145f, 이슈 #66 ①)

결론: 병합 불가(필수 1, 권장 5, 작가 확인 1)

| 구분 | 발견 | 처리(45bcf6f) |
|---|---|---|
| 필수 1 | tools/__pycache__/autorun.cpython-312.pyc가 커밋에 들어감 | git rm --cached, .gitignore에 __pycache__/와 *.pyc |
| 권장 2 | Neo 보충(버전 주석 이름) 미반영 | STYLE 5절 aside.version-note, CSS. 지금 aside.footnote 8곳은 장 정비 때 |
| 권장 3 | R1 검사가 주장 줄을 빼고, 빠르다/느리다가 없음 | 주장 줄 포함, 빠르다/느리다는 editor와 reader-expert로 REVIEW_RULES에 밝힘 |
| 권장 4 | R6 강제 판정이 주석 줄에도 걸릴 수 있음 | 주석 줄을 빼고 읽음 |
| 권장 5 | R4 탐지 범위가 문서에 없음 | REVIEW_RULES R4 탐지 칸에 밝힘 |
| 권장 6 | AUTHOR_PREFS 장 틀 "CR 적용" | Q-083에 포함(작가 영역 문구) |
| 작가 확인 7 | R6 단계 적용 | Q-085 |

함께 반영한 Neo 보충(이슈 #66 댓글): reader-expert 장마다 필수(review-chapter, next 새 판), fact-checker Bash(직접 반영, Q-084), 에이전트 실행 기록 표(editor 새 판에서 확인).
