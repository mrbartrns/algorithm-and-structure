# BOJ 2805
import sys

si = sys.stdin.readline

n, m = map(int, si().split())
trees = list(map(int, si().split()))
trees.sort()


def solve(start, end, k):
    mid = (start + end) // 2
    res = 0
    while start <= end:
        cnt = 0
        for i in range(n):
            if trees[i] > mid:
                cnt += trees[i] - mid

        if cnt >= k:
            res = mid
            start = mid + 1
        else:
            end = mid - 1
        mid = (start + end) // 2
    return res


print(solve(1, trees[-1], m))