# BOJ 17070
import sys

si = sys.stdin.readline

directions = [[0, 1], [1, 1], [1, 0]]


def dfs(y, x, p):
    if dp[y][x][p] > -1:
        return dp[y][x][p]

    if x == n - 1 and y == n - 1:
        dp[y][x][p] = 1
        return dp[y][x][p]
    dp[y][x][p] = 0
    for d in range(3):
        nx = x + directions[d][1]
        ny = y + directions[d][0]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if graph[ny][nx] == 1:
            continue
        if d == 1 and (graph[ny][x] == 1 or graph[y][nx] == 1):
            continue
        if p == 0 and d != 2:
            dp[y][x][p] += dfs(ny, nx, d)
        elif p == 1:
            dp[y][x][p] += dfs(ny, nx, d)
        elif p == 2 and d != 0:
            dp[y][x][p] += dfs(ny, nx, d)
    return dp[y][x][p]


n = int(si())
dp = [[[-1 for _ in range(3)] for _ in range(n)] for _ in range(n)]
graph = [list(map(int, si().split())) for _ in range(n)]
dp[0][0][0] = 0
dfs(0, 1, 0)
print(dp[0][1][0])
