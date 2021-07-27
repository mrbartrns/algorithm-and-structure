# BOJ 19236 (청소년 상어)
import copy
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline

dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, -1, -1, -1, 0, 1, 1, 1]


def fish_move(board, table):
    for i in range(1, 17):
        if table[i][2] == -1:
            continue
        y, x, d = table[i]
        for _ in range(8):
            ny = y + dy[d]
            nx = x + dx[d]
            if ny < 0 or ny >= 4 or nx < 0 or nx >= 4:
                d = (d + 1) % 8

            elif board[ny][nx] == 0:
                d = (d + 1) % 8

            else:
                nxt = board[ny][nx]
                table[i] = [ny, nx, d]
                if nxt > 0:
                    table[nxt][0], table[nxt][1] = y, x
                board[ny][nx], board[y][x] = i, nxt
                break


def backtrack(board, table, ret, answer):
    y, x, d = table[0]
    fish_move(board, table)
    for i in range(1, 5):
        b = copy.deepcopy(board)
        t = copy.deepcopy(table)
        ny = y + dy[d] * i
        nx = x + dx[d] * i
        if ny < 0 or ny >= 4 or nx < 0 or nx >= 4:
            continue

        if b[ny][nx] == -1:
            continue

        b[y][x] = -1
        fish = b[ny][nx]
        t[0] = [ny, nx, t[fish][2]]
        t[fish] = [-1, -1, -1]
        b[ny][nx] = 0
        ret.append(fish)
        answer.append(copy.deepcopy(ret))
        backtrack(b, t, ret, answer)
        ret.pop()


table = [[-1, -1, -1] for _ in range(17)]
board = [[0 for _ in range(4)] for _ in range(4)]

row = [list(map(int, si().split())) for _ in range(4)]
for i in range(4):
    for j in range(0, 8, 2):
        board[i][j // 2] = row[i][j]
        table[row[i][j]] = [i, j // 2, row[i][j + 1] - 1]


fish = board[0][0]
table[0] = [0, 0, table[fish][2]]
table[fish] = [-1, -1, -1]
board[0][0] = 0
ret = []

backtrack(board, table, [fish], ret)
answer = 0
for arr in ret:
    answer = max(answer, sum(arr))
print(answer)