from collections import deque


def topological_sort(graph, indegree):
    result = []
    que = deque()
    for i in range(1, len(indegree)):
        if indegree[i] == 0:
            que.append(i)

    while que:
        now = que.popleft()
        result.append(now)

        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                que.append(i)
    return result


def insert_node(edges, graph, indegree):
    for a, b in edges:
        indegree[b] += 1
        graph[a].append(b)


n = 5
graph = [[] for _ in range(n + 1)]
indegree = [0 for _ in range(n + 1)]
