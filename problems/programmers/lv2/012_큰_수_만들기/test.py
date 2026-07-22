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

# 테스트 케이스: (인자_튜플, 기대값). 반환값은 문자열이다.
cases = [
    # 1) 공식 예시 1
    (("1924", 2), "94"),
    # 2) 공식 예시 2
    (("1231234", 3), "3234"),
    # 3) 공식 예시 3
    (("4177252841", 4), "775841"),
    # 4) 앞자리 0 처리 — "10"에서 1 제거 -> "0"
    (("10", 1), "1"),
    # 5) 앞자리 0 처리 — "100"에서 1 제거 -> "10"
    (("100", 1), "10"),
    # 6) k == 자릿수 — 모두 제거되어 빈 문자열
    (("9", 1), ""),
    # 7) 같은 숫자 반복
    (("99999", 2), "999"),
    # 8) 이미 내림차순 — 뒤에서 제거해야 함
    (("54321", 2), "543"),
    # 9) 오름차순 — 앞에서 제거해야 함
    (("12345", 2), "345"),
    # 10) 중간 0 섞임
    (("10001", 3), "11"),
]

if __name__ == "__main__":
    check(solution, cases)
