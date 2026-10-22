# 2장 역할 검토: 실무자 2차 읽기(2026-10-22, 이슈 #66)
- 대상: 다시 쓴 src/chapters/ch02.html(ba0fab5). research/ch01, ch02-sources.md, examples/expense-app/reference/, docs/example-facts.md와 대조
- 고칠 문장 비율: 7 ÷ 158 = 4.4%(표, 그림 9건 별도). 절별 고칠 문장: 첫머리 1, components 1, tool-scope 2, instruct-enforce 2, example 1

## 총평
1. 권한 모드, PreToolUse 순서, PostToolUse 종료 코드 2, 강제 수단의 두 한계, 1장 Stop 훅 연결, 훅 실행 확인이 실제 동작과 맞음(S25, S28, S40, S42).
2. 남은 핵심: 장 사이 링크(권한 모드는 ch10#perm-claude, 샌드박스는 ch09#isolation), 예제가 기대는 나머지 장치(기본 권한 모드의 확인, 수용 기준 5), 편집 뒤 훅의 범위(Edit|Write 밖의 수정에서는 실행 안 됨).
3. 표 2-7 기록 확인 기준이 예제 사실과 맞지 않음(작업 1은 처음부터 true, 에이전트 commit 없음).

## 1차 대비
대부분 해결. 남음: 압축이 기록의 이유에서 빠짐, 표 2-2에 PreToolUse 없음, 반복 실패 중단과 웹 접근 위험의 9장 연결(선택)

## 발견
| 발견 | 위치 | 근거 | 제안 | 확신 |
|---|---|---|---|---|
| 1. 권한 모드 연결 장 | tool-scope "권한 모드의 선택 기준은 Chapter 9" | 모드 값은 ch10#perm-claude | 10장으로 | 높음 |
| 2. 샌드박스 링크 | instruct-enforce | 정의는 ch09#isolation | 링크 변경 | 높음 |
| 3. 표 2-2 소개 문장이 그림과 어긋남 | tool-scope "그림에 그리지 않은 두 가지" | 하위 에이전트 카드, "*" 줄 | 문장 고침 | 높음 |
| 4. 예제가 기대는 장치 | example 실습 문단 | allow에 Edit 없음, 수용 기준 5 | 기본 모드의 확인과 수용 기준 5(example-facts에 모드 없음, 작가 확인) | 중간 |
| 5. 압축이 기록의 이유에서 빠짐 | components 기록 | ch01-sources 자동 압축 | 같은 세션 안의 압축도 | 중간 |
| 6. 편집 뒤 훅 범위를 넓게 씀 | instruct-enforce "빠짐없이 실행되게" | matcher Edit\|Write, Bash 수정은 해당 없음 | "훅에 지정한 도구로 편집할 때마다" | 높음 |
| 7. [기준] 예제를 다른 이름으로 먼저 부름 | 첫머리 "경비 정산 예제" | R12, 기준서 6절 | 첫머리에 정식 이름 | 중간 |

## 표, 그림
| 발견 | 위치 | 제안 | 확신 |
|---|---|---|---|
| T1. 기록 확인 기준 | 표 2-7 | "에이전트가 통과 값을 true로 바꾼 작업 단위(작업 2~4)마다 commit" | 높음 |
| T2. 방지 장치에 맞지 않는 훅 | 표 2-6 검증 | 편집 뒤 훅은 단위 테스트만 실행. 수용 시험 실행 건수 확인으로 | 높음 |
| T3. 권한 모드 행 연결 장 | 표 2-2 | Chapter 10 | 높음 |
| T4. 웹 접근 도구를 /context로 볼 수 없음 | 표 2-7 도구 | /permissions, /mcp(fact-checker 실행 확인) | 중간 |
| T5. 권한 확인 행에 PreToolUse 없음 | 표 2-2 | "PreToolUse 훅이 먼저 실행된 뒤" | 중간 |
| T6. 단계 이름이 그림 1-2와 다름 | 그림 2-1 검증 카드 "완료 기준 확인" | "도구 실행, 최종 응답 전" | 중간 |
| T7. 검증 행 제약 | 표 2-1 | 지정한 도구 편집에만 실행, Stop 훅 없으면 완료 전 확인은 지시에 기댐 | 중간 |
| T8. 예제의 권한 모드 | 표 2-4 권한 | 작가 확인(example-facts에 없음) | 중간 |
| T9. 통과 값 변경 방지가 지시뿐 | 표 2-6 역할 | commit 확인 때 tasks.json 변경 확인 | 중간 |

## 선택(세지 않음)
핵심 내장 도구 정의와 MCP 지연 로드 구분, 모드가 allow보다 먼저, PreToolUse allow도 deny는 막음, 자동 메모리는 기기에만 남음, ./ 경로 기준, Edit 금지가 Write에도 적용, Ctrl+O, WebFetch 금지는 curl을 막지 않음, 반복 실패 중단 9장

## 범위 밖(practice-checker, 다른 장)
- 훅 명령이 python 고정(macOS python3, R17)
- 편집 뒤 훅이 작업 2 동안 기존 테스트를 깨면 작업 3을 미리 할 수 있음(R6 정비와 함께)
- 훅 명령 $CLAUDE_PROJECT_DIR 기준
- ch06 multi-agent의 "Chapter 2에서 정의한 하위 에이전트" 링크는 ch02#components인데 정의는 tool-scope

## 미해결
- Bash(git push *), Bash(git diff *)가 인자 없는 명령과 일치하는지(fact-checker)
- 예제의 권한 모드를 example-facts.md에 넣을지(작가 확인)
