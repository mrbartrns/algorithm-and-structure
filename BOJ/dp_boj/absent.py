# BOJ 1563 개근상
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
sys.setrecursionlimit(10000)
MOD = 1000000


def check(n, late, absent):
    if late <= 0:
        return 0
    if absent <= 0:
        return 0
    if n <= 0:
        return 1
    if cache[n][late][absent] > -1:
        return cache[n][late][absent]
    cache[n][late][absent] = 0
    cache[n][late][absent] += (
        check(n - 1, late, 3)
        + check(n - 1, late - 1, 3)
        + check(n - 1, late, absent - 1)
    )
    cache[n][late][absent] %= MOD
    return cache[n][late][absent]


N = int(si().strip())
cache = [[[-1 for _ in range(4)] for _ in range(3)] for _ in range(N + 1)]
print(check(N, 2, 3))
