# BOJ 2293
import sys

si = sys.stdin.readline


def solve(n, k):
    dp = [0] * (k + 1)
    dp[0] = 1
    for i in range(n):
        for j in range(k + 1):
            if j - coins[i] >= 0:
                dp[j] = dp[j] + dp[j - coins[i]]
    return dp[k]


n, k = map(int, si().split())
coins = []

for _ in range(n):
    coins.append(int(si()))


print(solve(n, k))