# BOJ 11779
import heapq
import sys

si = sys.stdin.readline
INF = int(1e9)


def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist:
            continue

        for j in graph[node]:
            cost = dist + j[1]
            next_node = j[0]
            if distance[next_node] > cost:  # >= 크거나 같은 부호를 사용하면 시간초과 발생
                distance[next_node] = cost
                trace[next_node] = node
                heapq.heappush(q, (cost, next_node))


n = int(si())
m = int(si())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)
trace = [0] * (n + 1)
route = []
for _ in range(m):
    a, b, c = map(int, si().split())
    graph[a].append((b, c))
s, e = map(int, si().split())
dijkstra(s)
cur_node = e
while cur_node:
    route.append(cur_node)
    cur_node = trace[cur_node]
print(distance[e])
print(len(route))
for i in range(len(route) - 1, -1, -1):
    print(route[i], end=" ")
