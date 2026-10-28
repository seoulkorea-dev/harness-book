# 문서 현황(harness-book)

저장소의 문서와 설정을 역할과 기준 여부로 정리한 목록입니다(2026-10-25 기준, main 339749d). 원고와 빌드 결과물(src/, chapters/, appendix/, index.html, assets/, examples/)은 목록에서 뺐습니다.

상태 구분
- **기준**: 지금 작업의 기준이 되는 문서. 내용이 부딪히면 이 문서를 따릅니다.
- **기록**: 작업 결과와 결정을 남기는 문서. 작업할 때마다 갱신합니다.
- **보조**: 기준 문서를 쓰기 위한 도구, 서식, 설정.
- **옛 문서**: 이전 체계의 문서. CLAUDE.md가 "정리 예정"이라고 한 것으로, 플레이북과 설계서와 다르면 플레이북과 설계서를 따릅니다. 지우지는 않았습니다.

## 1. 기준 문서(읽는 순서)

| 순서 | 문서 | 역할 | 상태 |
|---|---|---|---|
| 1 | book-kit/book/PLAYBOOK.md | 원고 원칙과 규칙, 최종 점검표(25장). 모든 원고 작업의 기준. 공통 원본을 ../book-kit에서 직접 읽음(D-147). 루트의 NEW_BOOK_PLAYBOOK.md는 위치 안내만 | 기준 |
| 2 | BOOK_SPEC.md | 이 책의 선택(목차, 용어표, 예제, 그림, 비교 도서)과 플레이북 예외 | 기준 |
| 3 | HARNESS_SETUP.md | 작업 진행 방식(한 장의 순서, 중단 없이 진행하는 규칙, 멈추는 경우) | 기준 |
| 4 | CLAUDE.md | 작성 세션 안내(읽을 순서, 역할, 끝낼 때) | 기준 |
| 5 | DECISIONS.md | 작가 결정(D-번호). BOOK_SPEC과 함께 의견 충돌의 최상위 기준 | 기준, 기록 |

## 2. 기록 문서

| 문서 | 역할 | 갱신 |
|---|---|---|
| HANDOFF.md | 인계 메모. 맨 위 "지금 상태"에 진행과 다음 할 일 | 단위마다 |
| docs/AUTHOR_QUEUE.md | 작가 확인 목록(Q-번호), 작가 검수 목록 | 생길 때마다 |
| FAILURES.md | 두 번째 나온 실패와 추가한 장치 | 실패가 반복될 때 |
| DASHBOARD.md | 장별 진행 표 | 예전 체계에서 갱신(최근 단위는 HANDOFF.md에 기록) |
| docs/example-facts.md | 예제(경비 정산 변경 요청 사항)의 사실 | 예제가 바뀔 때 |
| docs/specs/(34개) | 장 명세, 그림 명세 | 장마다 |
| research/(16개) | 장별 출처와 확인 날짜, bibliography.json(인용 키) | 조사와 점검마다 |
| reviews/agents/(300개) | 하위 에이전트 보고(편집장, 사실, 실습, 제작 점검) | 점검마다 |
| reviews/flow/(13개) | 옛 흐름 검토의 내용 정리표 | 예전 체계 |
| reviews/(그 밖 약 80개) | 옛 편집 검토서와 검수 기록 | 예전 체계 |
| docs/metrics.md | 작업 측정 기록 | 예전 체계 |

## 3. 작업 도구와 설정

### 3.1 에이전트(.claude/agents/)

| 에이전트 | 역할 | 상태 |
|---|---|---|
| chief-editor | 편집장. 장마다 1회 통독 판정 | 기준(HARNESS_SETUP 2장). 다섯 정의는 book-kit/book/agents에서 tools/sync_kit.py로 가져옴(D-147) |
| fact-checker | 사실 점검 | 기준 |
| practice-checker | 실습과 예제 점검 | 기준 |
| production-checker | 제작 점검(그림, 화면, 링크) | 기준 |
| researcher | 1차 출처 조사 | 기준 |
| editor | 옛 정식 검수(여섯 확인) | 보관(docs/archive/agents/, D-147) |
| flow-reviewer | 옛 흐름 검토 | 보관(같음) |
| reader-novice | 옛 초보 독자 검토 | 보관(같음) |

### 3.2 명령(.claude/commands/)과 스킬(.claude/skills/)

| 이름 | 역할 | 상태 |
|---|---|---|
| /next, /autopilot | 한 단위 진행, 반복 진행 | 기준(본문에 옛 대시보드, autorun 단계가 남아 있음) |
| /handoff | 인계 메모 갱신 | 기준 |
| /plan-chapter, /write-chapter, /review-chapter, /apply-review | 옛 장별 절차(editor, 여섯 확인 기준) | 옛 문서 |
| 스킬 book-structure, fact-check, ko-book-style, example-design, originality-check | 규칙 요약 | 보조(ai-book 시절 규칙이 섞여 있음. 플레이북과 다르면 플레이북) |

### 3.3 도구(tools/, lint/, .github/)

| 파일 | 역할 | 상태 |
|---|---|---|
| tools/build.py | src/로 쪽 파일 빌드, 위첨자 인용과 참고 문헌 생성 | 기준 |
| tools/check_all.py | 전체 검사 7항목(빌드, 금칙어, 번호, 구조, 문체, 그림 안 이름, 검수 규칙) | 기준 |
| lint/(check_numbers, check_structure, check_style, check_rules, banned.txt, rules_applied.txt) | check_all이 부르는 검사 | 기준 |
| tools/hooks/(session_start, pre_bash, stop_check), tools/hook_lint.py | 세션 시작, 명령 전, 수정 뒤, 끝날 때 훅 | 기준 |
| tools/check_tasks.py | 예제 작업 단위 확인(R6) | 보조 |
| tools/similarity_check.py | 비교 도서 유사도 | 보조 |
| tools/verify_site.py, .github/workflows/ | CI 검사, 배포 확인 | 기준 |
| tools/dashboard.py, tools/autorun.py, tools/check_review.py | 옛 대시보드 이슈 갱신, 자동 실행기, 옛 검수 문서 검사 | 옛 문서(D-130 뒤 쓰지 않음) |
| templates/(chapter-spec, figure-spec, issue-report) | 장 명세, 그림 명세, 이슈 보고 서식 | 보조(옛 용어 "CR" 남음) |

## 4. 옛 기준 문서(docs/archive/old-standards/로 옮김, D-147)

| 문서 | 내용 | 대체한 곳 |
|---|---|---|
| STYLE.md | 문체 규칙 | 플레이북 6장, ko-book-style |
| FIGURE_STYLE.md | 그림 스타일 | 플레이북 10장 |
| diagram_guide.md | 다이어그램 제작 가이드 | 플레이북 10장 |
| AI_DIAGRAM_GUIDE.md | AI 다이어그램, 일러스트 생성 참고 | 플레이북 10장(참고 자료) |
| BOOK_STANDARD.md | 1단계 기준서 | 플레이북, BOOK_SPEC.md |
| REVIEW_RULES.md | 검수 규칙 R1~R19, 여섯 확인 | 플레이북 20장, 22장, 25장(check_rules.py 출력에는 R 번호가 남음) |
| AUTHOR_PREFS.md | 작가 결정과 취향 | DECISIONS.md, BOOK_SPEC.md |
| RUNBOOK.md | 집필 자동화 실행 절차(ai-book 시범 시절) | HARNESS_SETUP.md |
| docs/external-review-prompt.md | 외부 검토 프롬프트 | 편집장 1회(HARNESS_SETUP 2장) |
| proposals/2026-10-15-ch03-example-spec.md | 3장 예제 설계 제안 | docs/example-facts.md, docs/specs/ |

- 2026-10-28 작가 결정으로 위 문서 가운데 STYLE.md부터 RUNBOOK.md까지 여덟 개를 docs/archive/old-standards/로 옮겼습니다(맨 위에 보관 문서 표시). 옛 에이전트 정의와 동기화 전의 다섯 정의는 docs/archive/agents/에 있습니다.
