# BOJ 11725
import sys

si = sys.stdin.readline
sys.setrecursionlimit(100001)

n = int(si())
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, si().split())
    tree[a].append(b)
    tree[b].append(a)


visited = [False] * (n + 1)
parent = [0] * (n + 1)


def pre_order(v, p):

    visited[v] = True
    parent[v] = p
    for i in tree[v]:
        if not visited[i]:
            pre_order(i, v)


pre_order(1, 0)
for i in range(n + 1):
    if parent[i] > 0:
        print(parent[i])