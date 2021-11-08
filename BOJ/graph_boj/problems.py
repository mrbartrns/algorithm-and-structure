# BOJ 1766 문제집
import heapq
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline


def topological_sort():
    q = []
    ret = []
    for i in range(1, N + 1):
        if indegree[i] == 0:
            heapq.heappush(q, i)
    while q:
        node = heapq.heappop(q)
        ret.append(node)

        for nxt_node in adj[node]:
            indegree[nxt_node] -= 1
            if indegree[nxt_node] == 0:
                heapq.heappush(q, nxt_node)
    return ret


N, M = map(int, si().split(" "))
adj = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)
for _ in range(M):
    a, b = map(int, si().split(" "))
    indegree[b] += 1
    adj[a].append(b)
print(" ".join(list(map(str, topological_sort()))))
