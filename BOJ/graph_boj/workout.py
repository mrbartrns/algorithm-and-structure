# BOJ 1956 운동
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
INF = 987654321


N, M = map(int, si().split(" "))
graph = [[] for _ in range(N + 1)]
dp = [[INF for _ in range(N + 1)] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, si().split(" "))
    graph[a].append((b, c))
    dp[a][b] = c

answer = INF
for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            dp[i][j] = min(dp[i][k] + dp[k][j], dp[i][j])

# for k in range(1, N + 1):
#     for i in range(1, N + 1):
#         dp[i][i] = min(dp[i][k] + dp[k][i], dp[i][i])

for i in range(1, N + 1):
    answer = min(answer, dp[i][i])
print(answer if answer < INF else -1)
