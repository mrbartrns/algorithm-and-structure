# 우선순위 큐를 이용한 다익스트라 알고리즘
import sys
import heapq

si = sys.stdin.readline

INF = 1e9

n, m = map(int, si().split())

start = int(si())

# graph 그리기
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)
for _ in range(m):
    a, b, c = map(int, si().split())
    graph[a].append((b, c))


# 다익스트라 알고리즘
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)

        # 이미 처리되었다면 무시하기
        if distance[now] < dist:
            continue

        for j in graph[now]:
            cost = dist + j[1]
            if distance[j[0]] > cost:
                distance[j[0]] = cost
                heapq.heappush(q, (cost, j[0]))


dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])