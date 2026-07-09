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

# 테스트 케이스: (인자_튜플, 기대값). 인자가 하나이므로 튜플로 감싼다.
cases = [
    (([1, 2],), 4),           # {1, 2, 12, 21}
    (([1, 1],), 2),           # {1, 11}
    (([7],), 1),              # {7}
    (([1, 2, 3],), 15),       # 3 + 6 + 6
    (([3, 3],), 2),           # {3, 33}
    (([2, 2, 2],), 3),        # {2, 22, 222}
    (([1, 2, 2],), 8),        # {1,2, 12,21,22, 122,212,221}
    (([5, 5, 5, 5, 5, 5, 5, 5],), 8),   # {5, 55, ..., 55555555}
    (([9, 8, 7, 6, 5, 4, 3, 2],), 109600),  # 서로 다른 8개 → P(8,1)+…+P(8,8)
]

if __name__ == "__main__":
    check(solution, cases)
