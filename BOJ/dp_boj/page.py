# BOJ 16493 최대 페이지 수
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline


def read(n, m):
    if n > N or m >= M:
        return 0
    if cache[n][m] > -1:
        return cache[n][m]
    cache[n][m] = 0
    cache[n][m] = read(n, m + 1)
    if times[m] + n <= N:
        cache[n][m] = max(cache[n][m], pages[m] + read(n + times[m], m + 1))
    return cache[n][m]


N, M = map(int, si().strip().split(" "))
times = []
pages = []
cache = [[-1 for _ in range(M)] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, si().strip().split(" "))
    times.append(a)
    pages.append(b)
print(read(0, 0))
