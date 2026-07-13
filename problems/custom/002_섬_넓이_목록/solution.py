def solution(grid):
    """여기에 풀이를 구현한다.

    - 함수 이름은 반드시 `solution` 으로 둔다(채점기가 이 이름을 호출한다).
    - grid: 0/1 로 이루어진 2차원 리스트.
    - 각 섬의 넓이를 오름차순 정렬한 리스트를 return 한다.
    """
    # 2차원 격자 gird 상하좌우로 이어진 땅의 크기를 구해 오춤차순으로 정렬한 리스트 반환

    # 격자 벗아났는지 확인 하는 함수 필요
    # 좌표 벗어났는지 여부와, 0이 아닌 경우 (접근 불가가)
    def grid_range_check(r,c):
        return 0 <= r and r < len(grid) and 0 <= c and c < len(grid[0]) and grid[r][c] != 0

    def dfs(r,c):
        grid[r][c] = 0
        area = 1

        for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
            if grid_range_check(r + dr, c + dc) == True:
                area += dfs(r + dr, c + dc)
        return area

    total = []
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == 1:
                total.append(dfs(r,c))
    total.sort()

    return total

# print(solution([[1, 1, 0], [0, 1, 0], [0, 0, 1]]))