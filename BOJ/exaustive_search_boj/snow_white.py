# BOJ 2309
import sys

# 9명중 두명만 빼면 7명이기때문에 2명을 고르는것으로 접근
si = sys.stdin.readline
arr = [int(si()) for _ in range(9)]
res = []
s = sum(arr)

for i in range(9):
    for j in range(9):
        if i == j:
            continue
        if s - arr[i] - arr[j] == 100:
            res = [arr[k] for k in range(9) if k != i and k != j]
            break

res.sort()
print("\n".join(list(map(str, res))))