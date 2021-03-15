# BOJ 2293
import sys

si = sys.stdin.readline

n, k = map(int, si().split())
coins = [int(si()) for _ in range(n)]

dp = [0 for _ in range(k + 1)]
dp[0] = 1

for i in range(n):
    for j in range(k + 1):
        if j - coins[i] >= 0:
            dp[j] += dp[j - coins[i]]

print(dp[k])