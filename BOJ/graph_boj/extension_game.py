# BOJ 16920 확장 게임
# TLE CODE
from collections import deque
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs(init):
    q = deque()
    for sy, sx, _ in init:
        q.append((sy, sx))
    while q:
        y, x = q.popleft()
        candidates = get_candidates(y, x, arr[int(graph[y][x])])
        for ny, nx in candidates:
            if graph[ny][nx] != ".":
                continue
            graph[ny][nx] = graph[y][x]
            q.append((ny, nx))


def get_candidates(sy, sx, count):
    ret = set()
    visited = set()
    q = deque()
    q.append((sy, sx, 0))
    visited.add((sy, sx))
    while q:
        y, x, cnt = q.popleft()
        if cnt == count:
            continue
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= N or nx < 0 or nx >= M:
                continue
            if graph[ny][nx] == "#":
                continue
            if (
                graph[ny][nx] == "."
                or graph[ny][nx] == graph[y][x]
                and (ny, nx) not in visited
            ):
                visited.add((ny, nx))
                q.append((ny, nx, cnt + 1))
                ret.add((ny, nx))
    return ret


N, M, P = map(int, si().strip().split(" "))
arr = [0] + list(map(int, si().strip().split(" ")))
graph = [list(si().strip()) for _ in range(N)]
init = []
answer = [0] * (P + 1)
for i in range(N):
    for j in range(M):
        if graph[i][j] == ".":
            continue
        if graph[i][j] == "#":
            continue
        init.append((i, j, graph[i][j]))
init.sort(key=lambda x: int(x[2]))
bfs(init)
for i in range(N):
    for j in range(M):
        if graph[i][j] == "#":
            continue
        if graph[i][j] == ".":
            continue
        answer[int(graph[i][j])] += 1
for i in range(1, P + 1):
    print(answer[i], end=" ")
