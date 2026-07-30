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

# 테스트 케이스: (인자_튜플, 기대값). 인자가 하나여도 튜플로: ((5,), 25)
cases = [
    # 1) 공식 예시 1
    ((6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]), [8, 10, 25]),
    # 2) 공식 예시 2 — 연속 쿼리가 누적 반영됨
    ((3, 3, [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]]), [1, 1, 5, 3]),
    # 3) 최소 규모 2x2 전체 테두리 (움직인 값 최소 = 1)
    ((2, 2, [[1, 1, 2, 2]]), [1]),
    # 4) 전체 행렬을 한 번 회전
    ((3, 4, [[1, 1, 3, 4]]), [1]),
    # 5) 세로로 긴 부분 직사각형 (폭 2)
    ((4, 3, [[1, 1, 4, 2]]), [1]),
    # 6) 같은 영역을 두 번 회전 — 두 번째도 이동값 최소는 1
    ((3, 3, [[1, 1, 3, 3], [1, 1, 3, 3]]), [1, 1]),
    # 7) 비정사각 판(5x4)의 부분 영역 두 번
    ((5, 4, [[2, 1, 4, 3], [1, 2, 5, 4]]), [5, 2]),
]

if __name__ == "__main__":
    check(solution, cases)
