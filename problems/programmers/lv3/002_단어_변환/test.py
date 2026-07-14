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
    # 1) 프로그래머스 공식 예시 1 — 4단계 변환
    (("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]), 4),
    # 2) 프로그래머스 공식 예시 2 — target(cog)이 words에 없어 도달 불가
    (("hit", "cog", ["hot", "dot", "dog", "lot", "log"]), 0),
    # 3) 1단계 변환 — target이 begin과 한 글자만 다르고 words에 있음
    (("hit", "hot", ["hot", "dot", "dog"]), 1),
    # 4) target은 words에 있지만 begin에서 어느 경로로도 도달 불가(고립)
    (("hit", "abc", ["hot", "dot", "dog", "abc"]), 0),
    # 5) begin에서 한 글자만 다른 단어가 아예 없음 → 출발 자체 불가
    (("aaa", "bbb", ["ccc", "ddd", "bbb"]), 0),
    # 6) 긴 사슬 — 한 글자씩 5단계에 걸쳐 변환
    (("aaaa", "bbbb", ["aaab", "aabb", "abbb", "bbbb"]), 4),
    # 7) 여러 경로 중 최단 선택 — 지름길(2단계)이 존재
    (("hit", "cog", ["hog", "hot", "dot", "dog", "lot", "log", "cog"]), 3),
    # 8) target이 begin에서 바로 한 글자 차이지만 words 순서상 뒤에 있음
    (("cat", "dog", ["cot", "dot", "dog", "cog", "cag"]), 3),
]

if __name__ == "__main__":
    check(solution, cases)
