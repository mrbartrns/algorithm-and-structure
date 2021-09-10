# BOJ 14916 거스름돈

import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
INF = 987654321

n = int(si())

dp = [INF] * 100001
dp[0] = 0

for i in range(1, n + 1):
    if dp[i - 2] < INF:
        dp[i] = min(dp[i], dp[i - 2] + 1)
    if dp[i - 5] < INF:
        dp[i] = min(dp[i], dp[i - 5] + 1)

print(dp[n] if dp[n] < INF else -1)