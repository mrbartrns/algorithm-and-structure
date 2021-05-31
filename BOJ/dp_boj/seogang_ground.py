# BOJ 14938
import heapq
import sys

si = sys.stdin.readline
INF = 987654321


def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, v = heapq.heappop(q)
        if distance[v] < dist:
            continue
        for j in graph[v]:
            cost = dist + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost
                heapq.heappush(q, (cost, j[0]))


n, m, r = map(int, si().split())
graph = [[] for _ in range(n + 1)]
items = [0] + list(map(int, si().split()))

s = 0
for _ in range(r):
    a, b, c = map(int, si().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

for u in range(1, n + 1):
    distance = [INF] * (n + 1)
    dijkstra(u)
    t = 0
    for i in range(1, n + 1):
        if distance[i] <= m:
            t += items[i]
    s = max(s, t)

print(s)
