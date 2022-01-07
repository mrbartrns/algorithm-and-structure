# BOJ 1757 달려달려 (dp)
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline

N, M = map(int, si().strip().split(" "))
arr = []
for _ in range(N):
    arr.append(int(si().strip()))
cache = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
for i in range(N):
    for j in range(M + 1):
        if i < j:
            continue
        if j == 0:
            cache[i + 1][j] = max(cache[i + 1][j], cache[i][j])
        elif j > 0 and i + j <= N:
            cache[i + j][0] = max(cache[i + j][0], cache[i][j])
        if j < M:
            cache[i + 1][j + 1] = max(cache[i + 1][j + 1], cache[i][j] + arr[i])
print(cache[N][0])
