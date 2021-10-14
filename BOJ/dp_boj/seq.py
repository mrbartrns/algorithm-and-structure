# BOJ 2491 수열
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline

N = int(si())
arr = list(map(int, si().split(" ")))
dp_min = [1] * N
dp_max = [1] * N

# min seq
for i in range(1, N):
    if arr[i] >= arr[i - 1]:
        dp_max[i] = dp_max[i - 1] + 1
    if arr[i] <= arr[i - 1]:
        dp_min[i] = dp_min[i - 1] + 1

print(max(max(dp_max), max(dp_min)))
