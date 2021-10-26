# BOJ 9658 돌게임 4
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline

N = int(si())
# 게임은 항상 0번부터 시작 (마지막에 돌을 가져가는 사람이 게임을 짐)
dp = [0] * 1001
dp[2] = dp[4] = 1

for i in range(5, N + 1):
    if min(dp[i - 1], dp[i - 3], dp[i - 4]) == 1:
        dp[i] = 0
    else:
        dp[i] = 1

print("SK" if dp[N] == 1 else "CY")
