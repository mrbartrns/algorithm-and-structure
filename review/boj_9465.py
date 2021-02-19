# BOJ 9465
import sys

si = sys.stdin.readline


def solve(n):
    for i in range(1, n):
        dp[0][i] = max(arr[0][i] + dp[1][i - 1], arr[0][i] + dp[1][i - 2])
        dp[1][i] = max(arr[1][i] + dp[0][i - 1], arr[1][i] + dp[0][i - 2])
    return max(dp[0][n - 1], dp[1][n - 1])


t = int(si())
for _ in range(t):
    n = int(si())
    arr = []
    for _ in range(2):
        arr.append(list(map(int, si().split())))
    dp = [[0 for _ in range(100000)] for _ in range(2)]
    dp[0][0], dp[1][0] = arr[0][0], arr[1][0]
    print(solve(n))
