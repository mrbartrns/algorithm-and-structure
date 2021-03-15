# BOJ 11051
import sys

si = sys.stdin.readline

"""
def binomial(n, r):
    if dp[n][r] > -1:
        return dp[n][r]

    if n == r or r == 0:
        dp[n][r] = 1
        return dp[n][r]

    dp[n][r] = (binomial(n - 1, r - 1) + binomial(n - 1, r)) % 10007
    return dp[n][r]
"""


def binomial(n, r):
    for i in range(n + 1):
        for j in range(r + 1):
            if i == j or j == 0:
                dp[i][j] = 1
            elif i >= 1 and j >= 1 and i > j:
                dp[i][j] = (dp[i - 1][j] + dp[i - 1][j - 1]) % 10007
    return dp[n][r]


n, r = map(int, si().split())
dp = [[-1 for _ in range(r + 1)] for _ in range(n + 1)]
print(binomial(n, r))