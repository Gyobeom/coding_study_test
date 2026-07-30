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

# 테스트 케이스: (인자_튜플, 기대값). 인자는 (nums, k) 두 개.
# 반환값은 오름차순 정렬 시 k번째로 작은 값.
cases = [
    (([7, 10, 4, 3, 20, 15], 3), 7),                     # 정렬 3번째
    (([1, 1, 1, 1], 2), 1),                              # 전부 동일
    (([5], 1), 5),                                       # 원소 하나
    (([9, 8, 7, 6, 5], 5), 9),                           # k=len → 최댓값
    (([9, 8, 7, 6, 5], 1), 5),                           # k=1 → 최솟값
    (([-3, -1, -2, 0, 5], 2), -2),                       # 음수 포함
    (([4, 4, 2, 2, 6, 6], 4), 4),                        # 중복 다수, 4번째
    (([100, -100, 50, -50, 0], 3), 0),                   # 큰 음/양수 혼합
]

if __name__ == "__main__":
    check(solution, cases)
