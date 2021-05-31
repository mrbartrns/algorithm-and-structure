# BOJ 10844
import sys

si = sys.stdin.readline

n = int(si())
dp = [[0 for _ in range(10)] for _ in range(100)]
for i in range(1, 10):
    dp[0][i] = 1


def solve(n):
    for i in range(1, 100):
        for j in range(10):
            if j >= 1:
                dp[i][j] += dp[i - 1][j - 1]
            if j < 9:
                dp[i][j] += dp[i - 1][j + 1]
    value = sum(dp[n - 1]) % 1000000000
    return value


print(solve(n))