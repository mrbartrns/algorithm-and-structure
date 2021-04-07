# BOJ 2631
import sys

si = sys.stdin.readline
n = int(si())
arr = [int(si()) for _ in range(n)]
dp = [1] * n
# dp[i] = i번째 까지 가장 긴 증가하는 부분 수열
for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))
