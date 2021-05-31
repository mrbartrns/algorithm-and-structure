# BOJ 1932
import sys

si = sys.stdin.readline


def solve(n):
    dp = [[0 for _ in range(n)] for _ in range(n)]
    dp[0][0] = triangle[0][0]
    for i in range(1, n):
        for j in range(len(triangle[i])):
            val = dp[i - 1][j] + triangle[i][j]
            if j > 0:
                val = max(val, dp[i - 1][j - 1] + triangle[i][j])
            dp[i][j] = val
    return max(dp[n - 1])


n = int(si())
triangle = []
for _ in range(n):
    temp = list(map(int, si().split()))
    triangle.append(temp)

print(solve(n))