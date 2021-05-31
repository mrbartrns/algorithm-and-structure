# BOJ 3108
import sys

si = sys.stdin.readline
sys.setrecursionlimit(400000)
MAX = 2001

n = int(si())
graph = [[0 for _ in range(MAX)] for _ in range(MAX)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# graph = [[0 for _ in range(10)] for _ in range(10)]

for _ in range(n):
    x1, y1, x2, y2 = map(int, si().split())
    x1 = (x1 + 500) * 2
    y1 = (y1 + 500) * 2
    x2 = (x2 + 500) * 2
    y2 = (y2 + 500) * 2

    for i in range(y1, y2 + 1):
        graph[x1][i] = 1
        graph[x2][i] = 1

    for i in range(x1, x2 + 1):
        graph[i][y1] = 1
        graph[i][y2] = 1


def dfs(x, y):
    if x < 0 or y < 0 or x >= MAX or y >= MAX:
        return False

    if graph[x][y] == 1:
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True

    return False


cnt = 0

if graph[1000][1000] == 1:
    cnt -= 1

for i in range(MAX):
    for j in range(MAX):
        if dfs(i, j):
            cnt += 1

sys.stdout.write(str(cnt))