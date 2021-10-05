# BOJ 2611 자동차경주
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
sys.setrecursionlimit(10000)


def dfs(node):
    if dp[node] > -1:
        return dp[node]

    if node == 1:
        dp[node] = 0
        return 0

    dp[node] = 0
    for i in range(len(graph[node])):
        dp[node] = max(dp[node], dfs(graph[node][i][0]) + graph[node][i][1])
    return dp[node]


N = int(si())
M = int(si())
dp = [-1] * (N + 1)
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    p, q, r = map(int, si().split(" "))
    graph[p].append((q, r))

ret = [1]
for i in range(len(graph[1])):
    dp[1] = max(dfs(graph[1][i][0]) + graph[1][i][1], dp[1])

print(dp[1])