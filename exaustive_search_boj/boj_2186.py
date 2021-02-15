# BOJ 2186
import sys


def dfs(x, y, idx):
    if dp[x][y][idx] > -1:
        return dp[x][y][idx]

    if idx >= len(word):
        return 1

    dp[x][y][idx] = 0
    for i in range(4):
        for j in range(1, k + 1):
            nx = x + dx[i] * j
            ny = y + dy[i] * j

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if board[nx][ny] != word[idx]:
                continue

            dp[x][y][idx] += dfs(nx, ny, idx + 1)
    return dp[x][y][idx]


n, m, k = 4, 4, 1
board = [
    ["K", "A", "K", "T"],
    ["X", "E", "A", "S"],
    ["Y", "R", "W", "U"],
    ["Z", "B", "Q", "P"],
]
word = "BREAK"

dp = [[[-1 for _ in range(81)] for _ in range(200)] for _ in range(200)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cnt = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == word[0]:
            cnt += dfs(i, j, 1)
print(cnt)