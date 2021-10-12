# BOJ 1058 친구
import sys


sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline

N = int(si())
graph = [list(si().strip()) for _ in range(N)]

dp = [[0 for _ in range(N)] for _ in range(N)]
for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if graph[i][j] == "Y":
                dp[i][j] = 1
                continue
            dp[i][j] = max(
                dp[i][j], 1 if graph[i][k] == "Y" and graph[k][j] == "Y" else 0
            )
answer = 0
for i in range(N):
    answer = max(answer, sum(dp[i]))
print(answer)
