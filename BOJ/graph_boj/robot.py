# BOJ 1726 로봇
"""
1. dy, dx 배열을 선언후, 처음 주어지는 방향과 매핑한다. (동:1 서: 2 남:3 북:4)
2. visited를 3차원 배열로 선언후 False로 초기화한다.
3. bfs에 이동부분과 회전 부분을 분리하여 선언한다.
"""
from collections import deque
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

MAP_STATE = {1: 3, 2: 1, 3: 2, 4: 0}


def bfs(sy, sx, sd, ey, ex, ed):
    que = deque()
    visited = [[[False for _ in range(4)] for _ in range(N)] for _ in range(M)]
    visited[sy][sx][sd] = True
    que.append((sy, sx, sd, 0))  # y, x, d, cnt
    while que:
        y, x, d, cnt = que.popleft()

        if y == ey and x == ex and d == ed:
            return cnt
        # move
        ny, nx = y, x
        for _ in range(3):
            ny += dy[d]
            nx += dx[d]
            if ny < 0 or ny >= M or nx < 0 or nx >= N:
                break
            if graph[ny][nx] == 1:
                break
            if not visited[ny][nx][d]:
                visited[ny][nx][d] = True
                que.append((ny, nx, d, cnt + 1))

        # rotate
        for i in range(1, 4, 2):
            nd = (d + i) % 4
            if not visited[y][x][nd]:
                visited[y][x][nd] = True
                que.append((y, x, nd, cnt + 1))


M, N = map(int, si().split(" "))  # M: 세로, N: 가로
graph = [list(map(int, si().split(" "))) for _ in range(M)]
y1, x1, d1 = map(int, si().split(" "))
y2, x2, d2 = map(int, si().split(" "))
print(bfs(y1 - 1, x1 - 1, MAP_STATE[d1], y2 - 1, x2 - 1, MAP_STATE[d2]))
