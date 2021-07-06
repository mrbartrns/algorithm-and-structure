# 위상 정렬
import sys
from collections import deque

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline
v, e = map(int, si().split())

indegree = [0] * (v + 1)  # 진입차수
graph = [[] for _ in range(v + 1)]

for _ in range(e):
    a, b = map(int, si().split())
    graph[a].append(b)
    indegree[b] += 1


def topology_sort():
    result = []
    que = deque()

    for i in range(1, v + 1):
        if indegree[i] == 0:
            que.append(i)

    while que:
        now = que.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                que.append(i)
    return result


print(topology_sort())
