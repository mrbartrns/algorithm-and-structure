# BOJ 9205
import sys


def dfs(node):
    visited[node] = True
    for i in range(n + 2):
        if not visited[i] and graph[node][i] == 1:
            dfs(i)


si = sys.stdin.readline

t = int(si())
for _ in range(t):
    n = int(si())
    graph = [[0 for _ in range(n + 2)] for _ in range(n + 2)]
    visited = [False] * (n + 2)
    dist = []
    hx, hy = map(int, si().split())
    dist.append((hx, hy))
    for _ in range(n):
        x, y = map(int, si().split())
        dist.append((x, y))
    dx, dy = map(int, si().split())
    dist.append((dx, dy))
    for i in range(n + 2):
        for j in range(n + 2):
            distance = abs(dist[i][0] - dist[j][0]) + abs(dist[i][1] - dist[j][1])
            if distance <= 1000:
                graph[i][j] = graph[j][i] = 1
    dfs(0)
    if visited[n + 1]:
        print('happy')
    else:
        print('sad')
