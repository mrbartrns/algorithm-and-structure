# BOJ 17143
import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline
dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]


def shark_move():
    temp = [[[] for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if graph[i][j]:
                y, x, s, d, z = i, j, graph[i][j][0], graph[i][j][1], graph[i][j][2]
                for _ in range(s):
                    ny = y + dy[d]
                    nx = x + dx[d]
                    if ny < 0 or ny >= n or nx < 0 or nx >= m:
                        if d == 0:
                            d = 1
                        elif d == 1:
                            d = 0
                        elif d == 2:
                            d = 3
                        else:
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


n, m, k = map(int, si().split())
graph = [[[] for _ in range(m)] for _ in range(n)]
for _ in range(k):
    a, b, j, d, e = map(int, si().split())  # r, c, s, d, z
    graph[a - 1][b - 1] = [j, d - 1, e]

score = 0
for j in range(m):
    for i in range(n):
        if graph[i][j]:
            score += graph[i][j][2]
            graph[i][j].clear()
            break
    graph = shark_move()
print(score)
