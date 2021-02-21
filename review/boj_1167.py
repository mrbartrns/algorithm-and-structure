# BOJ 1167
import sys

sys.setrecursionlimit(100001)
si = sys.stdin.readline


def dfs(v, dist):
    visited[v] = True
    distance[v] = dist
    for node, l in tree[v]:
        if not visited[node]:
            dfs(node, dist + l)


n = int(si())
tree = [[] for _ in range(n + 1)]
for _ in range(n):
    temp = list(map(int, si().split()))
    for i in range(1, len(temp), 2):
        if temp[i] > -1:
            tree[temp[0]].append((temp[i], temp[i + 1]))
"""
n = 5
tree = [[], [(3, 2)], [(4, 4)], [(1, 2), (4, 3)], [(2, 4), (3, 3), (5, 6)], [(4, 6)]]
"""
visited = [False] * (n + 1)
distance = [0] * (n + 1)
dfs(1, 0)

idx = distance.index(max(distance))

visited = [False] * (n + 1)
distance = [0] * (n + 1)
dfs(idx, 0)
print(max(distance))