# BOJ 3908 서로 다른 소수의 합
import math
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline

primes = []
sieve = [True] * 1120
for i in range(2, int(math.sqrt(1120)) + 1):
    if sieve[i]:
        for j in range(i + i, 1120, i):
            sieve[j] = False
for i in range(2, 1120):
    if sieve[i]:
        primes.append(i)
cache = [[0 for _ in range(15)] for _ in range(1121)]
cache[0][0] = 1
for p in primes:
    for i in range(1120, 0, -1):
        for k in range(1, 15):
            if i - p >= 0:
                cache[i][k] += cache[i - p][k - 1]
T = int(si().strip())
for _ in range(T):
    a, b = map(int, si().strip().split(" "))
    print(cache[a][b])
