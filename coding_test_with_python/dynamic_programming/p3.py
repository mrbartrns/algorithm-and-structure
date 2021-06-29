# 바닥 공사
import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline
MOD = 796796
n = int(si())
dp = [0] * 1001
dp[0], dp[1] = 1, 1
for i in range(2, n + 1):
    dp[i] = (dp[i - 1] + 2 * dp[i - 2]) % MOD

print(dp[n])
