# BOJ 6148번
import sys
from collections import deque


def solve(sum_heights: int):
    minimum = -1

    # 기저 사례
    if len(cows) == 1:
        return cows[0]

    if sum_heights < top:
        minimum = get_value(sum_heights)
        return minimum - top

    last = cows.popleft()
    to_sub.append(last)
    val = solve(sum_heights - last)
    if val != -1:
        minimum = val
        return minimum

    return minimum


def get_value(sum_heights):
    minimum = -1
    for i in range(1 << len(to_sub)):
        value = sum_heights
        for j in range(len(to_sub)):
            if i & (1 << j):
                value += to_sub[j]
        if value >= top and (minimum == -1 or minimum > value):
            minimum = value
    return minimum


"""
cows = deque([1, 3, 3, 5, 6])
sum_heights = 14
top = 16
to_sub = [1, 3]
print(solve(sum_heights))
# print(get_value(sum_heights))

"""
n, top = map(int, sys.stdin.readline().split())
arr = []
to_sub = []
sum_heights = 0
for _ in range(n):
    cow = int(sys.stdin.readline())
    arr.append(cow)
    sum_heights += cow
arr.sort()
cows = deque(arr)
# print(solve(sum_heights))
sys.stdout.write(str(solve(sum_heights)))