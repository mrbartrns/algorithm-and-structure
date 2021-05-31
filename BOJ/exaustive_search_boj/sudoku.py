# BOJ 2580
import sys

sys.setrecursionlimit(100000)
si = sys.stdin.readline


board = []
for _ in range(9):
    board.append(list(map(int, si().split())))


def dfs(x, y):
    if board[x][y] == 0:
        for i in range(1, 10):
            board[x][y] == i