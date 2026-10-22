# 예제 사실(R7)

모든 장, 그림 해설표, 부록 실습은 경비 정산 시스템 개편 변경 요청 사항(이하 변경 요청 사항)의 사실을 이 문서에서 가져옵니다(REVIEW_RULES R7, 이슈 #66). 원본은 examples/expense-app/의 파일이며, 이 문서와 원본이 다르면 원본을 따르고 이 문서를 고칩니다. "정비 예정"은 이슈 #66 ②(6장 정비, R6)에서 바뀔 항목입니다.

## 변경 요청 사항
- 내용: 정산 요청 화면에 프로젝트 코드 선택 항목 추가(examples/expense-app/docs/CR.md, 파일 이름은 코드 안 이름이라 그대로)
- 요청 부서: 재무팀, 요청일 2026-10-05, 사유: 프로젝트별 경비 집계를 월말 결산에 반영
- 결정: D-012(조건부 수용, 프로젝트 코드는 인사 시스템이 일 1회 갱신하는 data/projects.csv 사용)
- 수용 기준(acceptance/test_cr07.py로 시험): 1 등록 화면에서 프로젝트 코드 선택(project_code), 2 목록에 없는 코드는 거부하고 사유에 코드 표시, 3 목록 화면에 프로젝트 코드 표시, 4 코드가 없는 기존 요청도 목록에 표시, 5 data/projects.csv는 변경하지 않음
- 구현 전 상태: 수용 시험 1, 2, 3 실패, 4, 5 통과. 단위 테스트(tests/) 3건 통과(project_code 시험 0건)
- 검사 스크립트(check.py): 단위 테스트와 수용 시험을 실행하고, 두 폴더 모두 실패 0건, 건너뜀 0건, 수용 시험은 정한 수(5건)만큼 실행, 단위 테스트에 이름에 project_code가 든 시험 1건 이상일 때만 종료 코드 0. 출력은 "tests: 실행 n건, 실패 n건, 건너뜀 n건, project_code 시험 n건", "acceptance: 실행 n건, 실패 n건, 건너뜀 n건(정한 수 5건)". 수용 시험 파일을 통째로 지우거나 일부를 건너뛰게 하면 실패하지만, 시험 내용을 약하게 바꾸는 것은 잡지 못함(그래서 수정 금지 규칙과 commit 확인이 함께 필요)
- 수용 기준 5의 시험(test_5)은 등록 처리가 임시 복사본의 projects.csv를 바꾸지 않는지 봄. 에이전트가 data/를 직접 수정하는 것은 시험이 아니라 금지 규칙이 막음

## 작업 단위(reference/tasks.example.json)
| 작업 | 내용 | 담당 | 완료 기준 | 확인 방법 | 통과 값(시작) |
|---|---|---|---|---|---|
| 작업 1 | 프로젝트 코드 조회 방식 합의 | 사람(승인자) | 인사팀과 조회 방식과 갱신 주기 합의 | 결정 기록 D-012 | true(이미 완료) |
| 작업 2 | 데이터 모델에 프로젝트 코드 항목 추가 | 에이전트 | 정산 요청 데이터에 항목 추가, 기존 데이터 유지 | python check.py의 수용 시험 4, 5 통과(공백: 기존 동작만 시험해 구현 전에도 통과, R6. 수용 시험 추가는 작가 확인 Q-118) | false |
| 작업 3 | 기존 단위 테스트 갱신 | 에이전트 | 변경된 데이터 모델의 테스트 반영(project_code 시험 추가, 기존 시험 통과) | python check.py의 tests 실패 0건, project_code 시험 1건 이상(구현 전에는 project_code 시험 0건이라 실패, 3장 정비 PR #88) | false |
| 작업 4 | 정산 요청 화면에 선택 항목 추가 | 에이전트 | 화면에서 프로젝트 코드 선택 가능, 목록에 없는 코드 거부 | python check.py의 수용 시험 1, 2, 3 통과 | false |
| 작업 5 | 통합 테스트 시나리오 추가 | 에이전트 작성, 사람 승인 | 프로젝트별 집계 시나리오 초안(정비 예정: 초안 작성과 승인 완료를 나눔) | 사람 승인(통과 값은 사람이 변경) | false |
- 처리 규칙: 통과 값이 false인 첫 단위만 수행, 작업 5의 통과 값은 에이전트가 변경하지 않음(CLAUDE.example.md). 작업 3, 4의 번호는 Q-034로 맞바꿈
- 세션: 부록 실습 5 세션 1(작업 2, 작업 3), 실습 6 세션 2(작업 4). 실행 기록은 examples/expense-app/RUNLOG.md(실행 전)

## 규칙 문서(reference/CLAUDE.example.md, 32줄)
- 여섯 절: 목적, 읽는 순서, 작업 순서, 수정 범위, 중단 규칙, 명령
- 읽는 순서: docs/CR.md, DECISIONS.md, tasks.json, HANDOFF.md(있으면)
- 수정할 수 있음: expense/, app.py, tests/, tasks.json의 통과 값, HANDOFF.md. 수정하지 않음: data/, acceptance/, check.py, CLAUDE.md, DECISIONS.md, .claude/
- 작업 단위를 마치면 python check.py, 출력이 그 단위의 확인 방법을 충족하면 그 단위의 통과 값만 true(작업 2, 3을 마친 시점에는 작업 4가 맡은 수용 시험 1, 2, 3이 실패해 check.py 전체는 종료 코드 1), 완료 보고에 출력 원문, 확인 방법을 충족하면 commit 전에 reviewer 하위 에이전트에게 바뀐 파일 목록(git status 출력)과 함께 수용 기준 대조 요청, 작업 단위를 마치면 commit(사람 확인 후)
- 중단: 지금 작업 단위의 확인 방법에 든 시험이 세 번 연속 실패하면 중단하고 HANDOFF.md 작성

## 권한(reference/settings.example.json)
- 허용: 단위 테스트, python check.py, git status, git diff
- 확인 요청: git commit
- 금지: data/, acceptance/, check.py, CLAUDE.md, DECISIONS.md, .claude/의 수정, git push, WebFetch, WebSearch
- 훅: 파일 편집(Edit, Write) 뒤 프로젝트 폴더($CLAUDE_PROJECT_DIR)로 이동해 단위 테스트 실행, 실패하면 종료 코드 2

## 검토 에이전트(reference/reviewer.example.md)
- 이름 reviewer, 도구 Read, Grep, Glob, 수용 기준마다 충족, 미충족, 확인 불가를 근거 파일과 줄 번호와 함께 보고, 파일은 수정하지 않음

## 사람의 몫
- 수용 기준 확정, 작업 1 합의, 작업 5 승인, commit 확인, push
