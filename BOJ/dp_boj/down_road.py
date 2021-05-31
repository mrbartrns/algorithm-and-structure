# BOJ 1520
import sys


si = sys.stdin.readline
sys.setrecursionlimit(30000)

n, m = map(int, si().split())


graph = [list(map(int, si().split())) for _ in range(n)]
dp = [[-1 for _ in range(m)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    if dp[x][y] > -1:
        return dp[x][y]

    if x == n - 1 and y == m - 1:
        dp[x][y] = 1
        return dp[x][y]

    dp[x][y] = 0
    # 0으로 초기화 하는 이 부분이 중요 ->  0으로 초기화 하는 이유?
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue

        if graph[x][y] > graph[nx][ny]:
            dp[x][y] += dfs(nx, ny)

    return dp[x][y]


print(dfs(0, 0))
print(dp)


n, m = 4, 5
graph = [
    [50, 45, 37, 32, 30],
    [35, 50, 40, 20, 25],
    [30, 30, 25, 17, 28],
    [27, 24, 22, 15, 10],
]