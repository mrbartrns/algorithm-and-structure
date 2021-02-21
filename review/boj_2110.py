# BOJ 2110
import sys

si = sys.stdin.readline

n, m = map(int, si().split())
arr = [int(si()) for _ in range(n)]
arr.sort()
MIN = 1
MAX = arr[-1] - arr[0]


def get_count(gap):
    cnt = 1
    last = arr[0]
    for i in range(1, n):
        if arr[i] - last >= gap:
            cnt += 1
            last = arr[i]
    return cnt


def search(start, end, k):
    while start <= end:
        mid = (start + end) // 2
        cnt = get_count(mid)
        if cnt >= k:
            start = mid + 1
            res = mid
        else:
            end = mid - 1
    return res


print(search(MIN, MAX, m))