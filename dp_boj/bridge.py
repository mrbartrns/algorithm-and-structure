# BOJ 1010
# 조합의 개념 잘 알아두는 연습 필요
import sys

si = sys.stdin.readline


def solve(n, m):
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(1, m + 1):
        dp[1][i] = i

    for i in range(2, n + 1):
        for j in range(i, m + 1):
            for k in range(i - 1, j):
                dp[i][j] += dp[i - 1][k]

    return dp[n][m]


t = int(si())
for _ in range(t):
    n, m = map(int, si().split())
    print(solve(n, m))