# BOJ 4991 로봇 청소기
from collections import deque
from itertools import permutations
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
INF = 987654321
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs(sy, sx):
    q = deque()
    visited = [[False for _ in range(M)] for _ in range(N)]
    visited[sy][sx] = True
    distance[sy][sx][sy][sx] = 0
    q.append((sy, sx, 0))
    while q:
        y, x, cnt = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= N or nx < 0 or nx >= M:
                continue
            if graph[ny][nx] == "x":
                continue
            if not visited[ny][nx]:
                visited[ny][nx] = True
                if graph[ny][nx] == "*" or (ny == start_y and nx == start_x):
                    distance[sy][sx][ny][nx] = cnt + 1
                q.append((ny, nx, cnt + 1))


while True:
    M, N = map(int, si().split(" "))
    start_y, start_x = 0, 0
    if N == 0 and M == 0:
        break
    graph = [list(si().strip()) for _ in range(N)]
    dusts = []
    for i in range(N):
        for j in range(M):
            if graph[i][j] == "*":
                dusts.append((i, j))
            if graph[i][j] == "o":
                start_y = i
                start_x = j
    dusts.append((start_y, start_x))
    distance = [
        [[[INF for _ in range(M)] for _ in range(N)] for _ in range(M)]
        for _ in range(N)
    ]
    for sy, sx in dusts:
        bfs(sy, sx)
    dusts.pop()
    facts = list(permutations(dusts))
    answer = INF
    for dust_list in facts:
        t = 0
        sy, sx = start_y, start_x
        for ey, ex in dust_list:
            t += distance[sy][sx][ey][ex]
            sy, sx = ey, ex
        answer = min(answer, t)
    print(answer if answer < INF else -1)
