# Dijkstra Algorithms
import heapq
import sys

si = sys.stdin.readline
INF = 987654321


def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for j in graph[now]:
            cost = j[1] + dist
            if distance[j[0]] > cost:  # next node value
                distance[j[0]] = cost
                heapq.heappush(q, (cost, j[0]))


n, m = map(int, si().split())
distance = [INF for _ in range(n + 1)]
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, si().split())  # a -> b: c
    graph[a].append((b, c))

dijkstra(1)
