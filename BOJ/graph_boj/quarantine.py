# BOJ 2307 검문
"""
도로 하나를 막아 탈출을 지연시켜야 한다.
다익스트라는 이미 각 지점까지 최단 거리가 나와 있다.
다익스트라를 시작점에서 한번, 뒤집어서 마지맘ㄱ 노드에서 한번 실행한다.
"""
import heapq
import sys


sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
INF = 987654321


def memset(arr, value):
    for i in range(len(arr)):
        arr[i] = value


def dijkstra(start, node1, node2):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, cur = heapq.heappop(q)
        if distance[cur] < dist:
            continue
        for nxt, cost in adj[cur]:
            if (cur == node1 and nxt == node2) or (cur == node2 and nxt == node1):
                continue
            value = cost + dist
            if distance[nxt] > value:
                distance[nxt] = value
                prev[nxt] = cur
                heapq.heappush(q, (value, nxt))


N, M = map(int, si().split(" "))
distance = [INF] * (N + 1)
adj = [[] for _ in range(N + 1)]
prev = [-1] * (N + 1)
shortest_route = []
for _ in range(M):
    a, b, c = map(int, si().split(" "))
    adj[a].append((b, c))
    adj[b].append((a, c))
dijkstra(1, -1, -1)
minimum_distance = distance[N]
current_distance = 0
s = N
while s != -1:
    shortest_route.append(s)
    s = prev[s]
for i in range(len(shortest_route) - 1):
    memset(distance, INF)
    memset(prev, -1)
    dijkstra(1, shortest_route[i], shortest_route[i + 1])
    current_distance = max(current_distance, distance[N])
answer = current_distance - minimum_distance
print(answer if current_distance < INF else -1)
