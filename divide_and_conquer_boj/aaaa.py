# BOJ 1629
import sys

si = sys.stdin.readline

a, b, c = map(int, si().split())


def solve(base, square, mod):
    if square == 0:
        return 1

    if square % 2 == 0:
        return ((solve(base, square // 2, mod)) ** 2) % mod
    return ((solve(base, square // 2, mod) ** 2) * base) % mod


print(solve(a, b, c))
