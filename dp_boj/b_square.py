# BOJ 1915
import sys

si = sys.stdin.readline


n, m = map(int, si().split())
graph = [[0 for _ in range(m + 1)] for _ in range(n + 1)]


for i in range(1, n + 1):
    graph[i] = [0] + list(map(int, list(si().strip())))


def solve(n, m):
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    cnt = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if graph[i][j] == 1:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                cnt = max(dp[i][j], cnt)
    return cnt


print(solve(n, m) ** 2)
