# BOJ 3108
# 한붓그리기 dfs
import sys

si = sys.stdin.readline


def dfs(x, y):
    if x < 0 or x >= len(board) or y < 0 or y >= len(board):
        return False

    if board[x][y] == 1:
        board[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True

    return False


# 방향벡터
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 보드판
board = [[0 for _ in range(2001)] for _ in range(2001)]


# 입력
t = int(si())
for _ in range(t):
    x1, y1, x2, y2 = map(int, si().split())

    x1 = (x1 + 500) * 2
    x2 = (x2 + 500) * 2
    y1 = (y1 + 500) * 2
    y2 = (y2 + 500) * 2

    for i in range(x1, x2 + 1):
        board[i][y1] = board[i][y2] = 1
    for i in range(y1, y2 + 1):
        board[x1][i] = board[x2][i] = 1

cnt = 0
if board[1000][1000] == 1:
    cnt -= 1

for i in range(len(board)):
    for j in range(len(board[0])):
        if dfs(i, j):
            cnt += 1

print(cnt)