import sys

si = sys.stdin.readline


def solve(n, m, x):
    number = x - 1
    a = number % n
    b = number // n
    return a * m + b + 1


t = int(si())

for _ in range(t):
    n, m, x = map(int, si().split())
    print(solve(n, m, x))
