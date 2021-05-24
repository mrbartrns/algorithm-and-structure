# BOJ 14499
import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline
dy = [0, 0, 0, -1, 1]
dx = [0, 1, -1, 0, 0]


def roll(d):
    d1, d2, d3, d4, d5, d6 = dice[1], dice[2], dice[3], dice[4], dice[5], dice[6]
    if d == 1:
        dice[1] = d4
        dice[3] = d1
        dice[6] = d3
        dice[4] = d6
    elif d == 2:
        dice[1] = d3
        dice[3] = d6
        dice[6] = d4
        dice[4] = d1
    elif d == 3:
        dice[2] = d1
        dice[1] = d5
        dice[5] = d6
        dice[6] = d2
    elif d == 4:
        dice[2] = d6
        dice[1] = d2
        dice[5] = d1
        dice[6] = d5


dice = [0] * 7

n, m, init_y, init_x, k = map(int, si().split())
graph = [list(map(int, si().split())) for _ in range(n)]
order = list(map(int, si().split()))

y, x = init_y, init_x
for i in range(k):
    direction = order[i]
    ny = y + dy[direction]
    nx = x + dx[direction]
    if ny < 0 or ny >= n or nx < 0 or nx >= m:
        continue
    roll(direction)
    if graph[ny][nx] == 0:
        graph[ny][nx] = dice[6]
    else:
        dice[6] = graph[ny][nx]
        graph[ny][nx] = 0
    y, x = ny, nx
    print(dice[1])
