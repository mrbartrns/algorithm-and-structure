# BOJ 9095
# 저번보다 좀 더 발전한 코드

import sys

si = sys.stdin.readline


def solve(n):
    dp = [0] * 12
    dp[0] = 1  # 아무것도 더하지 않는 경우도 1이다.

    for i in range(1, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    return dp[n]


t = int(si())
for _ in range(t):
    n = int(si())
    print(solve(n))