# BOJ 10826 피보나치 수 4
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline

N = int(si())
dp = [0] * 10001
dp[1] = 1
for i in range(2, N + 1):
    dp[i] = dp[i - 1] + dp[i - 2]
print(dp[N])
