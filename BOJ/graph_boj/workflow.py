# BOJ 2056 작업
from collections import deque
import sys


sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline


def topological_sort():
    t = [0] * (N + 1)
    que = deque()
    for i in range(1, N + 1):
        if indegree[i] == 0:
            que.append(i)
            t[i] = time[i]

    while que:
        node = que.popleft()
        for nxt in graph[node]:
            indegree[nxt] -= 1
            # indegree가 0이든 그렇지 않던 간에 무조건 갱신해야 최댓값을 얻을 수 있다.
            t[nxt] = max(t[nxt], time[nxt] + t[node])
            if indegree[nxt] == 0:
                que.append(nxt)
    return t


N = int(si())
graph = [[] for _ in range(N + 1)]
time = [0] * (N + 1)

indegree = [0] * (N + 1)

for i in range(1, N + 1):
    info = list(map(int, si().split(" ")))
    cur_time, ind = info[0], info[1]
    indegree[i] = ind
    time[i] = cur_time
    for j in range(2, len(info)):
        graph[info[j]].append(i)
t = topological_sort()
print(max(t))
