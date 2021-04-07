# BOJ 16236
import sys
from collections import deque

si = sys.stdin.readline

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]


def fish_is_in(maps):
    flag = False
    for i in range(n):
        for j in range(n):
            if 0 < maps[i][j] < 9:
                flag = True
                return flag
    return flag


def bfs(x, y):
    que = deque()
    time = 0
    que.append((x, y, time))
    visited[x][y] = True
    graph[x][y] = 0
    res = []
    while que:
        x, y, time = que.popleft()
        if 0 < graph[x][y] < shark:
            res.append((x, y, time))
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] > shark:
                continue
            if not visited[nx][ny]:
                visited[nx][ny] = True
                que.append((nx, ny, time + 1))
    res.sort(key=lambda el: (el[2], el[0], el[1]))
    return res


n = int(si())
graph = [list(map(int, si().split())) for _ in range(n)]

sx, sy = 0, 0
shark = 2
time = 0
eat_count = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            sx, sy = i, j

x, y = sx, sy
while True:
    visited = [[False for _ in range(n)] for _ in range(n)]
    if not fish_is_in(graph):
        print(time)
        break
    res = bfs(x, y)
    if not res:
        print(time)
        break
    nx, ny, t = res[0]
    eat_count += 1
    time += t
    if eat_count == shark:
        shark += 1
        eat_count = 0
    x, y = nx, ny
