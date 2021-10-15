# BOJ 14495 피보나치 비스무리한 수열
import sys


sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline


dp = [0] * 117
dp[1] = dp[2] = dp[3] = 1
N = int(si())
for i in range(4, N + 1):
    dp[i] = dp[i - 1] + dp[i - 3]
print(dp[N])
