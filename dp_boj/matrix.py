# BOJ 11049
import sys

si = sys.stdin.readline
sys.setrecursionlimit(10000)
MAX = 500
INF = 987654321


def solve(x, y):
    if dp[x][y] < INF:
        return dp[x][y]

    if x == y:
        dp[x][y] = 0
        return dp[x][y]

    if x + 1 == y:
        dp[x][y] = matrix[x][0] * matrix[x][1] * matrix[y][1]
        return dp[x][y]

    for k in range(x, y):
        dp[x][y] = min(dp[x][y], solve(x, k) + solve(k + 1, y) + matrix[x][0] * matrix[k][1] * matrix[y][1])
    return dp[x][y]


dp = [[INF for _ in range(MAX)] for _ in range(MAX)]
matrix = []
n = int(si())
for _ in range(n):
    r, c = map(int, si().split())
    matrix.append([r, c])

print(solve(0, n - 1))
