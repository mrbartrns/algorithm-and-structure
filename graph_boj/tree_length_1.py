# BOJ 1167
import sys

si = sys.stdin.readline


def dfs(v):
    visited[v] = True
    for i, l in graph[v]:
        if not visited[i]:
            distance[i] = l + distance[v]
            dfs(i)


n = int(si())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
distance = [0] * (n + 1)

for _ in range(n):
    v, *arr = map(int, si().split())
    for i in range(0, len(arr) - 1, 2):
        graph[v].append([arr[i], arr[i + 1]])
print(graph)

dfs(1)
max_d = distance.index(max(distance))

visited = [False] * (n + 1)
distance = [0] * (n + 1)
dfs(max_d)
print(max(distance))