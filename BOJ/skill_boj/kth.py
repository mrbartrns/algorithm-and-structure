# BOJ 11004
import sys

si = sys.stdin.readline


def solve(arr, k):
    arr.sort()
    return arr[k - 1]


n, k = map(int, si().split())
arr = list(map(int, si().split()))
print(solve(arr, k))