# 작업 안내

작업 전에 NEW_BOOK_PLAYBOOK.md, DECISIONS.md, BOOK_SPEC.md, STYLE.md를 읽습니다.

- 원고는 `src/`만 고칩니다. 루트의 `index.html`, `chapters/`, `appendix/`는 빌드 결과물입니다.
- 현재 단계: 3 집필(Chapter 1 초안, 검수 누적 1차). 남은 미정 항목은 책 제목(가제)과 Chapter 1 핵심 예제의 실행 결과입니다. 목차 최종 확정은 전체 작성 후에 합니다(D-016).
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
