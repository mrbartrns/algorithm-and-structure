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
    max_value = 0
    idx = 0

    for i in range(1, n + 1):
        if max_value < distance[i]:
            max_value = distance[i]
            idx = i

    distance = [INF] * (n + 1)
    dijkstra(idx, distance, graph)

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

        for i in graph[now]:
            cost = dist + 1
            if distance[i] > cost:
                distance[i] = cost
                heapq.heappush(q, (cost, i))


def check_unique(distance):
    max_value = 0
    unique = True
    idx = 0
    for i in range(1, len(distance)):
        if distance[i] > max_value:
            max_value = distance[i]
            unique = True
            idx = i
        elif distance[i] == max_value:
            unique = False
    return unique, idx


if __name__ == '__main__':
    n = 4
    edges = [[1, 2], [2, 3], [3, 4]]
    print(solution(n, edges))
