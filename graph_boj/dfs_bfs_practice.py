"""
dfs: deep first search
bfs: breadth first search
"""
from collections import deque
import sys

input = sys.stdin.readline


def dfs(graph, v, visited):
    visited[v] = 1
    print(v, end=" ")
    for i in range(len(graph[v])):
        if graph[v][i] == 1 and visited[i] == 0:
            dfs(graph, i, visited)


def bfs(graph, v, visited):
    que = deque([v])
    visited[v] = 0
    while que:
        v = que.popleft()
        print(v, end=" ")
        for i in range(len(graph[v])):
            if graph[v][i] == 1 and visited[i] == 1:
                que.append(i)  # visited를 먼저 처리하여 추가적인 방문을 방지
                visited[i] = 0


n, m, v = map(int, input().split())
graph = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(m):
    x, y = map(int, input().split())
    graph[x][y] = graph[y][x] = 1


visited = [0] * (n + 1)
dfs(graph, v, visited)
print()
bfs(graph, v, visited)