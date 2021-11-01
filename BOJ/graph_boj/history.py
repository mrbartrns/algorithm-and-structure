# BOJ 1613 역사
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
INF = 987654321

N, M = map(int, si().split(" "))
dp = [[INF for _ in range(N + 1)] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, si().split(" "))
    dp[a][b] = 1


for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

S = int(si())
for _ in range(S):
    a, b = map(int, si().split(" "))
    if dp[a][b] < INF or dp[b][a] < INF:
        if dp[a][b] < INF:
            print(-1)
        else:
            print(1)
    else:
        print(0)
