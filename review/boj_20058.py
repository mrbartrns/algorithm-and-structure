# BOJ 20058 (마법사 상어와 파이어스톰)
import sys
from collections import deque

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def divide(start_y, start_x, k, l):
    if k == l:
        matrix = []
        for y in range(start_y, start_y + (1 << k)):
            temp = []
            for x in range(start_x, start_x + (1 << k)):
                temp.append(graph[y][x])
            matrix.append(temp)
        new_matrix = rotate(matrix, 1 << k)
        for y in range(start_y, start_y + (1 << k)):
            for x in range(start_x, start_x + (1 << k)):
                graph[y][x] = new_matrix[y - start_y][x - start_x]
        return

    scale = 1 << (k - 1)
    for i in range(2):
        for j in range(2):
            divide(start_y + scale * i, start_x + scale * j, k - 1, l)


def rotate(matrix, scale):
    ret = []
    for j in range(scale):
        temp = []
        for i in range(scale - 1, -1, -1):
            temp.append(matrix[i][j])
        ret.append(temp)
    return ret


def check_ice():
    sub = [[0 for _ in range(1 << n)] for _ in range(1 << n)]
    for y in range(1 << n):
        for x in range(1 << n):
            if graph[y][x] == 0:
                continue
            cnt = 4
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if ny < 0 or ny >= (1 << n) or nx < 0 or nx >= (1 << n):
                    cnt -= 1
                    continue

                if graph[ny][nx] == 0:
                    cnt -= 1

            if cnt < 3:
                sub[y][x] = 1

    for y in range(1 << n):
        for x in range(1 << n):
            graph[y][x] -= sub[y][x]


def bfs(y, x):
    cnt = 1
    que = deque()
    visited[y][x] = True
    que.append((y, x))
    while que:
        y, x = que.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= 1 << n or nx < 0 or nx >= 1 << n:
                continue

            if not visited[ny][nx] and graph[ny][nx] > 0:
                visited[ny][nx] = True
                que.append((ny, nx))
                cnt += 1
    return cnt


def print_graph():
    for i in range(1 << n):
        for j in range(1 << n):
            print(graph[i][j], end=" ")
        print()
    print()


n, q = map(int, si().split())
graph = [list(map(int, si().split())) for _ in range(1 << n)]
ls = list(map(int, si().split()))

visited = [[False for _ in range(1 << n)] for _ in range(1 << n)]

for l in ls:
    divide(0, 0, n, l)
    check_ice()

s = 0
cube = 0
for i in range(1 << n):
    for j in range(1 << n):
        s += graph[i][j]
        if graph[i][j] > 0 and not visited[i][j]:
            cube = max(cube, bfs(i, j))

print(s)
print(cube)
