# BOJ 1309
import sys

si = sys.stdin.readline
n = int(si())
MOD = 9901
dp = [[0, 0, 0] for _ in range(n)]
dp[0][0], dp[0][1], dp[0][2] = 1, 1, 1
for i in range(1, n):
    dp[i][0] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2]) % MOD
    dp[i][1] = (dp[i - 1][0] + dp[i - 1][2]) % MOD
    dp[i][2] = (dp[i - 1][0] + dp[i - 1][1]) % MOD

print((dp[n - 1][0] + dp[n - 1][1] + dp[n - 1][2]) % MOD)