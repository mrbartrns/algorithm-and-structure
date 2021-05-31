# BOJ 1261
import sys
import heapq

si = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
MAX = 1e9


def dijkstra(n, m):
    q = []
    heapq.heappush(q, (0, 0, 0))
    dp[0][0] = 0
    while q:
        cnt, x, y = heapq.heappop(q)
        if dp[x][y] < cnt:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            cost = dp[x][y] + graph[nx][ny]
            if cost < dp[nx][ny]:
                dp[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))
    return dp[n - 1][m - 1]


m, n = map(int, si().split())
graph = []
dp = [[MAX for _ in range(m)] for _ in range(n)]
for _ in range(n):
    graph.append(list(map(int, list(si().strip()))))

print(dijkstra(n, m))