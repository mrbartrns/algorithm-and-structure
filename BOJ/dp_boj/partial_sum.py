# BOJ 11660
import sys

si = sys.stdin.readline

n, m = map(int, si().split())
graph = [list(map(int, si().split())) for _ in range(n)]
dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + graph[i - 1][j - 1]


def psum(x1, y1, x2, y2):
    return dp[x2][y2] - dp[x1 - 1][y2] - dp[x2][y1 - 1] + dp[x1 - 1][y1 - 1]


for _ in range(m):
    x1, y1, x2, y2 = map(int, si().split())
    print(psum(x1, y1, x2, y2))