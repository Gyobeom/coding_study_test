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

# 테스트 케이스: (인자_튜플, 기대값). 인자는 (words,) 하나.
# 반환값은 애너그램 그룹의 개수.
cases = [
    ((["eat", "tea", "tan", "ate", "nat", "bat"],), 3),   # 대표 예시
    ((["abc", "bca", "cab", "xyz"],), 2),                 # 3개 묶음 + 단독
    ((["a"],), 1),                                        # 최소 규모(1개)
    ((["ab", "ab", "ba"],), 1),                           # 중복 포함 전부 한 그룹
    ((["abc", "def", "ghi"],), 3),                        # 전부 서로 다름 → 그룹 = 원소 수
    ((["aabb", "bbaa", "abab", "baba"],), 1),             # 같은 글자 구성 전부 한 그룹
    ((["listen", "silent", "enlist", "google", "gogole"],), 2),  # {listen류}=1, {google류}=1
    ((["z", "z", "z", "z"],), 1),                         # 동일 문자열 반복 → 1
    ((["ba", "ab", "cd", "dc", "ef"],), 3),               # {ab,ba},{cd,dc},{ef}
]

if __name__ == "__main__":
    check(solution, cases)
