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
    # 1) 공식 예시 — 나란히 짝지어진 괄호
    (("()()",), True),
    # 2) 공식 예시 — 중첩 + 나란히
    (("(())()",), True),
    # 3) 공식 예시 — 개수는 같지만 순서가 틀림
    ((")()(",), False),
    # 4) 공식 예시 — 여는 괄호가 더 많음
    (("(()(",), False),
    # 5) 최소 규모 — 닫는 괄호 하나만
    ((")",), False),
    # 6) 깊게 중첩된 올바른 괄호
    (("((()))",), True),
    # 7) 큰 규모 근처 — '('*50000 + ')'*50000 (길이 100000, 올바름)
    (("(" * 50000 + ")" * 50000,), True),
]

if __name__ == "__main__":
    check(solution, cases)
