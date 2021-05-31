# bellman ford algorithm
import sys

si = sys.stdin.readline
INF = 987654321


def bf(start):
    distance[start] = 0
    for i in range(n):
        for j in range(m):
            cur = edges[j][0]  # current node
            next_node = edges[j][1]
            cost = edges[j][2]
            if distance[cur] != INF and distance[next_node] > distance[cur] + cost:
                distance[next_node] = distance[cur] + cost
                if i == n - 1:
                    return False
    return True


edges = []
n = int(si())
m = int(si())
for _ in range(m):
    a, b, c = map(int, si().split())
    edges.append((a, b, c))
distance = [INF for _ in range(n + 1)]
