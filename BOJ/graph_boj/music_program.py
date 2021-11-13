# BOJ 2623 음악 프로그램
from collections import deque
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline


def topological_sort():
    q = deque()
    ret = []
    for i in range(1, N + 1):
        if indegree[i] == 0:
            ret.append(i)
            q.append(i)
    while q:
        cur = q.popleft()
        for nxt in range(1, N + 1):
            if adj[cur][nxt] == 1:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    ret.append(nxt)
                    q.append(nxt)
    if len(ret) < N:
        return [0]
    return ret


N, M = map(int, si().split(" "))
adj = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
indegree = [0] * (N + 1)
for _ in range(M):
    arr = list(map(int, si().split(" ")))
    for i in range(2, len(arr)):
        # 이미 정립되어 있는 두 노드 a, b를 중복으로 처리하지 않도록 방지한다.
        if adj[arr[i - 1]][arr[i]] == 0:
            indegree[arr[i]] += 1
            adj[arr[i - 1]][arr[i]] = 1
orders = topological_sort()
for order in orders:
    print(order)
