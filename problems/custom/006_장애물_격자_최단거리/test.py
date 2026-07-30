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

# 테스트 케이스: (인자_튜플, 기대값). 인자는 (maps,) 하나이므로 튜플로 감싼다.
# 반환값은 (0,0)→(n-1,m-1) 최단 칸 수, 도달 불가면 -1.
cases = [
    (([[1, 0, 1], [1, 1, 1], [0, 1, 1]],), 5),           # 우회 경로 5칸
    (([[1, 1], [1, 1]],), 3),                            # 2×2 → 3칸
    (([[1, 0], [0, 1]],), -1),                           # 도착 칸 고립 → -1
    (([[1]],), 1),                                       # 출발=도착 → 1
    (([[0, 1], [1, 1]],), -1),                           # 출발 칸이 벽 → -1
    (([[1, 1, 1, 1, 1]],), 5),                           # 1×5 일자 → 5
    (([[1, 1, 1],
       [0, 0, 1],
       [1, 1, 1],
       [1, 0, 0],
       [1, 1, 1]],), 11),                                # 지그재그 우회 경로
    (([[1, 1, 1],
       [1, 0, 1],
       [1, 0, 1],
       [1, 1, 1]],), 6),                                 # 가운데 벽 우회
]

if __name__ == "__main__":
    check(solution, cases)
