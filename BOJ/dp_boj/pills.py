# BOJ 4811 알약
# 처음의 상태를 default로 잡고 시작한다.

import sys

sys.stdin = open("../input.txt", "r")
sys.setrecursionlimit(1000000)
si = sys.stdin.readline


def take(idx, w, h):
    if w < 0 or h < 0:
        return 0
    if idx <= 0 and w + h <= 0:
        return 1
    if cache[idx][w][h] > -1:
        return cache[idx][w][h]
    cache[idx][w][h] = 0
    cache[idx][w][h] += take(idx - 1, w - 1, h + 1)
    cache[idx][w][h] += take(idx - 1, w, h - 1)
    return cache[idx][w][h]


cache = [[[-1 for _ in range(61)] for _ in range(61)] for _ in range(61)]
take(60, 30, 0)

while True:
    N = int(si().strip())
    if N == 0:
        break
    print(cache[2 * N][N][0])
