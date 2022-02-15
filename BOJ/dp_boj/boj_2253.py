# BOJ 2253 점프
import sys

sys.setrecursionlimit(1000000)
sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
INF = 987654321


N, M = map(int, si().strip().split(" "))
s = set()
for _ in range(M):
    s.add(int(si().strip()))
cache = [[INF for _ in range(150)] for _ in range(N + 1)]


# def solve(y, x):
#     if y > N or x <= 0:
#         return INF
#     if y in s:
#         return INF
#     if y == N:
#         return 0
#     if cache[y][x] < INF:
#         return cache[y][x]
#     cache[y][x] = min(
#         cache[y][x],
#         1 + solve(y + x, x - 1),
#         1 + solve(y + x, x),
#         1 + solve(y + x, x + 1),
#     )
#     return cache[y][x]


# solve(1, 1)
# print(cache[1][1])
cache[1][1] = 0
for i in range(1, N + 1):
    for j in range(1, 150):
        if i in s:
            continue
        if i + j > N:
            continue
        if j - 1 > 0:
            cache[i + j][j - 1] = min(cache[i + j][j - 1], 1 + cache[i][j])
        cache[i + j][j] = min(cache[i + j][j], 1 + cache[i][j])
        if j + 1 < 150:
            cache[i + j][j + 1] = min(cache[i + j][j + 1], 1 + cache[i][j])

ret = INF
for j in range(150):
    ret = min(ret, cache[N][j])
print(ret if ret < INF else -1)
