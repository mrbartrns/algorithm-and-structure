# BOJ 1806
import sys

si = sys.stdin.readline


def solve(n, m, arr):
    res = 1000000000
    s = start = end = 0
    flag = False
    while start < n:
        if s >= m:
            flag = True
            res = min(res, end - start)
            s -= arr[start]
            start += 1
        elif end == n:
            break
        else:
            s += arr[end]
            end += 1

    return res if flag else 0


n, m = map(int, si().split())
seq = list(map(int, si().split()))


print(solve(n, m, seq))