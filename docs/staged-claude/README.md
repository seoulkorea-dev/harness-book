# docs/staged-claude

.claude/(agents, commands, settings.json)의 새 판을 두는 곳입니다(이슈 #34, D-119). 같은 경로로 두고 PR로 병합하면 python tools/autorun.py --apply-only가 .claude/에 반영하고 이 폴더를 지웁니다.

이번 판(이슈 #66 06:12 작가 승인, D-130): fact-checker(reader-expert 통합), editor(재검수 최대 2회, 기술 확인 담당), commands/next(작성 범위, 재검수 2회), review-chapter(reader-expert 제외), autopilot(재검수 2회, autorun 반복 실행 사용 중지). .claude/agents/reader-expert.md는 이 PR에서 지움(에이전트 7개).
