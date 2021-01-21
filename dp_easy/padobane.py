# BOJ 9461
import sys

input = sys.stdin.readline


def solve(n):
    if n < 6:
        return dp[n]

    if dp[n] > 0:
        return dp[n]

    dp[n] = solve(n - 1) + solve(n - 5)
    return dp[n]


t = int(input())
for _ in range(t):
    n = int(input())
    dp = [0] * 101
    dp[1], dp[2], dp[3], dp[4], dp[5] = 1, 1, 1, 2, 2
    print(solve(n))