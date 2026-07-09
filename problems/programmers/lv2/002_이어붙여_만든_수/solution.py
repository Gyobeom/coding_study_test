def solution(digits):
    n = len(digits)
    used = [False] * n
    made = set()                     # 만든 수를 담을 집합(중복 자동 제거)

    def dfs(cur):                    # cur = 지금까지 이어붙인 문자열
        for i in range(n):
            if used[i]:
                continue
            used[i] = True
            nxt = cur + str(digits[i])   # i를 뒤에 이어붙임
            made.add(int(nxt))           # 이 시점의 수를 집합에 추가
            dfs(nxt)                     # TODO ①: nxt를 들고 더 깊이
            used[i] = False              # TODO ②: 되돌리기

    dfs("")                          # 빈 문자열에서 시작
    return len(made)                 # 서로 다른 수의 개수
