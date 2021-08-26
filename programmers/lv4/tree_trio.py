# 트리 트리오 중간값
import heapq

INF = 987654321


def solution(n, edges):
    distance = [INF] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    dijkstra(1, distance, graph)
    start = 0
    dist = 0
    for i in range(1, n + 1):
        if dist < distance[i]:
            dist = distance[i]
            start = i

    distance = [INF] * (n + 1)
    dijkstra(start, distance, graph)
    unique, idx = check_unique(distance)
    if not unique:
        return distance[idx]

    distance = [INF] * (n + 1)
    dijkstra(idx, distance, graph)
    unique, idx = check_unique(distance)
    if not unique:
        return distance[idx]
    return distance[idx] - 1


def dijkstra(start, distance, graph):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for nxt in graph[now]:
            cost = dist + 1
            if distance[nxt] > cost:
                distance[nxt] = cost
                heapq.heappush(q, (cost, nxt))


def check_unique(distance):
    unique = True
    idx = 0
    value = 0
    for i in range(1, len(distance)):
        if value < distance[i]:
            value = distance[i]
            idx = i
            unique = True
        elif value == distance[i]:
            unique = False
    return unique, idx


if __name__ == '__main__':
    n = 5
    edges = [[1, 5], [2, 5], [3, 5], [4, 5]]
    print(solution(n, edges))
