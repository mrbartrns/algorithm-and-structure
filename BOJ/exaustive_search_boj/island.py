# BOJ 2589
import sys
from collections import deque

si = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    que = deque([(x, y, 0)])
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[x][y] = True
    res = 0
    while que:
        x, y, cnt = que.popleft()
        res = max(res, cnt)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if not visited[nx][ny] and graph[nx][ny] == "L":
                visited[nx][ny] = True
                que.append((nx, ny, cnt + 1))
    return res


n, m = map(int, si().split())
graph = [list(si().strip()) for _ in range(n)]
res = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == "L":
            res = max(res, bfs(i, j))
print(res)
