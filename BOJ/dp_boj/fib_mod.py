# BOJ 9711 피보나치
import sys


sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline

cache = [0] * 10001
cache[0] = 1
for i in range(1, 10001):
    cache[i] = cache[i - 1] + cache[i - 2]
N = int(si())
for i in range(1, N + 1):
    a, b = map(int, si().split(" "))
    print(f"Case #{i}: {cache[a - 1] % b}")
