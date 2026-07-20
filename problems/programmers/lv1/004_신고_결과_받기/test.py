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
    # 1) 공식 예시 1
    ((["muzi", "frodo", "apeach", "neo"],
      ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"],
      2), [2, 1, 1, 0]),
    # 2) 공식 예시 2 — 같은 신고 4번은 1회 처리, k=3 미달로 정지 없음
    ((["con", "ryan"],
      ["ryan con", "ryan con", "ryan con", "ryan con"], 3), [0, 0]),
    # 3) 신고 내역이 하나 — con이 ryan을 신고, k=1이라 ryan 정지 → con만 메일 1통
    ((["con", "ryan"], ["con ryan"], 1), [1, 0]),
    # 4) 중복 신고 제거 확인 — muzi가 frodo를 2번 신고, k=1. frodo 정지. muzi만 메일 1통
    ((["muzi", "frodo", "apeach"],
      ["muzi frodo", "muzi frodo"], 1), [1, 0, 0]),
    # 5) 아무도 k에 도달 못함 — 각자 1번씩만 신고당함, k=2
    ((["a", "b", "c"], ["a b", "b c", "c a"], 2), [0, 0, 0]),
    # 6) 신고자 한 명이 여러 정지 유저를 신고 → 메일 여러 통
    #    a가 b,c,d를 신고. b,c,d 각각 k=1 도달로 모두 정지 → a는 메일 3통
    ((["a", "b", "c", "d"], ["a b", "a c", "a d"], 1), [3, 0, 0, 0]),
    # 7) 큰 규모 근처 — u0가 u1..u200을 각각 신고, 각 피신고자 1번씩만 신고당함
    #    k=1이면 u1..u200 전부 정지 → u0는 메일 200통, 나머지는 0
    ((["u%d" % i for i in range(201)],
      ["u0 u%d" % i for i in range(1, 201)], 1),
     [200] + [0] * 200),
]

if __name__ == "__main__":
    check(solution, cases)
