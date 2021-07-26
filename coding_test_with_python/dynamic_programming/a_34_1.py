# BOJ 18353 (병사 배치하기)
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline

n = int(si())
arr = list(map(int, si().split()))
dp = [1] * len(arr)
for i in range(1, len(arr)):
    for j in range(i):
        if arr[i] < arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(n - max(dp))