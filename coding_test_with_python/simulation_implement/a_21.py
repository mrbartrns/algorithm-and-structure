# BOJ 16234 (인구이동)
import sys
sys.setrecursionlimit(25000)
sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

n, l, r = map(int, si().split())
graph = [list(map(int, si().split())) for _ in range(n)]


def dfs(y, x, label):
    if visited[y][x] == 0:
        visited[y][x] = label
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or ny >= n or nx < 0 or nx >= n:
                continue

            if visited[ny][nx] > 0:
                continue

            if visited[ny][nx] == 0 and l <= abs(graph[y][x] - graph[ny][nx]) <= r:
                dfs(ny, nx, label)
        return True
    return False


cnt = 0
while cnt <= 2000:
    label = 1
    visited = [[0 for _ in range(n)] for _ in range(n)]
    labeling = [[0, 0] for _ in range(10000)]
    for i in range(n):
        for j in range(n):
            if dfs(i, j, label):
                label += 1

    if visited[n - 1][n - 1] == n * n:
        print(cnt)
        break

    for i in range(n):
        for j in range(n):
            cur_label = visited[i][j]
            labeling[cur_label][0] += graph[i][j]
            labeling[cur_label][1] += 1

    for i in range(n):
        for j in range(n):
            cur_label = visited[i][j]
            graph[i][j] = labeling[cur_label][0] // labeling[cur_label][1]

    cnt += 1
