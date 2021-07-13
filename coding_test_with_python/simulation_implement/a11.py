# BOJ 3190 뱀
import sys
from collections import deque

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline


def play():
    que = deque()
    que.append((0, 0))
    cur_y, cur_x = 0, 0
    cur_d = 0
    cnt = 1
    while True:
        ny = cur_y + dy[cur_d]
        nx = cur_x + dx[cur_d]
        if ny < 0 or ny >= n or nx < 0 or nx >= n:
            return cnt

        if board[ny][nx] == 1:
            return cnt

        que.append((ny, nx))
        if board[ny][nx] == 0:
            prev_y, prev_x = que.popleft()
            board[prev_y][prev_x] = 0

        board[ny][nx] = 1

        cur_d = (cur_d + order[cnt]) % 4
        cur_y, cur_x = ny, nx
        cnt += 1


n = int(si())
board = [[0 for _ in range(n)] for _ in range(n)]
board[0][0] = 1
order = [0] * 10001
t = int(si())
for _ in range(t):
    r, c = map(int, si().split())
    board[r - 1][c - 1] = 2
p = int(si())
for _ in range(p):
    order_cnt, direction = si().strip().split(" ")
    if direction == "D":
        order[int(order_cnt)] = 1
    elif direction == "L":
        order[int(order_cnt)] = 3

print(play())
