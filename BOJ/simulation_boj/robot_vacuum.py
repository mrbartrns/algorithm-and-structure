# BOJ 14503 로봇청소기
import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def play(r, c, direction):
    y, x, d = r, c, direction
    cnt = 0
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[y][x] = True
    cnt += 1
    while True:
        check = False
        for _ in range(4):
            d = (d + 3) % 4
            ny = y + dy[d]
            nx = x + dx[d]
            if graph[ny][nx] == 1:
                continue
            if not visited[ny][nx]:
                visited[ny][nx] = True
                y, x = ny, nx
                cnt += 1
                check = True
                break

        if check:
            continue

        ny = y - dy[d]
        nx = x - dx[d]
        if graph[ny][nx] == 1:
            break

        y, x = ny, nx
    return cnt


n, m = map(int, si().split())
r, c, d = map(int, si().split())
graph = [list(map(int, si().split())) for _ in range(n)]
print(play(r, c, d))
