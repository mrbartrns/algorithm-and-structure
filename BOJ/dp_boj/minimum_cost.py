# BOJ 1916
import heapq
import sys

si = sys.stdin.readline


def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist:
            continue

        for j in graph[node]:
            cost = j[1] + dist
            if cost < distance[j[0]]:
                distance[j[0]] = cost
                heapq.heappush(q, (cost, j[0]))


n = int(si())
m = int(si())
INF = 1e9
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)
for _ in range(m):
    a, b, c = map(int, si().split())
    graph[a].append([b, c])
    # graph[b].append([a, c])

s, e = map(int, si().split())
dijkstra(s)
print(distance[e])
