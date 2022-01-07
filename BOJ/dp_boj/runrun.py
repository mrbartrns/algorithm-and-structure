# BOJ 1757 달려달려
"""
정확히 N분에 완주해야 함
달릴 때 마다 지침 지수 1 증가
i분일 때 arr[i] 만큼 달릴 수 있음
"""
import sys

sys.setrecursionlimit(10000000)
sys.stdin = open("../input.txt")
si = sys.stdin.readline
INF = int(1e15)


def run(n, m):
    if m > M or n > N:
        return -INF
    if n == N:
        if m == 0:
            return 0
        return -INF
    if cache[n][m] > -INF:
        return cache[n][m]
    # 1) run
    if m <= M:
        cache[n][m] = max(cache[n][m], arr[n] + run(n + 1, m + 1))
    # 2) rest
    if m == 0:
        cache[n][m] = max(cache[n][m], run(n + 1, 0))
    else:
        cache[n][m] = max(cache[n][m], run(n + m, 0))
    return cache[n][m]


N, M = map(int, si().strip().split(" "))
cache = [[-INF for _ in range(M + 1)] for _ in range(N)]
arr = []
for _ in range(N):
    arr.append(int(si().strip()))
print(run(0, 0))
