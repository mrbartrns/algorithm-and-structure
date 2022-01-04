# BOJ 15724 주지수
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline


def psum():
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if i - 1 >= 0:
                board[i][j] += board[i - 1][j]
            if j - 1 >= 0:
                board[i][j] += board[i][j - 1]
            if i - 1 >= 0 and j - 1 >= 0:
                board[i][j] -= board[i - 1][j - 1]


def get_sum(y1, x1, y2, x2):
    return board[y2][x2] - board[y1 - 1][x2] - board[y2][x1 - 1] + board[y1 - 1][x1 - 1]


N, M = map(int, si().strip().split(" "))
board = [[0 for _ in range(M + 1)]]
for _ in range(N):
    board.append([0] + list(map(int, si().strip().split(" "))))
psum()
T = int(si())
for _ in range(T):
    i1, j1, i2, j2 = map(int, si().strip().split(" "))
    print(get_sum(i1, j1, i2, j2))
