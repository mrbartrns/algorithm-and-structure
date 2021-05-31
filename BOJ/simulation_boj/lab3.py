# BOJ 17142
import sys
from collections import deque
from itertools import combinations

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs(que):
    while que:
        y, x = que.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= n or nx < 0 or nx >= n:
                continue

            if graph[ny][nx] == 1:
                continue

            if not visited[ny][nx]:
                visited[ny][nx] = True
                maps[ny][nx] = maps[y][x] + 1
                que.append((ny, nx))


n, m = map(int, si().split())
graph = [list(map(int, si().split())) for _ in range(n)]
av = []
blank = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            av.append((i, j))
        if graph[i][j] != 1:
            blank += 1

locations = list(combinations(av, m))

INF = 987654321
res = INF

for viruses in locations:
    maps = [[-1 for _ in range(n)] for _ in range(n)]
    visited = [[False for _ in range(n)] for _ in range(n)]
    que = deque()
    for r, c in viruses:
        maps[r][c] = 0
        que.append((r, c))
        visited[r][c] = True
    bfs(que)
    temp = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                temp += 1
    if blank == temp:
        max_n = 0
        for i in range(n):
            for j in range(n):
                if graph[i][j] == 0:
                    max_n = max(max_n, maps[i][j])
        res = min(max_n, res)
print(res if res < INF else -1)
