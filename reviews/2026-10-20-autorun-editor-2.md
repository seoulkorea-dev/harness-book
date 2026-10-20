# 2차 검수: 자동 반복 실행(브랜치 autorun, 초안 PR #24, 커밋 cda8621)

**결론: 병합 불가** (필수 1, 권장 4, 작가 확인 1)

1차 필수 1(진전 없음, CI 실패, 검사 실패 판정)과 필수 2(write_stop의 작업 트리, 브랜치, 파일 범위 확인)는 코드상 반영됨. 그러나 --selftest가 시작부터 죽을 것으로 보임.

## 시험 출력
이 검수 세션에서도 `python tools/autorun.py --selftest` 실행이 거부됨(settings.json 허용 목록에 없음). 코드를 읽어 판단.

## 필수
| # | 발견 | 위치 | 근거 | 제안 | 확신 |
|---|---|---|---|---|---|
| 1 | selftest가 ROOT를 아직 없는 tmp/work로 바꾼 뒤 cwd=ROOT로 git init, clone을 실행해 FileNotFoundError. 멈춤 기록 시험이 실행되지 못함 | tools/autorun.py selftest | 이슈 #22 완료 기준, 1차 필수 2 | clone 뒤에 ROOT를 바꿈. 고친 뒤 일반 터미널의 --selftest 출력 원문을 PR에 붙이는 것을 병합 조건으로 함 | 높음 |

## 권장
| # | 발견 | 위치 | 근거 | 제안 | 확신 |
|---|---|---|---|---|---|
| 2 | 정상 결과 문장에 "usage limit" 등이 있으면 한도로 판정 | failure_reason | 이슈 | 실패한 실행에서만 문자열 검사, selftest 사례 추가 | 높음 |
| 3 | Windows에서 open "w"가 줄 끝을 CRLF로 바꿔 파일 전체 변경이 될 수 있음 | write_stop | 1차 필수 2 의도 | newline="", numstat로 한 줄 확인 | 중간 |
| 4 | PR 브랜치가 로컬에 없으면 switch 실패 | write_stop | 이슈 | 기록 전 git fetch origin <br> | 중간 |
| 5 | Co-Authored-By 모델 이름 고정 | CO_AUTHOR | 정확성 | 모델 이름을 빼는 안 검토 | 낮음 |

## 작가 확인
| # | 발견 | 위치 | 근거 | 제안(권장안) | 확신 |
|---|---|---|---|---|---|
| 6 | 단위 세션이 selftest를 실행하려면 settings.json 허용 추가가 필요(권한 방침 변경) | .claude/settings.json | 이슈 #22 할 일 2 "그대로" | 허용을 넣지 않고, selftest는 일반 터미널에서 실행해 출력을 PR에 붙임 | 중간 |

## 반영 처리(작성 쪽)
| 항목 | 처리 |
|---|---|
| 필수 1 | 반영: clone을 tmp에서 실행한 뒤 ROOT 변경 |
| 권장 2 | 반영: 실패한 실행에서만 한도 문구 검사, selftest 사례 추가 |
| 권장 3 | 반영: newline="", 줄 끝 유지, selftest에서 numstat "1 0 HANDOFF.md" 확인 |
| 권장 4 | 반영: 기록 전 git fetch origin <br> |
| 권장 5 | 보류: 작성 세션의 첨부 지침이 "Claude Opus 5.5"라 유지 |
| 작가 확인 6 | AUTHOR_QUEUE Q-025 |
| 시험 출력 | 단위 세션에서 실행 불가 → 멈춤(작가가 일반 터미널에서 --selftest 실행 필요) |
