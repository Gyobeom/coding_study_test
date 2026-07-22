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

# 테스트 케이스: (인자_튜플, 기대값). 인자가 하나여도 튜플로 감싼다.
cases = [
    # 1) 공식 예시 1 — 7, 17, 71
    (("17",), 3),
    # 2) 공식 예시 2 — 앞 0/중복 처리, 11 과 101
    (("011",), 2),
    # 3) 같은 숫자 중복 — 서로 다른 조합이 같은 수(11)로 합쳐짐
    (("11",), 1),
    # 4) 한 조각 소수 — 2
    (("2",), 1),
    # 5) 1은 소수 아님
    (("1",), 0),
    # 6) 0은 소수 아님
    (("0",), 0),
    # 7) 세 자리 조합
    (("123",), 5),
    # 8) 최대 길이(7) — 모두 같은 숫자
    (("7777777",), 1),
]

if __name__ == "__main__":
    check(solution, cases)
