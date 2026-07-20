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
    # 1) 공식 예시 1 — 동명이인 없음
    ((["leo", "kiki", "eden"], ["eden", "kiki"]), "leo"),
    # 2) 공식 예시 2 — 동명이인 없음, 순서 뒤섞임
    ((["marina", "josipa", "nikola", "vinko", "filipa"],
      ["josipa", "filipa", "marina", "nikola"]), "vinko"),
    # 3) 공식 예시 3 — 동명이인(mislav 2명 중 1명만 완주)
    ((["mislav", "stanko", "mislav", "ana"],
      ["stanko", "ana", "mislav"]), "mislav"),
    # 4) 최소 규모 — 참가자 1명, 완주자 0명
    ((["kim"], []), "kim"),
    # 5) 완주자가 없는 참가자가 맨 앞에 위치
    ((["a", "b", "c"], ["b", "c"]), "a"),
    # 6) 전원 동명이인 — 3명 중 1명 미완주
    ((["sam", "sam", "sam"], ["sam", "sam"]), "sam"),
    # 7) 최대 규모 근처 — 5만명, 마지막 1명만 미완주
    (([f"p{i}" for i in range(50000)],
      [f"p{i}" for i in range(49999)]), "p49999"),
]

if __name__ == "__main__":
    check(solution, cases)
