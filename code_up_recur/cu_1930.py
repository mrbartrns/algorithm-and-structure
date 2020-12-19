import sys


def super_sum(k, n):
    if k == 0:
        return n
    else:
        i = 1
        value = 0
        while i <= n:
            value += super_sum(k - 1, i)
            i += 1
        return value


# memoization을 활용한다면?

print(super_sum(10, 10))


def super_sum_memo(k, i, n, arr):
    if i == k:
        value = 0
        j = 1
        while j <= n:
            value += arr[k - 1][j]
    else:
        temp = [i for i in range(n + 1)]
        for i in range(1, n + 1):
            pass
