# 숨바꼭질
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
            if distance[j] > dist + 1:
                distance[j] = dist + 1
                heapq.heappush(q, (dist + 1, j))


n, m = map(int, si().split())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)
for _ in range(m):
    a, b = map(int, si().split())
    graph[a].append(b)
    graph[b].append(a)

dijkstra(1)
min_idx = 1
max_length = 0
cnt = 0
for i in range(1, n + 1):
    if max_length < distance[i]:
        max_length = distance[i]
        min_idx = i
        cnt = 1
    elif max_length == distance[i]:
        cnt += 1

print(min_idx, max_length, cnt)
