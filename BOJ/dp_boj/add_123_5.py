# BOJ 15990 1, 3, 5 더하기 5
# 2차원 배열 선언 필요 -> 규칙을 찾고 거기에 맞는 dp 배열 선언하기
import sys


sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
MOD = 1000000009

dp = [[0 for _ in range(4)] for _ in range(100001)]
dp[1][1], dp[2][2], dp[3][1], dp[3][2], dp[3][3] = 1, 1, 1, 1, 1
for i in range(4, 100001):
    if i - 1 >= 0:
        dp[i][1] = (dp[i - 1][2] + dp[i - 1][3]) % MOD
    if i - 2 >= 0:
        dp[i][2] = (dp[i - 2][1] + dp[i - 2][3]) % MOD
    if i - 3 >= 0:
        dp[i][3] = (dp[i - 3][1] + dp[i - 3][2]) % MOD
T = int(si())
for _ in range(T):
    N = int(si())
    print(sum(dp[N]) % MOD)
