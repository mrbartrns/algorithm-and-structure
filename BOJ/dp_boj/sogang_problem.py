# BOJ 2854 문제 출제
import sys

sys.stdin = open("../input.txt", "r")
sys.setrecursionlimit(10000000)
si = sys.stdin.readline
MOD = 1000000007


def solve(idx, t):
    if idx >= N:
        return 1
    if cache[idx][t] > -1:
        return cache[idx][t]
    cache[idx][t] = 0
    cache[idx][t] += exact[idx] * solve(idx + 1, 1)
    cache[idx][t] %= MOD
    if idx < len(not_exact):
        cache[idx][t] += not_exact[idx] * solve(idx + 1, 2)
        cache[idx][t] %= MOD
    if idx - 1 >= 0:
        if t == 2:
            cache[idx][t] += (
                not_exact[idx - 1] - 1 if not_exact[idx - 1] - 1 >= 0 else 0
            ) * solve(idx + 1, 3)
        else:
            cache[idx][t] += not_exact[idx - 1] * solve(idx + 1, 3)
        cache[idx][t] %= MOD
    return cache[idx][t]


N = int(si().strip())
cache = [[-1 for _ in range(4)] for _ in range(N + 1)]
exact = list(map(int, si().strip().split(" ")))
not_exact = list(map(int, si().strip().split(" ")))
print(solve(0, 0))
