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
    # 1) 공식 예시 1 — 가장 높은 우선순위가 먼저 실행
    (([2, 1, 3, 2], 2), 1),
    # 2) 공식 예시 2 — 동점 다수 사이 순서 판정
    (([1, 1, 9, 1, 1, 1], 0), 5),
    # 3) 최소 규모 — 프로세스 1개
    (([1], 0), 1),
    # 4) 전부 같은 우선순위 — 원래 순서 그대로 실행
    (([3, 3, 3, 3], 2), 3),
    # 5) 추적 프로세스가 가장 낮아 마지막에 실행
    (([5, 4, 3, 2, 1], 4), 5),
    # 6) 오름차순 우선순위 — 맨 뒤가 가장 높아 먼저 실행
    (([1, 2, 3, 4], 3), 1),
    # 7) 큰 규모 근처 — 100개 모두 동일 우선순위, 추적 대상은 인덱스 99
    (([5] * 100, 99), 100),
]

if __name__ == "__main__":
    check(solution, cases)
