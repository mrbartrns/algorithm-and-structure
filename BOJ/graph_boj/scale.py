# BOJ 10159 저울
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
INF = 987654321


N = int(si())
M = int(si())
cache = [[INF for _ in range(N + 1)] for _ in range(N + 1)]
for i in range(1, N + 1):
    cache[i][i] = 0

for _ in range(M):
    a, b = map(int, si().split(" "))
    cache[a][b] = 1

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            cache[i][j] = min(cache[i][j], cache[i][k] + cache[k][j])


for i in range(1, N + 1):
    cnt = 0
    for j in range(1, N + 1):
        if cache[i][j] == INF and cache[j][i] == INF:
            cnt += 1
    print(cnt)
