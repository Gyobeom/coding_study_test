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
    (([6, 10, 2],), "6210"),
    # 2) 공식 예시 2 — 접두 비교가 필요한 케이스 (3 vs 30, 34 등)
    (([3, 30, 34, 5, 9],), "9534330"),
    # 3) 원소 1개
    (([0],), "0"),
    # 4) 0으로 시작하는 엣지 — 모든 원소 0이면 "0"
    (([0, 0],), "0"),
    # 5) 접두가 같아 이어붙임 비교가 갈리는 케이스 (5 vs 55 vs 56)
    (([5, 56, 55],), "56555"),
    # 6) 같은 값 반복 + 큰 값과 섞임 ("1"*3 + "10" 비교 → 1이 앞)
    (([1, 1, 1, 10],), "11110"),
    # 7) 큰 규모 근처 — 길이 1000, 전부 동일한 값이면 이어붙인 결과도 그 값 반복
    (([100] * 1000,), "100" * 1000),
]

if __name__ == "__main__":
    check(solution, cases)
