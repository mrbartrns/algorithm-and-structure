# BOJ 13459 구슬 탈출
from collections import deque
import sys

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline


def get_balls_location(graph):
    by, bx = 0, 0
    ry, rx = 0, 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == "B":
                by, bx = i, j
            if graph[i][j] == "R":
                ry, rx = i, j
    return by, bx, ry, rx


def bfs():
    que = deque()
    visited = set()
    by, bx, ry, rx = get_balls_location(graph)
    que.append((by, bx, ry, rx, 0))
    visited.add((by, bx, ry, rx))

    while que:
        by, bx, ry, rx, check_count = que.popleft()
        if check_count <= 10 and graph[ry][rx] == "O":
            return 1
        elif check_count > 10:
            break

        for i in range(4):
            nby = by + dy[i]
            nbx = bx + dx[i]
            nry = ry + dy[i]
            nrx = rx + dx[i]
            cnt = 1
            rdone = 0
            bdone = 0

            while True:
                if bdone and rdone:
                    break

                if graph[nby][nbx] == "#":
                    bdone = cnt
                    cnt += 1
                    nby -= dy[i]
                    nbx -= dx[i]
                elif graph[nby][nbx] == "O":
                    bdone = cnt
                    cnt += 1

                if graph[nry][nrx] == "#":
                    rdone = cnt
                    cnt += 1
                    nry -= dy[i]
                    nrx -= dx[i]
                elif graph[nry][nrx] == "O":
                    rdone = cnt
                    cnt += 1

                if not bdone:
                    nby += dy[i]
                    nbx += dx[i]

                if not rdone:
                    nry += dy[i]
                    nrx += dx[i]

            if graph[nby][nbx] == "O":
                continue

            if nby == nry and nbx == nrx:
                if bdone < rdone:
                    nry -= dy[i]
                    nrx -= dx[i]
                else:
                    nby -= dy[i]
                    nbx -= dx[i]
            if (nby, nbx, nry, nrx) not in visited:
                visited.add((nby, nbx, nry, nrx))
                que.append((nby, nbx, nry, nrx, check_count + 1))

    return 0


N, M = map(int, si().split(" "))
graph = [list(si().strip()) for _ in range(N)]
# N, M = 3, 5
# graph = [
#     ["#", "#", "#", "#", "#"],
#     ["#", "O", "B", "R", "#"],
#     ["#", "#", "#", "#", "#"],
# ]
print(bfs())
