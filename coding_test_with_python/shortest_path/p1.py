# 미래 도시
"""
1번부터 N번까지의 회사가 있고, 특정 회사끼리는 서로 도로를 통해 연결되어 있다.
현재 1번 위치에 있고, X번 회사에 방문해 물건을 판매하고자 할때,
A -> K -> X 순서로 이동해야 함
"""
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
        # 이미 방문한 노드에 대해 처리
        if distance[now] < dist:
            continue

        for j in graph[now]:
            cost = j[1] + dist
            if cost < distance[j[0]]:
                distance[j[0]] = cost
                heapq.heappush(q, (cost, j[0]))


answer = 0
n, m = map(int, si().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, si().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))
x, k = map(int, si().split())
distance = [INF] * (n + 1)
dijkstra(1)
answer += distance[k]
distance = [INF] * (n + 1)
dijkstra(k)
answer += distance[x]
print(answer)
