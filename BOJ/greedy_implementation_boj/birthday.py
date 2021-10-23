# BOJ 5635
import sys


sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline

N = int(si())
arr = []
for _ in range(N):
    arr.append(list(si().strip().split(" ")))

arr.sort(key=lambda x: (int(x[3]), int(x[2]), int(x[1])))

print(arr[-1][0])
print(arr[0][0])
