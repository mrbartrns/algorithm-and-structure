# BOJ 14585 사수빈탕
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline


def move(y, x):
    if y > 300 or x > 300:
        return 0
    if y + x >= M:
        return 0
    if cache[y][x] > -1:
        return cache[y][x]
    left = M - (y + x)
    cache[y][x] = left if candies[y][x] else 0
    cache[y][x] += max(move(y + 1, x), move(y, x + 1))
    return cache[y][x]


N, M = map(int, si().split(" "))
candies = [[0 for _ in range(301)] for _ in range(301)]
cache = [[-1 for _ in range(301)] for _ in range(301)]
for _ in range(N):
    a, b = map(int, si().split(" "))
    candies[a][b] = M
print(move(0, 0))
