# BOJ 2606
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * (n + 1)


def bfs(graph, v, visited):
    cnt = 0
    que = deque([v])
    visited[v] = True
    while que:
        v = que.popleft()
        for i in graph[v]:
            if not visited[i]:
                que.append(i)
                visited[i] = True
                cnt += 1
    return cnt


# print(bfs(graph, 1, visited))

# how to solve to use dfs method?
def dfs(graph, v, visited):
    if not visited[v]:
        visited[v] = True
        for i in graph[v]:
            dfs(graph, i, visited)
        return True
    return False


cnt = 0
dfs(graph, 1, visited)
for i in range(2, n + 1):
    if not visited[i]:
        cnt += 1

print(n - cnt - 1)
