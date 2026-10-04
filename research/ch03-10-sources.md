# Chapter 3~10 사실 확인 기록

확인일: 2026-10-04. 원문을 직접 열어 확인한 내용만 적습니다. 1장 기록(ch01-sources.md)의 S1(Rajasekaran 외), S2(Lopopolo)는 다시 적지 않습니다.

## S3. Young, J., Effective harnesses for long-running agents (Anthropic, 2025-11-26)
- URL: https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
- 사용: 5, 6, 7장
  - 새 세션은 이전 세션의 기억 없이 시작함(7장)
  - 실패 1: 앱 전체를 한 번에 구현하려다 컨텍스트 소진, 다음 세션은 반쯤 구현되고 기록되지 않은 기능에서 시작(5장)
  - 실패 2: 일부 기능 구현 뒤 시작한 세션이 프로젝트 전체 완료로 판단(5장)
  - 기능 목록 200개 이상, 모두 failing으로 표시, 한 번에 기능 하나. 점진적 방식이 결정적이었다고 밝힘(5장)
  - JSON은 Markdown보다 모델이 부적절하게 변경하거나 덮어쓰는 일이 적었음(5장)
  - 충분한 시험 없이 완료 표시, 단위 테스트와 curl은 했으나 처음부터 끝까지 동작하지 않음을 인식 못함, 브라우저 자동화로 시험하자 개선(6장)
  - 진행 파일과 git 이력으로 상태 파악, 설명 있는 커밋과 진행 요약으로 잘못된 변경을 되돌리고 복구(7장)

## S4. Anthropic, Claude Code Docs (확인 2026-10-04)
- Configure permissions: https://code.claude.com/docs/en/permissions
  - allow, ask, deny 규칙, 평가 순서 deny → ask → allow, 처음 일치한 규칙이 결정, allow가 deny의 예외를 만들 수 없음(8장)
  - 권한 규칙은 모델이 아니라 Claude Code가 적용, CLAUDE.md는 허용 범위를 바꾸지 않음(4장)
  - 권한 모드 6개: default, acceptEdits, plan, auto, dontAsk, bypassPermissions(9장)
  - bypassPermissions는 컨테이너, VM 같은 격리 환경에서만 사용(8장)
  - Bash 규칙은 명령 문자열만 대조, git -C . push는 git push * 규칙과 불일치, 샌드박스 사용 안내(8장)
  - 권한과 샌드박스는 보완 계층, 샌드박스는 Bash 등 셸 명령과 하위 프로세스에 운영 체제 수준 적용(8, 9장)
  - 기본 접근 범위는 실행한 작업 디렉터리(9장)
- How Claude remembers your project: https://code.claude.com/docs/en/memory
  - 세션마다 새 컨텍스트, CLAUDE.md와 자동 메모리가 세션 사이 지식 전달(7장)
  - CLAUDE.md는 강제 설정이 아닌 컨텍스트, 막아야 할 동작은 PreToolUse 훅(3, 4장)
  - 구체적으로 작성(예: API handlers live in src/api/handlers/), 200줄 이내 권장, 모순 시 임의 선택 가능(3장)
  - 추가 시점 4가지(같은 실수 두 번째, 코드 리뷰 지적, 지난 세션 정정 반복, 새 팀원)(3장)
  - 다단계 절차나 일부 코드에만 해당하는 지침은 Skill이나 경로별 규칙(3장)
  - 관리형, 사용자, 프로젝트, 로컬의 범위, 상위 디렉터리부터 이어서 읽음, CLAUDE.md 없으면 AGENTS.md 읽음(v2.1.277 이상)(9장)
  - 대화에서만 준 지시는 압축 뒤 사라질 수 있음, CLAUDE.md에 추가(7장)
  - 훅은 정해진 시점에 셸 명령으로 실행, Claude의 판단과 무관하게 적용(4장)
  - managed settings의 sandbox.enabled 키(9장 설정 예)
- 문서 색인 llms.txt: Manage costs effectively 설명(토큰 사용량 추적, 팀 지출 한도, 컨텍스트 관리, 모델 선택)(8장)

## S5. Anthropic, Prompting best practices (확인 2026-10-04)
- ch02-sources.md S1과 같은 문서. 8장: 되돌리기 어려운 동작 전 확인 지시 예(파괴적 동작, 되돌리기 어려운 동작, 다른 사람에게 보이는 동작)

## S6. OpenAI, Codex 문서 (확인 2026-10-04)
- Custom instructions with AGENTS.md: https://developers.openai.com/codex/guides/agents-md
  - 작업 전에 AGENTS.md를 읽음, ~/.codex의 AGENTS.override.md 또는 AGENTS.md, 디렉터리마다 AGENTS.override.md → AGENTS.md → 대체 이름 순(9장)
- Agent approvals and security: https://developers.openai.com/codex/agent-approvals-security
  - 로컬은 운영 체제 수준 샌드박스와 승인 정책, 기본값은 네트워크 차단, 쓰기는 작업 공간으로 제한(8, 9장)
  - Auto 프리셋: --sandbox workspace-write --ask-for-approval on-request
  - 작업 공간 밖 수정과 네트워크가 필요한 명령은 승인 요청
  - sandbox_workspace_write.network_access 설정(스페인어판 확인)
  - untrusted 승인 정책 미지원(프랑스어판 확인, 9장 버전 주석)
- Sandbox: https://developers.openai.com/codex/concepts/sandboxing
  - 승인은 Codex가 멈추는 시점, 샌드박스는 명령이 접근할 수 있는 파일과 네트워크(8, 9장)
- Permissions: https://developers.openai.com/codex/permissions
  - 기본 권한 프로필 :read-only, :workspace, :danger-full-access(9장)
- Config basics: https://developers.openai.com/codex/config-basic
  - 사용자 설정 ~/.codex/config.toml, 프로젝트 .codex/는 신뢰한 프로젝트에서만 읽음(9장)

## 작가 경험(10장, 6장, 7장, 3장)
- NEW_BOOK_PLAYBOOK.md 0장: 73차 검수, 다섯 교훈(큰 결정 반복 변경, 첫 문단 틀 세 번 변경, 연결 단절 26건, 검수 문서 혼입, 설명 없는 링크, 반복 실수 lint화)
- 이 저장소: DECISIONS.md D-001~D-031(31건), .claude/agents 6, commands 3, skills 5, lint 4종, GitHub Actions(book-check, verify-site)
- 작가의 작업 방식: 완료 보고 대신 명령 출력 원문 요구(작가 진술), 작성과 검수 채팅 분리, 인계 메모
- 5, 8, 9장: 작가 경험 미확인으로 작가 경험 문단 없음(D-031)

## 2차 검수 반영 때 추가 확인(2026-10-04)
- Claude Code, Choose a permission mode(https://code.claude.com/docs/en/permission-modes): v2.1.283 이상에서 auto 모드가 대화형 터미널과 VS Code 세션의 기본 시작 모드. 릴리스 노트 v2.1.284(2026-09-28): 모든 요금제와 제공자에서 auto로 시작, permissions.defaultMode가 우선(9장 버전 주석)
- Codex, Rules(https://developers.openai.com/codex/rules): 규칙 기능은 실험 단계, ~/.codex/rules/default.rules, prefix_rule의 decision 값 forbidden은 확인 없이 요청을 막음, 여러 규칙이 일치하면 forbidden > prompt > allow(9장 예제)
