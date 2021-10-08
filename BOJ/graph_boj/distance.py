# BOJ 1240 노드 사이의 거리
from collections import deque
import sys

sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline


def bfs(node, target):
    que = deque()
    que.append((node, -1, 0))  # cur, parent, cnt
    while que:
        cur, parent, dist = que.popleft()
        if cur == target:
            return dist

        for nxt in graph[cur]:
            nxt_node = nxt[0]
            cost = nxt[1]
            if nxt_node == parent:
                continue
            que.append((nxt_node, cur, cost + dist))


N, M = map(int, si().split(" "))
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b, c = map(int, si().split(" "))
    graph[a].append((b, c))
    graph[b].append((a, c))
for _ in range(M):
    a, b = map(int, si().split(" "))
    print(bfs(a, b))
