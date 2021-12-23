# BOJ 2776 암기왕
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline


def search(arr, n):
    start = 0
    end = N - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == n:
            return 1
        elif arr[mid] > n:
            end = mid - 1
        else:
            start = mid + 1
    return 0


T = int(si())
for _ in range(T):
    N = int(si().strip())
    arr1 = list(map(int, si().strip().split(" ")))
    M = int(si().strip())
    arr2 = list(map(int, si().strip().split(" ")))
    arr1.sort()
    for i in range(M):
        print(search(arr1, arr2[i]))
