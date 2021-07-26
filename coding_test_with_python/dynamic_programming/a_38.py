# 정확한 순위
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
INF = 987654321
n, m = map(int, si().split())

dp = [[INF for _ in range(n + 1)] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, si().split())
    dp[a][b] = 1

for i in range(n + 1):
    dp[i][i] = 0

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])


answer = 0

for i in range(1, n + 1):
    check = True
    for j in range(1, n + 1):
        if dp[i][j] == INF and dp[j][i] == INF:
            check = False
            break
    if check:
        answer += 1

print(answer)
