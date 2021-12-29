# BOJ sort 마스터 배지훈의 후계자
from bisect import bisect_left, bisect_right
import sys

sys.stdin = open("../input.txt")
si = sys.stdin.readline

N, M = map(int, si().strip().split(" "))
arr1 = []
arr2 = []
for _ in range(N):
    arr1.append(int(si().strip()))
for _ in range(M):
    arr2.append(int(si().strip()))
arr1.sort()
for i in range(M):
    left = bisect_left(arr1, arr2[i])
    right = bisect_right(arr1, arr2[i])
    print(left if left < right else -1)
