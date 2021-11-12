# 폴리오미노
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
MOD = 10 * 1000 * 1000


def poly(n, first):
    if n == first:
        return 1
    if cache[n][first] > -1:
        return cache[n][first]
    cache[n][first] = 0
    for second in range(1, n - first + 1):
        add = second + first - 1
        add *= poly(n - first, second)
        add %= MOD
        cache[n][first] += add
        cache[n][first] %= MOD
    return cache[n][first]


T = int(si())
cache = [[-1 for _ in range(101)] for _ in range(101)]
for _ in range(T):
    N = int(si())
    s = 0
    for first in range(1, N + 1):
        s += poly(N, first)
        s %= MOD
    print(s)
