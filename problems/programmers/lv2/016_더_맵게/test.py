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

# 테스트 케이스: (인자_튜플, 기대값). 반환은 최소 섞기 횟수(int), 불가능하면 -1.
cases = [
    # 1) 공식 예시
    (([1, 2, 3, 9, 10, 12], 7), 2),
    # 2) 최소 규모(2개) — 아무리 섞어도 불가능
    (([1, 1], 7), -1),
    # 3) 이미 전부 K 이상 — 0회
    (([10, 20, 30], 5), 0),
    # 4) K=0 — 항상 0회(음수 스코빌은 없음)
    (([0, 0, 0], 0), 0),
    # 5) 2개인데 한 번 섞어 K 도달
    (([1, 2], 5), 1),
    # 6) 중복 값 다수 — 두 번 섞어야 전부 K 이상
    (([5, 5, 5, 5], 10), 2),
    # 7) 최종 1개까지 섞었는데도 K 미만 → -1
    (([1, 2, 3], 1000000000), -1),
    # 8) 딱 경계에서 만족(섞은 값이 정확히 K)
    (([1, 3], 7), 1),
    # 9) 여러 번 섞어야 하는 경우
    (([0, 0, 0, 0, 5], 6), 4),
]

if __name__ == "__main__":
    check(solution, cases)
