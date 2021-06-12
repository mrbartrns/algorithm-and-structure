# 게임 개발
import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def solve(r, c, direction):
    y, x, d = r, c, direction
    cnt = 1
    while True:
        i = 0
        while i < 4:
            d = (d + 3) % 4
            ny = y + dy[d]
            nx = x + dx[d]
            if not visited[ny][nx] and graph[ny][nx] == 0:
                visited[ny][nx] = True
                y, x = ny, nx
                cnt += 1
                break
            i += 1

        if i == 4:
            ny = y - dy[d]
            nx = x - dx[d]
            if ny < 0 or ny >= n or nx < 0 or nx >= m:
                break
            if graph[ny][nx] == 1:
                break

            y, x = ny, nx
    return cnt


n, m = map(int, si().split())
r, c, k = map(int, si().split())
graph = [list(map(int, si().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
visited[r][c] = True
print(solve(r, c, k))
