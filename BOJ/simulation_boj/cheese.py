# BOJ 2636
import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

si = sys.stdin.readline


def bfs(x, y):
    que = deque()
    que.append((y, x))
    visited[y][x] = True
    while que:
        y, x = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if not visited[ny][nx] and graph[ny][nx] == 0:
                visited[ny][nx] = True
                que.append((ny, nx))
            elif not visited[ny][nx] and graph[ny][nx] == 1:
                visited[ny][nx] = True
                graph[ny][nx] = 2


def oxidize():
    cheese = 0
    for y in range(n):
        for x in range(m):
            if graph[y][x] == 2:
                graph[y][x] = 0
            elif graph[y][x] == 1:
                cheese += 1
    return cheese


# n, m = 13, 12
# graph = [
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
#     [0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0],
#     [0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
#     [0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0],
#     [0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0],
#     [0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0],
#     [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
#     [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
#     [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
#     [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# ]
n, m = map(int, si().split())
graph = [list(map(int, si().split())) for _ in range(n)]
previous = 0
time = 0

# init cheese count
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            previous += 1

while True:
    time += 1
    visited = [[False for _ in range(m)] for _ in range(n)]
    bfs(0, 0)

    cur = oxidize()
    if cur > 0:
        previous = cur
    else:
        break

print(time)
print(previous)




