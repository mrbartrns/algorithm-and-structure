# BOJ 14852 타일링3
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
MOD = 1000000007

N = int(si())
cache = [[0 for _ in range(2)] for _ in range(1000001)]
cache[1][0] = 2
cache[2][0] = 7
cache[2][1] = 1
for i in range(3, N + 1):
    cache[i][1] = (cache[i - 3][0] + cache[i - 1][1]) % MOD
    cache[i][0] = (cache[i][1] * 2 + cache[i - 1][0] * 2 + cache[i - 2][0] * 3) % MOD
print(cache[N][0])
