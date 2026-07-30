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

# 테스트 케이스: (인자_튜플, 기대값). 인자는 (nums, target) 두 개.
# 반환값은 합이 target 인 부분집합(인덱스 기준)의 개수.
cases = [
    (([1, 2, 3, 4, 5], 5), 3),                           # {5},{1,4},{2,3}
    (([1, 1], 1), 2),                                    # 서로 다른 인덱스 → 2
    (([2, 4, 6], 5), 0),                                 # 불가능 → 0
    (([3, 3, 3], 6), 3),                                 # 3개 중 2개 → C(3,2)=3
    (([5], 5), 1),                                       # 원소 하나 일치
    (([5], 3), 0),                                       # 하나로 불일치 → 0
    (([1, 1, 1, 1], 2), 6),                              # 4개 중 2개 → C(4,2)=6
    (([2, 3, 5, 7, 11], 10), 2),                         # {3,7},{2,3,5}
]

if __name__ == "__main__":
    check(solution, cases)
