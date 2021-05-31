# BOJ 1149
import sys

si = sys.stdin.readline


def solve(n):
    for i in range(1, n):
        dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + arr[i][0]
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + arr[i][1]
        dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + arr[i][2]
    return min(dp[n - 1])


n = int(si())
arr = []
for _ in range(n):
    arr.append(list(map(int, si().split())))

dp = [[0 for _ in range(3)] for _ in range(n)]
dp[0] = arr[0]


print(solve(n))