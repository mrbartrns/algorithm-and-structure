# BOJ 2206
import sys
from collections import deque

si = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, si().split())
graph = [list(map(int, list(si().strip()))) for _ in range(n)]


def bfs(n, m):
    que = deque()
    que.append((0, 0, 1))
    visited = [[[0, 0] for _ in range(m)] for _ in range(n)]
    visited[0][0][1] = 1

    while que:
        x, y, block = que.popleft()
        if x == n - 1 and y == m - 1:
            return visited[x][y][block]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if graph[nx][ny] == 1 and block == 1:
                visited[nx][ny][block - 1] = visited[x][y][block] + 1
                # 틀렸던 이유: block -= 1을 한 후 넣어서 전체 block값이 모두 다 바뀜
                que.append((nx, ny, block - 1))
            elif graph[nx][ny] == 0 and visited[nx][ny][block] == 0:
                visited[nx][ny][block] = visited[x][y][block] + 1
                que.append((nx, ny, block))
    return -1


print(bfs(n, m))