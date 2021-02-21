# BOJ 1260
import sys
from collections import deque

si = sys.stdin.readline

n, m, v = map(int, si().split())

graph = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, si().split())
    graph[a][b] = graph[b][a] = 1

visited = [0] * (n + 1)


def dfs(v):
    visited[v] = 1
    print(v, end=" ")
    for i in range(1, n + 1):
        if visited[i] == 0 and graph[v][i] == 1:
            dfs(i)


def bfs(v):
    que = deque([v])
    visited[v] = 0
    while que:
        v = que.popleft()
        print(v, end=" ")
        for i in range(1, n + 1):
            if visited[i] == 1 and graph[v][i] == 1:
                visited[i] = 0
                que.append(i)


dfs(v)
print()
bfs(v)