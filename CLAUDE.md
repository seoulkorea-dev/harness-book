# 작업 안내

작업 전에 NEW_BOOK_PLAYBOOK.md, DECISIONS.md, BOOK_SPEC.md, STYLE.md를 읽습니다.

- 원고는 `src/`만 고칩니다. 루트의 `index.html`, `chapters/`, `appendix/`는 빌드 결과물입니다.
- 현재 단계: 3 집필(2026-10-15 독자 변경에 따른 재작성, D-067). 책 제목은 「하네스 엔지니어링: 모델을 에이전트로 만드는 설계」(D-069), 부제는 "프롬프트, 컨텍스트, 하네스로 에이전트 설계하기"(D-070). 목차는 11장 구조 유지(D-062, D-067). 다음 작업은 1장부터 장 단위 재작성과 3장 실습 자료(examples/ch03-01/) 작성입니다.
- 검수: 원고 작성과 검수는 별도 채팅이 맡고, 검수 문서는 `reviews/`에 별도 커밋으로 등록합니다.
- 문체: STYLE.md(플레이북 3장 기본 + 이 책의 예외, D-017)

## 검사 명령

```
python3 tools/build.py
LC_ALL=C.UTF-8 grep -nEf lint/banned.txt index.html chapters/*.html appendix/*.html
python3 lint/check_numbers.py
python3 lint/check_structure.py
python3 lint/check_style.py
```
