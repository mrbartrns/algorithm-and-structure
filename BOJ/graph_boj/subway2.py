# BOJ 16947 서울 지하철 2호선
from collections import deque
import sys

sys.setrecursionlimit(10000)
sys.stdin = open("../input.txt", "r")
si = sys.stdin.readline


def bfs(node, cycle):
    que = deque()
    visited = [False] * (N + 1)
    visited[node] = True
    que.append((node, 0))
    while que:
        cur, cnt = que.popleft()
        if cycle[cur]:
            return cnt

        for nxt in graph[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                que.append((nxt, cnt + 1))


def dfs(node, start, line, visited):
    visited[node] = True
    for nxt in graph[node]:
        if not visited[nxt]:
            if dfs(nxt, start, line + 1, visited):
                return True
        if start == nxt and line >= 2:
            return True
    return False


N = int(si())
graph = [[] for _ in range(N + 1)]
answer = [0] * (N + 1)
for _ in range(N):
    a, b = map(int, si().split())
    graph[a].append(b)
    graph[b].append(a)

cycle = [False] * (N + 1)
for i in range(1, N + 1):
    visited = [False] * (N + 1)
    cycle[i] = dfs(i, i, 0, visited)
for i in range(1, N + 1):
    if not cycle[i]:
        answer[i] = bfs(i, cycle)
for i in range(1, N + 1):
    print(answer[i], end=" ")
