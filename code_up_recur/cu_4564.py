# 계단 점수의 최댓값
import sys


def get_score(k, arr, location, result, counts):
    # global counts
    if k == len(arr) - 1:  # 횟수가 어찌됬건간에 마지막 칸은 무조건 도착점이어야 함
        location[k] = True
        if location[k] and location[k - 1] and location[k - 2]:
            location[k] = False
            return
        result[0] += arr[k]
        if counts[0] < result[0]:
            counts[0] = result[0]
        result[0] -= arr[k]
        location[k] = False
        return
    else:
        if k == 0:
            if k + 1 < len(arr):
                get_score(k + 1, arr, location, result, counts)
            if k + 2 < len(arr):
                get_score(k + 2, arr, location, result, counts)
        else:
            location[k] = True
            if k > 2 and location[k] and location[k - 1] and location[k - 2]:
                location[k] = False
                return
            result[0] += arr[k]
            if k + 1 < len(arr):
                get_score(k + 1, arr, location, result, counts)
            if k + 2 < len(arr):
                get_score(k + 2, arr, location, result, counts)
            location[k] = False
            result[0] -= arr[k]


"""
n = int(sys.stdin.readline())
arr = [0]
for _ in range(n):
    y = int(sys.stdin.readline())
    arr.append(y)
# n = 7
# arr = [0, 13, 1, 15, 27, 29, 21, 20]

counts = [0]
location = [False] * (n + 1)
result = [0]
get_score(0, arr, location, result, counts)
print(counts[0])
"""

arr = [0] * 100000


def get_score_memo(n, arr):
    pass