# BOJ 4963
import sys
from collections import deque

si = sys.stdin.readline

dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, 1, -1, -1, 1]


def bfs(x, y):
    que = deque([(x, y)])
    loc[x][y] = 0
    while que:
        x, y = que.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue

            if loc[nx][ny] == 0:
                continue

            if loc[nx][ny] == 1:
                que.append((nx, ny))
                loc[nx][ny] = 0
    return True


while True:
    n, m = map(int, si().split())
    loc = []
    cnt = 0
    if n == m == 0:
        break
    for _ in range(m):
        loc.append(list(map(int, si().split())))

    for i in range(m):
        for j in range(n):
            if loc[i][j] == 1 and bfs(i, j):
                cnt += 1
    print(cnt)
