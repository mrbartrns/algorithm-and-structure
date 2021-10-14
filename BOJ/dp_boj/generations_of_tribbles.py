# BOJ 9507
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline

dp = [0] * 68
dp[0], dp[1] = 1, 1
dp[2], dp[3] = 2, 4
for i in range(4, 68):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3] + dp[i - 4]
T = int(si())
for _ in range(T):
    N = int(si())
    print(dp[N])
