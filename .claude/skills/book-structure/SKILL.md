---
name: book-structure
description: 책 구성 단위, 장 구성, 번호, id, 링크, 조사 규칙. 장이나 표, 그림을 추가, 이동, 번호 변경할 때 사용.
---
# 책 구조 규칙
- 구성 단위: Book(권, 여러 권이면 Volume), Part(편, 부), Chapter(장), Section(절).
- 장 구성: 첫 문단(장 주제 정의) → 요점 상자(세 줄 안팎) → 본문 절. 절 제목 바로 뒤에 그림이나 표를 두지 않는다. 요약 그림은 표보다 앞.
- 번호: 본문은 `표 N-n`, `그림 N-n`(N은 파일 chNN의 장 번호). 부록은 `표 부N-n`, id는 `tbl-부N-n`. id는 캡션 번호와 같아야 한다.
- 번호를 바꾸면 id, 본문 참조, 다른 쪽 링크를 함께 바꾸고, 번호 뒤 조사(받침 0, 1, 3, 6, 7, 8 뒤 은, 이, 을, 과)를 다시 확인한다. "Chapter N" 뒤 조사도 같다.
- 링크: 같은 쪽의 표, 그림 참조는 링크 없음. 다른 쪽 참조만 링크(빌드가 자동 처리).
- 공통 사례(유명 판결, 보도)는 절 제목으로 쓰지 않고 근거 문단으로만 쓴다.
- 없어지는 쪽은 src/site.json "redirects"에 이동 쪽으로 등록한다.
- 확인: `python tools/build.py`, `python lint/check_numbers.py`, `python lint/check_structure.py` 모두 exit 0.
