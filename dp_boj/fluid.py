# BOJ 11404
import sys

si = sys.stdin.readline
INF = 987654321

n = int(si())
m = int(si())
dp = [[INF for _ in range(n + 1)] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, si().split())
    dp[a][b] = min(dp[a][b], c)

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                dp[i][j] = 0
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(dp[i][j] if dp[i][j] < INF else 0, end=" ")
    print()
