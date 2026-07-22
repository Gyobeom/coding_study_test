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

# 테스트 케이스: (인자_튜플, 기대값). 반환은 [가로, 세로] (가로 >= 세로).
cases = [
    # 1) 공식 예시 1
    ((10, 2), [4, 3]),
    # 2) 공식 예시 2 — 최소 규모(3x3)
    ((8, 1), [3, 3]),
    # 3) 공식 예시 3
    ((24, 24), [8, 6]),
    # 4) 가로로 긴 카펫
    ((18, 6), [8, 3]),
    # 5) 세로 3짜리
    ((14, 4), [6, 3]),
    # 6) 정사각형
    ((16, 9), [5, 5]),
    # 7) 큰 규모 근처 — yellow=1,000,000 (1002 x 1002)
    ((4004, 1000000), [1002, 1002]),
    # 8) brown 경계 근처(=5000) — 가로로 매우 긴 카펫
    ((5000, 2497), [2499, 3]),
]

if __name__ == "__main__":
    check(solution, cases)
