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

# 테스트 케이스: (인자_튜플, 기대값). 인자가 하나(grid)이므로 튜플로 감싼다.
# 반환값은 오름차순 정렬된 넓이 리스트.
cases = [
    (([[1, 1, 0], [0, 1, 0], [0, 0, 1]],), [1, 3]),   # 넓이 3 + 1
    (([[0, 0], [0, 0]],), []),                         # 섬 없음 → 빈 리스트
    (([[1, 1], [1, 1]],), [4]),                        # 한 섬(4칸)
    (([[1]],), [1]),                                   # 1칸 땅
    (([[0]],), []),                                    # 1칸 바다
    (([[1, 0], [0, 1]],), [1, 1]),                     # 크기 1 섬 둘
    (([[1, 1, 0, 0, 0],
       [1, 1, 0, 0, 1],
       [0, 0, 0, 1, 1],
       [0, 0, 0, 0, 0],
       [1, 0, 1, 0, 1]],), [1, 1, 1, 3, 4]),           # 넓이 4·3·1·1·1 정렬
    (([[0, 1, 0, 1, 1],
       [1, 1, 0, 1, 0],
       [0, 0, 0, 0, 0],
       [1, 1, 1, 0, 1]],), [1, 3, 3, 3]),              # 넓이 3·3·3·1 정렬
]

if __name__ == "__main__":
    check(solution, cases)
