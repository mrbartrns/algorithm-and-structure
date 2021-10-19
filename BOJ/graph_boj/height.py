# BOJ 2458 키 순서
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
            if i == j:
                dp[i][j] = 0
                continue
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

answer = 0
for i in range(1, N + 1):
    check = True
    cnt = 0
    for j in range(1, N + 1):
        if dp[i][j] < INF or dp[j][i] < INF:
            cnt += 1
    if cnt == N:
        answer += 1
print(answer)
