# BOJ 2583
import sys
from collections import deque


def bfs(x, y):
    que = deque([(x, y)])
    graph[x][y] = True
    counts = 1
    while que:
        x, y = que.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if not graph[nx][ny]:
                graph[nx][ny] = True
                que.append((nx, ny))
                counts += 1
    return counts


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
res = []
cnt = 0
si = sys.stdin.readline
m, n, k = map(int, si().split())
graph = [[False for _ in range(m)] for _ in range(n)]
for _ in range(k):
    x1, y1, x2, y2 = map(int, si().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            graph[i][j] = True

for i in range(n):
    for j in range(m):
        if not graph[i][j]:
            cnt += 1
            res.append(bfs(i, j))

res.sort()
print(cnt)
print(" ".join(list(map(str, res))))
