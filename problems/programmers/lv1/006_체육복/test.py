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
    # 1) 공식 예시 1 — 여벌로 모두 커버
    ((5, [2, 4], [1, 3, 5]), 5),
    # 2) 공식 예시 2 — 한 명은 못 빌림
    ((5, [2, 4], [3]), 4),
    # 3) 공식 예시 3 — 앞뒤 아니면 못 빌림(1번은 3번에게 못 줌)
    ((3, [3], [1]), 2),
    # 4) 여벌+도난 겹침 — 2번은 자기만 입고 남에게 못 빌려줌
    ((3, [1, 2], [2, 3]), 2),
    # 5) 전원 여벌+도난 — 모두 자기만 입어 전원 참여
    ((5, [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]), 5),
    # 6) 최소 규모 — n=2, 바로 옆이라 빌림 성공
    ((2, [1], [2]), 2),
    # 7) 큰 규모 근처 — 짝수 도난, 홀수 여벌이 전부 커버
    ((10, [2, 4, 6, 8], [1, 3, 5, 7, 9]), 10),
    # 8) 여벌 가진 학생이 전부 도난 — 아무도 못 빌려주지만 자기는 입음
    ((5, [2, 4], [2, 4]), 5),
]

if __name__ == "__main__":
    check(solution, cases)
