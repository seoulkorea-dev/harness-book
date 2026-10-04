# 작업 안내

작업 전에 NEW_BOOK_PLAYBOOK.md, DECISIONS.md, BOOK_SPEC.md, STYLE.md를 읽습니다.

- 원고는 `src/`만 고칩니다. 루트의 `index.html`, `chapters/`, `appendix/`는 빌드 결과물입니다.
- 현재 단계: 1 설계(설계 인터뷰). BOOK_SPEC.md의 미정 항목이 0이 되기 전에는 본문을 쓰지 않습니다.
- 문체: STYLE.md(플레이북 3장 기본 + 이 책의 예외, D-017)

## 검사 명령

```
python3 tools/build.py
LC_ALL=C.UTF-8 grep -nEf lint/banned.txt index.html chapters/*.html appendix/*.html
python3 lint/check_numbers.py
python3 lint/check_structure.py
python3 lint/check_style.py
```
