# BOJ 14502
import sys
import copy
from collections import deque

si = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

"""
1. 백트래킹을 이용하여 모든 벽의 위치를 선정
2. for문을 돌면서 모든 2의 위치를 지정 -> 큐에 삽입
"""


def backtrack(idx):
    if idx == 3:
        arr.append(copy.deepcopy(graph))
        return
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and graph[i][j] == 0:
                visited[i][j] = True
                graph[i][j] = 1
                backtrack(idx + 1)
                graph[i][j] = 0
                visited[i][j] = False


def bfs(maps, que):
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if maps[nx][ny] == 0:
                maps[nx][ny] = 2
                que.append((nx, ny))


n, m = map(int, si().split())
graph = [list(map(int, si().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
arr = []
res = 0


backtrack(0)

for maps in arr:
    que = deque()
    cnt = 0
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 2:
                que.append((i, j))
    bfs(maps, que)
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 0:
                cnt += 1

    if res < cnt:
        res = cnt

print(res)
