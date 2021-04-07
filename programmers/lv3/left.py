# 거스름 돈
from collections import deque


def solution(n, money):
    MOD = 1000000007
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        for j in money:

            if i - j >= 0 and j <= i - j:
                dp[i] += dp[i - j] % MOD
    return dp


n = 5
money = [1, 2, 5]
print(solution(n, money))