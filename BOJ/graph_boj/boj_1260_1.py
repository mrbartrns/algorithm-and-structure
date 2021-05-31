# BOJ 1260
import sys
from collections import deque

n = 4
m = 5
v = 1
graph = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
visited = [0] * (n + 1)
segment = [(1, 2), (1, 3), (1, 4), (2, 4), (3, 4)]
for x, y in segment:
    graph[x][y] = graph[y][x] = 1


def dfs(graph, v, visited):
    visited[v] = 1
    print(v, end=" ")
    for i in range(n + 1):
        if graph[v][i] == 1 and visited[i] == 0:
            dfs(graph, i, visited)


def bfs(graph, v, visitdd):
    que = deque([v])
    visited[v] = 0
    while que:
        v = que.popleft()
        print(v, end=" ")
        for i in range(n + 1):
            if graph[v][i] == 1 and visited[i] == 1:
                que.append(i)
                visited[i] = 0


dfs(graph, v, visited)
print()
bfs(graph, v, visited)