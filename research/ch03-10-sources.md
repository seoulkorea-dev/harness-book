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

## 용어 보강 때 추가 확인(2026-10-15)
- Claude Code, Manage costs effectively(https://code.claude.com/docs/en/costs): /usage의 Session 항목에 현재 세션 토큰 사용량, 구독 요금제는 같은 화면에 요금제 사용량 표시, 상태 줄 설정으로 지속 표시, /context로 컨텍스트 점유 확인, /clear로 대화 비우기, /compact로 요약(3장, 8장, 용어 풀이)
- Codex, Slash commands(https://developers.openai.com/codex/guides/slash-commands/): /status는 세션 설정, 토큰 사용량, 남은 컨텍스트 용량 표시, /compact는 대화를 요약해 토큰 확보(8장, 용어 풀이)

## 보강 1: 에이전트 루프와 종료 조건(2026-10-15)
- Anthropic, How the agent loop works(https://code.claude.com/docs/en/agent-sdk/agent-loop): 다섯 단계(요청 수신, 판단과 응답, 도구 실행, 반복, 결과 반환), 턴은 도구 호출 왕복 한 번, max_turns는 도구 사용 턴만 셈, max_budget_usd, 상한 없으면 열린 요청에서 오래 실행, 운영 에이전트는 예산 상한을 기본으로 권장, 결과 subtype(success, error_max_turns, error_max_budget_usd, error_during_execution), 거부된 도구 호출은 거부 메시지가 결과로 전달, Stop 훅은 결과 검증과 세션 상태 저장, PreToolUse 훅은 도구 실행 전(4장)
- OpenAI, Unrolling the Codex agent loop(https://openai.com/index/unrolling-the-codex-agent-loop/): Codex 하네스가 모든 Codex 경험의 핵심 에이전트 루프 제공, 대화 턴 하나에 모델 추론과 도구 호출이 여러 번 반복, 한 턴에 수백 번의 도구 호출로 컨텍스트 윈도를 소진할 수 있음(4장)

## 보강 2: 하네스 정의 차이와 도구 노출 범위(2026-10-15)
- Claude Code Glossary(https://code.claude.com/docs/en/glossary): Agentic harness는 언어 모델을 코딩 에이전트로 만드는 도구, 컨텍스트 관리, 실행 환경. Claude Code가 하네스이고 Claude는 그 안의 모델(1장, D-052)
- How the agent loop works: 내장 도구 스키마는 요청마다 로드, 도구 정의마다 컨텍스트 차지, 하위 에이전트는 tools 필드로 최소 도구 지정, MCP 도구 스키마는 기본적으로 지연 로드, allowed_tools는 자동 승인, disallowed_tools는 차단, 읽기 전용 도구는 동시 실행, 상태 변경 도구는 순차 실행(4장)
- Manage costs effectively: gh, aws 같은 CLI 도구가 도구 목록을 추가하지 않아 MCP 서버보다 컨텍스트 효율적, 사용하지 않는 서버는 /mcp로 끄기(4장)

## 보강 3: 실행 로그와 추적(2026-10-15)
- How Claude Code works: 메시지, 도구 사용, 결과를 ~/.claude/projects/ 아래 JSONL로 저장, 되감기, 이어 가기, 갈라 시작하기 가능(7장)
- How the agent loop works: 모든 결과 subtype에 total_cost_usd, usage, num_turns, session_id 포함, PostToolUse는 출력 감사, SubagentStart/Stop은 병렬 작업 결과 추적, PreCompact는 요약 전 전체 대화 보관(7장)
- Manage costs effectively: OpenTelemetry 내보내기는 모든 환경에서 동작하고 사용자별 토큰, 비용 지표를 거의 실시간으로 조직의 관측 시스템에 보내는 유일한 방법, 세션 데이터는 cleanupPeriodDays(기본 30일)가 지나면 시작 시 삭제(7장)

## 보강 4: 여러 에이전트에 나눠 맡기기(2026-10-15)
- How Claude Code works: 하위 에이전트는 자신의 컨텍스트 윈도에서 일하고, 포크가 아니면 새로 시작, 도구 호출은 주 컨텍스트 밖에 남고 끝나면 요약 반환(5장)
- How the agent loop works: 하위 에이전트는 부모의 턴을 보지 않고 최종 응답만 부모에게 도구 결과로 반환, 비용 상한은 하위 에이전트 지출 포함, 상한 도달 시 새 하위 에이전트 생성 실패(5장)
- Manage costs effectively: 에이전트 팀은 각자 컨텍스트 윈도를 가진 여러 인스턴스, 토큰 사용량은 팀 크기에 대략 비례, 계획 모드 팀원은 일반 세션보다 약 7배 토큰, 출력이 많은 작업은 하위 에이전트에 위임(5장)
- Glossary: 하위 에이전트는 한 세션 안에서 부모에게만 보고, 팀원은 각자 컨텍스트 윈도를 갖고 사용자가 직접 대화 가능(5장)

## 보강 5: 기준표와 예시 답안(2026-10-15)
- Anthropic, Define success criteria and build evaluations(https://platform.claude.com/docs/en/test-and-evaluate/develop-tests): 성공 기준은 구체적, 측정 가능, 달성 가능, 관련성. 평가 설계는 실제 작업 분포 반영, 자동화, 양 우선. 채점 방법은 가장 빠르고 신뢰할 수 있고 확장 가능한 것: 코드 기반(가장 빠르고 신뢰, 복잡한 판단에는 부족, exact match, string match), 사람(가장 유연, 품질 높음, 느리고 비쌈, 가능하면 피함), LLM 기반(빠르고 유연, 복잡한 판단, 신뢰도 시험 뒤 확대). LLM 채점 팁: 상세하고 명확한 기준표(첫 문장에 Acme Inc. 언급 없으면 오답 예), 정답/오답 또는 1~5 같은 구체적 판정, 채점 모델의 추론. 예제는 golden_answer와 비교, 코드 주석에 생성 모델과 다른 모델로 평가하는 것이 일반적으로 좋다는 안내(6장)
- 비교 도서의 "가중치 기준표"는 이 문서에 없어 쓰지 않음

## 보강 6: 정보를 제공하는 시점과 긴 작업의 기법(2026-10-15)
- Rajasekaran 외, Effective context engineering for AI agents(재확인, 수정일 2026-01-06): 많은 애플리케이션이 임베딩 기반 사전 검색 사용, "just in time" 방식은 파일 경로, 저장된 쿼리, 웹 링크 같은 가벼운 식별자를 두고 실행 중 도구로 로드, 탐색은 점진적 공개를 가능하게 하지만 사전 계산 데이터보다 느리고 지침 없이는 컨텍스트 낭비, Claude Code는 혼합 방식(CLAUDE.md는 먼저, glob과 grep으로 필요할 때). 긴 작업 기법 세 가지: 압축(한계 근처에서 요약 후 재시작, 지나친 압축은 나중에 중요해질 세부 정보 손실), 구조화된 노트(에이전트 기억, 컨텍스트 밖 노트를 다시 읽음, Claude Code의 할 일 목록), 하위 에이전트(깨끗한 컨텍스트, 요약 흔히 1,000~2,000 토큰 반환). 선택 기준: 압축은 주고받는 대화가 많은 작업, 노트는 마일스톤이 분명한 반복 개발, 다중 에이전트는 병렬 탐색이 효과적인 조사와 분석(3장)
- 비교 도서의 저장 계층 4분류는 가져오지 않음. 구조화된 노트는 7장 진행 기록과 연결
