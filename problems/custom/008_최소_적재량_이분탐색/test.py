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

# 테스트 케이스: (인자_튜플, 기대값). 인자는 (weights, D) 두 개.
# 반환값은 D대 이내로 순서대로 다 나르는 최소 적재 용량.
cases = [
    (([1, 2, 3, 4, 5], 2), 9),                           # 8→3대, 9→2대
    (([1, 2, 3, 4, 5], 5), 5),                           # D=len → max
    (([1, 2, 3, 4, 5], 1), 15),                          # D=1 → 총합
    (([10, 10, 10], 3), 10),                             # 각자 하나씩 → 10
    (([7], 1), 7),                                       # 물건 하나
    (([5, 4, 3, 2, 1], 3), 6),                           # 역순, 3대 → 6
    (([2, 2, 2, 2, 2, 2], 3), 4),                        # 균등, 3대에 2개씩 → 4
    (([1, 1, 1, 1, 1, 1, 1, 1, 9], 3), 9),               # 큰 원소 하나가 하한
]

if __name__ == "__main__":
    check(solution, cases)
