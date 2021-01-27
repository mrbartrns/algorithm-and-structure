"""
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ")
    for i in range(graph[v]):
        if not visited[i]:
            dfs(graph, i, visited)
"""

"""
dfs: deep first search (깊이 우선 탐색)
시스템 스택을 이용하여 노드의 깊이 방향으로 우선적으로 탐색=
"""


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ")
    for i in range(graph[v]):
        if not visited[i]:
            dfs(graph, v, visited)
