# BOJ 2156
import sys

si = sys.stdin.readline


def solve(n):
    for i in range(1, n):
        dp[i] = max(dp[i - 2] + arr[i], dp[i - 3] + arr[i - 1] + arr[i], dp[i - 1])
    return dp[n - 1]


arr = [0] * 10000
n = int(si())
for i in range(n):
    arr[i] = int(si())

dp = [0] * 10000
dp[0] = arr[0]

print(solve(n))