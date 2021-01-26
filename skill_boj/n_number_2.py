# BOJ 2745
import sys

input = sys.stdin.readline


def transform(c, k):
    t = 0
    if not c:
        return 0

    if c >= "0" and c <= "9":
        t = (k ** (len(c) - 1)) * int(c[0]) + transform(c[1:], k)
    else:
        t = (k ** (len(c) - 1)) * (ord(c[0]) - ord("A") + 10) + transform(c[1:], k)

    return t


a, b = input().split()
print(transform(a, int(b)))
