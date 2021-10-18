# BOJ 15988 1, 2, 3 더하기 3
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline


MAX = 1000001
MOD = 1000000009

dp = [0] * MAX
dp[0] = 1
for i in range(1, MAX):
    if i - 1 >= 0:
        dp[i] += dp[i - 1]
    if i - 2 >= 0:
        dp[i] += dp[i - 2]
    if i - 3 >= 0:
        dp[i] += dp[i - 3]
    dp[i] %= MOD

T = int(si())
for _ in range(T):
    N = int(si())
    print(dp[N])
