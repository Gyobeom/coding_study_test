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

# 테스트 케이스: (인자_튜플, 기대값). 반환은 (방법의 수) % 1234567 (int).
cases = [
    # 1) 공식 예시
    ((4,), 5),
    # 2) 공식 예시
    ((3,), 3),
    # 3) 최소 규모 n=1
    ((1,), 1),
    # 4) 최소 규모 n=2
    ((2,), 2),
    # 5) 작은 값
    ((5,), 8),
    # 6) mod가 실제로 작동하는 규모 (원래 값이 1234567을 초과)
    ((30,), 1346269 % 1234567),
    # 7) mod 확인용 중간 규모
    ((50,), 20365011074 % 1234567),
    # 8) 최대 규모 n=2000 — DP로 빠르게 도는지 + mod 확인
    ((2000,), 694725),
]

if __name__ == "__main__":
    check(solution, cases)
