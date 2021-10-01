# BOJ 1595 북쪽 나라의 도로
import heapq
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
INF = 987654321


def get_max_value():
    ret = 0
    for node in node_list:
        if ret < distance[node]:
            ret = distance[node]
    return ret


def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for j in graph[now]:
            nxt = j[0]
            cost = dist + j[1]
            if distance[nxt] > cost:
                distance[nxt] = cost
                heapq.heappush(q, (cost, nxt))


graph = [[] for _ in range(10001)]
distance = [INF] * 10001
node_list = set()

while True:
    try:
        a, b, c = map(int, si().split(" "))
        graph[a].append((b, c))
        graph[b].append((a, c))
        node_list.add(a)
        node_list.add(b)
    except:
        break

dijkstra(1)
ret = 0
start = 0
for node in node_list:
    if ret < distance[node]:
        start = node
        ret = distance[node]

distance = [INF] * 10001
dijkstra(start)
print(get_max_value())