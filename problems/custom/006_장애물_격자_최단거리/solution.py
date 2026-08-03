from collections import deque
def solution(maps):
    """게임 맵 최단거리: (0,0)에서 (n-1,m-1)까지 지나는 최소 칸 수를 반환한다.

    - maps: n×m 2차원 리스트. 1=길, 0=벽.
    - 출발·도착 칸을 모두 포함해 센 최단 칸 수를 return 한다.
    - 도달할 수 없으면 -1 을 return 한다.
    - print 가 아니라 return 으로 돌려준다(채점기가 반환값을 비교한다).
    """
    # 지나야 하는 칸의 최소 개수 반환
    # 2차원 배열 형태, 0,0에서 시작 해서 n-1, m-1 진영 도착
    # 0은벽 1은 길

    queue = deque()
    # 방문 기록
    maps_history = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]
    # 상하좌우 방향
    directions = [(1,0),(-1,0),(0,-1),(0,1)]
    cnt = 0

    # 좌표 벗어낫는지 + 접근 가능 한지 확인 함수
    def check_out_of_range(r,c):
        return 0 <= r and r <= len(maps)-1 and 0 <= c and c <= len(maps[r])-1 and maps[r][c] != 0

    def bfs(r, c, cnt):
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if check_out_of_range(nr,nc) and maps_history[nr][nc] == False:
                maps_history[nr][nc] = True
                queue.append((nr,nc,cnt+1))

    if maps[0][0] == 0 or maps[len(maps) -1][len(maps[0]) -1] == 0:
        return -1
    else:
      # 초기 방문 처리
      maps_history[0][0] = True
      # 초기 데이터 큐 삽입
      queue.append((0,0,1))

      while queue:
          r,c,cnt = queue.popleft()
          # 마지막 도착 했을 때
          if r == len(maps) - 1 and c == len(maps[r]) - 1:
            return cnt
          bfs(r,c,cnt)
      if maps_history[len(maps)-1][len(maps[0])-1] == False:
          return -1

print(solution([[0,1],[1,1]]))