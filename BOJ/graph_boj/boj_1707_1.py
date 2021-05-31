# BOJ 1707
from collections import deque

graph = [[], [3], [3], [1, 2]]
n = 3
visited = [0] * (n + 1)
flag = True


def dfs(graph, v, color):
    visited[v] = color
    for i in graph[v]:
        if visited[i] == 0 and not dfs(graph, i, 3 - color):
            return False
        elif visited[i] == visited[v]:
            return False
    return True


def bfs(graph, v, color):
    que = deque([v])
    visited[v] = color
    while que:
        v = que.popleft()
        color = 3 - visited[v]
        for i in graph[v]:
            if visited[i] == 0:
                que.append(i)
                visited[i] = color
            elif visited[i] == visited[v]:
                return False
    return True


for i in range(1, n + 1):
    if visited[i] == 0 and not dfs(graph, i, 1):
        flag = False
        break

print("YES" if flag else "NO")
