def solution(grid):

    # 좌표 내 + 좌표 접근 가능 여부 검토함수
    def grid_range_check(r,c):
      return 0 <= r and r < len(grid) and 0 <= c and c < len(grid[0]) and grid[r][c] == 1

    def dfs(r,c):
      grid[r][c] = 0
      area = 1

      for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
        if grid_range_check(r + dr, c + dc) == True:
          area += dfs(r + dr, c + dc)
      return area

    best = 0
    for r in range(len(grid)):
      for c in range(len(grid[0])):
        if grid[r][c] == 1:
          best = max(best,dfs(r,c))
    return best
# print(solution([[1,1],[1,1]]))