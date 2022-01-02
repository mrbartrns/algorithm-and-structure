# BOJ 2228 구간 나누기
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
INF = 987654321


def divide(start, m):
    if m >= M:
        return 0
    if start >= N:
        return -INF
    if cache[start][m] > -INF:
        return cache[start][m]
    cache[start][m] = divide(start + 1, m)
    for i in range(N):
        cache[start][m] = max(
            cache[start][m],
            sum(arr[start : start + i + 1]) + divide(start + i + 2, m + 1),
        )
    return cache[start][m]


N, M = map(int, si().strip().split(" "))
arr = []
cache = [[-INF for _ in range(M)] for _ in range(N)]
for i in range(N):
    arr.append(int(si().strip()))
print(divide(0, 0))
