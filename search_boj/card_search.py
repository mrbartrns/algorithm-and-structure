# BOJ 10815
import sys

si = sys.stdin.readline

n = int(si())
n_arr = list(map(int, si().split()))
m = int(si())
m_arr = list(map(int, si().split()))
"""
n = 5
m = 8
n_arr = [6, 3, 2, 10, -10]
m_arr = [10, 9, -5, 2, 3, 4, 5, -10]
"""
n_arr.sort()
res = [0] * m

"""
def search(arr: list, target: int) -> bool:
    mid = len(arr) // 2
    if arr[mid] == target:
        return True

    if len(arr) < 2:
        return False
    else:
        if arr[mid] > target:
            return search(arr[:mid], target)
        else:
            return search(arr[mid:], target)
"""


def search(arr, start, end, target):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return False


# for y in range(m):
#     if search(n_arr, m_arr[y]):
#         res[y] = 1
for i in range(m):
    if search(n_arr, 0, n - 1, m_arr[i]):
        res[i] = 1

sys.stdout.write(" ".join(list(map(str, res))))