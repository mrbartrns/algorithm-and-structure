import sys

sys.stdin = open("../input.txt", "r")
sys.setrecursionlimit(1000000)
si = sys.stdin.readline
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
DIRECTION_KEYS = {"N": 0, "S": 1, "W": 2, "E": 3}


def dfs(y, x):
    d = DIRECTION_KEYS[adj[y][x]]
    visited[y][x] = True
    ny = y + dy[d]
    nx = x + dx[d]
    if ny < 0 or ny >= N or nx < 0 or nx >= M:
        ret[0] += 1
        return
    if not visited[ny][nx]:
        dfs(ny, nx)
    if not finished[ny][nx]:
        ret[0] += 1
    finished[y][x] = True


N, M = map(int, si().strip().split(" "))
adj = [list(si().strip()) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
finished = [[False for _ in range(M)] for _ in range(N)]
ret = [0]
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            dfs(i, j)
print(ret[0])
