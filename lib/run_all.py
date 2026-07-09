"""전체 문제 일괄 채점.  실행: python lib/run_all.py

problems/ 하위에서 test.py를 모두 찾아 실행하고, 문제별 통과 여부를 요약한다.
각 test.py는 독립 프로세스로 실행되므로 solution 모듈 충돌이 없다.
"""
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROBLEMS = os.path.join(ROOT, "problems")


def find_tests():
    for dirpath, _dirs, files in os.walk(PROBLEMS):
        if "test.py" in files:
            yield os.path.join(dirpath, "test.py")


def main():
    tests = sorted(find_tests())
    if not tests:
        print("채점할 문제가 없습니다 (problems/ 하위 test.py 없음).")
        return
    # 자식 프로세스가 UTF-8로 출력하도록 강제(Windows cp949 환경 대비)
    env = dict(os.environ, PYTHONIOENCODING="utf-8", PYTHONUTF8="1")
    results = []
    for t in tests:
        rel = os.path.relpath(os.path.dirname(t), PROBLEMS)
        proc = subprocess.run(
            [sys.executable, t],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            env=env,
        )
        ok = proc.returncode == 0
        # judge.py의 마지막 결과 줄만 추출
        summary = ""
        for line in proc.stdout.splitlines():
            if line.startswith("--- 결과:"):
                summary = line.strip("- ").strip()
        results.append((rel, ok, summary))
        mark = "🟢" if ok else "🔴"
        print(f"{mark} {rel}  {summary}")

    passed = sum(1 for _r, ok, _s in results if ok)
    print(f"\n=== 전체: {passed}/{len(results)} 문제 통과 ===")
    sys.exit(0 if passed == len(results) else 1)


if __name__ == "__main__":
    main()
