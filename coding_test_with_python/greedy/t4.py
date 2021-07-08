# 만들 수 없는 금액
import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline


def solve(n, arr):
    arr.sort()
    target = 0
    for i in range(n):
        if target + 1 < arr[i]:
            return target + 1
        target += arr[i]
    return target + 1


n = int(si())
arr = list(map(int, si().split()))
print(solve(n, arr))
