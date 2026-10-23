# 2장 역할 검토: 실무자 3차 읽기(2026-10-22, 이슈 #66)
- 대상: src/chapters/ch02.html(7dbc9d7). 대조: research/ch02-sources.md(S25~S45), ch01-sources.md, examples/expense-app/reference/, check.py, acceptance/test_cr07.py, docs/example-facts.md, 그림 1-2, 부록 실습 2, 3
- 고칠 문장 비율 5 ÷ 157 = 3.2%(표, 그림 4건 별도). 절별: tool-scope 1, instruct-enforce 1, example 3
- check_all 통과(작업 2, 3 공백은 6장 정비 대상)

## 총평
1. 권한 평가 순서, 권한 모드, PreToolUse, PostToolUse 종료 코드 2, 강제 수단의 두 한계, 훅 실행 확인이 실제와 맞음. 장 사이 링크 10곳 대상 id 있음.
2. 예제 검사 장치가 본문만큼 막지 못함(실행 확인): check.py는 testsRun으로 세는데 건너뛴 시험도 들어감(@unittest.skip 두 건 → run 2, fail 0, skipped 2). 수용 기준 5(test_5)는 data/projects.csv의 임시 복사본을 등록 처리가 바꾸지 않는지만 봄. 2차에서 권한 문장 철회(R14). 실제 확인은 commit 확인 때 git status, git diff.
3. 정해진 것과 부딪히는 제안 없음.

## 발견
| 발견 | 위치 | 제안 | 확신 |
|---|---|---|---|
| 1. 인용 주체가 틀림 | instruct-enforce "같은 문서는 CLAUDE.md를…" | 메모리 문서와 설정 점검 문서 | 높음 |
| 2. 건너뜀과 일부 삭제를 막는다고 읽힘 | example 실습 문단 | 0건만 실패, 일부 삭제나 건너뜀은 commit 확인 때 git diff | 높음 |
| 3. 수용 기준 5를 원본 자료 보호처럼 씀 | example | git status로 data/ 확인, 수용 기준 5는 등록 처리 시험 | 높음 |
| 4. 허용으로 읽기만 제한할 수 없음 | tool-scope 목록 | 수정 도구를 금지하거나 목록에서 제외 | 중간 |
| 5. 자동 메모리 기본 켜짐, 이유 문장 | example | 기본으로 켜져 있지만 기록 구성 요소로 삼지 않음 | 중간 |

## 표, 그림
| 발견 | 위치 | 제안 | 확신 |
|---|---|---|---|
| T1. 권한 전체에 Bash 규칙 제약 | 표 2-1 권한 | Bash 규칙과 파일 규칙의 제약을 나눔 | 높음 |
| T2. 검사 스크립트 범위를 넓게 | 표 2-4 검증 이유 | 한 건도 실행되지 않은 통과를 막음 | 높음 |
| T3. 로컬 commit "되돌리기 어려움" | 표 2-5 commit | 확정 지점 | 중간 |
| T4. 없는 지시를 지시 수단으로 | 표 2-5 단위 테스트 행 | 없음(명령 절에 명령만) | 중간 |

## [기준]
주장 줄, 원칙 Q-113과 같음. R1 단어, 같은 장 링크, CR 0. 장 틀, 캡션 근거, 표 세트 통과. 발견 2, 3은 R14(필수 수정 등급), 발견 1은 출처 표기

## 선택(세지 않음)
dontAsk에서 확인 요청은 거부, 표 2-2 소개에 PreToolUse, 모드가 allow보다 먼저, "기본적으로", 실습 링크 #lab-2, 쉼표

## 범위 밖
check.py가 skipped도 실패로 보거나 기대 건수 확인(examples 변경, 작가 확인). example-facts.md 수용 기준 5를 "등록 처리가 data/projects.csv를 변경하지 않음"으로

## 미해결(fact-checker)
Bash(git push *), Bash(git diff *)가 인자 없는 명령과 일치하는지
