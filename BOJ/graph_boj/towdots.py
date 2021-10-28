# BOJ 16929 two dots
import sys


sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def dfs(py, px, y, x, cnt):
    visited[y][x] = True
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or ny >= N or nx < 0 or nx >= M:
            continue
        if graph[y][x] != graph[ny][nx]:
            continue
        if not visited[ny][nx]:
            if dfs(y, x, ny, nx, cnt + 1):
                return True
        elif visited[ny][nx] and not finished[ny][nx] and cnt + 1 >= 4:
            if py == ny and px == nx:
                continue
            return True
    finished[y][x] = True
    return False


N, M = map(int, si().split(" "))
graph = [list(si().strip()) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
finished = [[False for _ in range(M)] for _ in range(N)]
flag = False
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            if not flag and dfs(-1, -1, i, j, 0):
                flag = True
print("Yes" if flag else "No")
