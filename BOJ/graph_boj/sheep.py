# BOJ 16437 양 구출 작전
"""
N개의 섬으로 이루어진 나라가 있다. (섬들은 1번 섬부터 N번 섬까지 존재한다.)
1번 섬에는 구명보트만 존재
각 섬에서 1번 섬으로 가는 경로가 유일함 -> 트리 구조를 띄고 있는 형태
늑대 한마리는 최대 양 한마리를 잡아먹음
Ti가 w 일때 i번 섬에 늑대가 ai 마리 살고 있음 ti가 S인 경우 양이 ai 마리 살고 있음
4
S 100 3
W 50 1
S 10 1
양의 수 - 늑대의 수 값이 최댓값이 될 때 양의 수가 최대가 된다.

** 틀린 알고리즘임
"""
import heapq
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
INF = 987654321


def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, cur = heapq.heappop(q)
        if distance[cur] < dist:
            continue
        for nxt in adj[cur]:
            value = dist
            if info[nxt] == "W":
                value += counts[nxt]
            if distance[nxt] > value:
                distance[nxt] = value
                heapq.heappush(q, (value, nxt))


N = int(si())
info = [""] * (N + 1)
counts = [0] * (N + 1)
adj = [[] for _ in range(N + 1)]
distance = [INF] * (N + 1)

for i in range(2, N + 1):
    a, b, c = list(si().strip().split(" "))
    info[i] = a
    counts[i] = int(b)
    adj[i].append(int(c))
    adj[int(c)].append(i)
dijkstra(1)
ret = 0
for i in range(1, N + 1):
    if info[i] == "S" and counts[i] > distance[i]:
        ret += counts[i] - distance[i]
print(ret)
