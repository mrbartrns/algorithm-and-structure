# BOJ 13910 개업
from itertools import combinations
import sys

sys.stdin = open("../input.txt", "r")
sys.setrecursionlimit(1000000)
si = sys.stdin.readline
INF = 987654321


def cook(n):
    if n < 0:
        return INF
    if n == 0:
        return 0
    if cache[n] < INF:
        return cache[n]
    for c in s:
        cache[n] = min(cache[n], 1 + cook(n - c))
    return cache[n]


N, M = map(int, si().strip().split(" "))
arr = list(map(int, si().strip().split(" ")))
comb = combinations(arr, 2)
s = set(arr)
for c in comb:
    a, b = c
    s.add(a + b)

cache = [INF for _ in range(N + 1)]
print(cook(N))
