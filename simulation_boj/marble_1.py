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


def bfs(que: deque):
    while que:
        ry, rx, by, bx, cnt = que.popleft()
        if cnt > 10:
            break

        for i in range(4):
            nry, nrx, rc = move(ry, rx, i)
            nby, nbx, bc = move(by, bx, i)

            if graph[nby][nbx] == "O":
                continue

            if graph[nry][nrx] == "O":
                return cnt

            if nry == nby and nrx == nbx:
                if rc > bc:
                    nry -= dy[i]
                    nrx -= dx[i]
                else:
                    nby -= dy[i]
                    nbx -= dx[i]

            if not visited[nry][nrx][nby][nbx]:
                visited[nry][nrx][nby][nbx] = True
                que.append((nry, nrx, nby, nbx, cnt + 1))
    return -1


n, m = map(int, si().split())
graph = [list(si().strip()) for _ in range(n)]
visited = [[[[False for _ in range(m)] for _ in range(n)] for _ in range(m)] for _ in range(n)]
queue = deque()
init_ry, init_rx, init_by, init_bx = -1, -1, -1, -1
for i in range(n):
    for j in range(m):
        if graph[i][j] == "R":
            init_ry, init_rx = i, j
        if graph[i][j] == "B":
            init_by, init_bx = i, j
queue.append((init_ry, init_rx, init_by, init_bx, 1))
visited[init_ry][init_rx][init_by][init_bx] = True
print(bfs(queue))
