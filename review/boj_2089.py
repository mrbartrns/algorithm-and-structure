# BOJ 2089
import sys

si = sys.stdin.readline

n = int(si())


def solve(n):
    res = ""
    while n != 0:
        if n % (-2) == 0:
            res = "0" + res
            n = n // (-2)
        else:
            res = "1" + res
            n = n // (-2) + 1
    return res


print(solve(n) if n else 0)