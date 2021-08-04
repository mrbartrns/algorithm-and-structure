# BOJ 17142 (연구소 3)
import sys
from itertools import combinations
from collections import deque

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
INF = 987654321

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs(que):
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    for i in range(m):
        y, x, cnt = que[i]
        visited[y][x] = cnt

    while que:
        y, x, cnt = que.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or ny >= n or nx < 0 or nx >= n:
                continue

            if graph[ny][nx] == 1:
                continue

            if visited[ny][nx] == -1:
                visited[ny][nx] = cnt + 1
                que.append((ny, nx, cnt + 1))

    answer = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 2:
                continue
            if graph[i][j] == 0 and visited[i][j] == -1:
                return INF
            answer = max(answer, visited[i][j])
    return answer


n, m = map(int, si().split())
graph = [list(map(int, si().split())) for _ in range(n)]
twos = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            twos.append((i, j, 0))

comb = list(combinations(twos, m))
answer = INF
for locations in comb:
    que = deque()
    for loc in locations:
        que.append(loc)
    answer = min(answer, bfs(que))
print(answer if answer < INF else -1)