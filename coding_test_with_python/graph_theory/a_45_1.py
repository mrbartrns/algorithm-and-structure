# BOJ 3665 (최종 순위)
import sys
from collections import deque

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline


def topological_sort(graph, indegree):
    que = deque()
    answer = []
    for i in range(1, len(indegree)):
        if indegree[i] == 0:
            que.append(i)

    for _ in range(n):
        if not que:
            return "IMPOSSIBLE"
        elif len(que) >= 2:
            return "?"

        now = que.popleft()
        answer.append(now)

        for i in range(1, n + 1):
            if graph[now][i]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    que.append(i)

    return " ".join(list(map(str, answer)))


t = int(si())
for _ in range(t):
    n = int(si())
    arr = list(map(int, si().split()))
    graph = [[False for _ in range(n + 1)] for _ in range(n + 1)]
    indegree = [0] * (n + 1)
    for i in range(n):
        for j in range(i + 1, n):
            u = arr[i]
            v = arr[j]
            graph[u][v] = True
            indegree[v] += 1
    m = int(si())
    for _ in range(m):
        a, b = map(int, si().split())
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegree[b] -= 1
            indegree[a] += 1
        else:
            graph[b][a] = False
            graph[a][b] = True
            indegree[a] -= 1
            indegree[b] += 1
    print(topological_sort(graph, indegree))
