# BOJ 5569 출근 경로
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
MOD = 100000

dy = [-1, 0]
dx = [0, -1]


def go_to_work(y, x, d, t):
    if y < 0 or y >= H or x < 0 or x >= W:
        return 0
    if y == 0 and x == 0:
        return 1
    if cache[y][x][d][t] > -1:
        return cache[y][x][d][t]
    cache[y][x][d][t] = 0
    for i in range(2):
        ny = y + dy[i]
        nx = x + dx[i]
        if i == d:
            cache[y][x][d][t] += go_to_work(ny, nx, d, t - 1 if t > 0 else 0)
        elif t == 0:
            cache[y][x][d][t] += go_to_work(ny, nx, i, 1)
        cache[y][x][d][t] %= MOD
    return cache[y][x][d][t]


W, H = map(int, si().strip().split(" "))
cache = [
    [[[-1 for _ in range(2)] for _ in range(2)] for _ in range(W)] for _ in range(H)
]
ret = (go_to_work(H - 1, W - 2, 1, 0) + go_to_work(H - 2, W - 1, 0, 0)) % MOD
print(ret)
