# BOJ 11508 2 + 1 세일
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline

N = int(si())
arr = []
for _ in range(N):
    arr.append(int(si()))

arr.sort(key=lambda x: -x)
ret = 0
for i in range(N):
    if i % 3 == 2:
        continue
    ret += arr[i]
print(ret)
