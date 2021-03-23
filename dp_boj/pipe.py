# BOJ 17070
import sys

si = sys.stdin.readline

directions = [[0, 1], [1, 1], [1, 0]]


def dfs(x, y, mode):
    if dp[x][y] > -1:
        return dp[x][y]

    # 종결조건
    if x == n - 1 and y == n - 1:
        dp[x][y] = 1
        return dp[x][y]

    dp[x][y] = 0
    for i in range(3):
        nx = x + directions[i][0]
        ny = y + directions[i][1]

        if nx >= n or ny >= n:
            continue

        if i == 0 and nx != ny and ny == n - 1:
            continue

        if i == 2 and nx != ny and nx == n - 1:
            continue

        if graph[nx][ny] == 1 or (
            i == 1 and (graph[nx - 1][ny] == 1 or graph[nx][ny - 1] == 1)
        ):
            continue

        if mode == 1 or i != 2 - mode:
            dp[x][y] += dfs(nx, ny, i)
    return dp[x][y]


n = int(si())
graph = [list(map(int, si().split())) for _ in range(n)]
dp = [[-1 for _ in range(n)] for _ in range(n)]
print(dfs(0, 1, 0))
print(dp)

"""
def dfs(x, y, mode):
    if dp[x][y] > -1:
        return dp[x][y]

    if x == n - 1 and y == n - 1:
        dp[x][y] = 1
        return dp[x][y]

    dp[x][y] = 0
    for i in range(3):
        nx = x + directions[i][0]
        ny = y + directions[i][1]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if (graph[nx][ny] == 1) or (
            i == 1 and graph[nx - 1][ny] == 1 or graph[nx][ny - 1] == 1
        ):
            continue
        if i == 0 and nx != ny and ny == n - 1:
            continue
        if i == 2 and nx != ny and nx == n - 1:
            continue
        if mode == 1 or i != 2 - mode:
            dp[x][y] += dfs(nx, ny, i)
    return dp[x][y]
"""
