# BOJ 10211 maximum subarray
import sys


sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline


T = int(si())
for _ in range(T):
    N = int(si())
    arr = list(map(int, si().split(" ")))
    dp = [arr[i] for i in range(N)]
    for i in range(1, N):
        dp[i] = max(dp[i], dp[i - 1] + arr[i])
    print(max(dp))
