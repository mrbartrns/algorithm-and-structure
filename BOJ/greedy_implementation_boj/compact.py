# BOJ 18870
import sys

si = sys.stdin.readline

n = int(si())
vector = []
ans = [0] * 1000001
arr = list(map(int, si().split()))
for i in range(n):
    vector.append((arr[i], i))
vector.sort(key=lambda x: (x[0], x[1]))
pivot = vector[0][0]
cnt = 0
for i in range(1, n):
    if pivot == vector[i][0]:
        ans[vector[i][1]] = cnt
    else:
        cnt += 1
        ans[vector[i][1]] = cnt
        pivot = vector[i][0]

for i in range(n):
    print(ans[i], end=" ")
