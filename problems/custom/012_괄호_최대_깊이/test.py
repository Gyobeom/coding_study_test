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

# 테스트 케이스: (인자_튜플, 기대값). 인자는 (s,) 하나.
# 반환값은 괄호의 최대 중첩 깊이.
cases = [
    (("(())",), 2),            # 2겹
    (("()()",), 1),            # 나란히 → 최대 1
    (("((()))",), 3),          # 3겹
    (("",), 0),                # 빈 문자열 → 0
    (("()",), 1),              # 최소 괄호 한 쌍 → 1
    (("(()(()))",), 3),        # 여러 갈래 중 가장 깊은 곳 3
    (("(()())",), 2),          # 바깥 1 + 안쪽 나란히 → 2
    (("((((()))))",), 5),      # 5겹
    (("()(())((()))",), 3),    # 여러 덩어리, 최대 3
]

if __name__ == "__main__":
    check(solution, cases)
