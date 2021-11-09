# 달팽이
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stidn.readline


def distance(m, n):
    if m > M:
        return 0
    if n >= N:
        return 1
    cache[m][n] = 0
    cache[m][n] = distance(m + 1, n + 1) + distance(m + 1, n + 2)
    return cache[m][n]


M, N = map(int, si().split(" "))
cache = [[-1 for _ in range(N + 1)] for _ in range(M + 1)]
print(distance(0, 0))
