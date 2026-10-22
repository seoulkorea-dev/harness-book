# docs/staged-claude

.claude/(agents, commands, settings.json)의 새 판을 두는 곳입니다(이슈 #34, D-119). 같은 경로로 두고 PR로 병합하면 tools/autorun.py가 .claude/에 반영하고 이 폴더를 지웁니다. 허용 경로: agents/<이름>.md, commands/<이름>.md, settings.json. 권한에 닿는 변경(settings.json의 deny와 ask 삭제, allow 추가, 그 밖의 키, 머리말의 tools 등)은 자동 반영하지 않습니다.

이번 판: editor, fact-checker, flow-reviewer에 검수 규칙(REVIEW_RULES.md, D-127, 이슈 #66) 절 추가.
