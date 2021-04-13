# BOJ 1504
import heapq
import sys

si = sys.stdin.readline
INF = 1e12


def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist:
            continue
        for j in graph[node]:
            cost = dist + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost
                heapq.heappush(q, (cost, j[0]))


n, m = map(int, si().split())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)
for _ in range(m):
    a, b, c = map(int, si().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, si().split())
# 1
t = 0
dijkstra(1)
s1, s2 = distance[v1], distance[v2]

# v1 -> v2
distance = [INF] * (n + 1)
dijkstra(v1)
s1 += distance[v2]
s2 += distance[n]

# v2 -> v1
distance = [INF] * (n + 1)
dijkstra(v2)
s2 += distance[v1]
s1 += distance[n]

s = min(s1, s2)
if s < INF:
    print(s)
else:
    print(-1)

