# BOJ 11724
import sys

si = sys.stdin.readline
sys.setrecursionlimit(2000)


def dfs(graph, v, visited):
    if not visited[v]:
        visited[v] = True
        for i in graph[v]:
            dfs(graph, i, visited)
        return True
    return False


n, m = map(int, si().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, si().split())
    graph[x].append(y)
    graph[y].append(x)
visited = [False] * (n + 1)

res = 0
for i in range(1, len(graph)):
    if dfs(graph, i, visited):
        res += 1

print(res)