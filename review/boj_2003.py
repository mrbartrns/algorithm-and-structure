# BOJ 2003
import sys

si = sys.stdin.readline


# 투포인터 알고리즘
def solve(t):
    cnt = s = start = end = 0
    while True:
        if s >= t:
            s -= arr[start]
            start += 1
        elif end == n:
            break
        else:
            s += arr[end]
            end += 1

        if s == t:
            cnt += 1
    return cnt


n, m = map(int, si().split())
arr = list(map(int, si().split()))
print(solve(m))