# BOJ 10815
import sys

si = sys.stdin.readline

n = int(si())
user = list(map(int, si().split()))
m = int(si())
cards = list(map(int, si().split()))
counts = [0] * m
user.sort()

# 재귀함수를 이용한 이분탐색시 시간 초과
"""
def is_in(arr, target):
    mid = len(arr) // 2
    if arr[mid] == target:
        return True

    if len(arr) < 2:
        return False

    if arr[mid] < target:
        return is_in(arr[mid:], target)
    else:
        return is_in(arr[:mid], target)
"""


def is_in(start, end, target):
    while start <= end:
        mid = (start + end) // 2
        if user[mid] == target:
            return True

        if user[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return False


for i in range(m):
    if is_in(0, n - 1, cards[i]):
        counts[i] = 1

print(" ".join(map(str, counts)))
