# BOJ 1577 도로의 개수
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
dy = [1, 0]
dx = [0, 1]


def dfs(y, x):
    if y == N and x == M:
        return 1
    if cache[y][x] > -1:
        return cache[y][x]
    cache[y][x] = 0
    for i in range(2):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or ny > N or nx < 0 or nx > M:
            continue
        if not destructed[i][y][x]:
            cache[y][x] += dfs(ny, nx)
    return cache[y][x]


N, M = map(int, si().strip().split(" "))
cache = [[-1 for _ in range(M + 1)] for _ in range(N + 1)]
destructed = [[[False for _ in range(M + 1)] for _ in range(N + 1)] for _ in range(2)]
K = int(si().strip())
for _ in range(K):
    a, b, c, d = map(int, si().strip().split(" "))
    destructed[0 if abs(a - c) == 1 else 1][min(a, c)][min(b, d)] = True

print(dfs(0, 0))
