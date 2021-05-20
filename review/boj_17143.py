# BOJ 17143 (낚시왕)
import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline
dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]


def shark_move():
    temp = [[[] for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if graph[i][j]:
                y, x, s, d, z = i, j, graph[i][j][0], graph[i][j][1], graph[i][j][2]
                for _ in range(s):
                    ny = y + dy[d]
                    nx = x + dx[d]
                    if ny < 0 or ny >= R or nx < 0 or nx >= C:
                        if d == 0:
                            d = 1
                        elif d == 1:
                            d = 0
                        elif d == 2:
                            d = 3
                        elif d == 3:
                            d = 2
                        ny = y + dy[d]
                        nx = x + dx[d]
                    y, x = ny, nx
                if not temp[y][x]:
                    temp[y][x] = [s, d, z]
                else:
                    if temp[y][x][2] < z:
                        temp[y][x] = [s, d, z]
    return temp


R, C, M = map(int, si().split())
graph = [[[] for _ in range(C)] for _ in range(R)]
score = 0
for _ in range(M):
    r, c, s, d, z = map(int, si().split())
    graph[r - 1][c - 1] = [s, d - 1, z]

for j in range(C):
    for i in range(R):
        if graph[i][j]:
            score += graph[i][j][2]
            graph[i][j].clear()
            break
    graph = shark_move()

print(score)
