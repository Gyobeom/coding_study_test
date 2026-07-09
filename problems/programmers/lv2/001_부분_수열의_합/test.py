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
    (([1, 2, 3, 4, 5], 5), 3),      # {5}, {1,4}, {2,3}
    (([3, 3, 3], 3), 3),            # 인덱스로 구분
    (([1, 2, 3], 7), 0),            # 불가능
    (([1, 1, 1, 1], 2), 6),         # C(4,2)
    (([5], 5), 1),                  # 단일 원소 일치
    (([5], 3), 0),                  # 단일 원소 불일치
    (([2, 4, 6, 8], 10), 2),        # {2,8}, {4,6}
    (([10, 20, 30], 50), 1),        # {20,30}
    (([1, 2, 3, 4, 5, 6, 7], 8), 5),  # {1,7},{2,6},{3,5},{1,2,5},{1,3,4}
    (([1] * 20, 10), 184756),       # C(20,10) 최대 규모 완전탐색
]

if __name__ == "__main__":
    check(solution, cases)
