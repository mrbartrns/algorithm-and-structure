# BOJ 1707
import sys
from collections import deque

si = sys.stdin.readline


def bfs(v, c):
    que = deque([])
    que.append(v)
    visited[v] = c
    while que:
        v = que.popleft()
        for i in graph[v]:
            if visited[i] == 0:
                visited[i] = 3 - visited[v]
                que.append(i)
            elif visited[i] == visited[v]:
                return False
    return True


t = int(si())
for _ in range(t):
    n, m = map(int, si().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, si().split())
        graph[a].append(b)
        graph[b].append(a)
    visited = [0] * (n + 1)
    flag = True
    for i in range(1, n + 1):
        if visited[i] == 0 and not bfs(i, 1):
            flag = False
            break
    print("YES" if flag else "NO")
