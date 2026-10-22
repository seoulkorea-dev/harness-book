# docs/staged-claude

.claude/(agents, commands, settings.json)의 새 판을 두는 곳입니다(이슈 #34, D-119). 같은 경로로 두고 PR로 병합하면 tools/autorun.py가 .claude/에 반영하고 이 폴더를 지웁니다.

이번 판(이슈 #66 0단계, D-129, 작업 체계 마지막 변경): editor(편집자 방식, 총평, 수정 전과 수정 후, 여섯 확인), flow-reviewer(흐름, 문맥, 내용 정리표), fact-checker(실행 확인, 조건과 근거로 확정), reader-expert(장 PR마다 필수), reader-novice(교정), practice-checker(신규, alt-reviewer 대체), production-checker(신규, figure-checker 대체), commands/next.md, review-chapter.md, write-chapter.md. alt-reviewer.md와 figure-checker.md는 이 PR에서 .claude/agents/에서 지움(에이전트 수 8 유지).
