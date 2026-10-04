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
