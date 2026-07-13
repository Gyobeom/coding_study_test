def solution(n, computers):
    """여기에 풀이를 구현한다.

    - 함수 이름은 반드시 `solution` 으로 둔다(채점기가 이 이름을 호출한다).
    - n: 컴퓨터 수, computers: n×n 인접 행렬.
    - 가장 큰 네트워크에 속한 컴퓨터 수를 return 한다.
    """
    # 인접한 네트워크에서 연결이 가장 큰 수 반환 필요.
    # dfs로 분제 풀기

    # 방문 처리 배열
    visited = [False] * n

    def dfs(i):
        # 방문 처리
        visited[i] = True
        cnt = 1

        for j in range(n):
            if computers[i][j] == 1 and not visited[j]:
                cnt += dfs(j)
                visited[j] = True
        return cnt

    max_val = 0

    for i in range(n):
        if not visited[i]:
            max_val = max(max_val,dfs(i))
    return max_val

# print(solution(3,[[1, 1, 0], [1, 1, 1], [0, 1, 1]]))

