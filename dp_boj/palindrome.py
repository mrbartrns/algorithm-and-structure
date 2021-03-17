# BOJ 10942
import sys

si = sys.stdin.readline

n = int(si())
arr = [-1] + list(map(int, si().split()))
dp = [[1 for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(n - 1, 0, -1):
    for j in range(n, 1, -1):
        if j > i:
            dp[i][j] = dp[i + 1][j - 1] if arr[i] == arr[j] else 0

m = int(si())
for _ in range(m):
    x, y = map(int, si().split())
    print(dp[x][y])