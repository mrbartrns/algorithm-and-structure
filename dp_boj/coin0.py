# BOJ 9084
import sys

si = sys.stdin.readline


def solve(n, value):  # 금액
    dp = [0 for _ in range(value + 1)]
    dp[0] = 1
    for i in range(n):
        for j in range(1, value + 1):
            if j - coins[i] >= 0:
                dp[j] += dp[j - coins[i]]
    return dp[value]


t = int(si())
for _ in range(t):
    n = int(si())
    coins = list(map(int, si().split()))
    value = int(si())
    print(solve(n, value))