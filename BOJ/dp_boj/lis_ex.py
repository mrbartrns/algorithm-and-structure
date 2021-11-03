# 최대 증가 부분 수열
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline


def lis(idx):
    if idx > N:
        return 0

    ret = 1
    for i in range(idx + 1, N):
        if arr[idx] < arr[i]:
            ret = max(ret, 1 + lis(i))
    return ret


def lis_memo(idx):
    if idx > N:
        return 0

    if cache[idx] > -1:
        return cache[idx]

    cache[idx] = 1
    for i in range(idx + 1, N):
        if arr[idx] < arr[i]:
            cache[idx] = max(cache[idx], 1 + lis_memo(i))
    return cache[idx]


N = int(si())
arr = list(map(int, si().split()))
cache = [-1] * N

answer = 1
for i in range(N):
    re = lis_memo(i)
    print(re)
    answer = max(answer, re)
print(answer)
