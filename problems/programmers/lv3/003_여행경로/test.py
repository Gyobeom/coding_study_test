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
# 인자가 하나(tickets)이므로 ((tickets,), 기대값) 형태로 감싼다.
cases = [
    # 1) 프로그래머스 공식 예시 1
    (([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]],),
     ["ICN", "JFK", "HND", "IAD"]),

    # 2) 프로그래머스 공식 예시 2 (사전순으로 더 앞선 경로를 골라야 함)
    (([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]],),
     ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]),

    # 3) 엣지: 티켓 1장
    (([["ICN", "AAA"]],),
     ["ICN", "AAA"]),

    # 4) 엣지: 왕복 (ICN 으로 되돌아오는 순환)
    (([["ICN", "BBB"], ["BBB", "ICN"]],),
     ["ICN", "BBB", "ICN"]),

    # 5) 엣지: 같은 구간 티켓 중복 + 순환
    (([["ICN", "AAA"], ["AAA", "ICN"], ["ICN", "AAA"]],),
     ["ICN", "AAA", "ICN", "AAA"]),

    # 6) 사전순 함정: 그리디로 ICN->AAA 를 먼저 고르면 막다른 길.
    #    ICN->BBB 로 가야 모든 티켓을 사용할 수 있다 -> 백트래킹 필요.
    (([["ICN", "AAA"], ["ICN", "BBB"], ["BBB", "ICN"]],),
     ["ICN", "BBB", "ICN", "AAA"]),

    # 7) 사전순 함정 2: A 에서 사전순 빠른 A->B 를 먼저 쓰면 B 에서 막힘.
    #    A->C(그 다음 C->A) 를 먼저 소화해야 A->B 를 마지막에 쓸 수 있다.
    (([["ICN", "A"], ["A", "B"], ["A", "C"], ["C", "A"]],),
     ["ICN", "A", "C", "A", "B"]),

    # 8) 긴 사슬 (백트래킹 없이도 풀리지만 경로 복원 확인용)
    (([["ICN", "A"], ["A", "B"], ["B", "C"], ["C", "D"]],),
     ["ICN", "A", "B", "C", "D"]),
]

if __name__ == "__main__":
    check(solution, cases)
