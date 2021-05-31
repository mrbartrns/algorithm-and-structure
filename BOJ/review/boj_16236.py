# BOJ 16236 (아기상어)
import heapq
import sys
from collections import deque

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs(init_y: int, init_x: int, shark_size: int) -> tuple:
    """
    find location where baby shark to go.
    움직이려는 지점에 물고기가 있고, 현재 상어의 크기보다 작다면 힙 자료구조에 추가한다.
    움직이려는 지점의 물고기의 크기가 상어보다 크다면, 그 지점으로는 움직일 수 없다.
    먹을 수 있는 상어가 없다면, -1, -1을 반환한다.
    Args:
        init_y(int): start row index of baby shark
        init_x(int): start column index of baby shark
        shark_size: size of baby shark
    Returns(tuple): index of fish what baby shark has to eat and second (y, x, cnt)
                    y, x are a baby shark's location.
    """
    que = deque()
    visited = [[False for _ in range(n)] for _ in range(n)]
    q = []
    visited[init_y][init_x] = True
    que.append((init_y, init_x, 0))
    while que:
        y, x, cnt = que.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or ny >= n or nx < 0 or nx >= n:
                continue

            if graph[ny][nx] > shark_size:
                continue

            if not visited[ny][nx] and graph[ny][nx] <= shark_size:
                que.append((ny, nx, cnt + 1))
                visited[ny][nx] = True

                if 0 < graph[ny][nx] < shark_size:
                    heapq.heappush(q, (cnt + 1, ny, nx))
    if q:
        r_cnt, ry, rx = heapq.heappop(q)
        return ry, rx, r_cnt
    else:
        return -1, -1, -1


def initialize() -> tuple:
    """
    initialize location of baby shark. get 9's location in the graph.
    Returns: location of baby shark

    """
    for y in range(n):
        for x in range(n):
            if graph[y][x] == 9:
                return y, x


n = int(si())
graph = [list(map(int, si().split())) for _ in range(n)]
baby_shark = 2
time = 0
eat_cnt = 0

# initialize baby shark location
shark_y, shark_x = initialize()

while True:
    next_y, next_x, time_cnt = bfs(shark_y, shark_x, baby_shark)
    if next_y == -1 and next_x == -1 and time_cnt == -1:
        print(time)
        break

    # 바뀐 정보들 반영
    graph[shark_y][shark_x] = 0
    graph[next_y][next_x] = 9
    eat_cnt += 1
    time += time_cnt
    shark_y, shark_x = next_y, next_x

    if baby_shark == eat_cnt:
        baby_shark += 1
        eat_cnt = 0
