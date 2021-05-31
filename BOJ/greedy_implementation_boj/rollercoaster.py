# BOJ 2873
import sys

si = sys.stdin.readline


def solve(h, w, arr):
    if h % 2 == 1:
        return ("R" * (w - 1) + "D" + "L" * (w - 1) + "D") * (h // 2) + "R" * (w - 1)
    elif h % 2 == 0 and w % 2 == 1:
        return ("D" * (h - 1) + "R" + "U" * (h - 1) + "R") * (w // 2) + "D" * (h - 1)
    else:
        min_val = 1000
        min_idx = (0, 0)
        for i in range(w):
            for j in range(h):
                if (not (i % 2 == 0 and j % 2 == 0)) or (
                    not (i % 2 == 1 and j % 2 == 1)
                ):
                    if arr[i][j] < min_val:
                        min_val = arr[i][j]
                        min_idx = (i, j)
        # cnt = 0
        if min_idx[0] > min_idx[1]:
            pass
        else:
            pass


h, w = map(int, si().split())
arr = []
for _ in range(h):
    temp = list(map(int, si().split()))
    arr.append(temp)
print(solve(h, w, arr))
"""
arr = [1]
w = 3
h = 2
print(solve(w, h, arr))
"""