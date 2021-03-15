# BOJ 11051
import sys

sys.setrecursionlimit(3000)
si = sys.stdin.readline


def solve(n, r):
    if dp[n][r] > -1:
        return dp[n][r]

    if n == r or r == 0:
        dp[n][r] = 1
        return dp[n][r]

    dp[n][r] = (solve(n - 1, r - 1) + solve(n - 1, r)) % 10007
    return dp[n][r]


n, r = map(int, si().split())

dp = [[-1 for _ in range(r + 1)] for _ in range(n + 1)]


print(solve(n, r))