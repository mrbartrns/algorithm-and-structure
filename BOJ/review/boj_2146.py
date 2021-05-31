# BOJ 2146
import sys
from collections import deque

si = sys.stdin.readline
sys.setrecursionlimit(100001)


n = int(si())
graph = []
for _ in range(n):
    graph.append(list(map(int, si().split())))

"""
n = 10
graph = [
    [1, 1, 1, 0, 0, 0, 0, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 0, 1, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 1, 1],
    [0, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]
"""

visited = [[False for _ in range(n)] for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y, label):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False

    if graph[x][y] == 1 and not visited[x][y]:
        visited[x][y] = True
        graph[x][y] = label
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny, label)
        return True
    return False


def bfs(label):
    que = deque()
    for i in range(n):
        for j in range(n):
            if graph[i][j] == label:
                visited[i][j] = True
                que.append((i, j, 0))
    while que:
        x, y, cnt = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            if graph[nx][ny] > 0 and graph[nx][ny] != label:
                return cnt

            if graph[nx][ny] == 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                que.append((nx, ny, cnt + 1))


label = 1
for i in range(n):
    for j in range(n):
        if dfs(i, j, label):
            label += 1

dist = 1000
for i in range(1, label):
    visited = [[False for _ in range(n)] for _ in range(n)]
    dist = min(dist, bfs(i))
print(dist)