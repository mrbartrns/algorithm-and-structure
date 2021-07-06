# 전보
import heapq
import sys

sys.stdin = open('../input.txt', 'r')
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
            if distance[j[0]] > cost:
                distance[j[0]] = cost
                heapq.heappush(q, (cost, j[0]))


n, m, c = map(int, si().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, w = map(int, si().split())
    graph[u].append((v, w))
distance = [INF] * (n + 1)
dijkstra(c)
print(distance)
MAX = 0
cnt = 0
for i in range(1, n + 1):
    if MAX < distance[i] < INF:
        MAX = distance[i]
    if 0 < distance[i] < INF:
        cnt += 1
print(cnt, MAX)
