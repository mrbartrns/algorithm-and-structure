# [카카오] 동굴 탐험
# 유향 그래프 이용
from collections import deque
import sys

sys.setrecursionlimit(1000000)


def dfs(node, visited, on_same_path, graph):
    visited[node] = True
    on_same_path[node] = True
    for nxt in graph[node]:
        if not visited[nxt]:
            if not dfs(nxt, visited, on_same_path, graph):
                return False
        if on_same_path[nxt]:
            return False
    on_same_path[node] = False
    return True


def bfs(graph, visited):
    que = deque()
    dir_graph = [[] for _ in range(len(graph))]
    visited[0] = True
    que.append(0)
    while que:
        node = que.popleft()

        for nxt in graph[node]:
            if not visited[nxt]:
                visited[nxt] = True
                que.append(nxt)
                dir_graph[node].append(nxt)
    return dir_graph


def solution(n, path, order):
    visited = [False] * n
    dir_vsitied = [False] * n
    on_same_path = [False] * n
    graph = [[] for _ in range(n)]
    for a, b in path:
        graph[a].append(b)
        graph[b].append(a)

    dir_graph = bfs(graph, visited)

    for a, b in order:
        dir_graph[a].append(b)

    return dfs(0, dir_vsitied, on_same_path, dir_graph)


if __name__ == "__main__":
    n = 9
    path = [[0, 1], [0, 3], [0, 7], [8, 1], [3, 6], [1, 2], [4, 7], [7, 5]]
    order = [[8, 5], [6, 7], [4, 1]]
    print(solution(n, path, order))