# BOJ 1389
import sys

si = sys.stdin.readline
INF = 1e9
n, m = map(int, si().split())
graph = [[INF for _ in range(n + 1)] for _ in range(n + 1)]
cnt = INF
idx = 0
for i in range(m):
    a, b = map(int, si().split())
    graph[a][b] = graph[b][a] = 1
    graph[a][a] = graph[b][b] = 0

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, n + 1):
    ans = 0
    for j in range(1, n + 1):
        ans += graph[i][j]
    if cnt > ans:
        cnt = ans
        idx = i

print(idx)
