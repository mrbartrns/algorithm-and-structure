# BOJ 1920
"""
수 찾기
두개의 수열이 주어질 때, 어떤 한 수 x가 존재하는지 존재하지 않는지 알아내는 프로그램
"""
# 이분탐색 사용
# 두개의 수열중 첫번째 수열을 정렬후 이분탐색 ㄱㄱ
import sys

si = sys.stdin.readline


def search(arr, n):
    mid = len(arr) // 2
    if n == arr[mid]:
        return True
    if len(arr) <= 1:
        return False
    if n > arr[mid]:
        return search(arr[mid:], n)
    return search(arr[:mid], n)


pool_n = int(si())
pool = sorted(list(map(int, si().split())))
n = int(si())
arr = list(map(int, si().split()))
for target in arr:
    start = 0
    end = pool_n - 1
    res = 0
    while start <= end:
        mid = (start + end) // 2
        if pool[mid] == target:
            res = 1
            break
        elif pool[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    print(res)
