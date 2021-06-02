# fluid algorithms
import sys

si = sys.stdin.readline
INF = 987654321

n, m = map(int, si().split())
dp = [[INF for _ in range(n + 1)] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, si().split())
    dp[a][b] = c


def fluid():
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i == j:
                    dp[i][j] = 0
                dp[i][j] = min(dp[i][k] + dp[k][j], dp[i][j])
