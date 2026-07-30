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

# 테스트 케이스: (인자_튜플, 기대값). 인자는 (students,) 하나.
# 반환값은 정렬 후 이름만 담은 리스트.
cases = [
    (([["alice", 90], ["bob", 85], ["carol", 90]],), ["alice", "carol", "bob"]),  # 동점 이름순
    (([["tom", 70], ["amy", 70], ["zoe", 95]],), ["zoe", "amy", "tom"]),          # 최고점 먼저 + 동점
    (([],), []),                                                                  # 빈 입력
    (([["kim", 50]],), ["kim"]),                                                  # 한 명
    (([["a", 10], ["b", 10], ["c", 10]],), ["a", "b", "c"]),                      # 전부 동점 → 이름순
    (([["z", 5], ["y", 5], ["x", 5]],), ["x", "y", "z"]),                         # 동점, 역순 입력 → 이름순
    (([["p", -3], ["q", 2], ["r", -3]],), ["q", "p", "r"]),                       # 음수 점수 처리
    (([["dan", 100], ["dan", 100], ["ann", 100]],), ["ann", "dan", "dan"]),       # 이름 중복 동점
    (([["mid", 0], ["low", -1], ["high", 1]],), ["high", "mid", "low"]),          # 0/음수/양수 내림차순
]

if __name__ == "__main__":
    check(solution, cases)
