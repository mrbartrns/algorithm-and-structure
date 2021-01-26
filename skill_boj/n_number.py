# BOJ 11005
import sys


def solve(n, k):
    if n // k == 0:
        return n % k if n % k < 10 else chr(ord("A") + n % k - 10)

    t = 0
    if n % k < 10:
        t = str(solve(n // k, k)) + str(n % k)
    else:
        t = str(solve(n // k, k)) + chr(ord("A") + n % k - 10)
    return t


a, b = map(int, input().split())
print(solve(a, b))