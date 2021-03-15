# BOJ 1010

r, n = map(int, input().split())

dp = [[-1 for _ in range(r + 1)] for _ in range(n + 1)]


# 엎어질 수가 없다.
def solve(n, r):
    if dp[n][r] > -1:
        return dp[n][r]

    if n == r or r == 0:
        dp[n][r] = 1
        return dp[n][r]

    dp[n][r] = solve(n - 1, r - 1) + solve(n - 1, r)
    return dp[n][r]


print(solve(n, r))