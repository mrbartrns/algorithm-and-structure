# BOJ 2665 미로 만들기
import heapq
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
INF = 987654321
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def dijkstra(sy, sx):
    q = []
    visited[sy][sx] = 0
    heapq.heappush(q, (0, sy, sx))
    while q:
        cnt, y, x = heapq.heappop(q)

        if visited[y][x] < cnt:
            continue

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or ny >= N or nx < 0 or nx >= N:
                continue

            value = cnt
            if graph[ny][nx] == "0":
                value += 1

            if visited[ny][nx] > value:
                visited[ny][nx] = value
                heapq.heappush(q, (value, ny, nx))


N = int(si())
graph = [list(si().strip()) for _ in range(N)]
visited = [[INF for _ in range(N)] for _ in range(N)]
dijkstra(0, 0)
print(visited[N - 1][N - 1])
