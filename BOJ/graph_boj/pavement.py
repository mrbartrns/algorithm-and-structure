# BOJ 1162 도로 포장
import heapq
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
INF = int(1e15)


def dijkstra(start):
    q = []
    distance[0][start] = 0
    heapq.heappush(q, (0, start, 0))  # count, node, k
    while q:
        dist, now, k = heapq.heappop(q)
        if distance[k][now] < dist:
            continue
        for nxt, cost in adj[now]:
            value = dist + cost
            if distance[k][nxt] > value:
                distance[k][nxt] = value
                heapq.heappush(q, (value, nxt, k))
            if k >= K:
                continue
            if distance[k + 1][nxt] > dist:
                distance[k + 1][nxt] = dist
                heapq.heappush(q, (dist, nxt, k + 1))


N, M, K = map(int, si().strip().split(" "))
adj = [[] for _ in range(N + 1)]
distance = [[INF for _ in range(N + 1)] for _ in range(K + 1)]
for _ in range(M):
    a, b, c = map(int, si().strip().split(" "))
    adj[a].append((b, c))
    adj[b].append((a, c))
dijkstra(1)
answer = INF
for i in range(K + 1):
    answer = min(answer, distance[i][N])
print(answer)
