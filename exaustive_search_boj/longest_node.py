# 1번 노드로부터 가장 먼 노드 구하기
from collections import deque
from bisect import bisect_left, bisect_right


def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n + 1)]
    for x, y in edge:
        graph[x].append(y)
        graph[y].append(x)
    distance = bfs(graph)
    distance.sort()
    MAX = distance[-1]
    answer = bisect_right(distance, MAX) - bisect_left(distance, MAX)
    return answer


def bfs(graph):
    que = deque()
    distance = [-1] * len(graph)
    que.append((1, 0))
    distance[1] = 0
    while que:
        node, cnt = que.popleft()
        for j in graph[node]:
            if distance[j] > -1:
                continue
            distance[j] = cnt + 1
            que.append((j, cnt + 1))
    return distance


n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n, edge))