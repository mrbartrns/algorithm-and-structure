# BOJ 11047
import sys

si = sys.stdin.readline


def solve(coins, value):
    res = 0
    for i in range(len(coins)):
        target = value // coins[len(coins) - i - 1]
        res += target
        value -= target * coins[len(coins) - i - 1]
    return res


n, k = map(int, si().split())
coins = []
for _ in range(n):
    coins.append(int(si()))

print(solve(coins, k))