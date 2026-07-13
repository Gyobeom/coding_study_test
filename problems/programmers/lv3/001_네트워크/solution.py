def solution(n, computers):
    visited = [False] * n

    def dfs(i):
        visited[i] = True
        for j in range(n):
            if computers[i][j] == 1 and not visited[j]:
                dfs(j)          # 격자의 dfs(r+dr, c+dc) 자리

    cnt = 0
    for i in range(n):          # 격자의 이중 for문 → 여기선 단일 for
        if not visited[i]:      # 아직 방문 안 한 컴퓨터를 만나면
            cnt += 1            # 새 네트워크 하나 발견
            dfs(i)
                    # 그 네트워크 전체를 방문 처리

    return cnt