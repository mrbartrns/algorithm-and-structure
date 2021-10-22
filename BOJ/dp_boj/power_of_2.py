"""
기본적으로 동전문제와 비슷한 성격을 가진다. (순서만 바뀌면 동일한 경우로 취급)
동전문제와 같이 경우의 수에 대한 복습 필요
"""
# BOJ 2410 2의 멱수의 합
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
MOD = 1000000000

dp = [0] * 1000001
dp[0] = 1
N = int(si())
for i in range(21):
    for j in range(N + 1):
        if j - (1 << i) >= 0:
            dp[j] += dp[j - (1 << i)]
            dp[j] %= MOD
print(dp[N])
