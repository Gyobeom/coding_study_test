# def solution(grid):
#     """여기에 풀이를 구현한다.

#     - 함수 이름은 반드시 `solution` 으로 둔다(채점기가 이 이름을 호출한다).
#     - grid: 0(물)과 1(땅)으로 이루어진 2차원 리스트.
#     - 모든 땅 칸의 바깥 둘레(경계 또는 물에 닿은 변)의 총합을 return 한다.
#     """

#     # 상하좌우 탐방 및 둘레 구하기는 1이 아닌 경우에 카운트 + 1

#     # 상,하,좌,우
#     all_directions = [(1,0),(-1,0),(0,-1),(0,1)]

#     # 범위 확인
#     def range_check(r,c):
#         return 0 <= r and r < len(grid) and 0 <= c and c < len(grid[r])

#     # 파고들기
#     def dfs(r,c):
#         count = 0
#         # 방문처리
#         grid[r][c] = 2
#         for dr,dc in all_directions:
#             nr,nc = r + dr, c + dc
#             if range_check(nr, nc) == False:
#                 count += 1
#             else:
#                 if grid[nr][nc] == 2:
#                     continue
#                 elif grid[nr][nc] == 0:
#                     count += 1
#                 else:
#                     count += dfs(nr,nc)
#         return count

#     result = 0
#     for r in range(len(grid)):
#         for c in range(len(grid[r])):
#             if grid[r][c] == 1:
#                 result += dfs(r,c)
#     return result


# 0과 1로 이루어진 격자
def solution(grid):
    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    directions = [(1,0),(-1,0),(0,-1),(0,1)]


    # 좌표 접근 허용 가능 함수
    def check_can_go(r,c):
        return 0 <= r and r < len(grid) and 0 <= c and c < len(grid[r]) and grid[r][c] != 0


    def dfs(r, c):
        cnt = 0
        # 방문 처리
        visited[r][c] = True
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if check_can_go(nr, nc) == False:
                cnt += 1
            else:
                if visited[nr][nc] == True:
                    continue
                else:
                    cnt += dfs(nr, nc)
        return cnt


    result = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 1 and visited[r][c] == False:
                result += dfs(r,c)

    return result



# print(solution([[1,0,1]]))