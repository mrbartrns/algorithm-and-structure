# [카카오] 합승 택시 요금
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
            cost = i[1] + dist

            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


def solution(n, s, p, q, fares):
    answer = INF
    graph = [[] for _ in range(n + 1)]
    for a, b, c in fares:
        graph[a].append((b, c))
        graph[b].append((a, c))
    for i in range(1, n + 1):
        distance = [INF] * (n + 1)
        dijkstra(i, distance, graph)
        answer = min(answer, distance[s] + distance[p] + distance[q])
    return answer


if __name__ == "__main__":
    n = 6
    s = 4
    a = 6
    b = 2
    fares = [
        [4, 1, 10],
        [3, 5, 24],
        [5, 6, 2],
        [3, 1, 41],
        [5, 1, 24],
        [4, 6, 50],
        [2, 4, 66],
        [2, 3, 22],
        [1, 6, 25],
    ]
    print(solution(n, s, a, b, fares))