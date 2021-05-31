# BOJ 1451
import sys

si = sys.stdin.readline

n, m = map(int, si().split())
square = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    temp = list(map(int, si().strip()))
    square[i] = [0] + temp


dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + square[i][j]


def psum(x1, y1, x2, y2):
    return dp[x2][y2] - dp[x1 - 1][y2] - dp[x2][y1 - 1] + dp[x1 - 1][y1 - 1]


def solve(n, m):
    res = 0
    # case 1
    for i in range(1, m - 1):
        for j in range(i, m):
            s1 = psum(1, 1, n, i)
            s2 = psum(1, i + 1, n, j)
            s3 = psum(1, j + 1, n, m)
            res = max(res, s1 * s2 * s3)

    # case 2
    for i in range(1, n - 1):
        for j in range(1, n):
            s1 = psum(1, 1, i, m)
            s2 = psum(i + 1, 1, j, m)
            s3 = psum(j + 1, 1, n, m)
            res = max(res, s1 * s2 * s3)

    # case 3
    for i in range(1, n):
        for j in range(1, m):
            s1 = psum(1, 1, i, j)
            s2 = psum(i + 1, 1, n, j)
            s3 = psum(1, j + 1, n, m)
            res = max(res, s1 * s2 * s3)

    # case 4
    for i in range(1, n):
        for j in range(1, m):
            s1 = psum(1, 1, n, j)
            s2 = psum(1, j + 1, i, m)
            s3 = psum(i + 1, j + 1, n, m)
            res = max(res, s1 * s2 * s3)

    # case 5
    for i in range(1, n):
        for j in range(1, m):
            s1 = psum(1, 1, i, j)
            s2 = psum(1, j + 1, i, m)
            s3 = psum(i + 1, 1, n, m)
            res = max(res, s1 * s2 * s3)

    # case 6
    for i in range(1, n):
        for j in range(1, m):
            s1 = psum(1, 1, i, m)
            s2 = psum(i + 1, 1, n, j)
            s3 = psum(i + 1, j + 1, n, m)
            res = max(res, s1 * s2 * s3)

    return res


print(solve(n, m))