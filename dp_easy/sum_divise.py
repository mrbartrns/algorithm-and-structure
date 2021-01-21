# BOJ 2225
import sys

input = sys.stdin.readline


n = 200
k = 200
dp = [[0 for _ in range(n + 1)] for _ in range(k + 1)]
for i in range(n + 1):
    dp[1][i] = 1


def solve(n, k):
    for i in range(2, k + 1):
        for j in range(n + 1):
            dp[i][j] = sum(dp[i - 1][: j + 1]) % 1000000000
    return dp[k][n]


n, k = map(int, input().split())
sys.stdout.write(str(solve(n, k)))