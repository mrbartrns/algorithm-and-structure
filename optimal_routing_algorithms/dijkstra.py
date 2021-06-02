# 다익스트라 알고리즘
import heapq
import sys

si = sys.stdin.readline
INF = 987654321

n, m = map(int, si().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, si().split())
    graph[a].append((b, c))
distance = [INF for _ in range(n + 1)]


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

