# BOJ 18352 특정 거리의 도시 찾기 (BFS)
import sys
from collections import deque

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline
INF = 987654321


def bfs(start):
    que = deque()
    distance = [INF for _ in range(n + 1)]
    distance[start] = 0
    que.append((start, 0))
    while que:
        node, cnt = que.popleft()

        for j in graph[node]:
            cost = cnt + 1
            if distance[j] > cost:
                distance[j] = cost
                que.append((j, cost))
    return distance


n, m, k, x = map(int, si().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, si().split())
    graph[u].append(v)

answer = []
dist = bfs(x)
for i in range(1, n + 1):
    if dist[i] == k:
        answer.append(i)

print("\n".join(list(map(str, answer))) if answer else -1)
