# BOJ 2638
import sys
from collections import deque

si = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(init_y, init_x):
    que = deque()
    que.append((init_y, init_x))
    visited[init_y][init_x] = True
    while que:
        y, x = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if not visited[ny][nx] and graph[ny][nx] == 0:
                visited[ny][nx] = True
                que.append((ny, nx))
            elif graph[ny][nx] >= 1:
                graph[ny][nx] += 1


def check():
    flag = True
    for y in range(n):
        for x in range(m):
            if graph[y][x] > 2:
                graph[y][x] = 0
                flag = False
            elif graph[y][x] == 2:
                graph[y][x] = 1
                flag = False
    return flag


n, m = map(int, si().split())
graph = [list(map(int, si().split())) for _ in range(n)]
# n, m = 8, 9
# graph = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 1, 0, 0, 0, 0], [0, 0, 0, 1, 1, 0, 1, 1, 0],
#          [0, 0, 1, 1, 1, 1, 1, 1, 0], [0, 0, 1, 1, 1, 1, 1, 0, 0], [0, 0, 1, 1, 0, 1, 1, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
# visited = [[False for _ in range(m)] for _ in range(n)]

time = 0
while True:
    visited = [[False for _ in range(m)] for _ in range(n)]
    bfs(0, 0)
    if check():
        break
    time += 1
print(time)
