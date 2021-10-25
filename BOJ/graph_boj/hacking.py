# BOJ 10282 해킹
import heapq
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
INF = 987654321


def dijkstra(start, visited):
    q = []
    visited[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if visited[now] < dist:
            continue
        for nxt, cost in graph[now]:
            value = cost + dist
            if visited[nxt] > value:
                visited[nxt] = value
                heapq.heappush(q, (value, nxt))


T = int(si())
for _ in range(T):
    N, D, C = map(int, si().split(" "))
    graph = [[] for _ in range(N + 1)]
    distance = [INF] * (N + 1)
    for _ in range(D):
        a, b, c = map(int, si().split(" "))
        graph[b].append((a, c))
    dijkstra(C, distance)
    counts = 0
    max_distance = 0
    for i in range(1, N + 1):
        if distance[i] < INF:
            max_distance = max(max_distance, distance[i])
            counts += 1
    print(counts, max_distance)
