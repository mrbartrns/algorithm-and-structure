# BOJ 4485 녹색 옷 입은 애가 젤다죠?
import heapq
import sys


sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline

INF = 987654321
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def dijkstra(distance, maps):
    q = []
    distance[0][0] = maps[0][0]
    heapq.heappush(q, (maps[0][0], 0, 0))  # cost, y, x
    while q:
        cost, y, x = heapq.heappop(q)
        if distance[y][x] < cost:
            continue
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= N or nx < 0 or nx >= N:
                continue
            if cost + maps[ny][nx] < visited[ny][nx]:
                visited[ny][nx] = cost + maps[ny][nx]
                heapq.heappush(q, (visited[ny][nx], ny, nx))


# input
tc = 0
while True:
    N = int(si())
    if N == 0:
        break
    tc += 1
    graph = [list(map(int, si().split(" "))) for _ in range(N)]
    visited = [[INF for _ in range(N)] for _ in range(N)]
    dijkstra(visited, graph)
    print(f"Problem {tc}: {visited[N - 1][N - 1]}")
