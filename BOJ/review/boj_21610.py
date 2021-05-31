# BOJ 21610 (마법사 상어와 비바라기)
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline


def move_cloud(d, s):
    ret = []
    for y, x in cloud:
        ny = (y + dy[d] * s) % n
        nx = (x + dx[d] * s) % n
        ret.append((ny, nx))
    return ret


def water(y, x):
    cnt = 0
    dy = [-1, -1, 1, 1]
    dx = [-1, 1, 1, -1]
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or ny >= n or nx < 0 or nx >= n:
            continue
        if graph[ny][nx] > 0:
            cnt += 1
    return cnt


def print_graph():
    for i in range(n):
        for j in range(n):
            print(graph[i][j], end=" ")
        print()
    print()


n, m = map(int, si().split())
graph = [list(map(int, si().split())) for _ in range(n)]

dy = [0, n - 1, n - 1, n - 1, 0, 1, 1, 1]
dx = [n - 1, n - 1, 0, 1, 1, 1, 0, n - 1]

orders = []
cloud = [(n - 1, 0), (n - 1, 1), (n - 2, 0), (n - 2, 1)]
for _ in range(m):
    a1, a2 = map(int, si().split())
    orders.append((a1 - 1, a2))

for cur_d, cur_s in orders:
    cloud = move_cloud(cur_d, cur_s)
    visited = [[False for _ in range(n)] for _ in range(n)]
    for r, c in cloud:
        graph[r][c] += 1
        visited[r][c] = True
    cloud.clear()
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                graph[i][j] += water(i, j)

    for i in range(n):
        for j in range(n):
            if not visited[i][j] and graph[i][j] >= 2:
                cloud.append((i, j))
                graph[i][j] -= 2

res = 0
for i in range(n):
    for j in range(n):
        res += graph[i][j]
print(res)
