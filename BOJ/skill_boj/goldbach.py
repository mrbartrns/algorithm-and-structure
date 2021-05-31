# BOJ 6588
import sys

si = sys.stdin.readline


def prime_check(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


while True:
    n = int(si())
    if n == 0:
        break

    sub = 0
    a = b = 0
    for i in range(3, n, 2):
        if prime_check(i) and prime_check(n - i):
            sub = n - (i * 2)
            a = i
            b = n - i
            break

    print(n, "=", a, "+", b)
