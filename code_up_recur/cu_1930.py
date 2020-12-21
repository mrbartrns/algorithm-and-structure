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


def super_sum_memo(k, n):
    arr = [[i for i in range(n + 1)]]
    i = 0
    while len(arr) - 1 < k:
        j = 0
        temp = []
        sum_val = 0
        while j < len(arr[0]):
            sum_val += arr[i][j]
            temp.append(sum_val)
            j += 1
        arr.append(temp)
        i += 1
    return arr[-1][-1]


while True:
    try:
        k, n = map(int, sys.stdin.readline().split())
        print(super_sum_memo(k, n))
    except EOFError:
        break

k, n = map(int, sys.stdin.readline().split())
print(super_sum_memo(k, n))
