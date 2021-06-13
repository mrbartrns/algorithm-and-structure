# 미로 탈출
import sys
from collections import deque

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

n, m = map(int, si().split())
graph = [list(map(int, si().strip())) for _ in range(n)]


def bfs(n, m):
    que = deque()
    visited = [[False for _ in range(m)] for _ in range(n)]
    que.append((0, 0, 1))
    visited[0][0] = True
    while que:
        y, x, cnt = que.popleft()
        if y == n - 1 and x == m - 1:
            return cnt

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or ny >= n or nx < 0 or nx >= m:
                continue

            if graph[ny][nx] == 0:
                continue

            if not visited[ny][nx] and graph[ny][nx] == 1:
                visited[ny][nx] = True
                que.append((ny, nx, cnt + 1))
    return -1


print(bfs(n, m))
