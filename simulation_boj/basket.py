# BOJ 10811
import sys


def reverse_basket(a, b):
    a -= 1
    b -= 1
    mid = (a + b) // 2 + 1
    for i in range(mid - a):
        arr[a + i], arr[b - i] = arr[b - i], arr[a + i]


si = sys.stdin.readline
n, m = map(int, si().split())
arr = [i for i in range(1, n + 1)]
for _ in range(m):
    x, y = map(int, si().split())
    reverse_basket(x, y)
print(" ".join(list(map(str, arr))))
