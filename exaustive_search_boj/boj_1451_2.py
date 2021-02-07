# BOJ 1451
import sys

si = sys.stdin.readline

n, m = map(int, si().split())
matrix = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
dp = matrix[:]
for i in range(1, n + 1):
    matrix[i] = [0] + list(map(int, si().split()))

for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + matrix[i][j]


def add(x1, y1, x2, y2):
    return dp[x2][y2] - dp[x1 - 1][y2] - dp[x2][y1 - 1] + dp[x1 - 1][y1 - 1]


def solve(n, m):
    res = 0

    # c1 이런 형식으로 범위를 1씩만 증가시켜서 하면 됨
    for i in range(1, m - 1):
        for j in range(i, m):
            r1 = add(1, 1, n, i)
            r2 = add(1, i + 1, n, j)
            r3 = add(1, j + 1, n, m)
            res = max(res, r1 * r2 * r3)

    for i in range(1, n - 1):
        for j in range(i, n):
            r1 = add(1, 1, i, m)
            r2 = add(i + 1, 1, j, m)
            r3 = add(j + 1, 1, n, m)
            res = max(res, r1 * r2 * r3)

    for i in range(1, n):
        for j in range(1, m):
            r1 = add(1, 1, n, j)
            r2 = add(1, j + 1, i, m)
            r3 = add(i + 1, j + 1, n, m)
            res = max(res, r1 * r2 * r3)

    for i in range(1, n):
        for j in range(1, m):
            r1 = add(1, 1, i, j)
            r2 = add(i + 1, 1, n, j)
            r3 = add(1, j + 1, n, m)
            res = max(res, r1 * r2 * r3)

    for i in range(1, n):
        for j in range(1, m):
            r1 = add(1, 1, i, m)
            r2 = add(i + 1, 1, n, j)
            r3 = add(i + 1, j + 1, n, m)
            res = max(res, r1 * r2 * r3)

    for i in range(1, n):
        for j in range(1, m):
            r1 = add(1, 1, i, j)
            r2 = add(1, j + 1, i, m)
            r3 = add(i + 1, 1, n, m)
            res = max(res, r1 * r2 * r3)
    return res


print(solve(n, m))