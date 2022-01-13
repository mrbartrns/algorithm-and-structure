# BOJ 2624 동전 바꿔주기
import sys

sys.stdin = open("../input.txt", "r")
sys.setrecursionlimit(1000000)
si = sys.stdin.readline


def exchange(idx, value):
    if value < 0:
        return 0
    if idx >= K:
        if value == 0:
            return 1
        return 0
    if cache[idx][value] > -1:
        return cache[idx][value]
    cache[idx][value] = 0
    for i in range(numbers[idx] + 1):
        cache[idx][value] += exchange(idx + 1, value - i * coins[idx])
    return cache[idx][value]


T = int(si().strip())  # value of money
K = int(si().strip())  # number of coins
coins = []
numbers = []
cache = [[-1 for _ in range(T + 1)] for _ in range(K)]
for _ in range(K):
    a, b = map(int, si().strip().split(" "))
    coins.append(a)
    numbers.append(b)
print(exchange(0, T))
