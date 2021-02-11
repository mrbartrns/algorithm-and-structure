# BOJ 2186
import sys

si = sys.stdin.readline


def dfs(x, y, idx):
    if dp[x][y][idx] > -1:
        return dp[x][y][idx]

    if idx >= len(word):
        return 1

    dp[x][y][idx] = 0
    for i in range(4):
        for j in range(1, k + 1):
            nx = x + j * dx[i]
            ny = y + j * dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if board[nx][ny] != word[idx]:
                continue

            dp[x][y][idx] += dfs(x, y, idx + 1)
    return dp[x][y][idx]


n, m, k = map(int, si().split())
board = []
for _ in range(n):
    board.append(list(si().strip()))

word = si().strip()

dp = [[[-1 for _ in range(81)] for _ in range(101)] for _ in range(101)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

res = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == word[0]:
            res += dfs(i, j, 1)
print(res)