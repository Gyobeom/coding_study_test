def solution(n, computers):
    """여기에 풀이를 구현한다.

    - 함수 이름은 반드시 `solution` 으로 둔다(채점기가 이 이름을 호출한다).
    - n: 컴퓨터 수, computers: n×n 인접 행렬.
    - 각 네트워크의 크기를 오름차순 정렬한 리스트를 return 한다.
    """

    # 컴퓨터 n대 존재, 컴퓨터 끼리 연결되어 있음.
    # n * n 행렬 DFS

    # 방문 처리 담당 배열
    visited = [False] * n

    # 순회 하면서 연결된 네트워크 방문 처리
    def dfs(i):
        visited[i] = True
        cnt = 1

        for j in range(n):
            # 연결되어 있는 네트워크 이면서 미방문일 경우
            if computers[i][j] == 1 and not visited[j]:
                cnt += dfs(j)
        return cnt

    net_list = []
    # 순회 하면서 방문 반복문 방문 하지 않은 경우에만 카운트
    for i in range(n):
        if visited[i] == False:
            net_list.append(dfs(i))
    net_list.sort()
    return net_list
