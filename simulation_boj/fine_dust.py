# BOJ 17144
import sys
from collections import deque
from functools import reduce

si = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def diffuse():
    for y in range(r):
        for x in range(c):
            if graph[y][x] > 0:
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if nx < 0 or nx >= c or ny < 0 or ny >= r:
                        continue
                    if graph[ny][nx] == -1:
                        continue
                    graph[ny][nx] += dusts[y][x]
                    graph[y][x] -= dusts[y][x]


def save_diffusion_values(maps):
    value_maps = [[0 for _ in range(c)] for _ in range(r)]
    for y in range(r):
        for x in range(c):
            value_maps[y][x] = maps[y][x] // 5
    return value_maps


def rotate(direction, y):
    if direction == 0:  # counter clockwise
        que = deque()
        # 1
        for i in range(y):
            que.append((graph[i][0]))
        que.pop()
        que.appendleft(0)
        for i in range(y):
            graph[i][0] = que[i]
        # 2
        que = deque()
        for i in range(c):
            que.append(graph[0][i])
        que.popleft()
        que.append(0)
        for i in range(c):
            graph[0][i] = que[i]
        # 3
        que = deque()
        for i in range(y + 1):
            que.append(graph[i][c - 1])
        que.popleft()
        que.append(0)
        for i in range(y + 1):
            graph[i][c - 1] = que[i]
        # 4
        que = deque()
        for i in range(1, c):
            que.append(graph[y][i])
        que.pop()
        que.appendleft(0)
        for i in range(len(que)):
            graph[y][i + 1] = que[i]
    else:  # clockwise
        # 1
        que = deque()
        for i in range(y + 1, r):
            que.append(graph[i][0])
        que.popleft()
        que.append(0)
        for i in range(len(que)):
            graph[i + y + 1][0] = que[i]
        # 2
        que = deque()
        for i in range(c):
            que.append(graph[r - 1][i])
        que.popleft()
        que.append(0)
        for i in range(c):
            graph[r - 1][i] = que[i]
        # 3
        que = deque()
        for i in range(y, r):
            que.append(graph[i][c - 1])
        que.pop()
        que.appendleft(0)
        for i in range(len(que)):
            graph[i + y][c - 1] = que[i]
        # 4
        que = deque()
        for i in range(1, c):
            que.append(graph[y][i])
        que.pop()
        que.appendleft(0)
        for i in range(len(que)):
            graph[y][1 + i] = que[i]


r, c, t = map(int, si().split())
graph = [list(map(int, si().split())) for _ in range(r)]

# r, c, t = 7, 8, 50
# graph = [[0, 0, 0, 0, 0, 0, 0, 9],
#          [0, 0, 0, 0, 3, 0, 0, 8],
#          [-1, 0, 5, 0, 0, 0, 22, 0],
#          [-1, 8, 0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 10, 43, 0],
#          [0, 0, 5, 0, 15, 0, 0, 0],
#          [0, 0, 40, 0, 0, 0, 20, 0]]
s = 0
for _ in range(t):
    dusts = save_diffusion_values(graph)
    diffuse()
    direction = 0
    for i in range(r):
        for j in range(c):
            if graph[i][j] == -1:
                rotate(direction, i)
                direction += 1
# for y in range(r):
#     print(" ".join(list(map(str, graph[y]))))
for i in range(r):
    s += reduce(lambda acc, cur: acc + cur, graph[i], 0)
s += 2
print(s)
