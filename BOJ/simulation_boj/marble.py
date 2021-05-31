# BOJ 13460
import sys
from collections import deque

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs(que: deque):
    """

    @type que: deque
    """
    while que:
        ry, rx, by, bx, cnt = que.popleft()
        if cnt >= 10:
            return -1
        for i in range(4):
            nry, nrx = ry, rx
            nby, nbx = by, bx
            r_stop, b_stop = False, False
            goal = False
            app = False
            while True:
                if not r_stop and graph[nry + dy[i]][nrx + dx[i]] == "O":
                    nry += dy[i]
                    nrx += dx[i]
                    goal = True
                    r_stop = True

                if not b_stop and graph[nby + dy[i]][nbx + dx[i]] == "O":
                    goal = False
                    break

                if graph[nry + dy[i]][nrx + dx[i]] == "#":
                    r_stop = True

                if graph[nby + dy[i]][nbx + dx[i]] == "#":
                    b_stop = True

                if not r_stop and b_stop and nry + dy[i] == nby and nrx + dx[i] == nbx:
                    r_stop = True

                if not b_stop and r_stop and nby + dy[i] == nry and nbx + dx[i] == nrx:
                    b_stop = True

                if r_stop and b_stop:
                    app = True
                    break

                if not r_stop:
                    nry += dy[i]
                    nrx += dx[i]

                if not b_stop:
                    nby += dy[i]
                    nbx += dx[i]
            if goal:
                return cnt + 1

            if not visited[nby][nbx][nry][nrx] and app:
                visited[nby][nbx][nry][nrx] = True
                que.append((nry, nrx, nby, nbx, cnt + 1))
    return -1


n, m = map(int, si().split())
graph = [list(si().strip()) for _ in range(n)]
visited = [[[[False for _ in range(m)] for _ in range(n)] for _ in range(m)] for _ in range(n)]

init_ry, init_rx, init_by, init_bx = -1, -1, -1, -1
queue = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == "R":
            init_ry, init_rx = i, j
        if graph[i][j] == "B":
            init_by, init_bx = i, j
queue.append((init_ry, init_rx, init_by, init_bx, 0))
visited[init_by][init_bx][init_ry][init_rx] = True
print(bfs(queue))
