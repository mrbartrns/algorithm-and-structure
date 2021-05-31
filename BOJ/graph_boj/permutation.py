# BOJ 10451

import sys
from collections import deque

si = sys.stdin.readline
sys.setrecursionlimit(2000)


def dfs(graph, v, visited):
    if not visited[v]:
        visited[v] = True
        for i in graph[v]:
            dfs(graph, i, visited)
        return True
    return False


t = int(si())
for _ in range(t):
    n = int(si())
    graph = [[] for _ in range(n + 1)]
    arr = list(map(int, si().split()))

    for i in range(n):
        graph[i + 1].append(arr[i])
        if i + 1 != arr[i]:
            graph[arr[i]].append(i + 1)

    visited = [False] * (n + 1)

    ret = 0
    for i in range(1, n + 1):
        if dfs(graph, i, visited):
            ret += 1

    print(ret)