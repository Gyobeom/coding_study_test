"""채점 테스트 (Claude가 작성). 실행: python test.py"""
import os
import sys

# --- 저장소 루트를 찾아 sys.path에 추가 (수정 불필요) ---
_here = os.path.dirname(os.path.abspath(__file__))
_cur = _here
while not os.path.isfile(os.path.join(_cur, "lib", "judge.py")):
    _parent = os.path.dirname(_cur)
    if _parent == _cur:
        raise RuntimeError("저장소 루트(lib/judge.py)를 찾지 못했습니다.")
    _cur = _parent
sys.path[:0] = [_here, _cur]
# ---------------------------------------------------------

from lib.judge import check
from solution import solution

# 테스트 케이스: (인자_튜플, 기대값)
cases = [
    # 1) 공식 예시 1 — 종류 수(3) > N/2(2)라 N/2가 상한
    (([3, 1, 2, 3],), 2),
    # 2) 공식 예시 2 — 종류 수(3) == N/2(3), 모든 종류 확보 가능
    (([3, 3, 3, 2, 2, 4],), 3),
    # 3) 공식 예시 3 — 종류 수(2) < N/2(3)라 종류 수가 상한
    (([3, 3, 3, 2, 2, 2],), 2),
    # 4) 최소 규모 — 2마리, 서로 다른 종류
    (([1, 2],), 1),
    # 5) 최소 규모 — 2마리 모두 같은 종류
    (([9, 9],), 1),
    # 6) 전부 다른 종류 — 종류 수(6) > N/2(3)
    (([1, 2, 3, 4, 5, 6],), 3),
    # 7) 최대 규모 근처 — 1만 마리, 종류는 500가지뿐 → N/2(5000)보다 작아 500이 상한
    (([i % 500 + 1 for i in range(10000)],), 500),
]

if __name__ == "__main__":
    check(solution, cases)
