"""book-kit(공통 원본)에서 검사 도구, 하위 에이전트 정의, 스킬을 가져온다(D-147, D-149).

플레이북은 복사하지 않고 book-kit/book/PLAYBOOK.md를 직접 읽는다. 검사 도구, 에이전트, 스킬은 Claude Code와
check_all이 이 저장소 안의 경로에서 읽으므로 세션 시작 훅과 check_all이 이 스크립트로 가져온다.
가져온 파일은 git에 넣지 않는다(.gitignore, D-150). CI는 book-kit을 받아 환경 변수 BOOK_KIT로 넘긴다.

    python tools/sync_kit.py          # book-kit에서 복사
    python tools/sync_kit.py --check  # 다르면 목록을 출력하고 종료 코드 1, book-kit이 없으면 0(건너뜀)

book-kit 위치: 환경 변수 BOOK_KIT, 없으면 이 저장소 옆 폴더(../book-kit).
"""
import os
import shutil
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KIT = os.environ.get("BOOK_KIT") or os.path.join(os.path.dirname(ROOT), "book-kit")

# (book-kit 안의 경로, 이 저장소 안의 경로)
FILES = [(f"book/lint/{n}", f"lint/{n}") for n in
         ("check_numbers.py", "check_rules.py", "check_structure.py", "check_style.py", "banned.txt")]
FILES += [(f"book/agents/{n}.md", f".claude/agents/{n}.md") for n in
          ("chief-editor", "fact-checker", "practice-checker", "production-checker", "researcher")]
FILES += [(f"book/skills/{n}/SKILL.md", f".claude/skills/{n}/SKILL.md") for n in
          ("book-structure", "chapter-review", "example-design", "fact-check", "figure-design",
           "ko-book-style", "originality-check", "practice-design", "table-design")]


def read(p):
    with open(p, "rb") as f:
        return f.read()


def main():
    check = "--check" in sys.argv
    if not os.path.isfile(os.path.join(KIT, "book", "PLAYBOOK.md")):
        print(f"book-kit 없음({KIT}): 동기화 확인을 건너뜀")
        return 0
    diff = []
    for src, dst in FILES:
        s, d = os.path.join(KIT, src), os.path.join(ROOT, dst)
        if os.path.exists(d) and read(s) == read(d):
            continue
        if check:
            diff.append(f"{dst} ≠ book-kit/{src}")
        else:
            os.makedirs(os.path.dirname(d), exist_ok=True)
            shutil.copyfile(s, d)
            print(f"복사 book-kit/{src} → {dst}")
    if diff:
        print("book-kit과 다름(python tools/sync_kit.py로 맞추거나, 고칠 내용은 book-kit에서 고침)\n" + "\n".join(diff))
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
