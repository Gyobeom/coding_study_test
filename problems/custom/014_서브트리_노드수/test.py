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

# 테스트 케이스: (인자_튜플, 기대값). 인자는 (parent,) 하나.
# 반환값은 각 노드의 서브트리 노드 수를 노드 번호 순서대로 담은 리스트.
cases = [
    (([-1, 0, 0, 1, 1],), [5, 3, 1, 1, 1]),   # 대표 예시
    (([1, -1, 1],), [1, 3, 1]),               # 루트가 가운데(1번)
    (([-1],), [1]),                           # 노드 1개
    (([-1, 0, 1, 2],), [4, 3, 2, 1]),         # 일자 사슬
    (([-1, 0, 0, 0, 0],), [5, 1, 1, 1, 1]),   # 루트에 자식 4개(별 모양)
    (([2, 2, -1, 2],), [1, 1, 4, 1]),         # 루트 2번, 나머지 리프
    (([-1, 0, 1, 1, 3, 3],), [6, 5, 1, 3, 1, 1]),  # 불균형 트리
    (([3, 3, 3, -1],), [1, 1, 1, 4]),         # 루트 3번, 자식 0·1·2
]

if __name__ == "__main__":
    check(solution, cases)
