# BOJ 1937
import sys

sys.setrecursionlimit(30000)
si = sys.stdin.readline


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(si())
graph = [list(map(int, si().split())) for _ in range(n)]
dp = [[-1 for _ in range(n)] for _ in range(n)]  # dp배열 for문 내에 있으면 시간초과


def dfs(x, y):
    if dp[x][y] > -1:
        return dp[x][y]

    dp[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if graph[x][y] < graph[nx][ny]:
            dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)
    return dp[x][y]


ans = 0
for i in range(n):
    for j in range(n):

        ans = max(ans, dfs(i, j))

print(ans)