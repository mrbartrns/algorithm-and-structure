# BOJ 9655
import sys

si = sys.stdin.readline

n = int(si())
dp = [0] * (n + 1)
for i in range(1, n + 1):
    if i - 1 >= 0:
        dp[i] = 1 - dp[i - 1]
    if i - 3 >= 0:
        dp[i] = 1 - dp[i - 3]
print("CY" if dp[n] == 0 else "SK")