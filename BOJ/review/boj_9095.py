# BOJ 9095
import sys

si = sys.stdin.readline


def solve(n):
    for i in range(1, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    return dp[n]


t = int(si())
for _ in range(t):
    n = int(si())

    dp = [0] * 11
    dp[0] = 1

    print(solve(n))