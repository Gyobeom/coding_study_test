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

# 테스트 케이스: (인자_튜플, 기대값). 인자는 (grid,) 하나.
# 반환값은 모든 1이 젖는 최소 시간(없으면 0, 불가능하면 -1).
cases = [
    (([[2, 1, 1], [1, 1, 0], [0, 1, 1]],), 4),      # 대표 예시
    (([[2, 1, 1], [0, 1, 1], [1, 0, 1]],), -1),     # 도달 불가한 1 존재
    (([[0, 2]],), 0),                               # 젖을 1이 없음
    (([[2, 1, 1, 1, 1]],), 4),                      # 한 줄 확산
    (([[2, 2], [1, 1]],), 1),                       # 다중 발화점 동시
    (([[1]],), -1),                                 # 발화점 없고 1만 → 불가
    (([[2]],), 0),                                  # 발화점만 → 0
    (([[0, 0], [0, 0]],), 0),                       # 전부 벽, 젖을 1 없음
    (([[2, 1, 0, 1, 2]],), 1),                      # 벽으로 나뉜 두 구역, 각 발화점이 1씩 처리
    (([[1, 2, 1], [1, 1, 1], [1, 1, 1]],), 3),      # 가운데 위 발화점 하나에서 확산(최원거리 모서리)
]

if __name__ == "__main__":
    check(solution, cases)
