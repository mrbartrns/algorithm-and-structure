# BOJ 14502
import sys
from collections import deque
import copy

si = sys.stdin.readline
MAX = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def backtrack(k):
    if k == 3:
        arr.append(copy.deepcopy(graph))
        return
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and graph[i][j] == 0:
                visited[i][j] = True
                graph[i][j] = 1
                backtrack(k + 1)
                graph[i][j] = 0
                visited[i][j] = False


def bfs(que):
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if maps[nx][ny] == 0:
                maps[nx][ny] = 2
                que.append((nx, ny))


arr = []
n, m = map(int, si().split())
graph = [list(map(int, si().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
# 백트래킹 후 arr 생성하기
backtrack(0)

for maps in arr:
    que = deque()
    s = 0
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 2:
                que.append((i, j))
    bfs(que)
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 0:
                s += 1
    MAX = max(s, MAX)

print(MAX)
