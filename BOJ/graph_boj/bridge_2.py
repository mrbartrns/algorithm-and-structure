# BOJ 2146
import sys
from collections import deque

si = sys.stdin.readline


# n = int(si())
# graph = []
# for _ in range(n):
#     graph.append(list(map(int, si().split())))
# visited = [[False for _ in range(n)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
label = 1
n = 10
graph = [
    [1, 1, 1, 0, 0, 0, 0, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 0, 1, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 1, 1],
    [0, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

visited = [[False for _ in range(n)] for _ in range(n)]


def dfs(x, y, label):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    if not visited[x][y] and graph[x][y] == 1:
        visited[x][y] = True
        graph[x][y] = label
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny, label)
        return True
    return False


def bfs(label):
    que = deque()
    for i in range(n):
        for j in range(n):
            if graph[i][j] == label:
                que.append((i, j))
                visited[i][j] = True
    cnt = 0
    while que:
        size = len(que)
        for _ in range(size):
            x, y = que.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue

                if graph[nx][ny] != 0 and graph[nx][ny] != label:
                    return cnt
                elif not visited[nx][ny] and graph[nx][ny] == 0:
                    que.append((nx, ny))
                    visited[nx][ny] = True
        cnt += 1


# labeling
for i in range(n):
    for j in range(n):
        if not visited[i][j] and graph[i][j] == 1:
            dfs(i, j, label)
            label += 1

# initialize visited array
ret = 10000
for i in range(1, label):
    visited = [[False for _ in range(n)] for _ in range(n)]
    ret = min(ret, bfs(i))

print(ret)