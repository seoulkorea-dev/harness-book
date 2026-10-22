# 경비 정산 미니 웹 앱: 변경 요청 사항(docs/CR.md) 구현

## 목적
재무팀이 월말 결산에서 프로젝트별 경비를 집계할 수 있도록, 정산 요청에 프로젝트 코드를 기록한다(docs/CR.md).

## 읽는 순서
1. docs/CR.md(수용 기준)
2. DECISIONS.md
3. tasks.json
4. HANDOFF.md(있으면)

## 작업 순서
- tasks.json에서 "통과"가 false인 첫 작업 단위만 수행한다. 작업 5의 "통과" 값은 변경하지 않는다.
- 작업 단위를 마치면 python check.py를 실행하고, 출력이 tasks.json에 적은 그 단위의 "확인 방법"을 충족하면 그 단위의 "통과" 값만 true로 변경한다. 다음 작업 단위가 맡은 수용 시험의 실패는 이 판정에 넣지 않는다.
- 확인 방법을 충족하면 commit 전에 reviewer 하위 에이전트에게 바뀐 파일 목록(git status 출력)과 함께 수용 기준 대조를 요청한다.
- 완료 보고에는 python check.py의 출력 원문과 reviewer의 대조 보고를 포함한다.
- 대조 보고 뒤 그 단위의 변경을 commit한다(commit은 사람 확인 후).

## 수정 범위
- 수정할 수 있음: expense/, app.py, tests/, tasks.json의 "통과" 값, HANDOFF.md
- 수정하지 않음: data/, acceptance/, check.py, CLAUDE.md, DECISIONS.md, .claude/
- 수용 시험이 실패하면 시험이 아니라 구현을 고친다.

## 중단 규칙
- 지금 작업 단위의 확인 방법에 든 시험이 세 번 연속 실패하면 중단하고 HANDOFF.md를 작성한다.
- 세션을 마칠 때 HANDOFF.md에 현재 상태, 읽을 문서, 미결정, 다음 작업, 확인 명령을 적는다.

## 명령
- 단위 테스트: python -m unittest discover tests -q
- 전체 검사: python check.py
- 앱 실행: python app.py (http://localhost:8000)
- macOS, Linux에서 python 명령이 없으면 python3를 사용한다.
