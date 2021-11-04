# 합친 LIS(memoization)
import sys


sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
INF = int(1e15)


def jlis(index_a, index_b):
    if cache[index_a + 1][index_b + 1] > -1:
        return cache[index_a + 1][index_b + 1]
    ret = 0
    a = -INF
    b = -INF
    if index_a > -1:
        a = arr1[index_a]
    if index_b > -1:
        b = arr2[index_b]
    max_element = max(a, b)
    for next_a in range(index_a + 1, A):
        if max_element < arr1[next_a]:
            ret = max(ret, jlis(next_a, index_b) + 1)
    for next_b in range(index_b + 1, B):
        if max_element < arr2[next_b]:
            ret = max(ret, jlis(index_a, next_b) + 1)
    cache[index_a + 1][index_b + 1] = ret
    return cache[index_a + 1][index_b + 1]


T = int(si())
for _ in range(T):
    cache = [[-1 for _ in range(101)] for _ in range(101)]
    A, B = map(int, si().split(" "))
    arr1 = list(map(int, si().split(" ")))
    arr2 = list(map(int, si().split(" ")))
    print(jlis(-1, -1))
