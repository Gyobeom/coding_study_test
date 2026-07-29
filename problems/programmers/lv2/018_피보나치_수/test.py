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

# 테스트 케이스: (인자_튜플, 기대값). 반환은 F(n) % 1234567 (int).
cases = [
    # 1) 공식 예시
    ((3,), 2),
    # 2) 공식 예시
    ((5,), 5),
    # 3) 제약 최소값 n=2
    ((2,), 1),
    # 4) 작은 값
    ((6,), 8),
    # 5) 작은 값
    ((10,), 55),
    # 6) mod가 실제로 작동하는 규모 (F(40)이 1234567 초과)
    ((40,), 102334155 % 1234567),
    # 7) mod 확인용 중간 규모
    ((100,), 354224848179261915075 % 1234567),
    # 8) 최대 규모 n=100000 — DP로 빠르게 도는지 (재귀 완전탐색 불가) + mod 확인
    ((100000,), 1168141),
]

if __name__ == "__main__":
    check(solution, cases)
