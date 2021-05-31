# BOJ 13305
import sys

sys.stdin = open('input.txt', 'r')
si = sys.stdin.readline

n = int(si())
route = list(map(int, si().split()))
prices = list(map(int, si().split()))
res = 0
minimum_oil_prices = prices[0]
for i in range(n - 1):
    minimum_oil_prices = min(prices[i], minimum_oil_prices)
    res += minimum_oil_prices * route[i]

print(res)
