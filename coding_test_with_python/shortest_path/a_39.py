# 화성 탐사
import sys
from collections import deque

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline
INF = 987654321
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs(graph, visited):
    que = deque()
    visited[0][0] = graph[0][0]
    que.append((0, 0, graph[0][0]))
    while que:
        y, x, cost = que.popleft()
        if y == n - 1 and x == n - 1:
            continue

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or ny >= n or nx < 0 or nx >= n:
                continue

            if cost + graph[ny][nx] <= visited[ny][nx]:
                visited[ny][nx] = cost + graph[ny][nx]
                que.append((ny, nx, cost + graph[ny][nx]))


t = int(si())
for _ in range(t):
    n = int(si())
    graph = [list(map(int, si().split())) for _ in range(n)]
    visited = [[INF for _ in range(n)] for _ in range(n)]
    bfs(graph, visited)
    print(visited[n - 1][n - 1])
