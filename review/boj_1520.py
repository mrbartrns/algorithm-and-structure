# BOJ 1520
import sys

sys.setrecursionlimit(30000)
si = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, si().split())
graph = [list(map(int, si().split())) for _ in range(n)]
dp = [[-1 for _ in range(m)] for _ in range(n)]


def dfs(x, y):
    if dp[x][y] > -1:
        return dp[x][y]

    if x == n - 1 and y == m - 1:
        dp[x][y] = 1
        return dp[x][y]

    dp[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue

        if graph[x][y] > graph[nx][ny]:
            dp[x][y] += dfs(nx, ny)

    return dp[x][y]


print(dfs(0, 0))