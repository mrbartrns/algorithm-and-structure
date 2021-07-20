# 정확한 순위 플루이드
import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline
INF = 987654321

n, m = map(int, si().split())
dp = [[INF for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(n + 1):
    dp[i][i] = 0

for _ in range(m):
    a, b = map(int, si().split())
    dp[a][b] = 1

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dp[i][j] = min(dp[i][k] + dp[k][j], dp[i][j])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(dp[i][j], end=" ")
    print()

answer = 0
for i in range(1, n + 1):
    cnt = 0
    for j in range(1, n + 1):
        if dp[i][j] < INF or dp[j][i] < INF:
            cnt += 1
        if cnt == n:
            answer += 1
print(answer)
