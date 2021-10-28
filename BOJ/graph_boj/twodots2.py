# BOJ 16929 Two Dots
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def dfs(y, x, cnt):
    visited[y][x] = cnt
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or ny >= N or nx < 0 or nx >= M:
            continue
        if graph[y][x] != graph[ny][nx]:
            continue
        if visited[ny][nx] == -1:
            if dfs(ny, nx, cnt + 1):
                return True
        elif not finished[ny][nx] and visited[ny][nx] < visited[y][x]:
            if abs(visited[ny][nx] - visited[y][x]) >= 3:
                return True
    finished[y][x] = True
    return False


N, M = map(int, si().split(" "))
counter = [0]
graph = [list(si().strip()) for _ in range(N)]
visited = [[-1 for _ in range(M)] for _ in range(N)]
finished = [[False for _ in range(M)] for _ in range(N)]
flag = False
for i in range(N):
    for j in range(M):
        if visited[i][j] == -1 and dfs(i, j, 0):
            flag = True
print("Yes" if flag else "No")
