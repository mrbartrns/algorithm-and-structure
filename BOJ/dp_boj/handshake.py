# BOJ 8394 악수
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline

N = int(si())
dp = [0] * 10000001
dp[0], dp[1] = 1, 1
for i in range(2, N + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 10
print(dp[N])
