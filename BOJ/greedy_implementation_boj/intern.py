# BOJ 2875
import sys

si = sys.stdin.readline

n, m, k = map(int, si().split())


def solve(women, men, k):
    total = 0
    i = 0
    while i < k:
        if men * 2 > women:
            men -= 1
        else:
            women -= 1
        i += 1
    if men > 0 and women > 0:
        if men * 2 >= women:
            total = women // 2
        else:
            total = men
    return total


print(solve(n, m, k))