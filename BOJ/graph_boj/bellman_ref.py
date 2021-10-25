# 벨만 포드 알고리즘
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline
INF = 987654321


def bf(start):
    distance[start] = 0
    for i in range(N):
        for j in range(M):
            cur = edges[j][0]
            next_node = edges[j][1]
            cost = edges[j][2]
            if distance[cur] != INF and distance[next_node] > distance[cur] + cost:
                distance[next_node] = distance[cur] + cost
                if i == N - 1:
                    return True
    return False


N, M = map(int, si().split(" "))
edges = []
distance = [INF] * (N + 1)
for _ in range(M):
    a, b, c = map(int, si().split(" "))
    edges.append((a, b, c))

negative = bf(1)
if negative:
    print(-1)
else:
    for i in range(2, N + 1):
        if distance[i] == INF:
            print(-1)
        else:
            print(distance[i])
