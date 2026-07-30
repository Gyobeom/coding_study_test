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

# 테스트 케이스: (인자_튜플, 기대값). 인자는 (meetings,) 하나이므로 튜플로 감싼다.
# 반환값은 겹치지 않게 배정 가능한 회의의 최대 개수.
cases = [
    (([[1, 4], [3, 5], [0, 6], [5, 7], [3, 8], [5, 9],
       [6, 10], [8, 11], [8, 12], [2, 13], [12, 14]],), 4),  # 고전 예제 → 4
    (([[0, 1], [1, 2], [2, 3]],), 3),                    # 끝=시작 접함 → 전부
    (([[0, 10], [1, 2], [3, 4]],), 2),                   # 긴 것 버리고 2개
    (([],), 0),                                          # 회의 없음 → 0
    (([[5, 8]],), 1),                                    # 하나 → 1
    (([[1, 3], [2, 4], [3, 5], [4, 6]],), 2),            # [1,3],[3,5] → 2
    (([[0, 0], [0, 0], [0, 1]],), 3),                    # 길이 0 회의 접함 → 3
    (([[2, 3], [1, 2], [3, 4], [0, 1]],), 4),            # 정렬 필요, 전부 접함 → 4
]

if __name__ == "__main__":
    check(solution, cases)
