# BOJ 2281 데스노트
import sys


sys.setrecursionlimit(1000000)
sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
INF = 987654321


def solve(y, x):
    if y == N:
        return 0
    if cache[y][x] < INF:
        return cache[y][x]
    cache[y][x] = (M - x + 2) ** 2 + solve(y + 1, arr[y] + 2)
    if x + arr[y] - 1 <= M:
        cache[y][x] = min(cache[y][x], solve(y + 1, x + arr[y] + 1))
    return cache[y][x]


N, M = map(int, si().strip().split(" "))
arr = []
for _ in range(N):
    arr.append(int(si().strip()))
cache = [[INF for _ in range(M + 10)] for _ in range(N + 10)]

print(solve(1, arr[0] + 2))
