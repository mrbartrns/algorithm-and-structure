# BOJ 11568 민균이의 계략
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline

N = int(si())
arr = list(map(int, si().split(" ")))
dp = [1] * N
for i in range(1, N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))
