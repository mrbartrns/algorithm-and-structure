# SWEA 2072
from functools import reduce

t = int(input())


def add(acc, cur):
    if cur % 2 == 1:
        acc += cur
    return acc


for tc in range(t):
    arr = list(map(int, input().split()))
    s = reduce(add, arr, 0)
    print("#" + str(tc + 1), str(s))