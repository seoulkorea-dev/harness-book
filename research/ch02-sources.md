# Chapter 2 사실 확인 기록

확인일: 2026-10-04. 원문을 직접 열어 확인한 내용만 적습니다.

## S1. Anthropic, Prompting best practices (Claude Platform Docs)

- URL: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
- 페이지에 게시일 표기 없음(검색 메타데이터 2026-08-21). 확인일로 표기
- 2장에서 사용한 내용
  - 명확하고 명시적인 지시에 잘 반응함. 원하는 출력 형식과 제약 조건을 구체적으로 지정
  - 단계의 순서나 완결성이 중요하면 번호 목록이나 글머리 기호로 순차 지시
  - 지시의 이유(맥락, 동기)를 함께 주면 목표를 이해해 더 맞는 응답을 함
  - 예시는 출력 형식, 어조, 구조를 조정하는 가장 신뢰할 수 있는 방법 중 하나. 실제 사례와 가깝게, 다양하게, 태그로 구분. 3~5개 권장
  - XML 태그로 지시, 맥락, 예시, 입력을 구분하면 해석 오류가 줄어듦
  - 하지 말 것 대신 할 것을 지시(예: 마크다운 금지 대신 문단으로 작성)
  - 최신 모델은 정확한 지시 이행에 맞춰 훈련됨. "변경을 제안해 줄 수 있어?"는 제안만, "이 함수를 변경해 줘"는 실행
  - 시스템 프롬프트의 역할 지정

## S2. Anthropic, Prompt engineering overview (Claude Platform Docs)

- URL: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview
- 2장에서 사용한 내용
  - 프롬프트 엔지니어링 전에 성공 기준의 명확한 정의, 그 기준으로 시험하는 방법, 첫 초안이 있어야 함
  - 모든 성공 기준이나 실패한 평가가 프롬프트 엔지니어링으로 가장 잘 해결되는 것은 아님. 지연 시간과 비용은 다른 모델 선택으로 더 쉽게 개선되기도 함

# 2026-10-20 ch02 v1.0 보강 확인(fact-checker)

## S23. Anthropic, Hooks reference / Automate actions with hooks(Claude Code Docs)
- URL: https://code.claude.com/docs/en/hooks , https://code.claude.com/docs/en/hooks-guide
- 게시일: 표기 없음, 확인일: 2026-10-20
- 작성: Anthropic
- 2장 확인 방법 절(표 2-5 검증 행)에서 사용한 내용
  - PostToolUse 훅이 종료 코드 2로 끝나면 도구는 이미 실행된 뒤이므로 차단하지 못하고 오류 출력을 모델에 전달
  - 성공한 훅의 출력은 디버그 로그로 가며 대화 기록에 나타나지 않음. 대화 기록에는 차단이나 실패 때 hook error 알림이 보임
  - 훅 확인: /hooks는 읽기 전용 목록, 실행 기록은 claude --debug
  - 훅 명령은 현재 디렉터리에서 실행, CLAUDE_PROJECT_DIR은 프로젝트 루트

## S24. Anthropic, Configure permissions(Claude Code Docs)
- URL: https://code.claude.com/docs/en/permissions
- 게시일: 표기 없음, 확인일: 2026-10-20
- 작성: Anthropic
- 사용한 내용
  - Edit 규칙은 파일을 수정하는 내장 도구 전체에 적용
  - Read, Edit deny는 Bash의 인식되는 파일 명령과 리다이렉션에도 적용되나, Python 스크립트 같은 간접 접근은 막지 못함. 운영 체제 수준 강제는 샌드박스
  - 이름만 쓴 WebFetch deny는 도구를 제거함
  - ./path는 현재 디렉터리 기준
  - /permissions는 규칙과 규칙이 나온 설정 파일을 보여 줌
