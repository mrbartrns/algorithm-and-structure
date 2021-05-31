# BOJ 1074
import sys

si = sys.stdin.readline


def divide(x, y, k):
    if k == 0:
        return 0
    half = 1 << (k - 1)
    if x < half and y < half:
        return divide(x, y, half)
    elif x < half <= y:
        return half * half + divide(x, y - half, k - 1)
    elif x >= half > y:
        return 2 * half * half + divide(x - half, y, k - 1)
    return 3 * half * half + divide(x - half, y - half, k - 1)


n, r, c = map(int, si().split())
print(divide(r, c, n))
