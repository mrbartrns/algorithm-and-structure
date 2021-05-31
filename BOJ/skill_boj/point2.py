# BOJ 11651 좌표 정렬하기2
import sys

input = sys.stdin.readline


def solve(arr):
    arr.sort(key=lambda x: (x[1], x[0]))
    return arr


arr = []
n = int(input())
for _ in range(n):
    temp = list(map(int, input().split()))
    arr.append(temp)

new_arr = solve(arr)
for i in range(len(new_arr)):
    print(" ".join(list(map(str, arr[i]))))