# BOJ 1987
import sys

si = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = set()
n, m = map(int, si().split())
board = []
counter = [0]

for _ in range(n):
    board.append(list(si().strip()))


def dfs(x, y, cnt):
    if board[x][y] in visited:
        counter[0] = max(counter[0], cnt)
        return

    visited.add(board[x][y])
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        dfs(nx, ny, cnt + 1)
    visited.remove(board[x][y])


dfs(0, 0, 0)
print(counter[0])
