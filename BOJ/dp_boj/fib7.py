# BOJ 15624 피보나치 수 7
import sys

si = sys.stdin.readline
MOD = 1000000007


# def fibonacci(n):
#     if n <= 0:
#         return 0
#     if n <= 1:
#         return 1
#     if cache[n] > -1:
#         return cache[n]
#     cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
#     cache[n] %= MOD
#     return cache[n]


N = int(si().strip())
cache = [0] * (1000001)
cache[1] = 1
for i in range(2, N + 1):
    cache[i] = cache[i - 1] + cache[i - 2]
    cache[i] %= MOD
print(cache[N])
