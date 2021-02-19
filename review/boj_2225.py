# BOJ 2225
import sys

si = sys.stdin.readline

n, k = map(int, si().split())
dp = [[0 for _ in range(201)] for _ in range(201)]
for i in range(201):
    dp[1][i] = 1


def solve(n, k):
    for i in range(2, 201):
        for j in range(201):
            dp[i][j] = sum(dp[i - 1][: j + 1]) % 1000000000
    return dp[k][n]


print(solve(n, k))