# BOJ 12865
# 생각하면서 짜기

import sys

input = sys.stdin.readline


def solve(n, k):
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            if wt[i - 1] <= j:
                dp[i][j] = max(dp[i - 1][j], val[i - 1] + dp[i - 1][j - wt[i - 1]])
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[n][k]


n, k = map(int, input().split())
wt = []
val = []
for _ in range(n):
    w, v = map(int, input().split())
    wt.append(w)
    val.append(v)

dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

print(solve(n, k))