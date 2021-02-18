import sys
import heapq

si = sys.stdin.readline

INF = 1e9

# 그래프 만들기
# 노드의 개수와 간선의 정보 입력
n, m = map(int, si().split())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)
visited = [False] * (n + 1)


start = int(si())

for _ in range(m):
    # 현재노드, 이어진 노드, 비용
    a, b, c = map(int, si().split())
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    # 힙에 삽입시에는 비용, 노드번호 순으로
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + graph[i[1]]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))