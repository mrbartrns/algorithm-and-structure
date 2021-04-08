# BOJ 12865
import sys

si = sys.stdin.readline

n, k = map(int, si().split())
dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
weights = []
values = []
for _ in range(n):
    a, b = map(int, si().split())
    weights.append(a)
    values.append(b)

for i in range(1, n + 1):
    for j in range(1, k + 1):
        if weights[i - 1] <= j:
            dp[i][j] = max(dp[i - 1][j - weights[i - 1]] + values[i - 1], dp[i - 1][j])
        else:
            dp[i][j] = dp[i - 1][j]

res = 0
for i in range(1, n + 1):
    res = max(dp[i])

print(res)
