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
    # 1) 공식 예시 1
    (([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]), [5, 6, 3]),
    # 2) 공식 예시 2 — 전체 정렬 후 첫/마지막
    (([9, 8, 7, 6, 5], [[1, 5, 1], [1, 5, 5]]), [5, 9]),
    # 3) 최소 규모 — 원소 1개, 명령 1개
    (([42], [[1, 1, 1]]), [42]),
    # 4) 이미 정렬된 배열 — 부분 구간에서 k번째
    (([1, 2, 3, 4, 5], [[2, 4, 2]]), [3]),
    # 5) 역순 배열 — 구간을 잘라 정렬해야 함
    #    [1,3,1]: [5,4,3]->[3,4,5] 1번째=3.  [3,5,3]: [3,2,1]->[1,2,3] 3번째=3.
    (([5, 4, 3, 2, 1], [[1, 3, 1], [3, 5, 3]]), [3, 3]),
    # 6) 중복 값 포함 — 정렬 후 위치 확인
    (([3, 3, 3, 1, 1], [[1, 5, 2], [1, 5, 5]]), [1, 3]),
    # 7) 큰 규모 근처 — 길이 100, 전체를 정렬해 k번째
    ((list(range(100, 0, -1)),
      [[1, 100, 1], [1, 100, 100], [1, 100, 50]]),
     [1, 100, 50]),
]

if __name__ == "__main__":
    check(solution, cases)
