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

# 테스트 케이스: (인자_튜플, 기대값). 반환은 모든 사람 심사 최소 시간(int).
cases = [
    # 1) 공식 예시
    ((6, [7, 10]), 28),
    # 2) 최소 규모 — 사람 1명, 심사관 1명
    ((1, [5]), 5),
    # 3) 심사관 1명이 n명을 순차 처리
    ((5, [3]), 15),
    # 4) 심사관이 사람보다 많음 — 가장 빠른 1명이면 충분
    ((1, [2, 5, 9]), 2),
    # 5) 동일한 심사시간 여러 명
    ((10, [2, 2, 2, 2, 2]), 4),
    # 6) 큰 n — 이분탐색으로 빠르게 도는지
    ((1000000000, [1]), 1000000000),
    # 7) 큰 n + 여러 심사관
    ((1000000000, [7, 10]), 4117647060),
    # 8) 최대 심사시간 근처 + 큰 n
    ((1000000000, [1000000000]), 1000000000000000000),
    # 9) 서로 다른 심사시간 다수
    ((100, [1, 2, 3, 4, 5]), 45),
]

if __name__ == "__main__":
    check(solution, cases)
