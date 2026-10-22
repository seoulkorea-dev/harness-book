# 검수 1차: 자동 실행 자가 복구와 상태 알림(PR #52, afd665e, 이슈 #34)

결론: 병합 불가(필수 3, 권장 6, 작가 확인 2)

| 구분 | 발견 | 처리(6738951) |
|---|---|---|
| 필수 1 | 권한 확대 차단이 알려진 키 블랙리스트(env, apiKeyHelper, additionalDirectories, agents의 tools, commands의 allowed-tools 우회) | 허용 목록 방식: settings.json은 deny와 ask 추가, allow 삭제만, 그 밖의 키 변경은 차단. agents, commands 머리말의 tools, allowed-tools, disallowedTools, hooks, permissionMode, mcpServers 변경 차단, 새 에이전트는 tools 필수. selftest에 env, apiKeyHelper, additionalDirectories, tools, allowed-tools 사례 |
| 필수 2 | 반영 뒤 이 폴더의 .claude/가 갱신되지 않음 | 반영 성공 시 지금 main이고 깨끗하면 pull, 아니면 상태 이슈에 안내. selftest에 main에서 반영 뒤 로컬 .claude/가 새 판인지 확인 |
| 필수 3 | HANDOFF 기록 누락(결과 줄, 진행 기록 행, 브랜치 줄, 4장 줄의 #34) | 반영 |
| 권장 1 | 실패한 반영을 단위마다 되풀이 | 실패한 staged 트리 해시를 logs/autorun_stage_failed.txt에 기억해 같은 내용이면 건너뜀 |
| 권장 2 | 다시 시작을 조용히 건너뜀 | main을 받지 못하면 로그와 상태 댓글 |
| 권장 3 | next.md와 명세 문구 차이 | 명세를 "안내만"으로 고침 |
| 권장 4 | 긴 보고 본문의 같은 말로 오분류 | 오류 출력과 500자 이하 결과에서만 판정 |
| 권장 5 | 다시 시작 실행 경로 시험 없음 | Q-080 유지(다음 autorun 실행 때 확인) |
| 권장 6 | README만 있는 폴더, tasklist 숫자 겹침, 빈 임시 폴더 | 폴더만 정리하는 반영, tasklist CSV pid 열 비교, 임시 부모 폴더 삭제 |
| 작가 확인 | 다시 시작 실제 확인 미룸, D-119와 Q-079 | Q-080, Q-077에 허용 목록 방식 한 줄, Q-079 |
