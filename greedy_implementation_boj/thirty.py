# BOJ 10610
import sys

si = sys.stdin.readline

arr = list(map(int, si().strip()))
arr.sort(reverse=True)


def check(arr):
    tot = 0
    if arr[-1] == 0:
        for i in range(len(arr)):
            tot += arr[i] % 10
    if tot > 0 and tot % 3 == 0:
        return True
    return False


print("".join(list(map(str, arr))) if check(arr) else -1)