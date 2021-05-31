import sys

"""
def solve(n):
    for y in range(coins[-1]):
        for x in coins:
            if y < len(memo) and y - x >= 0 and y - x not in coins:
                memo[y] = -1

    for y in range(coins[0], n + 1):
        val = -1
        for x in coins:
            if y - x >= 0 and (val == -1 or val > memo[y - x]):
                val = memo[y - x]
        memo[y] = val + 1
        print(memo)
    return memo[n]
"""


def solve(n, m):
    for i in range(n):
        for j in range(coins[i], m + 1):
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
