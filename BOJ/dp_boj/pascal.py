# BOJ 15489 파스칼의 삼각형
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline

R, C, W = map(int, si().split(" "))
dp = [[0 for _ in range(30)] for _ in range(30)]
dp[0][0] = 1
for i in range(1, 30):
    dp[i][0] = 1
    for j in range(30):
        dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
s = 0
for i in range(W):
    for j in range(W):
        if j > i:
            continue
        s += dp[R + i - 1][C + j - 1]
print(s)