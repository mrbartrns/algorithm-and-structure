# BOJ 19947 투자의 귀재 배주형
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline


H, Y = map(int, si().split(" "))
dp = [0] * (Y + 1)
dp[0] = H
for i in range(1, Y + 1):
    if i - 1 >= 0:
        dp[i] = max(dp[i], int(dp[i - 1] * 0.05 + dp[i - 1]))
    if i - 3 >= 0:
        dp[i] = max(dp[i], int(dp[i - 3] * 0.2 + dp[i - 3]))
    if i - 5 >= 0:
        dp[i] = max(dp[i], int(dp[i - 5] * 0.35 + dp[i - 5]))
print(dp[Y])
