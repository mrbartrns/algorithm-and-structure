# heapq를 이용한 화성 탐사
import heapq
import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline
INF = 987654321
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


# 큐를 이용하는 방법과 동일하지만 그중 최단 거리 먼저 방문하게 되는 특징이 있다.
# 기존 큐를 이용한 bfs 실행 후 시간적인 측면에서 손해라면 다익스트라 고려
def dijkstra(graph, distance):
    q = []
    heapq.heappush(q, (graph[0][0], 0, 0))
    distance[0][0] = graph[0][0]
    while q:
        cost, y, x = heapq.heappop(q)
        if distance[y][x] < cost:
            continue

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or ny >= n or nx < 0 or nx >= n:
                continue

            if distance[ny][nx] > cost + graph[ny][nx]:
                distance[ny][nx] = cost + graph[ny][nx]
                heapq.heappush(q, (cost + graph[ny][nx], ny, nx))


t = int(si())
for _ in range(t):
    n = int(si())
    graph = [list(map(int, si().split())) for _ in range(n)]
    visited = [[INF for _ in range(n)] for _ in range(n)]
    dijkstra(graph, visited)
    print(visited[n - 1][n - 1])
