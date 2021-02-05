# BOJ 1931
import sys

si = sys.stdin.readline

"""
arr = [
    (1, 4),
    (3, 5),
    (0, 6),
    (5, 7),
    (3, 8),
    (5, 9),
    (6, 10),
    (8, 11),
    (8, 12),
    (2, 13),
    (12, 14),
]
"""
# arr = [(3, 3), (2, 3), (3, 4)]

n = int(si())
arr = []
for _ in range(n):
    arr.append(tuple(map(int, si().split())))

arr.sort(key=lambda x: (x[1], x[0]))


def optimize(arr):
    last = arr[0]
    count = 1
    for i in range(1, len(arr)):
        if last[1] <= arr[i][0]:
            last = arr[i]
            count += 1
    return count


print(optimize(arr))