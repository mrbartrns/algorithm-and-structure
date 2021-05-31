# BOJ 11048
import sys

si = sys.stdin.readline


def solve(n, m):
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + dp[i][j]

    return dp[n][m]


n, m = map(int, si().split())
dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    dp[i] = [0] + list(map(int, si().split()))


print(solve(n, m))