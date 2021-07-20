# BOJ 11404 (플루이드)
import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline
INF = 987654321

n = int(si())
m = int(si())

dp = [[INF for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(n + 1):
    dp[i][i] = 0
for _ in range(m):
    a, b, c = map(int, si().split())
    dp[a][b] = min(dp[a][b], c)

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dp[i][j] = min(dp[i][k] + dp[k][j], dp[i][j])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(dp[i][j] if dp[i][j] < INF else 0, end=" ")
    print()
