# BOJ 2533 얼리어답터
import sys

sys.setrecursionlimit(1000001)
sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline


def dfs(node, parent):
    leaf = True
    for child in graph[node]:
        if child != parent:
            leaf = False
            dfs(child, node)
    if leaf:
        dp[node][0] = 0
        dp[node][1] = 1
        return
    s1 = 0
    s2 = 0
    for child in graph[node]:
        s1 += min(dp[child][0], dp[child][1])
        s2 += dp[child][1]
    dp[node][1] = s1 + 1
    dp[node][0] = s2


n = int(si())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, si().split())
    graph[a].append(b)
    graph[b].append(a)

dp = [[0 for _ in range(2)] for _ in range(n + 1)]
dfs(1, -1)
print(min(dp[1][0], dp[1][1]))