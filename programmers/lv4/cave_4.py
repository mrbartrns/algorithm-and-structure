# [카카오] 동굴 탐험
from collections import deque
import sys

sys.setrecursionlimit(1000000)


def dfs(node, visited, route, dir_graph):
    visited[node] = True
    route[node] = True
    for nxt in dir_graph[node]:
        if not visited[nxt]:
            if not dfs(nxt, visited, route, dir_graph):
                return False
        if route[nxt]:
            return False
    route[node] = False
    return True


def bfs(start, graph, n):
    que = deque()
    dir_graph = [[] for _ in range(n)]
    visited = [False] * n
    visited[start] = True
    que.append(0)
    while que:
        node = que.popleft()

        for nxt in graph[node]:
            if not visited[nxt]:
                visited[nxt] = True
                dir_graph[node].append(nxt)
                que.append(nxt)
    return dir_graph


def solution(n, path, order):
    graph = [[] for _ in range(n)]
    for a, b in path:
        graph[a].append(b)
        graph[b].append(a)

    dir_graph = bfs(0, graph, n)
    for a, b in order:
        dir_graph[a].append(b)
    return dfs(0, [False] * n, [False] * n, dir_graph)


if __name__ == "__main__":
    n = 9
    path = [[0, 1], [0, 3], [0, 7], [8, 1], [3, 6], [1, 2], [4, 7], [7, 5]]
    order = [[4, 1], [8, 7], [6, 5]]
    print(solution(n, path, order))