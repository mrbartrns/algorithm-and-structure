# BOJ 7568
import sys

si = sys.stdin.readline

n = int(si())
arr = []
priorities = [1] * n
for _ in range(n):
    w, h = map(int, si().split())
    arr.append((w, h))

for i in range(n):
    for j in range(n):
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            priorities[i] += 1

print(" ".join(list(map(str, priorities))))