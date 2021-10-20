# BOJ 2302 극장 좌석
import sys


sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline

N = int(si())
dp = [0] * (N + 1)
dp[0], dp[1] = 1, 1
vip = [False] * (N + 1)

M = int(si())
for _ in range(M):
    p = int(si())
    vip[p] = True

for i in range(2, N + 1):
    dp[i] = dp[i - 1]
    if not vip[i] and not vip[i - 1]:
        dp[i] += dp[i - 2]
print(dp[N])
