# 인계(HANDOFF)

- 갱신: 2026-10-19
- 브랜치: ch01-rewrite(1장 계획 단계, 개요 작가 확인 대기)

## 지금 상태
- 하네스 설정(PR #1), 작동 시험과 F-13 수정(PR #2), 하위 에이전트 보강(PR #3)은 main에 병합됨.
- Step 3 작동 시험을 했다(reviews/agents/2026-10-19-harness-test.md). 시작 훅, main 커밋·push 차단, 편집 직후 검사, 하위 에이전트 읽기 전용은 통과. 종료 훅은 처음에 Windows에서 막지 못했으나(구조 검사 경로 결함, F-13) 수정 뒤 재시험에서 막음.
- 원고는 2026-10-19 결정(장 틀, CR 이름)에 따라 1장부터 다시 쓴다.

## 다음 할 일
1. 1장 개요 작가 확인(/plan-chapter 1 결과, 이 세션 대화). 조사 기록은 research/ch01-sources.md의 2026-10-19 절(S3~S19).
2. 확인된 개요로 /write-chapter 1. flow-reviewer의 1장 첫 절 의견(reviews/agents/2026-10-19-ch01-flow-reviewer.md)을 이때 반영.
3. OpenAI 글 두 편(Unrolling the Codex agent loop, Harness engineering)은 403으로 재확인 못 함. 작가가 원문을 직접 확인.

## 미결정
- 그림 글자 크기 기준 미달 그림 8개(2-2, 4-2, 5-2, 6-2, 7-2, 8-2, 9-2, 11-1): 해당 장을 다시 쓸 때 고치고, 모두 고치면 check_all을 --strict-figures로 바꾼다.

## 주의할 점
- main에서 작업하지 않는다. 결정 기록 수정과 push는 작가 확인 후.
- 작업 환경: 책 작업은 Windows의 harness-book 폴더를 VS Code 프로필 Harness-book으로 열어서 한다. WSL은 앱 개발에만 쓴다.
