# BOJ 2252 줄 세우기
from collections import deque
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline


def topological_sort():
    q = deque()
    ret = []
    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append(i)
            ret.append(i)
    while q:
        here = q.popleft()
        for there in adj[here]:
            indegree[there] -= 1
            if indegree[there] == 0:
                q.append(there)
                ret.append(there)
    return ret


N, M = map(int, si().split(" "))
adj = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)
for _ in range(M):
    a, b = map(int, si().split(" "))
    adj[a].append(b)
    indegree[b] += 1

print(" ".join(list(map(str, topological_sort()))))
