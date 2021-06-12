# 상하좌우
import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

n = int(si())
ops = list(si().split())
OPER_DICT = {'U': 0, 'D': 1, 'L': 2, 'R': 3}
y, x = 0, 0

for op in ops:
    d = OPER_DICT[op]
    ny = y + dy[d]
    nx = x + dx[d]
    if ny < 0 or ny >= n or nx < 0 or nx >= n:
        continue
    y, x = ny, nx

print(y + 1, x + 1)
