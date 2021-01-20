import sys

input = sys.stdin.readline


def solve(n, m):
    for i in range(n):
        for j in range(coins[i], m + 1):
            if memo[j - coins[i]] != LIMIT:
                memo[j] = min(memo[j], memo[j - coins[i]] + 1)
    return memo[m]


n, m = map(int, input().split())
coins = []
LIMIT = 10001
memo = [LIMIT] * (m + 1)

memo[0] = 0
for _ in range(n):
    coin = int(sys.stdin.readline())
    coins.append(coin)
print(solve(n, m))
