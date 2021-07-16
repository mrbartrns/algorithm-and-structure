import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline


def solve(arr, left, right):
    mid = (left + right) // 2
    if mid == arr[mid]:
        return mid

    if left >= right:
        return -1

    if arr[mid] > mid:
        return solve(arr, left, mid - 1)
    return solve(arr, mid + 1, right)


n = int(si())
arr = list(map(int, si().split()))
left = 0
right = len(arr) - 1
print(solve(arr, left, right))
