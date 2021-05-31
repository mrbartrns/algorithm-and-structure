# BOJ 7569
import sys
from collections import deque

si = sys.stdin.readline

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]


def bfs(tomatos):
    que = deque(tomatos)
    cnt = 1
    while que:
        z, y, x = que.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if nz < 0 or nz >= h or ny < 0 or ny >= n or nx < 0 or nx >= m:
                continue

            if graph[nz][ny][nx] == -1:
                continue

            if graph[nz][ny][nx] == 0:
                graph[nz][ny][nx] = graph[z][y][x] + 1
                cnt = max(cnt, graph[nz][ny][nx])
                que.append((nz, ny, nx))
    return cnt - 1


m, n, h = map(int, si().split())
graph = [[] for _ in range(h)]
tomatos = []
zero = False
for i in range(h):
    for j in range(n):
        arr = list(map(int, si().split()))
        graph[i].append(arr)


# 익은 토마토를 배열에 넣기
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                tomatos.append((i, j, k))


val = bfs(tomatos)
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 0:
                zero = True
                break

print(val if not zero else -1)