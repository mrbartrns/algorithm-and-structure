# BOJ 1904
import sys

si = sys.stdin.readline

n = int(si())


def solve(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 15746
    return dp[n]


print(solve(n))