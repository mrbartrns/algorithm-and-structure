# BOJ 18352 특정 거리의 도시 찾기(30)
# 다익스트라로 해결하기
import heapq
import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline
INF = 987654321


def dijkstra(start, distance):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for j in graph[now]:
            cost = dist + 1
            if distance[j] > cost:
                distance[j] = cost
                heapq.heappush(q, (cost, j))


n, m, k, x = map(int, si().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, si().split())
    graph[u].append(v)

distance = [INF for _ in range(n + 1)]
dijkstra(x, distance)
answer = []
for i in range(1, n + 1):
    if distance[i] == k:
        answer.append(i)

print("\n".join(list(map(str, answer))) if answer else -1)
