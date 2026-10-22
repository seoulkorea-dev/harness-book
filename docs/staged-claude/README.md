# docs/staged-claude

.claude/(agents, commands, settings.json)의 새 판을 두는 곳입니다(이슈 #34, D-119). 같은 경로로 두고 PR로 병합하면 tools/autorun.py가 .claude/에 반영하고 이 폴더를 지웁니다. 허용 경로: agents/<이름>.md, commands/<이름>.md, settings.json. settings.json에서 권한을 넓히는 변경(deny나 ask 삭제, allow 추가, 훅이나 기본 모드 변경)은 자동 반영하지 않습니다.
