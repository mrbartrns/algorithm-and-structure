# BOJ 1865
import sys

si = sys.stdin.readline
INF = 1e9


def bf(start):
    distance[start] = 0
    for i in range(n):
        for j in range(len(edges)):
            cur = edges[j][0]
            next_node = edges[j][1]
            cost = edges[j][2]
            if distance[next_node] > distance[cur] + cost:
                distance[next_node] = distance[cur] + cost
                if i == n - 1:
                    return True
    return False


t = int(si())
for _ in range(t):
    edges = []
    n, m, w = map(int, si().split())
    distance = [INF] * (n + 1)
    for _ in range(m):
        a, b, c = map(int, si().split())
        edges.append((a, b, c))
        edges.append((b, a, c))
    for _ in range(w):
        a, b, c = map(int, si().split())
        edges.append((a, b, -c))
    negative_cycle = bf(1)
    if negative_cycle:
        print("YES")
    else:
        print("NO")
