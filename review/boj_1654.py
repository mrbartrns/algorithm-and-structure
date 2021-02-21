# BOJ 1654
import sys

si = sys.stdin.readline

n, k = map(int, si().split())
arr = []
for _ in range(n):
    arr.append(int(si()))

arr.sort()
max_length = arr[-1]


def search(start, end, k):
    res = 0
    mid = (start + end) // 2
    while start <= end:
        cnt = 0

        for i in range(len(arr)):
            cnt += arr[i] // mid

        if cnt >= k:
            res = mid
            start = mid + 1
        else:
            end = mid - 1

        mid = (start + end) // 2
    return res


print(search(1, max_length, k))