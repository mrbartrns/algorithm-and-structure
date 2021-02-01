from collections import deque

n = 3
graph = [[], [3], [3], [1, 2]]
visited = [0] * (n + 1)
color = 1
bipartite = True


def dfs(v, color):
    visited[v] = color
    for i in graph[v]:
        if visited[i] == 0 and not dfs(i, 3 - color):
            return False
        elif visited[i] != 0 and visited[i] == color:
            return False
    return True


# dfs
for i in range(1, n + 1):
    if not visited[i] and not dfs(i, color):
        bipartite = False
        break

print("YES" if bipartite else "NO")


def bfs(v, color):
    que = deque([v])
    visited[v] = color
    while que:
        v = que.popleft()
        for i in graph[v]:
            if visited[i] == 0:
                que.append(i)
                visited[i] = 3 - visited[v]
            elif visited[i] == visited[v]:
                return False
    return True


bipartite = True
color = 1

# bfs
for i in range(1, n + 1):
    if not visited[i] and not bfs(i, color):
        bipartite = False
        break

print("YES" if bipartite else "NO")