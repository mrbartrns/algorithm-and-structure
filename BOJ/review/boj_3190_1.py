# BOJ 3190 (뱀)
import sys
from collections import deque

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


def play():
    y, x = 0, 0
    que = deque([(0, 0)])
    d = 0
    time = 1
    while True:
        ny = y + dy[d]
        nx = x + dx[d]
        que.append((ny, nx))
        if ny < 0 or ny >= n or nx < 0 or nx >= n:
            break

        if graph[ny][nx] == 1:
            break

        if graph[ny][nx] == 0:
            oy, ox = que.popleft()
            graph[oy][ox] = 0

        graph[ny][nx] = 1
        y, x = ny, nx

        if order[time] == "D":
            d = (d + 1) % 4
        elif order[time] == "L":
            d = (d + 3) % 4
        time += 1

    return time


n = int(si())
graph = [[0 for _ in range(n)] for _ in range(n)]
order = [""] * 10001
apple = int(si())
for _ in range(apple):
    a, b = map(int, si().split())
    graph[a - 1][b - 1] = 2

op = int(si())
for _ in range(op):
    a, b = si().split()
    order[int(a)] = b
print(play())
