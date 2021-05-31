# BOJ 1753
import sys
import heapq

si = sys.stdin.readline


def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for j in graph[now]:
            cost = dist + j[1]
            if distance[j[0]] > cost:
                distance[j[0]] = cost
                heapq.heappush(q, (cost, j[0]))


n, e = map(int, si().split())
start = int(si())
INF = 1e9
distance = [INF] * (n + 1)
graph = [[] for _ in range(n + 1)]
for _ in range(e):
    u, v, w = map(int, si().split())
    graph[u].append((v, w))

dijkstra(start)

for i in range(1, n + 1):
    if distance[i] < INF:
        print(distance[i])
    else:
        print("INF")
