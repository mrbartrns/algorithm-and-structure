# BOJ 1005 ACM CRAFT
import sys
from collections import deque

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline


def topological_sort(times, indegree, graph):
    ret = [0] * (n + 1)
    que = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            que.append(i)
            ret[i] += times[i]

    while que:
        u = que.popleft()

        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                que.append(v)
            ret[v] = max(ret[v], times[v] + ret[u])
    return ret


t = int(si())
for _ in range(t):
    n, k = map(int, si().split())
    times = [0] + list(map(int, si().split()))
    indegree = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    for _ in range(k):
        a, b = map(int, si().split())
        indegree[b] += 1
        graph[a].append(b)
    ret = topological_sort(times, indegree, graph)
    print(ret[int(si())])
