# 인계(HANDOFF)

- 갱신: 2026-10-19
- 브랜치: harness-test(PR 생성, 작가 병합 대기)

## 지금 상태
- 하네스 설정(Step 2)은 PR #1로 main에 병합됨.
- Step 3 작동 시험을 했다(reviews/agents/2026-10-19-harness-test.md). 시작 훅, main 커밋·push 차단, 편집 직후 검사, 하위 에이전트 읽기 전용은 통과. 종료 훅은 처음에 Windows에서 막지 못했으나(구조 검사 경로 결함, F-13) 수정 뒤 재시험에서 막음.
- 원고는 2026-10-19 결정(장 틀, CR 이름)에 따라 1장부터 다시 쓴다.

## 다음 할 일
1. harness-test PR 병합(작가). check_structure.py Windows 경로 수정(F-13) 뒤 종료 훅 재시험 통과.
2. 1장 시범: /plan-chapter 1 → /write-chapter 1. flow-reviewer의 1장 첫 절 의견(reviews/agents/2026-10-19-ch01-flow-reviewer.md)을 이때 반영 여부 판단.

## 미결정
- 그림 글자 크기 기준 미달 그림 8개(2-2, 4-2, 5-2, 6-2, 7-2, 8-2, 9-2, 11-1): 해당 장을 다시 쓸 때 고치고, 모두 고치면 check_all을 --strict-figures로 바꾼다.

## 주의할 점
- main에서 작업하지 않는다. 결정 기록 수정과 push는 작가 확인 후.
- 작업 환경: 책 작업은 Windows의 harness-book 폴더를 VS Code 프로필 Harness-book으로 열어서 한다. WSL은 앱 개발에만 쓴다.
