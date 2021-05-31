# BOJ 11650 좌표 정렬하기
import sys

input = sys.stdin.readline


def solve(arr):
    arr.sort(key=lambda x: (x[0], x[1]))
    return arr


arr = []
n = int(input())
for _ in range(n):
    temp = list(map(int, input().split()))
    arr.append(temp)

new_arr = solve(arr)
for i in range(len(new_arr)):
    print(" ".join(list(map(str, arr[i]))))