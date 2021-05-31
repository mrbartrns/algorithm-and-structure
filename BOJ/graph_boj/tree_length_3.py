graph = [[], [[3, 2]], [[4, 4]], [[1, 2], [4, 3]], [[2, 4], [3, 3], [5, 6]], [[4, 6]]]
visited = [False, False, False, False, False, False]
n = 5
distance = [0] * (n + 1)


def dfs(v):
    visited[v] = True
    for i, l in graph[v]:
        if not visited[i]:
            distance[i] = l + distance[v]
            dfs(i)


dfs(1)
max_d = distance.index(max(distance))
distance = [0] * (n + 1)
visited = [False, False, False, False, False, False]

# print(max_d)
dfs(max_d)
print(max(distance))