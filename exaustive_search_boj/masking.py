# BOJ 14888
import sys
from itertools import permutations


si = sys.stdin.readline
n = int(si())
arr = list(map(int, si().split()))
temp = list(map(int, si().split()))
ops = []
MIN = 1e15
MAX = -1e15
for i in range(4):
    if temp[i] > 0:
        for _ in range(temp[i]):
            ops.append(i)
per = list(permutations(ops))


for i in range(len(per)):
    s = arr[0]
    for j in range(1, len(arr)):
        if per[i][j - 1] == 0:
            s += arr[j]
        elif per[i][j - 1] == 1:
            s -= arr[j]
        elif per[i][j - 1] == 2:
            s *= arr[j]
        elif per[i][j - 1] == 3:
            if s >= 0:
                s //= arr[j]
            else:
                s = -(abs(s) // arr[j])
    if s > MAX:
        MAX = s
    if s < MIN:
        MIN = s

print(MAX)
print(MIN)
