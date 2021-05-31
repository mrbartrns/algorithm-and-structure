# BOJ 4963
import sys

sys.setrecursionlimit(3000)

si = sys.stdin.readline

dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, 1, -1, -1, 1]


def dfs(x, y):
    if x < 0 or x >= m or y < 0 or y >= n:
        return False

    if loc[x][y] == 1:
        loc[x][y] = 0
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True

    return False


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
            if loc[i][j] == 1 and dfs(i, j):
                cnt += 1

    print(cnt)
