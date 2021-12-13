# BOJ 13239 combinations
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
MOD = 1000000007


def combination(n, r):
    if n == r or r == 0:
        return 1
    if cache[n][r] > -1:
        return cache[n][r]
    cache[n][r] = combination(n - 1, r - 1) + combination(n - 1, r)
    cache[n][r] %= MOD
    return cache[n][r]


T = int(si())
for _ in range(T):
    a, b = map(int, si().strip().split(" "))
    cache = [[-1 for _ in range(a + 1)] for _ in range(a + 1)]
    print(combination(a, b))
