# BOJ 2157 여행
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
INF = 987654321


def dfs(m, node):
    if m <= 1 and node != 1:
        return -INF
    if node == 1:
        return 0
    if cache[m][node] != -1:
        return cache[m][node]
    cache[m][node] = -INF
    for i in range(1, node):
        if not adj[i][node]:
            continue
        cache[m][node] = max(cache[m][node], adj[i][node] + dfs(m - 1, i))
    return cache[m][node]


N, M, K = map(int, si().strip().split(" "))
adj = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
for _ in range(K):
    a, b, c = map(int, si().strip().split(" "))
    adj[a][b] = max(adj[a][b], c)
cache = [[-1 for _ in range(N + 1)] for _ in range(M + 1)]
dfs(M, N)
print(cache[M][N])
