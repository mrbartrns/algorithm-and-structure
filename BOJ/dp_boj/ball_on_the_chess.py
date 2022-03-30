# BOJ 16957 체스판 위의 공
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline

dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, -1, -1, -1, 0, 1, 1, 1]


def dfs(y, x):
    if cache[y][x] > -1:
        return cache[y][x]
    ty, tx = y, x
    current_item = chess[y][x]
    idx = C * y + x
    cache[y][x] = idx
    for i in range(8):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or ny >= R or nx < 0 or nx >= C:
            continue
        if chess[ny][nx] < current_item:
            current_item = min(current_item, chess[ny][nx])
            ty, tx = ny, nx
    cache[y][x] = dfs(ty, tx)
    return cache[y][x]


R, C = map(int, si().strip().split(" "))
chess = [list(map(int, si().strip().split(" "))) for _ in range(R)]
cache = [[-1 for _ in range(C)] for _ in range(R)]
ret = [[0 for _ in range(C)] for _ in range(R)]

for i in range(R):
    for j in range(C):
        dfs(i, j)

for i in range(R):
    for j in range(C):
        idx = cache[i][j]
        y = idx // C
        x = idx % C
        ret[y][x] += 1

for i in range(R):
    for j in range(C):
        print(ret[i][j], end=" ")
    print()
