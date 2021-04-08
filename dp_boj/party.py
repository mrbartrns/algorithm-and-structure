# BOJ 1238
import heapq
import sys

si = sys.stdin.readline
INF = 101


def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, node = heapq.heappop(q)
        if dist > distance[node]:
            continue
        for j in graph[node]:
            cost = dist + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost
                heapq.heappush(q, (cost, j[0]))


n, m, x = map(int, si().split())
graph = [[] for _ in range(n + 1)]
max_value = 0
for _ in range(m):
    a, b, c = map(int, si().split())
    graph[a].append((b, c))
for i in range(1, n + 1):
    s = 0
    distance = [INF] * (n + 1)
    dijkstra(i)
    s += distance[x]
    distance = [INF] * (n + 1)
    dijkstra(x)
    s += distance[i]
    max_value = max(max_value, s)

print(max_value)
