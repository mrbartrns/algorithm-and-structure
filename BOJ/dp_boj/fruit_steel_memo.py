# BOJ 17213
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline

N = int(si().strip())
M = int(si().strip())
cache = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
cache[0][0] = 1
for i in range(1, N + 1):
    for j in range(1, M + 1):
        cache[i][j] = cache[i - 1][j - 1] + cache[i][j - 1]
print(cache[N][M])
