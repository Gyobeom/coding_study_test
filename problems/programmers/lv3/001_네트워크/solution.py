from collections import deque


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


# def solution(n, computers):
#     visited = [False] * n

#     def bfs(start):
#         visited[start] = True
#         q = deque([start])

#         while q:
#             i = q.popleft()
#             for j in range(n):
#                 if computers[i][j] == 1 and not visited[j]:
#                     visited[j] = True   # (수정) 원래 `visited[j]`로만 적혀 있어 표시가 안 됨 → 삼각형 연결에서 무한 루프
#                     q.append(j)

#     cnt = 0
#     for i in range(n):
#         if not visited[i]:
#             cnt += 1
#             bfs(i)
#     return cnt