# BOJ 1932 (정수 삼각형)
import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline

n = int(si())
dp = [[-1 for _ in range(n)] for _ in range(n)]
graph = []
for _ in range(n):
    graph.append(list(map(int, si().split())))

dp[0][0] = graph[0][0]
for i in range(1, n):
    for j in range(i + 1):
        val = dp[i - 1][j]
        if j - 1 >= 0:
            val = max(dp[i - 1][j - 1], val)
        dp[i][j] = val + graph[i][j]

print(max(dp[n - 1]))
