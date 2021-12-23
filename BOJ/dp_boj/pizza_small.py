# BOJ 14606 피자 (small)
import sys

si = sys.stdin.readline


def divide(n):
    if n <= 0:
        return 0
    if cache[n] > -1:
        return cache[n]
    cache[n] = 0
    ret = 0
    for i in range(n):
        ret = i * (n - i)
        ret += divide(i)
        cache[n] = max(cache[n], ret)
    return cache[n]


N = int(si().strip())
cache = [-1] * (N + 1)
print(divide(N))

print(N * (N - 1) // 2)