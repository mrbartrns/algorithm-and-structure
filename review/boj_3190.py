# BOJ 3190 (뱀)
import sys
from collections import deque

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


def play(order):
    que = deque([(0, 0)])
    y, x = 0, 0
    d = 0
    time = 1
    while True:
        ny = y + dy[d]
        nx = x + dx[d]
        if ny < 0 or ny >= N or nx < 0 or nx >= N:
            break
        if graph[ny][nx] == 1:
            break

        # 머리 먼저 집어넣어야 함
        que.append((ny, nx))

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


# 뱀 설정
N = int(si())
graph = [[0 for _ in range(N)] for _ in range(N)]
graph[0][0] = 1

# 사과 설정
K = int(si())
for _ in range(K):
    r, c = map(int, si().split())
    graph[r - 1][c - 1] = 2

# 명령어 설정
L = int(si())
order = [""] * 10001
for _ in range(L):
    a, b = si().split()
    order[int(a)] = b

print(play(order))
