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

# 테스트 케이스: (인자_튜플, 기대값). 인자는 (nums, limit) 두 개.
# 반환값은 합이 limit 이하인 부분집합 중 최대 합.
cases = [
    (([3, 5, 8], 10), 8),          # {3,5}=8, {3,8}=11 초과 → 8
    (([1, 2, 3], 100), 6),         # 전부 합 6 ≤ 100 → 6
    (([5, 6, 7], 4), 0),           # 어떤 원소도 4 이하 불가 → 빈 집합 0
    (([-2, -3], -1), -2),          # limit 음수, {-2} 최대
    (([], 5), 0),                  # 빈 배열 → 0
    (([10], 10), 10),              # 정확히 limit
    (([4, 4, 4], 8), 8),           # 중복 원소, {4,4}=8
    (([-1, 2, 3], 4), 4),          # {-1,2,3}=4 ≤ 4 → 4
    (([1, 2, 3, 4, 5], 7), 7),     # {3,4}=7 또는 {2,5} → 7
    (([1000] * 20, 1000000), 20000),  # 최대 규모, 전부 골라도 2만 ≤ 100만
    (([-5, -1], -3), -5),          # limit -3, {-5} 최대(-1은 -1>-3 초과)
]

if __name__ == "__main__":
    check(solution, cases)
