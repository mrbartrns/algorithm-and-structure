# 가장 먼 노드 bfs, dfs
# dfs로는 가장 짧은 노드보다는 가장 깊은 노드를 찾는것에 적합하고, 짧은 노드를 찾기에는 다소 부적합
from bisect import bisect_left, bisect_right
from collections import deque


def solution(n, edge):
    graph = [[] for _ in range(n + 1)]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    distance = bfs(n, graph)
    distance.sort()
    max_value = distance[-1]
    answer = bisect_right(distance, max_value) - bisect_left(distance, max_value)
    return answer


def bfs(n, graph):
    que = deque()
    distance = [-1] * (n + 1)
    que.append((1, 0))
    distance[1] = 0
    while que:
        node, cost = que.popleft()
        for nxt in graph[node]:
            # 이미 방문했다는 뜻이므로
            if distance[nxt] > -1:
                continue
            que.append((nxt, cost + 1))
            distance[nxt] = cost + 1
    return distance


if __name__ == "__main__":
    n = 6
    vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
    print(solution(n, vertex))
