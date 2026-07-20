from collections import deque

def solution(maps):
    """게임 맵 최단거리: (0,0)에서 (n-1,m-1)까지 지나는 최소 칸 수를 반환한다.

    - maps: n×m 2차원 리스트. 1=길, 0=벽.
    - 출발·도착 칸을 모두 포함해 센 최단 칸 수를 return 한다.
    - 도달할 수 없으면 -1 을 return 한다.
    - print 가 아니라 return 으로 돌려준다(채점기가 반환값을 비교한다).
    """

    # n * m 2차원 배열 순회 필요
    # 1인 경우에만 지나갈 수 있는 길, 상,하,좌,우로만 이동 가능
    # 목적지는 n-1, m-1
    # 지나가야 하는 최소 개수를 반환 해야하기에, bfs 사용
    # 출발칸과 도착 칸 또한 개수에 포함.
    # 도착할 방법이 아예 없으면 -1 반환

    # 방문 여부 필요
    visited = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]
    visited[0][0] = True

    # 상하좌우 좌표 배열 리스트
    dir_list = [(1,0),(-1,0),(0,-1),(0,1)]

    # 범위/접근 가능 여부 확인
    def is_in_range(r,c):
        return 0 <= r and len(maps) > r and 0 <= c and len(maps[0]) > c and maps[r][c] != 0 and not visited[r][c]

    def bfs(r,c,cnt):
        q = deque([(r,c,cnt)])
        while q:
            now_r, now_c, now_cnt = q.popleft()
            # 마지막 도달 확인
            if now_r == len(maps) - 1 and now_c == len(maps[0]) - 1:
                return now_cnt

            # 상,하,좌,우 접근
            for dr, dc in dir_list:
                nx_r, nx_c = now_r + dr , now_c + dc
                if is_in_range(nx_r, nx_c):
                    visited[nx_r][nx_c] = True
                    q.append((nx_r, nx_c, now_cnt + 1))
        return -1

    # 초기시작
    return(bfs(0,0,1))

# print(solution(
#     [[1, 0, 1, 1, 1],
#        [1, 0, 1, 0, 1],
#        [1, 0, 1, 1, 1],
#        [1, 1, 1, 0, 1],
#        [0, 0, 0, 0, 1]]
#        ))