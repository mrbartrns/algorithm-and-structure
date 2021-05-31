# BOJ 2133
import sys

si = sys.stdin.readline

n = int(si())
dp = [0] * 31
dp[0] = 1
dp[2] = 3


def solve(n):
    for i in range(4, n + 1, 2):
        dp[i] = dp[i - 2] * 3
        for j in range(4, i, 2):
            dp[i] += dp[i - j] * 2
        dp[i] += 2
    return dp[n]


print(solve(n))