# BOJ 1167
import sys

si = sys.stdin.readline
sys.setrecursionlimit(100001)
"""
n = int(si())
graph = [[] for _ in range(n + 1)]
length = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
distance = [0] * (n + 1)
for _ in range(n):
    a, *arr = map(int, si().split())
    for i in range(len(arr) - 1):
        if i % 2 == 0:
            graph[a].append(arr[i])
        else:
            length[a].append(arr[i])

"""
graph = [[], [3], [4], [1, 4], [2, 3, 5], [4]]
length = [[], [2], [4], [2, 3], [4, 3, 6], [6]]
visited = [False, False, False, False, False, False]
n = 5
distance = [0] * (n + 1)


def dfs(v):
    visited[v] = True
    for i in range(len(graph[v])):
        nv = graph[v][i]
        if not visited[nv]:
            distance[nv] = length[v][i] + distance[nv]
            dfs(nv)


dfs(1)
max_v = distance.index(max(distance))

visited = [False] * (n + 1)
distance = [0] * (n + 1)

dfs(max_v)
print(max(distance))