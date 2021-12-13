# BOJ 2982 국왕의 방문
"""
문제 말이 너무 이해가 안됨
"""
import heapq
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
INF = 987654321


def dijkstra(start, t):
    q = []
    distance[start] = t
    heapq.heappush(q, (t, start))
    while q:
        dist, here = heapq.heappop(q)
        if distance[here] < dist:
            continue
        for there, cost in adj[here]:
            value = cost + dist
            if route[here][there][0] <= dist < route[here][there][1]:
                value = route[here][there][1] + cost
            if distance[there] > value:
                distance[there] = value
                heapq.heappush(q, (value, there))


N, M = map(int, si().strip().split(" "))
A, B, K, G = map(int, si().strip().split(" "))
visit_list = list(map(int, si().strip().split(" ")))
graph = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
adj = [[] for _ in range(N + 1)]
route = [[[INF, INF] for _ in range(N + 1)] for _ in range(N + 1)]
distance = [INF] * (N + 1)
for _ in range(M):
    a, b, c = map(int, si().strip().split(" "))
    adj[a].append((b, c))
    adj[b].append((a, c))
    graph[a][b] = c
    graph[b][a] = c
s = 0
for i in range(G - 1):
    here = visit_list[i]
    there = visit_list[i + 1]
    route[here][there] = [s, s + graph[here][there]]
    route[there][here] = [s, s + graph[there][here]]
    s += graph[here][there]
dijkstra(A, K)
print(distance[B] - K)
