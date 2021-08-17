# [카카오 채용연계형 인턴십] 미로 탈출
import heapq

INF = 987654321


def solution(n, start, end, roads, traps):
    distance = [[INF for _ in range(n + 1)] for _ in range(n + 1)]
    graph = [[INF for _ in range(n + 1)] for _ in range(n + 1)]
    for a, b, c in roads:
        graph[a][b] = min(graph[a][b], c)
    dijkstra(distance, graph, start, traps)
    answer = INF
    for i in range(1, len(distance)):
        answer = min(answer, distance[i][end])
    return answer if answer < INF else -1


def dijkstra(distance, graph, start, traps):
    q = []
    distance[start][start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)

        if now in traps:
            for i in range(1, n + 1):
                if graph[now][i] < INF or graph[i][now] < INF:
                    graph[now][i], graph[i][now] = graph[i][now], graph[now][i]

        for i in range(1, n + 1):
            if graph[now][i] == '1':
                cost = graph[now][i] + dist
                if cost <= distance[now][i]:
                    distance[now][i] = cost
                    heapq.heappush(q, (cost, i))


if __name__ == '__main__':
    n = 4
    start = 1
    end = 4
    roads = [[1, 2, 1], [3, 2, 1], [2, 4, 1]]
    traps = [2, 3]
    print(solution(n, start, end, roads, traps))
