import sys

"""
def solve(n):
    for i in range(coins[-1]):
        for j in coins:
            if i < len(memo) and i - j >= 0 and i - j not in coins:
                memo[i] = -1

    for i in range(coins[0], n + 1):
        val = -1
        for j in coins:
            if i - j >= 0 and (val == -1 or val > memo[i - j]):
                val = memo[i - j]
        memo[i] = val + 1
        print(memo)
    return memo[n]
"""


def solve(n, m):
    for i in range(n):
        for j in range(coins[i], n + 1):
            if memo[j - coins[i]] != 10001:
                memo[j] = min(memo[j], 1 + memo[j - coins[i]])
    return memo[m] if memo[m] != 10001 else -1


n, m = map(int, sys.stdin.readline().split())
coins = []
memo = [10001] * (m + 1)
memo[0] = 0
for _ in range(n):
    coin = int(sys.stdin.readline())
    coins.append(coin)
print(solve(n, m))
