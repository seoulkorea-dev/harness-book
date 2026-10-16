# 경비 정산 미니 웹 앱(실습 저장소)

「하네스 엔지니어링: 모델을 에이전트로 만드는 설계」 Chapter 3의 CR-07 예제와 부록 실습에서 쓰는 실습 자료입니다.
Python 표준 라이브러리만 사용하므로 추가 패키지를 설치하지 않습니다.

- 앱 실행: `python app.py` 뒤 http://localhost:8000
- 단위 테스트: `python -m unittest discover tests -q`
- 전체 검사(단위 테스트와 수용 시험): `python check.py`

이 폴더는 하네스가 없는 기준 상태입니다. 규칙 문서(CLAUDE.md), 권한과 훅(.claude/settings.json), 검토 하위 에이전트(.claude/agents/reviewer.md), 작업 단위 목록(tasks.json)은 부록 실습 2~5에서 직접 만듭니다.
reference/ 폴더에는 실습에서 만든 파일과 비교할 참고본이 있습니다. 참고본은 이름 끝에 .example이 붙어 있어 Claude Code가 설정으로 읽지 않습니다.

기준 상태에서는 단위 테스트가 통과하고, CR-07 수용 시험 5건 가운데 3건이 실패합니다. 실습 순서와 실행 기록은 RUNLOG.md에 있습니다.
