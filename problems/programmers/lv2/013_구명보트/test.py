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
    # 1) 공식 예시 1 — (50,50) 한 보트, 70·80 각자
    (([70, 50, 80, 50], 100), 3),
    # 2) 공식 예시 2 — 어떤 두 명도 못 합쳐 각자
    (([70, 80, 50], 100), 3),
    # 3) 가벼운 둘은 함께 — (40,40) + 40
    (([40, 40, 40], 80), 2),
    # 4) 최소 규모 — 한 명
    (([40], 240), 1),
    # 5) 전부 제한과 같은 무게 — 둘씩 못 태워 전원 각자
    (([100, 100, 100, 100], 100), 4),
    # 6) 딱 맞는 짝 — 두 쌍
    (([40, 40, 40, 40], 80), 2),
    # 7) 섞인 규모
    (([50, 50, 70, 80, 50, 80], 100), 5),
    # 8) 큰 규모 근처 — 50명 모두 최대 무게라 각자
    (([240] * 50, 240), 50),
]

if __name__ == "__main__":
    check(solution, cases)
