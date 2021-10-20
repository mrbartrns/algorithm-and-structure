# BOJ 1495
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline

N, S, M = map(int, si().split())
dp = [[False for _ in range(M + 1)] for _ in range(N + 1)]
arr = list(map(int, si().split(" ")))
dp[0][S] = True
for i in range(0, N):
    for j in range(M + 1):
        if dp[i][j]:
            if j - arr[i] >= 0:
                dp[i + 1][j - arr[i]] = True
            if j + arr[i] <= M:
                dp[i + 1][j + arr[i]] = True

answer = -1
for i in range(M + 1):
    if dp[N][i]:
        answer = i
print(answer)
