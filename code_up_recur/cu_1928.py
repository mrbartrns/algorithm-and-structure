import sys


def collatz(n):
    print(n)
    if n // 2 > 0:
        if n % 2 == 1:
            collatz(3 * n + 1)
        else:
            collatz(n // 2)


n = int(sys.stdin.readline())
collatz(n)