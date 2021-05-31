# BOJ 15591
import sys
from collections import deque

si = sys.stdin.readline
sys.setrecursionlimit(300000)


# def dfs(k, v):
#     visited[v] = True
#     counts[0] += 1
#     for u, value in graph[v]:
#         if not visited[u] and value >= k:
#             dfs(k, u)


def bfs(k, v):
    que = deque()
    que.append(v)
    visited[v] = True
    cnt = 0
    while que:
        v = que.popleft()
        for u, value in graph[v]:
            if not visited[u] and value >= k:
                visited[u] = True
                cnt += 1
                que.append(u)
    return cnt


n, q = map(int, si().split())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, c = map(int, si().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

for _ in range(q):
    visited = [False for _ in range(n + 1)]
    k, v = map(int, si().split())
    res = bfs(k, v)
    print(res)
