# BOJ 17143
import sys
from collections import deque

si = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]

R, C, M = map(int, si().split())
graph = [[[] for _ in range(101)] for _ in range(101)]
for _ in range(M):
    r, c, s, d, z = map(int, si().split())
    graph[r][c].append([z, s, d - 1])

cur = 0  # 현재 낙시왕의 위치
res = 0
for c in range(C):
    cur += 1
    for i in range(1, R + 1):
        if len(graph[i][cur]) > 0:
            res += graph[i][cur][0][0]
            graph[i][cur].clear()
            break
    que = deque()
    for i in range(1, R + 1):
        for j in range(1, C + 1):
            if len(graph[i][j]):
                que.append([i, j, graph[i][j][0][0], graph[i][j][0][1], graph[i][j][0][2]])  # [i, j, s, d - 1, z]
                graph[i][j].clear()

    while que:
        y, x, size, speed, direction = que.popleft()

        for _ in range(speed):
            ny = y + dy[direction]
            nx = x + dx[direction]
            if ny <= 0 or ny > R or nx <= 0 or nx > C:
                if direction == 0:
                    direction = 1
                elif direction == 1:
                    direction = 0
                elif direction == 2:
                    direction = 3
                elif direction == 3:
                    direction = 2
                ny = y + dy[direction]
                nx = x + dx[direction]
            y, x = ny, nx

        if len(graph[y][x]):
            if graph[y][x][0][0] < size:
                graph[y][x].clear()
                graph[y][x].append([size, speed, direction])
        else:
            graph[y][x].append([size, speed, direction])

print(res)
