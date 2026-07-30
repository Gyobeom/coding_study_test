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
    (([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"), "LRLLLRLLRRL"),
    # 2) 공식 예시 2
    (([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"), "LRLLRRLLLRR"),
    # 3) 동점·hand 규칙 확인 (오른손잡이) — 2에서 동점→R
    (([2, 5, 0], "right"), "RRL"),
    # 4) 같은 입력, 왼손잡이 — 2에서 동점→L (대칭)
    (([2, 5, 0], "left"), "LLR"),
    # 5) 최소 규모: 가운데 숫자 하나, 시작 동점 아님 확인
    (([5], "right"), "R"),
    (([5], "left"), "L"),
    # 6) 함정: 2로 시작 동점→오른손, 이후 8/5/0 거리로 결정
    (([2, 8, 5, 5, 5, 0], "right"), "RRRRRL"),
    # 7) 전부 0 — 매번 가까운 손 판정
    (([0, 0, 0], "left"), "LLL"),
    # 8) 고정 손가락만 (1/4/7 왼, 3/6/9 오른)
    (([1, 4, 7, 3, 6, 9], "right"), "LLLRRR"),
]

if __name__ == "__main__":
    check(solution, cases)
