import heapq
import sys

si = sys.stdin.readline
INF = 987654321


def dijkstra(start, distance_arr):
    q = []
    distance_arr[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, cur = heapq.heappop(q)
        for nxt, cost in adj[cur]:
            value = dist + cost
            if distance_arr[nxt] > value:
                distance_arr[nxt] = value
                heapq.heappush(q, (value, nxt))


T = int(si())
for _ in range(T):
    candidates = []
    N, M, t = map(int, si().split(" "))
    s, g, h = map(int, si().split(" "))
    adj = [[] for _ in range(N + 1)]
    distance1 = [INF] * (N + 1)
    distance2 = [INF] * (N + 1)
    distance3 = [INF] * (N + 1)
    for _ in range(M):
        a, b, d = map(int, si().split(" "))
        adj[a].append((b, d))
        adj[b].append((a, d))
    for _ in range(t):
        candidates.append(int(si()))
    candidates.sort()
    # 항상 특정 노드까지 최단 경로를 보장하므로 다른 처리를 할 필요가 없다.
    dijkstra(s, distance1)
    dijkstra(g, distance2)
    dijkstra(h, distance3)
    for x in candidates:
        if distance1[x] == distance1[g] + distance2[h] + distance3[x]:
            print(x, end=" ")
        elif distance1[x] == distance1[h] + distance3[g] + distance2[x]:
            print(x, end=" ")
    print()
