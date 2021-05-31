# BOJ 2206
import sys
from collections import deque

si = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, si().split())
graph = [list(map(int, list(si().strip()))) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]


def bfs(n, m):
    que = deque([(0, 0, True, 1)])
    visited[0][0] = True
    while que:
        x, y, check, cnt = que.popleft()
        if x == n - 1 and y == m - 1:
            return cnt
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if not visited[nx][ny]:
                if graph[nx][ny] == 0:
                    visited[nx][ny] = True
                    que.append((nx, ny, check, cnt + 1))
                else:
                    if check:
                        visited[nx][ny] = True
                        que.append((nx, ny, False, cnt + 1))
    return -1


print(bfs(n, m))
"""
주어진 정점을 그래프로 표현-? how?
"""