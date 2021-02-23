# BOJ 1261
import sys
import heapq

si = sys.stdin.readline
INF = 1e9

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

m, n = map(int, si().split())
graph = []
dp = [[INF for _ in range(m)] for _ in range(n)]

for _ in range(n):
    graph.append(list(map(int, si().strip())))


def solve(n, m):
    q = []
    dp[0][0] = 0
    heapq.heappush(q, (0, 0, 0))
    while q:
        value, x, y = heapq.heappop(q)
        if dp[x][y] < value:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            cost = value + graph[nx][ny]
            if cost < dp[nx][ny]:
                dp[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))
    return dp[n - 1][m - 1]


print(solve(n, m))