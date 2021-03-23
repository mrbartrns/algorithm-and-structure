# BOJ 2468
import sys

sys.setrecursionlimit(100000)
si = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    if not visited[x][y]:
        visited[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True
    return False


res = 0
n = int(si())
graph = [list(map(int, si().split())) for _ in range(n)]

MAX = 0
res = 0
for i in range(n):
    for j in range(n):
        if MAX < graph[i][j]:
            MAX = graph[i][j]

for i in range(MAX):
    visited = [[False for _ in range(n)] for _ in range(n)]
    cnt = 0
    for x in range(n):
        for y in range(n):
            if graph[x][y] - i <= 0:
                visited[x][y] = True

    for x in range(n):
        for y in range(n):
            if dfs(x, y):
                cnt += 1

    res = max(cnt, res)

print(res)