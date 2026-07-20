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
    # 1) 공식 예시 1 — headgear 2, eyewear 1 → (2+1)*(1+1)-1 = 5
    (([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"],
       ["green_turban", "headgear"]],), 5),
    # 2) 공식 예시 2 — face 종류 하나에 3개 → (3+1)-1 = 3
    (([["crow_mask", "face"], ["blue_sunglasses", "face"],
       ["smoky_makeup", "face"]],), 3),
    # 3) 최소 규모 — 의상 1개 → (1+1)-1 = 1
    (([["hat", "headgear"]],), 1),
    # 4) 두 종류 각각 1개 → (1+1)*(1+1)-1 = 3
    (([["a", "top"], ["b", "bottom"]],), 3),
    # 5) 세 종류 각각 1개 → (1+1)^3 - 1 = 7
    (([["a", "top"], ["b", "bottom"], ["c", "shoes"]],), 7),
    # 6) 종류별 개수 다양 — top 3, bottom 2, shoes 1 → 4*3*2 - 1 = 23
    (([["t1", "top"], ["t2", "top"], ["t3", "top"],
       ["b1", "bottom"], ["b2", "bottom"], ["s1", "shoes"]],), 23),
    # 7) 최대 규모 근처 — 종류 1개에 의상 30개 → (30+1)-1 = 30
    (([["c%d" % i, "face"] for i in range(30)],), 30),
]

if __name__ == "__main__":
    check(solution, cases)
