# 벨만 포드 알고리즘
import sys

si = sys.stdin.readline
INF = int(1e9)

n, m = map(int, si().split())
edges = []  # 모든 간선에 대한 정보
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, si().split())
    edges.append((a, b, c))  # a번 노드에서 b번 노드로 가는 값이 c


def bf(start):
    distance[start] = 0
    # 전체 n번의 라운드를 반복
    for i in range(n):
        for j in range(m):
            cur = edges[j][0]
            next_node = edges[j][1]
            cost = edges[j][2]
            # 현재 간선이 INF라면 현재 간선까지 갈 수 있는 경로가 없다
            if distance[cur] != INF and distance[next_node] > distance[cur] + cost:
                distance[next_node] = distance[cur] + cost
                if i == n - 1:
                    return True
    return False
