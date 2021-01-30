# BOJ 2146
import sys
from collections import deque

si = sys.stdin.readline
sys.setrecursionlimit(10000)


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
label = 1


n = int(si())
graph = []
for _ in range(n):
    graph.append(list(map(int, si().split())))

print(graph)

# n = 10
# graph = [
#     [1, 1, 1, 0, 0, 0, 0, 1, 1, 1],
#     [1, 1, 1, 1, 0, 0, 0, 0, 1, 1],
#     [1, 0, 1, 1, 0, 0, 0, 0, 1, 1],
#     [0, 0, 1, 1, 1, 0, 0, 0, 0, 1],
#     [0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
#     [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# ]
answer = 10000
visited = [[False for _ in range(n)] for _ in range(n)]


def dfs(x, y, label):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    if graph[x][y] == 1 and not visited[x][y]:
        graph[x][y] = label
        visited[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny, label)
        return True
    return False


def bfs(num):
    que = deque()
    res = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] == num:
                visited[i][j] = True
                que.append((i, j))
    while que:
        size = len(que)
        for _ in range(size):
            x, y = que.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue

                if graph[nx][ny] != 0 and graph[nx][ny] != num:
                    return res
                elif graph[nx][ny] == 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    que.append((nx, ny))
        res += 1


for i in range(n):
    for j in range(n):
        if dfs(i, j, label):
            label += 1

for i in range(1, label):
    visited = [[False for _ in range(n)] for _ in range(n)]
    answer = min(answer, bfs(i))

print(answer)