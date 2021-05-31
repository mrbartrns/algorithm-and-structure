# 다익스트라 알고리즘 O(n ** 2) 복습
import sys

si = sys.stdin.readline

INF = 1e9

# 그래프 만들기
# 노드의 개수와 간선의 정보 입력
n, m = map(int, si().split())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)
visited = [False] * (n + 1)


start = int(si())


for _ in range(m):
    # 현재노드, 이어진 노드, 비용
    a, b, c = map(int, si().split())
    graph[a].append((b, c))


# 최소 인덱스 구하기
def get_minimum_idx():
    min_value = INF
    min_idx = 0
    for i in range(1, n + 1):
        if not visited[i] and min_value > distance[i]:
            min_value = distance[i]
            min_idx = i
    return min_idx


# 다익스트라 알고리즘
def dijkstra(start):
    # 시작 노드에 대해 먼저 초기화하기
    distance[start] = 0
    visited[start] = True

    for i in graph[start]:
        distance[i[0]] = i[1]

    for _ in range(n - 1):
        now = get_minimum_idx()
        visited[now] = True
        for i in graph[now]:
            cost = distance[now] + i[1]
            distance[i[0]] = min(distance[i[0]], cost)


dijkstra(start)