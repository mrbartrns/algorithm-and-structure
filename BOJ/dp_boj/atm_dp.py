# BOJ 2624 동전 바꾸기
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline

T = int(si().strip())  # value of money
K = int(si().strip())  # number of coins
coins = []
numbers = []
cache = [[0 for _ in range(T + 1)] for _ in range(K)]
for _ in range(K):
    a, b = map(int, si().strip().split(" "))
    coins.append(a)
    numbers.append(b)
for i in range(numbers[0] + 1):
    if i * coins[0] <= T:
        cache[0][i * coins[0]] = 1
for i in range(1, K):
    for j in range(T + 1):
        for k in range(numbers[i] + 1):
            if j - coins[i] * k >= 0:
                cache[i][j] += cache[i - 1][j - coins[i] * k]

print(cache[K - 1][T])
