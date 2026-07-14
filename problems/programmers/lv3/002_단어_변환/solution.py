import sys

def solution(begin, target, words):
    # 변환 해야 하는 각 단어 별로 경우의 수 필요.
    # 시작 값은 words 순회 하면서, 시작 되어지고 방문 처리 필요.
    # 비교 하는 단어와 비교해서 1글자 틀린지 여부 확인 필요.

    # 조건
    # 만약 words에 최종 변환 값이 없다면 0 처리
    # 못 찾는 다면 0 처리
    # 반복문에서 시작 할 때, 값 비교 하는 부분을 통과한 값 만 실행 되도록

    # 변경 가능 여부 반환 함수 a - 비교 할 단어, b - 비교 당할 단어
    def can_change_word(a,b):
        cnt = 0
        for i in range(len(a)):
            # 포함되어 있지 않을 때,
            if a[i] != b[i]:
                cnt += 1
            if cnt == 2:
                return False
        return True

    # 이미 단어 변경 가능 한 상태로 전달 됨. 방문 처리 진행
    def dfs(i,cnt, selected_words):
        if words[i] == target:
            return cnt

        # 반목문을 통해서 배열 돌면서 또 변경이 가능한, 여부 확인 필요.
        best = sys.maxsize   # "아직 성공한 가지 없음" = 무한대 (바깥 min_val과 같은 패턴)
        for j in range(len(words)):
            # 단어 변경이 가능하며, 지금까지 선택한 배열리스트에 포함이 안되어 있을 경우 가능
            if can_change_word(words[i],words[j]) and words[j] not in selected_words:
                best = min(best, dfs(j,cnt + 1,[*selected_words, words[j]]))  # 자식의 답을 받아 최소만 남김
        return best          # 갈 곳이 없거나 전부 실패면 sys.maxsize가 그대로 올라감


    if target not in words:
        return 0
    else:
        min_val = sys.maxsize
        for i in range(len(words)):
            if can_change_word(begin, words[i]):
                min_val = min(dfs(i, 1, [words[i]]),min_val)

        if min_val == sys.maxsize:
            return 0
        else:
            return min_val

# print(solution('hit','cog',["hot","dot","dog","lot","log","cog"]))
