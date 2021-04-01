# BOJ 11659
# 메모리 초과 -> 배열 100000 * 100000
import sys

si = sys.stdin.readline


n, m = map(int, si().split())
arr = [0] + list(map(int, si().split()))

dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(n, 0, -1):
    for j in range(i, n + 1):
        dp[i][j] = dp[i][j - 1] + arr[j]

for _ in range(m):
    a, b = map(int, si().split())
    print(dp[a][b])
