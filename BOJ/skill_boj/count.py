# BOJ 11652
# arr = [1, 1, 1, 2, 3]
# # print(arr.count(1))

import sys

input = sys.stdin.readline


def solve(arr):
    value_dict = {}
    for i in range(len(arr)):
        value_dict[arr[i]] = value_dict.get(arr[i], 0) + 1

    return sorted(value_dict.items(), key=lambda x: (-x[1], x[0]))[0][0]


n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
print(solve(arr))