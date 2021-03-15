import sys

si = sys.stdin.readline


def solve(n, r):
    # dp 활용 조건
    if dp[n][r] > -1:
        return dp[n][r]

    # 종결조건
    if r == n or r == 0:
        dp[n][r] = 1
        return dp[n][r]

    dp[n][r] = solve(n - 1, r) + solve(n - 1, r - 1)
    return dp[n][r]


t = int(si())
for _ in range(t):
    r, n = map(int, si().split())
    dp = [[-1 for _ in range(r + 1)] for _ in range(n + 1)]
    print(solve(n, r))