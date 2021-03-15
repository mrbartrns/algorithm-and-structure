# BOJ 1012
import sys

sys.setrecursionlimit(3000)
si = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False

    if graph[x][y] == 1:
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True

    return False


t = int(si())
for _ in range(t):
    m, n, k = map(int, si().split())
    graph = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        y, x = map(int, si().split())
        graph[x][y] = 1

    cnt = 0

    for i in range(n):
        for j in range(m):
            if dfs(i, j):
                cnt += 1
    print(cnt)
