# 트리 트리오 중간값
import heapq

INF = 987654321


def dijkstra(start, distance, graph):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + 1
            if distance[i] > cost:
                distance[i] = cost
                heapq.heappush(q, (cost, i))


def solution(n, edges):
    graph = [[] for _ in range(n + 1)]
    distance = [INF] * (n + 1)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    dijkstra(1, distance, graph)
    start = 1
    dist = 0
    for i in range(1, n + 1):
        if dist < distance[i]:
            start = i
            dist = distance[i]

    distance = [INF] * (n + 1)
    dijkstra(start, distance, graph)

    dist = 0
    idx = 1
    unique = True
    for i in range(1, n + 1):
        if dist < distance[i]:
            unique = True
            idx = i
            dist = distance[i]
        elif dist == distance[i]:
            unique = False
            idx = i

    if not unique:
        return dist

    distance = [INF] * (n + 1)
    dijkstra(idx, distance, graph)
    unique = True
    dist = 0
    for i in range(1, n + 1):
        if dist < distance[i]:
            dist = distance[i]
            unique = True
        elif dist == distance[i]:
            unique = False

    return dist if not unique else dist - 1


if __name__ == '__main__':
    n = 5
    edges = [[1, 5], [2, 5], [3, 5], [4, 5]]
    print(solution(n, edges))
