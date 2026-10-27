# 하네스 엔지니어링: 모델을 에이전트로 만드는 설계

프롬프트, 컨텍스트, 하네스로 에이전트 설계하기

같은 모델을 사용해도 모델 바깥의 하네스(역할, 도구, 권한, 기록, 검증)를 어떻게 설계했는지에 따라 에이전트의 결과가 달라질 수 있습니다. 이 책은 하네스를 정의하고, 하네스로 에이전트를 설계하고, 맡긴 일을 운영하는 방법을 Claude Code와 Codex의 설정과 실습으로 다룹니다.

- 온라인으로 읽기: https://seoulkorea-dev.github.io/harness-book/
- 상태: 원고 정리를 마치고 작가 최종 검수 중입니다(2026년 10월). 작가가 정할 항목은 [docs/AUTHOR_QUEUE.md](docs/AUTHOR_QUEUE.md)에 있습니다.
- 제품 기능은 2026년 10월에 확인한 공식 문서를 기준으로 설명합니다.
- 이전 원고(3부 16장 계획, 1장 작성): 태그 `v0-before-reset`

## 구성

| 위치 | 제목 |
|---|---|
| 시작하며 | 책의 목적, 장 순서와 목적별 읽는 경로 |
| Chapter 1 | 하네스란 무엇인가 |
| Chapter 2 | 하네스의 구성 요소 |
| Chapter 3 | 하네스로 에이전트 설계하기 |
| Chapter 4 | 프롬프트 엔지니어링: 한 번의 요청 설계 |
| Chapter 5 | 컨텍스트 엔지니어링: 에이전트가 읽는 정보 설계 |
| Chapter 6 | 착수: 맡길 업무 선정과 작업 단위 분할 |
| Chapter 7 | 검증 설계: 완료 보고 대신 증거 받기 |
| Chapter 8 | 기록과 인계: 결정, 진행, 규칙의 문서화 |
| Chapter 9 | 위험 관리: 승인, 격리, 비용 |
| Chapter 10 | 제품 단위 비교: Codex와 Claude Code의 하네스 |
| 마치며 | 장별 원칙, 작가 사례(책 두 권을 에이전트와 함께 만든 과정), 작업하며 겪은 어려움, 잘된 점, 하네스의 앞으로 |
| 부록 | 용어 풀이, 실습(실습 1~6), 참고 문헌 |

- 장마다 같은 틀을 따릅니다: 주장 한 문장, 도입부와 요약, 원리 절, 예제 절, 실패를 예방하는 장치, 설정과 결과의 확인 방법, 설계 원칙과 점검 질문.
- 예제는 가상 프로젝트 "경비 정산 시스템 개편"의 변경 요청 사항 한 건을 여러 장에서 함께 사용합니다. 실습 파일은 `examples/expense-app/`에 있습니다.
- 옛 Chapter 11(작가 사례)은 2026년 10월 26일 마치며로 옮겼습니다(D-144). 옛 주소는 마치며로 이동합니다.

## 이 책을 만드는 방식

원고는 작가와 에이전트가 역할을 나눠 만들고, 그 과정 자체를 이 저장소에 공개합니다. 마치며의 작가 사례가 이 저장소의 하네스를 다룹니다.

| 역할 | 맡은 일 |
|---|---|
| 작가 | 목차, 장의 주장, 핵심 정의, 용어, 문체 같은 결정과 최종 검수 |
| 작성 에이전트(Claude Code) | 원고를 작성하는 유일한 주체. 장마다 명세 → 원고 → 자동 검사 → 점검 → 편집 검토 → PR 병합 |
| 점검 에이전트(.claude/agents/) | 원고를 읽고 판정한 결과를 문서로만 돌려줌(편집장, 사실, 실습, 제작 점검 등). 원고는 고치지 않음 |

- main에는 직접 반영하지 않고 작업 브랜치와 PR로 반영합니다. PR마다 자동 검사(`python tools/check_all.py`)와 CI를 통과해야 병합합니다.
- 결정은 [DECISIONS.md](DECISIONS.md), 두 번째 나온 실패와 추가한 장치는 [FAILURES.md](FAILURES.md), 진행 상황은 [HANDOFF.md](HANDOFF.md)에 남깁니다.
- 문서마다의 역할과 읽는 순서는 [docs/DOCUMENTS.md](docs/DOCUMENTS.md)에 정리했습니다.

## 폴더 구조

- `src/` 원고 원본(`chapters/`, `appendix/`, `index.html`)과 `site.json`(목차, 쪽 정보, 이동 쪽)
- `index.html`, `chapters/`, `appendix/` 빌드 결과물(`python tools/build.py`로 생성, 직접 고치지 않음)
- `examples/expense-app/` 실습 예제
- `tools/` 빌드, 통합 검사(`check_all.py`), 배포 확인, 유사도 측정, 훅
- `lint/` 자동 검사와 금칙어, 규칙을 적용한 쪽 목록(`rules_applied.txt`)
- `research/` 장별 출처와 확인 날짜, 인용 키(`bibliography.json`)
- `reviews/` 점검과 검수 기록(`reviews/agents/`는 점검 에이전트 보고)
- `docs/` 작가 확인 목록, 장 명세(`specs/`), 예제 사실, 문서 현황
- `templates/` 장 명세, 그림 명세, 이슈 보고 서식
- `assets/` 스타일과 Pretendard 글꼴(SIL Open Font License 1.1)
- `.claude/` Claude Code용 에이전트, 명령, Skill, 훅 설정

## 기준 문서

| 문서 | 역할 |
|---|---|
| [NEW_BOOK_PLAYBOOK.md](NEW_BOOK_PLAYBOOK.md) | 원고 원칙과 규칙, 최종 점검표 |
| [BOOK_SPEC.md](BOOK_SPEC.md) | 이 책의 선택(목차, 용어표, 예제, 그림)과 플레이북 예외 |
| [HARNESS_SETUP.md](HARNESS_SETUP.md) | 작업 진행 방식(한 장의 순서, 중단 없이 진행하는 규칙) |
| [CLAUDE.md](CLAUDE.md) | 작성 세션 안내 |

옛 기준 문서(STYLE.md, FIGURE_STYLE.md, BOOK_STANDARD.md, REVIEW_RULES.md 등)는 기록으로 남아 있고, 내용이 다르면 위 문서를 따릅니다.
