import heapq

INF = int(1e12)


def solution(n, s, a, b, fares):
    graph = [[] for _ in range(n + 1)]
    res = INF
    for c, d, f in fares:
        graph[c].append((d, f))
        graph[d].append((c, f))

    for i in range(1, n + 1):
        distance = [INF] * (n + 1)
        dijkstra(i, graph, distance)
        res = min(res, distance[s] + distance[a] + distance[b])
    return res


def dijkstra(start, graph, distance):
    q = []
    distance[start] = 0

    heapq.heappush(q, (0, start))
    while q:
        dist, node = heapq.heappop(q)

        if distance[node] < dist:
            continue

        for j in graph[node]:
            cost = dist + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost
                heapq.heappush(q, (cost, j[0]))


if __name__ == "__main__":
    n = 6
    s = 4
    a = 5
    b = 6
    fares = [[2, 6, 6], [6, 3, 7], [4, 6, 7], [6, 5, 11], [2, 5, 12], [5, 3, 20], [2, 4, 8], [4, 3, 9]]
    print(solution(n, s, a, b, fares))
