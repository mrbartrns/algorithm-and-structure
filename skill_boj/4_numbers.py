# BOJ 10824
import sys

si = sys.stdin.readline


def solve(arr):
    return int(arr[0] + arr[1]) + int(arr[2] + arr[3])


arr = list(si().split())
print(solve(arr))