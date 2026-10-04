---
name: originality-check
description: 비교 대상 도서와의 유사도 측정(문장, 표, 예제, 제목)과 기본틀 점검. 목차 확정 후, 출간 전에 사용.
---
# 독창성 점검
- 문장 수준: `python tools/similarity_check.py --ab src --gb <비교 도서 docs 경로>` (일치 0.95 이상은 고유 표기 외 0건이 기준)
- 기본틀 수준(사람 판단): 장 제목 문구 일치 0, 부록 이름 일치 0, 핵심 틀 이름 일치 0, 주 예제 소재 겹침 0, 공통 사례는 근거 문장으로만.
- 결과는 reviews/originality-<날짜>.md에 측정 출력 원문과 함께 남긴다.
