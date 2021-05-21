# BOJ 14503 (로봇청소기)
import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def clean(init_y, init_x, init_d):
    y, x, d = init_y, init_x, init_d
    visited[y][x] = True
    while True:
        check = 0
        while check < 4:
            d = (d + 3) % 4
            ny = y + dy[d]
            nx = x + dx[d]
            if not visited[ny][nx] and graph[ny][nx] == 0:
                visited[ny][nx] = True
                y, x = ny, nx
                break
            check += 1

        if check == 4:
            ny = y - dy[d]
            nx = x - dx[d]
            if graph[ny][nx] == 1:
                break
            y, x = ny, nx


n, m = map(int, si().split())
start_y, start_x, start_d = map(int, si().split())
graph = [list(map(int, si().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
clean(start_y, start_x, start_d)
cnt = 0
for i in range(n):
    for j in range(m):
        if visited[i][j]:
            cnt += 1
print(cnt)
