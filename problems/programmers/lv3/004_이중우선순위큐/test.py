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

# 테스트 케이스: (인자_튜플, 기대값). 반환은 [최댓값, 최솟값], 비면 [0, 0].
cases = [
    # 1) 공식 예시 1 — 결국 비게 됨
    ((["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"],), [0, 0]),
    # 2) 공식 예시 2
    ((["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"],), [333, -45]),
    # 3) 최소 규모(명령 1개) — 삽입만
    ((["I 5"],), [5, 5]),
    # 4) 빈 큐에 D 명령 — 무시
    ((["D 1"],), [0, 0]),
    # 5) 원소 1개일 때 최댓값=최솟값
    ((["I 7", "I 3", "D 1"],), [3, 3]),
    # 6) 중복 값 + 최댓값 삭제가 중복 하나만 지우는지
    ((["I 5", "I 5", "I 5", "D 1"],), [5, 5]),
    # 7) 음수만 삽입
    ((["I -10", "I -20", "I -30"],), [-10, -30]),
    # 8) 넣은 만큼 다 빼서 빈 큐
    ((["I 1", "I 2", "D 1", "D -1", "D 1"],), [0, 0]),
    # 9) 삽입·삭제 섞임, 남은 원소 다수
    ((["I 100", "I 50", "I 200", "I 25", "D 1", "D -1"],), [100, 50]),
]

if __name__ == "__main__":
    check(solution, cases)
