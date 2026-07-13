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

# 테스트 케이스: (인자_튜플, 기대값). 인자는 (n, computers) 두 개.
cases = [
    ((3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]), 2),          # {0,1} + {2}
    ((3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]), 1),          # 1이 다리 역할 → 전부 하나
    ((1, [[1]]), 1),                                       # 컴퓨터 1대 → 1
    ((2, [[1, 0], [0, 1]]), 2),                            # 연결 없음 → 각자 하나
    ((4, [[1, 1, 0, 0],
          [1, 1, 0, 0],
          [0, 0, 1, 1],
          [0, 0, 1, 1]]), 2),                             # {0,1} + {2,3}
    ((5, [[1, 0, 0, 0, 0],
          [0, 1, 0, 0, 0],
          [0, 0, 1, 0, 0],
          [0, 0, 0, 1, 0],
          [0, 0, 0, 0, 1]]), 5),                          # 전부 고립 → 5
    ((5, [[1, 1, 0, 0, 0],
          [1, 1, 1, 0, 0],
          [0, 1, 1, 1, 0],
          [0, 0, 1, 1, 1],
          [0, 0, 0, 1, 1]]), 1),                          # 사슬처럼 이어짐 → 1
    ((4, [[1, 1, 1, 0],
          [1, 1, 0, 0],
          [1, 0, 1, 0],
          [0, 0, 0, 1]]), 2),                             # 삼각형 {0,1,2} + 고립 {3}
]

if __name__ == "__main__":
    check(solution, cases)
