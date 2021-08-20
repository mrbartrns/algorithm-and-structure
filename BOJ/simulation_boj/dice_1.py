# BOJ 14499 주사위 복습
import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline

dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]


def roll(op, dice):
    d1, d2, d3, d4, d5, d6 = dice[1], dice[2], dice[3], dice[4], dice[5], dice[6]
    if op == 1:
        dice[1] = d4
        dice[3] = d1
        dice[4] = d6
        dice[6] = d3
    elif op == 2:
        dice[1] = d3
        dice[3] = d6
        dice[4] = d1
        dice[6] = d4
    elif op == 3:
        dice[1] = d5
        dice[2] = d1
        dice[5] = d6
        dice[6] = d2
    else:
        dice[1] = d2
        dice[2] = d6
        dice[5] = d1
        dice[6] = d5


n, m, sy, sx, k = map(int, si().split())
board = [list(map(int, si().split())) for _ in range(n)]
order = list(map(int, si().split()))
dice = [0] * 7
y, x = sy, sx

for op in order:
    ny = y + dy[op - 1]
    nx = x + dx[op - 1]
    if ny < 0 or ny >= n or nx < 0 or nx >= m:
        continue
    roll(op, dice)
    if board[ny][nx] == 0:
        board[ny][nx] = dice[6]
    else:
        dice[6] = board[ny][nx]
        board[ny][nx] = 0

    y, x = ny, nx
    print(dice[1])
