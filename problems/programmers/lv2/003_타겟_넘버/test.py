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

# 테스트 케이스: (인자_튜플, 기대값). 인자가 둘이므로 (numbers, target) 튜플로.
cases = [
    (([1, 1, 1, 1, 1], 3), 5),   # 공식 예시
    (([4, 1, 2, 1], 4), 2),      # 공식 예시
    (([1], 1), 1),               # 단일 원소, 도달 가능
    (([1], 2), 0),               # 단일 원소, 도달 불가
    (([1, 1], 3), 0),            # 최대합(2) 초과 → 불가
    (([0, 0, 0], 0), 8),         # 0 포함: ±0 8조합 모두 합 0
    (([1, 0, 1], 0), 4),         # 0 + 부호 조합 경계
    (([1, 2, 3, 4, 5], 3), 3),   # 조금 큰 케이스
]

if __name__ == "__main__":
    check(solution, cases)
