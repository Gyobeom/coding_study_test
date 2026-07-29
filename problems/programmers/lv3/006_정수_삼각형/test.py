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

# 테스트 케이스: (인자_튜플, 기대값). 반환은 경로 합의 최댓값(int).
cases = [
    # 1) 공식 예시
    (([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]],), 30),
    # 2) 높이 2
    (([[3], [2, 4]],), 7),
    # 3) 최소 규모 — 높이 1 (한 칸)
    (([[5]],), 5),
    # 4) 최소 규모 — 값이 0인 한 칸
    (([[0]],), 0),
    # 5) 왼쪽 아래로만 내려가는 것이 최대
    (([[1], [9, 1], [9, 1, 1]],), 19),
    # 6) 오른쪽 아래로만 내려가는 것이 최대
    (([[1], [1, 9], [1, 1, 9]],), 19),
    # 7) 0이 섞인 삼각형
    (([[7], [3, 8], [8, 1, 0]],), 18),
    # 8) 큰 값이 섞인 케이스
    (([[9999], [0, 9999], [0, 0, 9999], [1, 1, 1, 1]],), 29998),
    # 9) 최대 규모 500행 — 모든 값 9999, 어느 경로든 합 500*9999
    (([[9999] * (i + 1) for i in range(500)],), 500 * 9999),
]

if __name__ == "__main__":
    check(solution, cases)
