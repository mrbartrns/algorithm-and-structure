# 택시 합승 요금
import heapq

INF = int(1e12)


def solution(n, s, a, b, fares):
    answer = INF
    graph = make_graph(n, fares)
    for i in range(1, n + 1):
        distance = [INF for _ in range(n + 1)]
        dijkstra(distance, graph, i)
        answer = min(answer, get_sum(distance, s, a, b))
    return answer


def make_graph(n, fares):
    graph = [[] for _ in range(n + 1)]
    for i in range(len(fares)):
        a, b, c = fares[i]
        graph[a].append((b, c))
        graph[b].append((a, c))
    return graph


def dijkstra(distance, maps, start):
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for j in maps[now]:
            cost = j[1] + dist
            if distance[j[0]] > cost:
                distance[j[0]] = cost
                heapq.heappush(q, (cost, j[0]))


def get_sum(distance, s, a, b):
    ret = 0
    ret += distance[s]
    ret += distance[a]
    ret += distance[b]
    return ret


if __name__ == "__main__":
    n = 7
    s = 3
    a = 4
    b = 1
    fares = [[1, 2, 6], [2, 3, 3], [3, 6, 1], [4, 6, 4], [5, 7, 9]]
    print(solution(n, s, a, b, fares))
