# BOJ 7576
import sys
from collections import deque

si = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(que):
    cnt = 1
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if graph[nx][ny] == -1:
                continue

            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                cnt = max(cnt, graph[nx][ny])
                que.append((nx, ny))
    return cnt - 1


m, n = map(int, si().split())

graph = []
que = deque()
one = False
done = True
for i in range(n):
    temp = list(map(int, si().split()))
    for j in range(m):
        if temp[j] == 1:
            one = True
            que.append((i, j))
    graph.append(temp)
if not one:
    print(0)
else:
    val = bfs(que)
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                done = False
                break
    print(val if done else -1)