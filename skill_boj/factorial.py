# BOJ 1676
import sys

input = sys.stdin.readline


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def solve(n, k):
    counts = 0
    if n % 10 > 0:
        return k

    counts = solve(n // 10, k + 1)
    if counts > 0:
        return counts
    return counts


n = factorial(int(input()))
print(solve(n, 0))