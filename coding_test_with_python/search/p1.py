# 부품 찾기
import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline


def binary_search(start, end, target, arr):
    if start > end:
        return False
    mid = (start + end) // 2
    if target == arr[mid]:
        return True

    if target < arr[mid]:
        end = mid - 1
    else:
        start = mid + 1
    return binary_search(start, end, target, arr)


n = int(si())
arr1 = list(map(int, si().split()))
m = int(si())
arr2 = list(map(int, si().split()))
arr1.sort()

for i in range(m):
    chk = True
    if not binary_search(0, len(arr1) - 1, arr2[i], arr1):
        chk = False
    print('yes' if chk else 'no')
