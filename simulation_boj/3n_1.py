# BOJ 14920
import sys

si = sys.stdin.readline

n = int(si())


def solve(number):
    if number == 1:
        return 1
    if number % 2 == 0:
        return 1 + solve(number // 2)
    return 1 + solve(3 * number + 1)


print(solve(n))
