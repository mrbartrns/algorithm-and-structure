# BOJ 11058 크리보드
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline


def solve(n):
    if n <= 0:
        return 0
    if cache[n] > -1:
        return cache[n]
    cache[n] = 0
    cache[n] = 1 + solve(n - 1)
    for i in range(3, n):
        cache[n] = max(cache[n], (i - 1) * solve(n - i))
    return cache[n]


N = int(si().strip())
cache = [-1 for _ in range(N + 1)]
print(solve(N))
