# 참고 문헌 형식 정리 제작 점검(production-checker, PR #84)

범위: appendix/references.html, tools/build.py bib_entry, research/bibliography.json, chapters/ch01.html 위첨자 링크, assets/style.css ol.bib

| 발견 | 위치 | 근거 | 제안 | 확신 |
|---|---|---|---|---|
| (편집 권고) ReAct 항목의 연도가 링크 안 매체 칸 "ICLR 2023(arXiv 공개 2022.10.6)"과 링크 밖 ", 2023."에 두 번 나옴. 형식 규칙 위반은 아님 | references.html bib-5, bibliography.json react | 전부터 있던 구성, 규칙 5 발행일은 링크 밖 | 작가 결정(매체 "ICLR"로 줄이는 안), 이번 PR에서 바꾸지 않아도 됨 | 중간 |
| (편집 권고) 항목 전체가 링크색, 발행일만 본문색. 긴 제목은 overflow-wrap: anywhere로 작은 화면에서 줄바꿈됨 | assets/style.css 39행, 251~253행 | 작은 화면 가독성 | 조치 없음, li:target 배경과 링크색 대비를 눈으로 확인 | 낮음 |

점검 결과: 12항목 모두 견본 형식, 주소 글 노출과 "열람" 없음(research/*-sources.md의 장별 출처 기록은 대상 아님), 발행일은 링크 밖, ch01의 #bib-1~#bib-12가 모두 대상 있음, 같은 자료 한 번, check_rules 경고만.

필수 0건, 권고 2건.
