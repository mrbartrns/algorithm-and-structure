# BOJ 1753
import sys
import heapq as hq

si = sys.stdin.readline
INF = 1e9


def dijkstra(start):
    q = []
    distance[start] = 0
    hq.heappush(q, (0, start))
    while q:
        # dist는 start node로 부터 현재 node 까지의 거리
        dist, now = hq.heappop(q)
        # 현재 노드가 출발노드로부터의 거리보다 짧다면 더이상 진행하지 않는다.
        if distance[now] < dist:
            continue

        for j in graph[now]:
            cost = dist + j[1]
            if distance[j[0]] > cost:
                distance[j[0]] = cost
                hq.heappush(q, (cost, j[0]))


n, e = map(int, si().split())
start = int(si())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)
for _ in range(e):
    u, v, w = map(int, si().split())
    graph[u].append((v, w))

dijkstra(start)
for i in range(1, n + 1):
    print(distance[i] if distance[i] < INF else "INF")