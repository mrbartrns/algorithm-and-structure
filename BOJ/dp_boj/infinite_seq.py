# BOJ 1351 무한 수열
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline


def solve(n):
    if n == 0:
        return 1
    if n in cache:
        return cache[n]
    cache[n] = 0
    cache[n] = solve(n // P) + solve(n // Q)
    return cache[n]


N, P, Q = map(int, si().strip().split(" "))
cache = {}
print(solve(N))
