# 커리큘럼
"""
topological sort 이용
"""
import sys
from collections import deque

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline


def topological_sort():
    values = [0] * (n + 1)
    que = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            que.append(i)
            values[i] = time[i]
    while que:
        now = que.popleft()
        for i in graph[now]:
            indegree[i] -= 1
            values[i] = max(values[i], values[now] + time[i])
            if indegree[i] == 0:
                que.append(i)
    return values


n = int(si())
graph = [[] for _ in range(n + 1)]
time = [0] * (n + 1)
indegree = [0] * (n + 1)
for i in range(1, n + 1):
    temp = list(map(int, si().split()))
    time[i] = temp[0]
    for j in range(1, len(temp) - 1):
        graph[temp[j]].append(i)
        indegree[i] += 1

result = topological_sort()
for i in range(1, len(result)):
    print(result[i])
