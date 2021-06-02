# bellman ford algorithms
import sys

si = sys.stdin.readline
INF = 987654321

n, m = map(int, si().split())
edges = []
for _ in range(m):
    edges.append(list(map(int, si().split())))  # a -> b : c
distance = [INF for _ in range(n + 1)]


def bf(start):
    distance[start] = 0
    for i in range(n):
        for j in edges:
            cur = j[0]
            next_node = j[1]
            cost = j[2]
            if distance[cur] != INF and distance[next_node] > distance[cur] + cost:
                distance[next_node] = distance[cur] + cost
                if i == n - 1:  # 두 노드간 최대 거리는 n - 1이다
                    return False
    return True


if bf(1):
    print(True)
else:
    print(False)
