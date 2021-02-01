# BOJ 1654
import sys

si = sys.stdin.readline


def search(start, end, target):
    res = 0
    while start <= end:
        tot = 0
        mid = (start + end) // 2
        for i in range(len(arr)):
            tot += arr[i] // mid
        if tot < target:
            end = mid - 1
        else:
            res = mid
            start = mid + 1
    return res


k, n = map(int, si().split())
tot = 0
MAX = 0
MIN = 2 ** 31 - 1
arr = []
for _ in range(k):
    el = int(si())
    arr.append(el)
    if MAX < el:
        MAX = el
    if MIN > el:
        MIN = el


print(search(1, MAX, n))