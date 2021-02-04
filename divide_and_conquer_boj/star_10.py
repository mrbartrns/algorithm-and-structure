# BOJ 2447
import sys

si = sys.stdin.readline

n = int(si())


def solve(x, y, n):
    if (x // n) % 3 == 1 and (y // n) % 3 == 1:
        print(" ", end="")
    else:
        if n // 3 == 0:
            print("*", end="")
        else:
            solve(x, y, n // 3)


# 이런 형태 많은 연습 필요
def print_star(n):
    for i in range(n):
        for j in range(n):
            solve(i, j, n)
        print()


print_star(n)