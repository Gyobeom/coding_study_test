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

# 테스트 케이스: (인자_튜플, 기대값). 인자는 (grid,) 하나이므로 튜플로 감싼다.
# 반환값은 모든 땅 칸의 바깥 둘레 총합.
cases = [
    (([[0, 1, 0], [1, 1, 1], [0, 1, 0]],), 12),          # 십자 5칸 → 12
    (([[1]],), 4),                                       # 단일 칸 → 4
    (([[1, 1], [1, 1]],), 8),                            # 2×2 블록 → 8
    (([[0, 0], [0, 0]],), 0),                            # 땅 없음 → 0
    (([[1, 0, 1]],), 8),                                 # 떨어진 두 칸 각각 4 → 8
    (([[1, 1, 1, 1]],), 10),                             # 1×4 줄 → 10
    (([[1, 0, 0, 0],
       [1, 1, 0, 0],
       [0, 1, 0, 0],
       [0, 1, 1, 1]],), 16),                            # L/계단 모양 섬
    (([[1, 1, 0, 1],
       [0, 1, 1, 1],
       [0, 0, 0, 0],
       [1, 0, 1, 1]],), 24),                            # 여러 섬 혼합
]

if __name__ == "__main__":
    check(solution, cases)
