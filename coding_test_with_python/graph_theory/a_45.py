# BOJ 3665 최종 순위
import sys
from collections import deque

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline


# 모든 인접리스트로 나타낸 그래프는 인접 행렬로 나타낼 수 있다.
def topological_sort(graph, indegree):
    result = []
    que = deque()
    for i in range(1, len(indegree)):
        if indegree[i] == 0:
            que.append(i)
    for _ in range(n):
        if len(que) == 0:
            return "IMPOSSIBLE"
        elif len(que) >= 2:
            return "?"
        now = que.popleft()
        result.append(now)

        for i in range(1, n + 1):
            if graph[now][i]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    que.append(i)

    return " ".join(list(map(str, result)))


def topological_sort_reverse(graph, indegree):
    result = []
    que = deque()
    for i in range(len(indegree) - 1, 0, -1):
        if indegree[i] == 0:
            que.append(i)

    while que:
        now = que.popleft()
        for i in range(n, 0, -1):
            if graph[now][i]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    que.append(i)
    return result


t = int(si())
for _ in range(t):
    # make graph
    n = int(si())
    arr = list(map(int, si().split()))
    graph = [[False for _ in range(n + 1)] for _ in range(n + 1)]
    indegree = [0] * (n + 1)
    for i in range(n):
        for j in range(i + 1, n):
            first = arr[i]
            second = arr[j]
            graph[first][second] = True
            indegree[second] += 1

    # reverse
    m = int(si())
    for _ in range(m):
        a, b = map(int, si().split())
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegree[b] -= 1
            indegree[a] += 1
        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[b] += 1
            indegree[a] -= 1

    # topological sort
    print(topological_sort(graph, indegree))
