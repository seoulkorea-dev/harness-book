# ch10 fact-checker (2026-10-20, v1.0 보강)

범위: 주장 줄, 표 10-3, 표 10-4, 원칙과 점검 질문. 문서: Codex Slash commands, Rules, Agent approvals and security(learn.chatgpt.com으로 이전된 주소), Claude Code Sandboxing, memory, permissions(2026-10-20). 대조: settings.example.json.

| 발견 | 위치 | 근거 | 제안 | 확신 | 심각도 |
|---|---|---|---|---|---|
| Codex /status는 활성 모델, 승인 정책, 쓰기 가능 경로, 남은 컨텍스트를 보여 주며 샌드박스 모드와 network_access는 항목에 없음 | 표 10-4 2행 | Codex Slash commands /status | 확인 기준을 승인 정책과 쓰기 가능 경로로 좁히고 네트워크는 config.toml로 | 높음 | 필수(반영) |
| Claude Code의 "거부함"은 git push … 형태의 요청에 한정(git -C . push는 불일치) | 표 10-4 3행 | permissions 문서 | 단서 추가 | 중간 | 권장 |
| /permissions, forbidden 규칙과 승인 정책, 샌드박스 기본 꺼짐과 sandbox.enabled, AGENTS.md를 CLAUDE.md에서 불러오는 방법(@AGENTS.md), CR 예제의 push와 웹 접근 금지 | 표 10-3, 10-4, fail 첫 문단 | Rules, Agent approvals, Sandboxing, memory, permissions, 예제 파일 | 없음 | 높음 | 일치 |
| 새 표에 발표 주체와 참고 자료 링크 없음, 참고 자료에 Sandboxing과 Slash commands 없음, 확인일 갱신 | 표 10-3, 10-4, 참고 자료 | 형식 | 주체 표기, 문서명 추가 | 중간 | 권장 |
| 예제 settings.example.json에는 sandbox 키가 없음(본문의 두 제품 설정 예와 다름) | 표 10-3 2행 | 예제 파일 | PR에 기록 | 중간 | 참고 |
| 샌드박스는 네이티브 Windows에서 동작하지 않음 | 표 10-3 2행 | Sandboxing | v1.1 검토 | 중간 | 참고 |
| /status의 실제 출력 문구는 문서에 예시가 없어 미확인 | 표 10-4 2행 | Slash commands | 설치 버전에서 확인 | 낮음 | 참고(미확인) |

필수 1, 권장 3, 참고 4, 확인한 사실 문장 13개
