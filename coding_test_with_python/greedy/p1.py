# 큰 수의 법칙
import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline


def solve(numbers, m, k):
    numbers.sort()
    cnt = m
    res = 0
    while cnt - k > 0:
        res += k * numbers[-1]
        cnt -= k
        res += numbers[-2]
        cnt -= 1

    if cnt > 0:
        res += cnt * numbers[-1]
    return res


n, m, k = map(int, si().split())
arr = list(map(int, si().split()))
print(solve(arr, m, k))
