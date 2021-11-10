import heapq
import sys

sys.stdin = open("../input.txt", "r")
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
        for nxt, cost in adj[now]:
            value = dist + cost
            if distance[nxt] > value:
                distance[nxt] = value
                prev[nxt] = now
                heapq.heappush(q, (value, nxt))


N, M = map(int, si().split(" "))
count = 0
adj = [[] for _ in range(N + 1)]
distance = [INF] * (N + 1)
prev = [-1] * (N + 1)
ret = []
for _ in range(M):
    a, b, c = map(int, si().split(" "))
    adj[a].append((b, c))
    adj[b].append((a, c))
dijkstra(1)
for i in range(1, N + 1):
    if prev[i] != -1:
        ret.append((i, prev[i]))
        count += 1
print(count)
for a, b in ret:
    print(a, b)
