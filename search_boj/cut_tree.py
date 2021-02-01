# BOJ 2805
import sys

si = sys.stdin.readline


def search(start, end, target):
    res = 0
    while start <= end:
        tot = 0
        mid = (start + end) // 2
        for i in range(len(arr)):
            if arr[i] > mid:
                tot += arr[i] - mid
        if tot < target:
            end = mid - 1
        else:
            res = mid
            start = mid + 1
    return res


n, m = map(int, si().split())
arr = list(map(int, si().split()))
start = 1
end = max(arr)
print(search(start, end, m))