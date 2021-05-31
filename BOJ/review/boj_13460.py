# BOJ 13460
import sys
from collections import deque

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def move(y, x, d):
    cnt = 0
    while graph[y + dy[d]][x + dx[d]] != "#" and graph[y][x] != "O":
        y += dy[d]
        x += dx[d]
        cnt += 1
    return y, x, cnt


def bfs(ry, rx, by, bx):
    que = deque()
    visited[ry][rx][by][bx] = True
    que.append((ry, rx, by, bx, 1))
    while que:
        ry, rx, by, bx, cnt = que.popleft()
        if cnt > 10:
            break
        for i in range(4):
            nry, nrx, r_cnt = move(ry, rx, i)
            nby, nbx, b_cnt = move(by, bx, i)
            if graph[nby][nbx] == "O":
                continue
            if graph[nry][nrx] == "O":
                return cnt
            if nry == nby and nrx == nbx:
                if r_cnt > b_cnt:
                    nry -= dy[i]
                    nrx -= dx[i]
                else:
                    nby -= dy[i]
                    nbx -= dx[i]
            if not visited[nry][nrx][nby][nbx]:
                visited[nry][nrx][nby][nbx] = True
                que.append((nry, nrx, nby, nbx, cnt + 1))
    return -1


n, m = map(int, si().split())  # 세로, 가로
graph = [list(si().strip()) for _ in range(n)]
visited = [[[[False for _ in range(m)] for _ in range(n)] for _ in range(m)] for _ in range(n)]  # by, bx, ry, rx

sry, srx = 0, 0
sby, sbx = 0, 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == "B":
            sby, sbx = i, j
        if graph[i][j] == "R":
            sry, srx = i, j
print(bfs(sry, srx, sby, sbx))
