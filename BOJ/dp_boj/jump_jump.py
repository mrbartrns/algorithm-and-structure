# BOJ 11060 점프 점프
import sys


sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
INF = 987654321

N = int(si())
arr = list(map(int, si().split(" ")))
dp = [INF] * N
dp[0] = 0
for i in range(1, N):
    for j in range(i):
        if arr[j] + j >= i:
            dp[i] = min(dp[i], dp[j] + 1)
print(dp[N - 1] if dp[N - 1] < INF else -1)
