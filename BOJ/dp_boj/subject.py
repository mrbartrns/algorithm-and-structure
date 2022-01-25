# BOJ 14567 선수 과목
from collections import deque
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline


def topological_sort():
    while q:
        node = q.popleft()
        for nxt in adj[node]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                cache[nxt] = max(cache[nxt], cache[node] + 1)
                q.append(nxt)


N, M = map(int, si().strip().split(" "))
adj = [[] for _ in range(N + 1)]
cache = [1] * (N + 1)
indegree = [0] * (N + 1)
q = deque()
for _ in range(M):
    a, b = map(int, si().strip().split(" "))
    adj[a].append(b)
    indegree[b] += 1
for i in range(1, N + 1):
    if indegree[i] == 0:
        q.append(i)
topological_sort()
for i in range(1, N + 1):
    print(cache[i], end=" ")
