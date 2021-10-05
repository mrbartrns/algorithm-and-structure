# BOJ 1516
from collections import deque
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline


def topological_sort(indegree):
    que = deque()
    ret = [0] * (N + 1)
    for i in range(1, N + 1):
        if indegree[i] == 0:
            ret[i] = time[i]
            que.append(i)
    while que:
        node = que.popleft()

        for nxt in graph[node]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                que.append(nxt)
            ret[nxt] = max(ret[nxt], ret[node] + time[nxt])
    return ret


N = int(si())
indegree = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]
time = [0] * (N + 1)
for i in range(1, N + 1):
    arr = list(map(int, si().split(" ")))
    time[i] = arr[0]
    for j in range(1, len(arr) - 1):
        graph[arr[j]].append(i)
        indegree[i] += 1
ret = topological_sort(indegree)
for i in range(1, N + 1):
    print(ret[i])