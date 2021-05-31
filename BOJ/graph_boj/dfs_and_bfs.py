# BOJ 1260
import sys
from collections import deque


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ")
    for i in range(len(graph[v])):
        if not visited[i]:
            dfs(graph, v, visited)


def bfs(graph, v, visited):
    que = deque()
    que.append(v)
    visited[v] = True
    while que:
        v = que.popleft()
        print(v, end=" ")
        for i in range(len(graph[v])):
            if not visited[i]:
                que.append(i)
                visited[i] = True