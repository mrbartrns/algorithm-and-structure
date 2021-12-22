# BOJ 10217
# 플루이드 워셜로 해결 불가능
import heapq
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
INF = 987654321

T = int(si().strip())


def dijkstra(start):
    q = []
    distance[0][start] = 0
    heapq.heappush(q, (0, 0, start))
    while q:
        dist, cost, now = heapq.heappop(q)
        if distance[cost][now] < dist:
            continue
        for nxt, nxt_cost, nxt_dist in adj[now]:
            if nxt_cost + cost > M:
                continue
            if distance[nxt_cost + cost][nxt] > dist + nxt_dist:
                distance[nxt_cost + cost][nxt] = dist + nxt_dist
                heapq.heappush(q, (dist + nxt_dist, nxt_cost + cost, nxt))


for _ in range(T):
    N, M, K = map(int, si().strip().split(" "))
    distance = [[INF for _ in range(N + 1)] for _ in range(M + 1)]
    adj = [[] for _ in range(N + 1)]
    for i in range(K):
        a, b, c, d = map(int, si().strip().split(" "))
        adj[a].append((b, c, d))  # next, cost, dist
        # adj[b].append((a, c, d))
    dijkstra(1)
    answer = INF
    for i in range(M + 1):
        answer = min(answer, distance[i][N])
    print(answer if answer < INF else "Poor KCM")
