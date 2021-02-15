# 다익스트라 알고리즘 연습
import sys

si = sys.stdin.readline
INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수, 간선의 개수를 입력받기
n, m = map(int, si().split())

# 시작 노드 번호를 입력받기
start = int(si())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for _ in range(n + 1)]

# 방문한 적이 있는지 체크하는 목적의 리스트를 만들기
visited = [False] * (n + 1)

# 최단 거리 테이블을 모두 무한으로 초기화
d = [INF] * (n + 1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, si().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b, c))

# 방문하지 않은 노드 중에서, 가장 최단거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    idx = 0  # 가장 최단 거리가 짧은 노드
    for i in range(1, n + 1):
        if d[i] < min_value and not visited[i]:
            min_value = d[i]
            idx = i
    return idx


# 다익스트라 알고리즘
def dijkstra(start):
    # 시작 노드에 대해서 초기화
    d[start] = 0
    visited[start] = True

    # 최단 거리 테이블 초기 갱신
    for j in graph[start]:
        d[j[0]] = j[1]

    # 시작 노드를 제외한 전체 n - 1개의 노드에 대해 반복
    for i in range(n - 1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문처리
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            cost = d[now] + j[1]
            d[j[0]] = min(cost, d[j[0]])


dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n + 1):
    # 도달할 수 없는 경우, 무한이라고 출력
    if d[i] == INF:
        print("INF")
    else:
        print(d[i])