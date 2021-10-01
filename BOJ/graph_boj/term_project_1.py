# BOJ 9466
import sys

sys.setrecursionlimit(1000000)
sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline


def dfs(node):
    visited[node] = True
    nxt = graph[node]
    if visited[nxt] and not cycled[nxt]:
        u = nxt
        counts[0] += 1
        while u != node:
            u = graph[u]
            counts[0] += 1

    elif not visited[nxt]:
        dfs(nxt)
    cycled[node] = True


t = int(si())
for _ in range(t):
    n = int(si())
    graph = [0] + list(map(int, si().split(" ")))
    visited = [False] * (n + 1)
    cycled = [False] * (n + 1)
    counts = [0]
    for i in range(1, n + 1):
        c = graph[i]
        if not visited[c]:
            dfs(c)
    print(n - counts[0])