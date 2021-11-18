# BOJ 9370 미확인 도착지
"""
n, m, t -> 교차로, 도로, 목적지 후보의 개수
s, g, h -> 시작점, g, h 교차로 사이에 있는 도로를 무조건 지나감
a, b, d -> a, b 사이에 거리가 d인 양방향 도로가 있음
t개의 줄에 정수 x -> t개의 목적지 후보
# 입력에서 주어진 목적지 후보들 중 불가능한 경우들을 제외한 목적지들을 공백으로 출력

g, h 사이의 도로를 통과하는 경로가 최단 경로를 만족하는지 확인
목적지에서 g 또는 h까지의 거리중 짧은 거리, 시작지점에서 g 또는 h 까지의 거리 중 짧은 거리, 그리고 시작점에서 목적지 까지의 거리를 비교하여 두 개가 동일한지 확인
"""
import heapq
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
INF = 987654321


def dijkstra(start, distance_arr):
    q = []
    distance_arr[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, cur = heapq.heappop(q)
        if distance_arr[cur] < dist:
            continue
        for nxt, cost in adj[cur]:
            value = dist + cost
            if distance_arr[nxt] > value:
                distance_arr[nxt] = value
                heapq.heappush(q, (value, nxt))


T = int(si())
for _ in range(T):
    candidate = []
    N, M, t = map(int, si().split(" "))
    s, g, h = map(int, si().split(" "))
    adj = [[] for _ in range(N + 1)]
    distance_s = [INF] * (N + 1)
    distance_g = [INF] * (N + 1)
    distance_h = [INF] * (N + 1)
    for _ in range(M):
        a, b, d = map(int, si().split(" "))
        adj[a].append((b, d))
        adj[b].append((a, d))
    for _ in range(t):
        dest = int(si())
        candidate.append(dest)
    candidate.sort()
    dijkstra(s, distance_s)
    dijkstra(g, distance_g)
    dijkstra(h, distance_h)
    for dest in candidate:
        if distance_s[dest] == distance_s[g] + distance_g[h] + distance_h[dest]:
            print(dest, end=" ")
        elif distance_s[dest] == distance_s[h] + distance_h[g] + distance_g[dest]:
            print(dest, end=" ")
    print()
