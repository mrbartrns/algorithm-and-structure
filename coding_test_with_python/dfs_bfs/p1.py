# 음료수 얼려 먹기
import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

n, m = map(int, si().split())
graph = [list(si().strip()) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]


def dfs(y, x):
    if y < 0 or y >= n or x < 0 or x >= m:
        return False

    if graph[y][x] == "1":
        return False

    if graph[y][x] == "0" and not visited[y][x]:
        visited[y][x] = True
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            dfs(ny, nx)
        return True
    return False


cnt = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            cnt += 1
print(cnt)
