# BOJ 2294
import sys

si = sys.stdin.readline

MAX = 1e6
n, k = map(int, si().split())
dp = [MAX] * (k + 1)
dp[0] = 0
coins = [int(si()) for _ in range(n)]


def solve(n, k):
    for i in range(n):
        for j in range(1, k + 1):
            if j - coins[i] >= 0:
                dp[j] = min(dp[j], dp[j - coins[i]] + 1)
    return dp[k] if dp[k] < MAX else -1


print(solve(n, k))