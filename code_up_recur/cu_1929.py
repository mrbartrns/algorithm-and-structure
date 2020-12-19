import sys


def collatz(n):
    if n // 2 > 0:
        if n % 2 == 1:
            collatz(3 * n + 1)
        else:
            collatz(n // 2)
    print(n)


n = int(sys.stdin.readline())
collatz(n)