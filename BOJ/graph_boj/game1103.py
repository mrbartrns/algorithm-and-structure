# BOJ 1103 게임
import sys

sys.stdin = open("../input.txt", "r")
sys.setrecursionlimit(1000000)
si = sys.stdin.readline
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
INF = 987654321


def dfs(y, x):
    if y < 0 or y >= N or x < 0 or x >= M:
        return 0
    if adj[y][x] == 0:
        return 0
    if cycle[y][x]:
        return INF
    if cache[y][x] > -1:
        return cache[y][x]
    cache[y][x] = 0
    cycle[y][x] = True
    for i in range(4):
        ny = y + dy[i] * adj[y][x]
        nx = x + dx[i] * adj[y][x]
        cache[y][x] = max(cache[y][x], 1 + dfs(ny, nx))
    cycle[y][x] = False
    return cache[y][x]


# initialize
N, M = map(int, si().split(" "))
g = [list(si().strip()) for _ in range(N)]
cycle = [[False for _ in range(M)] for _ in range(N)]
cache = [[-1 for _ in range(M)] for _ in range(N)]
adj = []
for i in range(N):
    temp = []
    for j in range(M):
        if g[i][j] == "H":
            temp.append(0)
        else:
            temp.append(int(g[i][j]))
    adj.append(temp)
answer = dfs(0, 0)
print(answer if answer < INF else -1)
