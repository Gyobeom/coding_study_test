def solution(grid):
    """0(바다)/1(땅) 격자에서 가장 큰 섬의 넓이(칸 수)를 반환. 섬이 없으면 0.

    - 함수 이름은 반드시 `solution` 으로 둔다(채점기가 이 이름을 호출한다).
    - 반환값이 곧 정답이다. print 가 아니라 return 으로 돌려준다.

    힌트:
      dfs(r, c) = "여기서부터 이어진 땅의 칸 수"를 반환
        - 경계 밖/바다면 0 반환
        - 그 외엔 현재 칸 방문 처리 후
          return 1 + dfs(상) + dfs(하) + dfs(좌) + dfs(우)
      바깥 이중 for에서 땅을 만날 때마다 넓이를 구해 최댓값 갱신.
    """
    answer = None
    return answer
