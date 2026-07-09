"""공용 채점기.

각 문제의 test.py에서 import하여 사용한다.

    from lib.judge import check
    from solution import solution

    check(solution, [
        ((인자1, 인자2), 기대값),
        ...
    ])

- 케이스는 (args_tuple, expected) 형태. args_tuple은 solution에 언패킹되어 전달된다.
- 인자가 하나여도 튜플로 감싼다: ((5,), 25)
- 모든 케이스 통과 시 종료코드 0, 하나라도 실패 시 1.
"""
import sys
import time


def check(solution_fn, cases, *, name=None):
    title = name or getattr(solution_fn, "__name__", "solution")
    print(f"=== 채점: {title} ({len(cases)} cases) ===")
    passed = 0
    for i, (args, expected) in enumerate(cases, 1):
        if not isinstance(args, tuple):
            args = (args,)
        try:
            t0 = time.perf_counter()
            got = solution_fn(*args)
            dt = (time.perf_counter() - t0) * 1000
        except Exception as e:  # 풀이 중 예외도 실패로 처리
            print(f"[{i:>2}] 💥 예외 발생: {type(e).__name__}: {e}")
            continue
        if got == expected:
            passed += 1
            print(f"[{i:>2}] ✅ pass  ({dt:.2f} ms)")
        else:
            print(f"[{i:>2}] ❌ FAIL  ({dt:.2f} ms)")
            print(f"      입력:   {args!r}")
            print(f"      기대값: {expected!r}")
            print(f"      실제값: {got!r}")

    total = len(cases)
    print(f"--- 결과: {passed}/{total} 통과 ---")
    ok = passed == total
    sys.exit(0 if ok else 1)
    return ok
