import heapq
import sys

si = sys.stdin.readline

INF = 987654321


def dijkstra(start, distance):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for nxt, cost in adj[now]:
            value = cost + dist
            if distance[nxt] > value:
                distance[nxt] = value
                heapq.heappush(q, (value, nxt))


V, E = map(int, si().strip().split(" "))
adj = [[] for _ in range(V + 1)]
distance_mc = [INF] * (V + 1)
distance_star = [INF] * (V + 1)
for _ in range(E):
    a, b, c = map(int, si().strip().split(" "))
    adj[a].append((b, c))
    adj[b].append((a, c))
mcs = list(map(int, si().strip().split(" ")))
mc_limit = mcs[1]
mc_arr = list(map(int, si().strip().split(" ")))
for mc in mc_arr:
    dijkstra(mc, distance_mc)
stars = list(map(int, si().strip().split(" ")))
star_limit = stars[1]
star_arr = list(map(int, si().strip().split(" ")))
for star in star_arr:
    dijkstra(star, distance_star)
answer = INF
for i in range(1, V + 1):
    if distance_mc[i] <= 0 or distance_mc[i] > mc_limit:
        continue
    if distance_star[i] <= 0 or distance_star[i] > star_limit:
        continue
    answer = min(answer, distance_mc[i] + distance_star[i])
print(answer if answer < INF else -1)
