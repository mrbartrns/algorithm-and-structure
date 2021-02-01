# BOJ 1167
n = 5
graph = [[], [[3, 2]], [[4, 4]], [[1, 2], [4, 3]], [[2, 4], [3, 3], [5, 6]], [[4, 6]]]
visited = [False] * (n + 1)
distance = [0] * (n + 1)


def dfs(v):
    visited[v] = True
    for i, j in graph[v]:
        if not visited[i]:
            distance[i] = distance[v] + j
            dfs(i)


dfs(1)
max_d = distance.index(max(distance))

visited = [False] * (n + 1)
distance = [0] * (n + 1)
dfs(max_d)
print(max(distance))