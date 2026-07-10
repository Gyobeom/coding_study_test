def solution(grid):
    """0(바다)/1(땅) 격자에서 상하좌우로 이어진 땅 덩어리(섬)의 개수를 반환.

    - 함수 이름은 반드시 `solution` 으로 둔다(채점기가 이 이름을 호출한다).
    - 반환값이 곧 정답이다. print 가 아니라 return 으로 돌려준다.

    힌트:
      1) 이중 for로 격자를 훑다가 방문 안 한 땅(1)을 만나면 섬 +1, 그 자리서 dfs 시작
      2) dfs(r, c): 현재 칸 방문 처리 후 상하좌우 4칸으로 재귀
         (재귀 앞에서 경계 밖/바다/방문됨이면 즉시 return)
    """
    answer = None

    # 상,하,좌,우로 이동 해야함
    # 이동 한 경우에는 이동 한 것으로 쳐야함. (방문 기록 필요)
    # 좌표를 벗어나는 경우 확인 필요
    def grid_range_check(r,c):
      return 0 <= r and r < len(grid) and 0 <= c and c < len(grid[0]) and grid[r][c] != 0

    cnt = 0

    def dfs(r,c):
      grid[r][c] = 0

      for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
          if grid_range_check(r+dr, c+dc) == True:
            dfs(r + dr, c + dc)

    for r in range(len(grid)):
      for c in range(len(grid[0])):
        if grid[r][c] == 1:
          cnt += 1
          dfs(r,c)

    return cnt

# print(solution([[1, 1, 0],
#         [0, 1, 0],
#         [0, 0, 1]]))
