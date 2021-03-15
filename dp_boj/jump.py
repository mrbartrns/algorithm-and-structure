# BOJ 1890
import sys

si = sys.stdin.readline
sys.setrecursionlimit(100000)

n = int(si())
graph = [list(map(int, si().split())) for _ in range(n)]
dp = [[-1 for _ in range(n)] for _ in range(n)]


def dfs(x, y):
    if dp[x][y] > -1:
        return dp[x][y]

    if x == n - 1 and y == n - 1:
        dp[x][y] = 1
        return dp[x][y]

    dp[x][y] = 0
    if x + graph[x][y] < n:
        dp[x][y] += dfs(x + graph[x][y], y)

    if y + graph[x][y] < n:
        dp[x][y] += dfs(x, y + graph[x][y])

    return dp[x][y]


print(dfs(0, 0))