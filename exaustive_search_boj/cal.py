# BOJ 1476
import sys

si = sys.stdin.readline

n, m, k = map(int, si().split())


def solve(n, m, k):
    num = 1
    while True:
        num1 = num % 15 if num % 15 > 0 else 15
        num2 = num % 28 if num % 28 > 0 else 28
        num3 = num % 19 if num % 19 > 0 else 19
        if num1 == n and num2 == m and num3 == k:
            break
        num += 1
    return num


def solve1(n, m, k):
    num = 1
    while True:
        if (num - n) % 15 == 0 and (num - m) % 28 == 0 and (num - k) % 19 == 0:
            break
        num += 1
    return num


print(solve1(n, m, k))