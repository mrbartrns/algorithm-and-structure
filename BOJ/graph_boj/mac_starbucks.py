"""
정점의 개수와 도로의 개수
E줄에 걸쳐 각 도로를 나타내는 세 개의 정수 u, v, w
다른 두 정점 사이에는 여러개의 간선이 존재할 수 있다.
맥도날드의 수 M과 맥세권일 조건 X
그 다음 M개 줄에 맥도날드 정점 번호
그 다음 S, 스세권일 조건 Y
스타벅스 정점 번호
"""
import heapq
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
INF = 987654321


def dijkstra(q, distance):
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

mcs, mc_limit = map(int, si().strip().split(" "))
mc_arr = list(map(int, si().strip().split(" ")))
stars, star_limit = map(int, si().strip().split(" "))
star_arr = list(map(int, si().strip().split(" ")))
mq, sq = [], []

for mc in mc_arr:
    heapq.heappush(mq, (0, mc))
    distance_mc[mc] = 0

for star in star_arr:
    heapq.heappush(sq, (0, star))
    distance_star[star] = 0
answer = INF
dijkstra(mq, distance_mc)
dijkstra(sq, distance_star)
for i in range(1, V + 1):
    if distance_mc[i] <= 0 or distance_mc[i] > mc_limit:
        continue
    if distance_star[i] <= 0 or distance_star[i] > star_limit:
        continue
    answer = min(answer, distance_mc[i] + distance_star[i])
print(answer if answer < INF else -1)
